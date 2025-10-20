from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
import requests
import base64
import subprocess
import threading
import time

app = Flask(__name__)

# Arquivos de dados
DATA_FILE = 'ligacoes.json'
CONFIG_FILE = 'config.json'
CONVERSAS_FILE = 'conversas_ia.json'

# Carregar dados existentes
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'ligacoes': [], 'clientes': {}}

# Salvar dados
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Conversas IA
def load_conversas():
    if os.path.exists(CONVERSAS_FILE):
        with open(CONVERSAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'conversas': []}

def save_conversas(data):
    with open(CONVERSAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Carregar configurações
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            # Decodificar API Key se existir
            if 'gemini_api_key' in config and config['gemini_api_key']:
                try:
                    config['gemini_api_key'] = base64.b64decode(config['gemini_api_key']).decode('utf-8')
                except:
                    config['gemini_api_key'] = ''
            return config
    return {'gemini_api_key': '', 'ollama_model': 'llama2', 'save_ai_conversations': False, 'retention_days': 90}

# Salvar configurações
def save_config(config):
    # Codificar API Key antes de salvar
    config_to_save = config.copy()
    if 'gemini_api_key' in config_to_save and config_to_save['gemini_api_key']:
        config_to_save['gemini_api_key'] = base64.b64encode(config_to_save['gemini_api_key'].encode('utf-8')).decode('utf-8')
    
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_to_save, f, ensure_ascii=False, indent=2)

def apply_retention():
    """Apaga conversas mais antigas que a retenção configurada."""
    config = load_config()
    retention_days = int(config.get('retention_days', 90) or 90)
    if retention_days <= 0:
        return
    conv = load_conversas()
    lim = datetime.now().timestamp() - (retention_days * 86400)
    conv['conversas'] = [c for c in conv.get('conversas', []) if _parse_iso(c.get('data_hora')).timestamp() >= lim]
    save_conversas(conv)

def _parse_iso(s):
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return datetime.now()

def registrar_conversa(pergunta: str, resposta: str, ia: str, modelo: str, cliente: str | None):
    config = load_config()
    if not config.get('save_ai_conversations', False):
        return
    conv = load_conversas()
    novo_id = (conv['conversas'][-1]['id'] + 1) if conv['conversas'] else 1
    registro = {
        'id': novo_id,
        'data_hora': datetime.now().isoformat(),
        'ia': ia,
        'modelo': modelo,
        'cliente': cliente or '',
        'pergunta': pergunta or '',
        'resposta': resposta or ''
    }
    conv['conversas'].append(registro)
    save_conversas(conv)
    apply_retention()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota de configurações
@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

# Rota de chat em tela cheia
@app.route('/chat')
def chat_full():
    return render_template('chat.html')

# API: Obter configurações
@app.route('/api/config', methods=['GET'])
def get_config():
    config = load_config()
    
    # Verificar qual IA está configurada
    has_gemini = bool(config.get('gemini_api_key'))
    has_ollama = False
    
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        has_ollama = response.status_code == 200
    except:
        pass
    
    return jsonify({
        'has_gemini_key': has_gemini,
        'gemini_api_key': config.get('gemini_api_key', ''),
        'ollama_model': config.get('ollama_model', 'llama2'),
        'save_ai_conversations': bool(config.get('save_ai_conversations', False)),
        'retention_days': int(config.get('retention_days', 90) or 90),
        'has_ollama': has_ollama,
        'active_ia': 'gemini' if has_gemini else ('ollama' if has_ollama else None)
    })

# API: Salvar configurações
@app.route('/api/config', methods=['POST'])
def save_config_route():
    config_data = request.json
    save_config(config_data)
    return jsonify({'success': True, 'message': 'Configurações salvas com sucesso!'})

# Conversas IA - listar
@app.route('/api/ai/conversas', methods=['GET'])
def list_ai_conversas():
    cliente = request.args.get('cliente')
    conv = load_conversas()
    itens = conv.get('conversas', [])
    if cliente:
        itens = [c for c in itens if c.get('cliente', '').lower() == cliente.lower()]
    return jsonify({'success': True, 'conversas': itens})

# Conversas IA - exportar
@app.route('/api/ai/conversas/export', methods=['GET'])
def export_ai_conversas():
    from flask import make_response
    conv = load_conversas()
    response = make_response(json.dumps(conv, ensure_ascii=False, indent=2))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Content-Disposition'] = f'attachment; filename=conversas_ia_{datetime.now().strftime("%Y%m%d")}.json'
    return response

