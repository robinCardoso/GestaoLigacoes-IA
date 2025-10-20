# 🚀 Sistema de Gestão de Ligações com IA

Sistema web 100% online para gerenciar ligações de clientes com assistente de IA integrado (Google Gemini).

[![Deploy no Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/robinCardoso/GestaoLigacoes-IA)

## ✨ Funcionalidades

- 📞 **Registro de Ligações**: Grave detalhes de todas as conversas com clientes
- 🤖 **Assistente IA**: Use Google Gemini para analisar conversas e obter insights
- 💬 **Chat Dedicado**: Interface full-screen para conversas com a IA
- 📊 **Histórico**: Armazene e consulte todas as ligações e conversas
- 🔍 **Busca**: Filtros por cliente, data e muito mais
- 📱 **Responsivo**: Funciona perfeitamente em desktop e mobile
- ☁️ **100% Online**: Deploy no Vercel + dados no Supabase

## 🛠️ Tecnologias

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **IA**: Google Gemini API
- **Banco de Dados**: Supabase (PostgreSQL)
- **Deploy**: Vercel
- **Autenticação**: Session-based (UUID por usuário)

## 🚀 Deploy

### 1. Criar conta no Supabase

1. Acesse [supabase.com](https://supabase.com) e crie uma conta
2. Crie um novo projeto
3. Copie a URL e a chave pública (anon key)

### 2. Configurar banco de dados

No Supabase SQL Editor, execute o script `sql/create_tables.sql`:

```sql
-- Copie e cole o conteúdo de sql/create_tables.sql
```

### 3. Deploy no Vercel

1. Faça fork deste repositório
2. Acesse [vercel.com](https://vercel.com) e importe o projeto
3. Configure as variáveis de ambiente:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-publica-aqui
SECRET_KEY=uma-chave-secreta-aleatoria
```

4. Deploy! 🎉

## 🔧 Desenvolvimento Local

### Pré-requisitos

- Python 3.8+
- Conta no Supabase (ou use armazenamento local)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/robinCardoso/GestaoLigacoes-IA.git
cd GestaoLigacoes-IA

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp env.example .env
# Edite .env com suas credenciais

# Execute o servidor
python app.py
```

Acesse: `http://localhost:5000`

## 📝 Configuração

### Google Gemini API

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova API Key
3. Configure no sistema em **⚙️ Configurações**

### Armazenamento

- **Online (Supabase)**: Configure `SUPABASE_URL` e `SUPABASE_KEY`
- **Local (Fallback)**: Sem configuração, usa arquivos JSON localmente

## 🎯 Como Usar

### 1. Registrar uma Ligação

1. Preencha os campos:
   - Nome do Cliente
   - Data da Ligação
   - Duração
   - Assuntos Discutidos
   - Notas
   - Próximos Passos
2. Clique em **Salvar Ligação**

### 2. Usar o Assistente IA

1. Configure sua API Key do Gemini em **⚙️ Configurações**
2. Digite sua pergunta no chat
3. A IA terá acesso a todas as ligações do cliente selecionado
4. Receba insights e sugestões

### 3. Chat Full-Screen

- Clique em **💬 Abrir Chat em Tela Cheia**
- Aproveite uma interface dedicada para conversas longas

## 📊 Estrutura do Banco (Supabase)

### Tabela: `ligacoes`
- `id`: ID único
- `user_id`: ID do usuário
- `cliente`: Nome do cliente
- `data`: Data da ligação
- `duracao`: Duração
- `assuntos`: Assuntos discutidos
- `notas`: Notas adicionais
- `proximos_passos`: Próximos passos
- `data_registro`: Data do registro
- `created_at`: Data de criação
- `updated_at`: Data de atualização

### Tabela: `conversas_ia`
- `id`: ID único
- `user_id`: ID do usuário
- `ia`: Nome da IA (gemini)
- `modelo`: Modelo usado
- `cliente`: Cliente relacionado
- `pergunta`: Pergunta feita
- `resposta`: Resposta da IA
- `data_hora`: Data e hora da conversa

### Tabela: `user_configs`
- `id`: ID único
- `user_id`: ID do usuário (único)
- `gemini_api_key`: Chave API do Gemini (criptografada)
- `save_ai_conversations`: Salvar conversas (boolean)
- `retention_days`: Dias de retenção

## 🔒 Segurança

- ✅ Row Level Security (RLS) habilitado no Supabase
- ✅ API Keys criptografadas com Base64
- ✅ Cada usuário acessa apenas seus próprios dados
- ✅ Session-based authentication
- ✅ HTTPS em produção (Vercel)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

## 🙏 Agradecimentos

- Google Gemini pela IA gratuita e poderosa
- Supabase pelo banco de dados gratuito
- Vercel pelo hosting gratuito
- Comunidade open source

## 📞 Contato

- GitHub: [@robinCardoso](https://github.com/robinCardoso)
- Projeto: [GestaoLigacoes-IA](https://github.com/robinCardoso/GestaoLigacoes-IA)

---

**Feito com ❤️ para melhorar o relacionamento com clientes**
