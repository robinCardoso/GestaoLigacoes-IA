-- Tabela de ligações
CREATE TABLE IF NOT EXISTS ligacoes (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    cliente TEXT NOT NULL,
    data DATE NOT NULL,
    duracao TEXT,
    assuntos TEXT,
    notas TEXT,
    proximos_passos TEXT,
    data_registro TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de conversas com IA
CREATE TABLE IF NOT EXISTS conversas_ia (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    ia TEXT NOT NULL,
    modelo TEXT NOT NULL,
    cliente TEXT,
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de configurações de usuário
CREATE TABLE IF NOT EXISTS user_configs (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT UNIQUE NOT NULL,
    gemini_api_key TEXT,
    ollama_model TEXT DEFAULT 'mistral',
    save_ai_conversations BOOLEAN DEFAULT false,
    retention_days INTEGER DEFAULT 90,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Índices para melhorar performance
CREATE INDEX IF NOT EXISTS idx_ligacoes_user_id ON ligacoes(user_id);
CREATE INDEX IF NOT EXISTS idx_ligacoes_cliente ON ligacoes(cliente);
CREATE INDEX IF NOT EXISTS idx_ligacoes_data ON ligacoes(data);
CREATE INDEX IF NOT EXISTS idx_conversas_user_id ON conversas_ia(user_id);
CREATE INDEX IF NOT EXISTS idx_conversas_cliente ON conversas_ia(cliente);
CREATE INDEX IF NOT EXISTS idx_user_configs_user_id ON user_configs(user_id);

-- Row Level Security (RLS)
ALTER TABLE ligacoes ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversas_ia ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_configs ENABLE ROW LEVEL SECURITY;

-- Políticas de segurança (permitir acesso apenas aos próprios dados)
CREATE POLICY "Users can view own ligacoes" ON ligacoes
    FOR SELECT USING (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can insert own ligacoes" ON ligacoes
    FOR INSERT WITH CHECK (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can update own ligacoes" ON ligacoes
    FOR UPDATE USING (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can delete own ligacoes" ON ligacoes
    FOR DELETE USING (user_id = current_setting('app.user_id', true));

-- Repetir para conversas_ia
CREATE POLICY "Users can view own conversas" ON conversas_ia
    FOR SELECT USING (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can insert own conversas" ON conversas_ia
    FOR INSERT WITH CHECK (user_id = current_setting('app.user_id', true));

-- Repetir para user_configs
CREATE POLICY "Users can view own config" ON user_configs
    FOR SELECT USING (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can insert own config" ON user_configs
    FOR INSERT WITH CHECK (user_id = current_setting('app.user_id', true));

CREATE POLICY "Users can update own config" ON user_configs
    FOR UPDATE USING (user_id = current_setting('app.user_id', true));