# Conversas IA - limpar
@app.route('/api/ai/conversas/clear', methods=['POST'])
def clear_ai_conversas():
    save_conversas({'conversas': []})
    return jsonify({'success': True})

# API: Listar todas as ligações
@app.route('/api/ligacoes', methods=['GET'])
def get_ligacoes():
    data = load_data()
    return jsonify(data['ligacoes'])

# API: Adicionar nova ligação
@app.route('/api/ligacoes', methods=['POST'])
def add_ligacao():
    data = load_data()
    ligacao = request.json
    ligacao['id'] = len(data['ligacoes']) + 1
    ligacao['data_registro'] = datetime.now().isoformat()
    
    data['ligacoes'].append(ligacao)
    
    # Atualizar informações do cliente
    cliente_nome = ligacao['cliente']
    if cliente_nome not in data['clientes']:
        data['clientes'][cliente_nome] = {
            'nome': cliente_nome,
            'total_ligacoes': 0,
            'ultima_ligacao': None
        }
    
    data['clientes'][cliente_nome]['total_ligacoes'] += 1
    data['clientes'][cliente_nome]['ultima_ligacao'] = ligacao['data_registro']
    
    save_data(data)
    return jsonify({'success': True, 'ligacao': ligacao})

# API: Obter ligação específica
@app.route('/api/ligacoes/<int:ligacao_id>', methods=['GET'])
def get_ligacao(ligacao_id):
    data = load_data()
    ligacao = next((l for l in data['ligacoes'] if l['id'] == ligacao_id), None)
    if ligacao:
        return jsonify(ligacao)
    return jsonify({'error': 'Ligação não encontrada'}), 404

# API: Deletar ligação
@app.route('/api/ligacoes/<int:ligacao_id>', methods=['DELETE'])
def delete_ligacao(ligacao_id):
    data = load_data()
    data['ligacoes'] = [l for l in data['ligacoes'] if l['id'] != ligacao_id]
    save_data(data)
    return jsonify({'success': True})

# API: Listar clientes
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    data = load_data()
    return jsonify(list(data['clientes'].values()))

# API: Chat com IA (Ollama)
@app.route('/api/chat/ollama', methods=['POST'])
def chat_ollama():
    try:
        pergunta = request.json.get('pergunta')
        modelo = request.json.get('modelo')
        
        # Se não veio no request, carregar do config salvo
        if not modelo:
            config = load_config()
            modelo = config.get('ollama_model', 'mistral')
        
        # Verificar se o modelo existe antes de tentar usar
        try:
            models_response = requests.get('http://localhost:11434/api/tags', timeout=5)
            if models_response.status_code == 200:
                models_data = models_response.json()
                available_models = [m['name'] for m in models_data.get('models', [])]
                if not available_models:
                    return jsonify({
                        'success': False,
                        'error': 'Nenhum modelo instalado no Ollama. Execute: ollama pull llama2'
                    }), 400
                if modelo not in available_models:
                    return jsonify({
                        'success': False,
                        'error': f'Modelo "{modelo}" não encontrado. Modelos disponíveis: {", ".join(available_models)}'
                    }), 400
        except requests.exceptions.ConnectionError:
            return jsonify({
                'success': False,
                'error': 'Ollama não está rodando. Vá em Configurações para iniciar o servidor.'
            }), 500
        
        # Carregar todo o histórico de ligações
        data = load_data()
        contexto = construir_contexto(data['ligacoes'], request.json.get('cliente'))
        
        # Preparar prompt com contexto (instruir a responder em Markdown enxuto)
        prompt = f"""Você é um assistente especializado em análise de relacionamento com clientes.

INSTRUÇÕES DE FORMATAÇÃO (obrigatórias):
- Responda em Markdown conciso.
- Use títulos (##), listas com bullets e negritos para pontos chave.
- Traga no máximo 6 bullets por seção.
- Inclua uma seção final com Próximos Passos (bullets práticos e objetivos).

HISTÓRICO DE LIGAÇÕES:
{contexto}

PERGUNTA DO USUÁRIO: {pergunta}

Agora responda seguindo as instruções acima."""

        # Chamar Ollama
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': modelo,
                'prompt': prompt,
                'stream': False
            },
            timeout=60
        )
        
        if response.status_code == 200:
            resultado = response.json()
            texto = resultado.get('response', '')
            # salvar conversa
            registrar_conversa(pergunta, texto, 'ollama', modelo, request.json.get('cliente'))
            return jsonify({
                'success': True,
                'resposta': texto,
                'modelo': modelo
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Erro ao conectar com Ollama: {response.status_code} - {response.text}'
            }), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({
            'success': False,
            'error': 'Não foi possível conectar ao Ollama. Vá em Configurações para iniciar o servidor ou verifique se está rodando (ollama serve).'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro: {str(e)}'
        }), 500

