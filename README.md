# 📞 Sistema de Gestão de Ligações com IA

Sistema completo para registrar suas ligações com clientes e obter insights inteligentes usando IA **100% gratuita**!

## ✨ Funcionalidades

- ✅ **Registro Completo de Ligações**: Guarde todas as informações importantes de cada conversa
- ✅ **Histórico Organizado**: Visualize todas as suas ligações de forma clara
- ✅ **Estatísticas em Tempo Real**: Acompanhe total de ligações, clientes e mais
- ✅ **Chat Inteligente com IA**: Faça perguntas sobre seus clientes e receba análises detalhadas
- ✅ **2 Opções de IA**:
  - **Ollama** (Local, privado, 100% offline)
  - **Google Gemini** (Online, gratuito, API generosa)
- ✅ **Interface Moderna e Intuitiva**: Design bonito e fácil de usar
- ✅ **API Key Salva Automaticamente**: Configure uma vez, use sempre! 🔐
- ✅ **Executável para Desktop**: Crie um .exe para usar sem Python
- ✅ **Inicialização com 1 Clique**: Script .bat para Windows

## 🚀 Como Instalar e Usar

### ⚡ FORMA MAIS FÁCIL (Windows)

**Duplo clique no arquivo:**
```
INICIAR.bat
```
Pronto! O sistema instala tudo automaticamente e abre no navegador! 🎉

---

### 🐍 Forma Tradicional (Todos os Sistemas)

#### 1️⃣ Pré-requisitos

- Python 3.7 ou superior
- Conexão com internet (apenas para Google Gemini)

#### 2️⃣ Instalação

1. **Clone ou baixe este repositório**

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar as IAs

#### Opção A: Ollama (Local - 100% Privado)

1. **Instale o Ollama:**
   - Acesse: https://ollama.ai/download
   - Baixe e instale para o seu sistema operacional

2. **Baixe um modelo:**
```bash
ollama pull llama2
```
Ou outros modelos: `mistral`, `codellama`, `gemma`, etc.

3. **Inicie o Ollama:**
```bash
ollama serve
```

#### Opção B: Google Gemini (Online - Gratuito)

1. **Obtenha uma API Key gratuita:**
   - Acesse: https://makersuite.google.com/app/apikey
   - Faça login com sua conta Google
   - Clique em "Create API Key"
   - Copie sua chave

2. **Cole a API Key na interface do sistema** quando selecionar o Gemini
3. **Clique em "💾 Salvar"** - Sua chave ficará salva para sempre! 🔐

### 4️⃣ Iniciar o Sistema

**Opção A - Automático (abre navegador sozinho):**
```bash
python iniciar.py
```

**Opção B - Manual:**
```bash
python app.py
```
E acesse: http://localhost:5000

**Opção C - Windows (1 clique):**
```
Duplo clique em: INICIAR.bat
```

**Opção D - Executável (.exe):**
```bash
# Criar o executável primeiro
python criar_executavel.py

# Depois usar
dist/GestaoLigacoes.exe
```

## 📖 Como Usar

### Registrar uma Ligação

1. Preencha o formulário "Nova Ligação"
2. Informe:
   - Nome do cliente
   - Data da ligação
   - Duração
   - Assuntos discutidos
   - Notas detalhadas
   - Próximos passos
3. Clique em "Salvar Ligação"

### Usar o Chat com IA

1. **Selecione a IA** que deseja usar (Ollama ou Gemini)
2. **Configure** (escolha o modelo ou insira API Key)
3. **Faça perguntas**, por exemplo:
   - "Quais são as principais necessidades do cliente João?"
   - "Que assuntos foram mais discutidos esta semana?"
   - "Quais clientes precisam de follow-up urgente?"
   - "Resuma todas as conversas com a empresa XYZ"

### Filtrar Análises por Cliente

- Use o campo "Filtrar por Cliente" no chat
- A IA analisará apenas as ligações daquele cliente específico

## 💡 Exemplos de Perguntas para a IA

- "Quais clientes mencionaram problemas com preços?"
- "Que oportunidades de venda foram identificadas?"
- "Liste os principais pontos de dor dos clientes"
- "Qual cliente teve mais ligações este mês?"
- "Resuma as necessidades do cliente [NOME]"
- "Quais próximos passos estão pendentes?"
- "Que padrões você identifica nas conversas?"

## 🎯 Vantagens

### Ollama
- ✅ 100% gratuito e offline
- ✅ Dados ficam no seu computador
- ✅ Privacidade total
- ✅ Sem limites de uso
- ⚠️ Requer instalação

### Google Gemini
- ✅ 100% gratuito (quota generosa)
- ✅ Não precisa instalar nada localmente
- ✅ Respostas rápidas
- ✅ Acesso de qualquer lugar
- ⚠️ Requer internet

## 📁 Estrutura de Arquivos

```
.
├── app.py                 # Backend (Flask + APIs)
├── templates/
│   └── index.html        # Interface web
├── ligacoes.json         # Dados salvos (criado automaticamente)
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

## 🔧 Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **IA Local**: Ollama
- **IA Online**: Google Gemini API
- **Armazenamento**: JSON (local)

## 🛡️ Segurança e Privacidade

- ✅ Todos os dados ficam salvos **localmente** no seu computador
- ✅ Nenhuma informação é enviada para servidores externos (exceto ao usar Gemini)
- ✅ Você tem controle total dos seus dados
- ✅ API Key do Gemini não é armazenada (apenas em memória)

## 🐛 Solução de Problemas

### Erro ao conectar com Ollama
- Verifique se o Ollama está instalado: `ollama --version`
- Certifique-se de que está rodando: `ollama serve`
- Verifique se baixou algum modelo: `ollama list`

### Erro no Google Gemini
- Verifique se a API Key está correta
- Confirme se tem quota disponível em: https://makersuite.google.com/
- Tente gerar uma nova API Key

### Porta 5000 já está em uso
- Mude a porta no arquivo `app.py` (última linha):
```python
app.run(debug=True, port=5001)  # Mude para 5001 ou outra porta
```

## 📝 Licença

Este projeto é de código aberto e gratuito para uso pessoal e comercial.

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas!

## 📧 Suporte

Se tiver dúvidas ou problemas, abra uma issue no repositório.

---

**Desenvolvido com ❤️ para ajudar você a gerenciar melhor suas ligações com clientes!**

