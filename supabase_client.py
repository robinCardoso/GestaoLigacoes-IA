"""
Cliente Supabase para gerenciar dados online
"""
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Cliente Supabase
supabase: Client = None

def init_supabase():
    """Inicializa o cliente Supabase"""
    global supabase
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("[AVISO] Supabase não configurado. Usando armazenamento local.")
        return None
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("[OK] Supabase conectado")
        return supabase
    except Exception as e:
        print(f"[ERRO] Falha ao conectar Supabase: {e}")
        return None

def get_supabase():
    """Retorna o cliente Supabase"""
    global supabase
    
    if supabase is None:
        supabase = init_supabase()
    
    return supabase

# Funções de ligações
def salvar_ligacao(ligacao_data):
    """Salva uma ligação no Supabase"""
    try:
        sb = get_supabase()
        if sb:
            result = sb.table('ligacoes').insert(ligacao_data).execute()
            return result.data
        return None
    except Exception as e:
        print(f"[ERRO] Falha ao salvar ligação: {e}")
        return None

def listar_ligacoes(user_id=None):
    """Lista todas as ligações"""
    try:
        sb = get_supabase()
        if sb:
            query = sb.table('ligacoes').select('*')
            if user_id:
                query = query.eq('user_id', user_id)
            result = query.execute()
            return result.data
        return []
    except Exception as e:
        print(f"[ERRO] Falha ao listar ligações: {e}")
        return []

def deletar_ligacao(ligacao_id):
    """Deleta uma ligação"""
    try:
        sb = get_supabase()
        if sb:
            result = sb.table('ligacoes').delete().eq('id', ligacao_id).execute()
            return result.data
        return None
    except Exception as e:
        print(f"[ERRO] Falha ao deletar ligação: {e}")
        return None

# Funções de conversas IA
def salvar_conversa(conversa_data):
    """Salva uma conversa com IA no Supabase"""
    try:
        sb = get_supabase()
        if sb:
            result = sb.table('conversas_ia').insert(conversa_data).execute()
            return result.data
        return None
    except Exception as e:
        print(f"[ERRO] Falha ao salvar conversa: {e}")
        return None

def listar_conversas(user_id=None, cliente=None):
    """Lista conversas com IA"""
    try:
        sb = get_supabase()
        if sb:
            query = sb.table('conversas_ia').select('*')
            if user_id:
                query = query.eq('user_id', user_id)
            if cliente:
                query = query.eq('cliente', cliente)
            result = query.execute()
            return result.data
        return []
    except Exception as e:
        print(f"[ERRO] Falha ao listar conversas: {e}")
        return []

# Funções de configuração de usuário
def salvar_config_usuario(user_id, config_data):
    """Salva configurações do usuário"""
    try:
        sb = get_supabase()
        if sb:
            # Verificar se já existe configuração
            result = sb.table('user_configs').select('*').eq('user_id', user_id).execute()
            
            if result.data:
                # Atualizar
                result = sb.table('user_configs').update(config_data).eq('user_id', user_id).execute()
            else:
                # Inserir
                config_data['user_id'] = user_id
                result = sb.table('user_configs').insert(config_data).execute()
            
            return result.data
        return None
    except Exception as e:
        print(f"[ERRO] Falha ao salvar configuração: {e}")
        return None

def obter_config_usuario(user_id):
    """Obtém configurações do usuário"""
    try:
        sb = get_supabase()
        if sb:
            result = sb.table('user_configs').select('*').eq('user_id', user_id).execute()
            if result.data:
                return result.data[0]
        return {}
    except Exception as e:
        print(f"[ERRO] Falha ao obter configuração: {e}")
        return {}