# API: Chat com IA (Google Gemini)
@app.route('/api/chat/gemini', methods=['POST'])
def chat_gemini():
    try:
        pergunta = request.json.get('pergunta')
        api_key = request.json.get('api_key')
        
        # Se não veio no request, carregar do config salvo
        if not api_key:
            config = load_config()
            api_key = config.get('gemini_api_key', '')
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'API Key do Google Gemini não configurada. Vá em Configurações para salvar sua chave.'
            }), 400
        
        # Carregar todo o histórico de ligações
        data = load_data()
        contexto = construir_contexto(data['ligacoes'], request.json.get('cliente'))
        
        # Preparar prompt com contexto
        prompt = f"""Você é um assistente especializado em análise de relacionamento com clientes.
        
HISTÓRICO DE LIGAÇÕES:
{contexto}

PERGUNTA DO USUÁRIO: {pergunta}

Analise o histórico e responda de forma clara, objetiva e útil. Identifique padrões, necessidades e oportunidades."""

        # Chamar Google Gemini API (usando gemini-2.5-flash - modelo correto e gratuito)
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}'
        
        response = requests.post(
            url,
            json={
                'contents': [{
                    'parts': [{
                        'text': prompt
                    }]
                }]
            },
            timeout=30
        )
        
        if response.status_code == 200:
            resultado = response.json()
            resposta_texto = resultado['candidates'][0]['content']['parts'][0]['text']
            # salvar conversa
            registrar_conversa(pergunta, resposta_texto, 'gemini', 'gemini-2.5-flash', request.json.get('cliente'))
            return jsonify({
                'success': True,
                'resposta': resposta_texto,
                'modelo': 'gemini-2.5-flash'
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Erro na API do Gemini: {response.status_code} - {response.text}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro: {str(e)}'
        }), 500

# Construir contexto das ligações
def construir_contexto(ligacoes, cliente_filtro=None):
    if not ligacoes:
        return "Nenhuma ligação registrada ainda."
    
    # Filtrar por cliente se especificado
    if cliente_filtro:
        ligacoes = [l for l in ligacoes if l.get('cliente', '').lower() == cliente_filtro.lower()]
    
    contexto = []
    for ligacao in ligacoes:
        contexto.append(f"""
---
Data: {ligacao.get('data', 'N/A')}
Cliente: {ligacao.get('cliente', 'N/A')}
Duração: {ligacao.get('duracao', 'N/A')}
Notas: {ligacao.get('notas', 'N/A')}
Assuntos: {ligacao.get('assuntos', 'N/A')}
Próximos Passos: {ligacao.get('proximos_passos', 'N/A')}
---
""")
    
    return '\n'.join(contexto)

# API: Obter modelos disponíveis do Ollama
@app.route('/api/ollama/models', methods=['GET'])
def get_ollama_models():
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return jsonify({
                'success': True,
                'models': [m['name'] for m in models]
            })
        return jsonify({'success': False, 'models': []})
    except:
        return jsonify({'success': False, 'models': []})

# API: Listar modelos disponíveis do Google Gemini
@app.route('/api/gemini/models', methods=['GET'])
def list_gemini_models():
    try:
        api_key = request.args.get('api_key')
        if not api_key:
            config = load_config()
            api_key = config.get('gemini_api_key', '')
        
        if not api_key:
            return jsonify({'success': False, 'error': 'API Key não fornecida'})
        
        # Listar modelos disponíveis
        url = f'https://generativelanguage.googleapis.com/v1beta/models?key={api_key}'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            models = []
            for model in data.get('models', []):
                models.append({
                    'name': model.get('name', ''),
                    'displayName': model.get('displayName', ''),
                    'supportedMethods': model.get('supportedGenerationMethods', [])
                })
            return jsonify({
                'success': True,
                'models': models,
                'raw': data
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Erro {response.status_code}: {response.text}'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# API: Verificar status do Ollama
@app.route('/api/ollama/status', methods=['GET'])
def get_ollama_status():
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=3)
        return jsonify({
            'success': True,
            'online': response.status_code == 200
        })
    except:
        return jsonify({
            'success': True,
            'online': False
        })

# API: Iniciar servidor Ollama
@app.route('/api/ollama/start', methods=['POST'])
def start_ollama():
    try:
        # Verificar se já está rodando
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        if response.status_code == 200:
            return jsonify({
                'success': True,
                'message': 'Servidor já está rodando'
            })
    except:
        pass
    
    try:
        # Tentar iniciar o servidor Ollama
        if os.name == 'nt':  # Windows
            subprocess.Popen(['ollama', 'serve'], 
                           creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:  # Linux/Mac
            subprocess.Popen(['ollama', 'serve'], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
        
        # Aguardar um pouco para o servidor inicializar
        time.sleep(3)
        
        # Verificar se iniciou com sucesso
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        if response.status_code == 200:
            return jsonify({
                'success': True,
                'message': 'Servidor Ollama iniciado com sucesso'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Servidor não respondeu após inicialização'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro ao iniciar servidor: {str(e)}'
        })

# API: Parar servidor Ollama
@app.route('/api/ollama/stop', methods=['POST'])
def stop_ollama():
    try:
        # No Windows, tentar parar o processo
        if os.name == 'nt':
            subprocess.run(['taskkill', '/f', '/im', 'ollama.exe'], 
                         capture_output=True)
        else:
            subprocess.run(['pkill', '-f', 'ollama serve'], 
                         capture_output=True)
        
        time.sleep(2)
        
        # Verificar se parou
        try:
            response = requests.get('http://localhost:11434/api/tags', timeout=2)
            if response.status_code == 200:
                return jsonify({
                    'success': False,
                    'error': 'Servidor ainda está rodando'
                })
        except:
            pass
        
        return jsonify({
            'success': True,
            'message': 'Servidor Ollama parado com sucesso'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro ao parar servidor: {str(e)}'
        })

# API: Exportar dados
@app.route('/api/export', methods=['GET'])
def export_data():
    try:
        data = load_data()
        config = load_config()
        
        export_data = {
            'ligacoes': data['ligacoes'],
            'clientes': data['clientes'],
            'config': config,
            'export_date': datetime.now().isoformat()
        }
        
        from flask import make_response
        response = make_response(json.dumps(export_data, ensure_ascii=False, indent=2))
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Disposition'] = f'attachment; filename=backup_ligacoes_{datetime.now().strftime("%Y%m%d")}.json'
        return response
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# API: Importar dados
@app.route('/api/import', methods=['POST'])
def import_data():
    try:
        import_data = request.json
        
        if 'ligacoes' in import_data:
            data = {
                'ligacoes': import_data['ligacoes'],
                'clientes': import_data.get('clientes', {})
            }
            save_data(data)
        
        if 'config' in import_data:
            save_config(import_data['config'])
        
        return jsonify({'success': True, 'message': 'Dados importados com sucesso'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# API: Limpar todos os dados
@app.route('/api/clear', methods=['POST'])
def clear_all_data():
    try:
        # Limpar dados de ligações
        save_data({'ligacoes': [], 'clientes': {}})
        
        # Limpar configurações (manter apenas estrutura básica)
        save_config({'gemini_api_key': '', 'ollama_model': 'llama2'})
        
        return jsonify({'success': True, 'message': 'Todos os dados foram limpos'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # Configurar encoding do console para UTF-8
    import sys
    if sys.platform == 'win32':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except:
            pass
    
    # Verificar se deve controlar Ollama automaticamente
    auto_ollama = os.environ.get('AUTO_OLLAMA', 'false').lower() == 'true'
    
    if auto_ollama:
        try:
            from ollama_manager import setup_ollama_auto_control
            setup_ollama_auto_control()
            print("Controle automatico do Ollama ativado!")
        except ImportError:
            print("Modulo ollama_manager nao encontrado")
    
    print("=" * 60)
    print("Sistema de Gestao de Ligacoes com IA iniciado!")
    print("=" * 60)
    print("Acesse: http://localhost:5000")
    print("Configuracoes: http://localhost:5000/configuracoes")
    print("\nDicas:")
    print("  - Para usar Ollama: certifique-se de executar 'ollama serve'")
    print("  - Para usar Gemini: obtenha uma API key gratuita")
    print("    em https://makersuite.google.com/app/apikey")
    print("  - Acesse /configuracoes para gerenciar IAs e dados")
    print("=" * 60)
    print()
    
    app.run(debug=True, port=5000)

