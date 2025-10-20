# 🚀 Guia de Deploy - Sistema de Gestão de Ligações

Este guia mostra como fazer o deploy do sistema no Vercel + Supabase.

## 📋 Pré-requisitos

- Conta no [Supabase](https://supabase.com) (gratuita)
- Conta no [Vercel](https://vercel.com) (gratuita)
- Conta no [Google AI Studio](https://makersuite.google.com) para API Key do Gemini (gratuita)
- Repositório no GitHub

## 🗄️ Passo 1: Configurar Supabase

### 1.1 Criar Projeto

1. Acesse [supabase.com](https://supabase.com)
2. Clique em **New Project**
3. Escolha:
   - **Nome**: `gestao-ligacoes` (ou outro nome)
   - **Database Password**: (crie uma senha forte)
   - **Region**: Escolha a mais próxima de você
4. Aguarde a criação do projeto (~2 minutos)

### 1.2 Criar Tabelas

1. No painel do Supabase, vá em **SQL Editor**
2. Clique em **New Query**
3. Copie e cole o conteúdo de `sql/create_tables.sql`
4. Clique em **Run** para executar

### 1.3 Obter Credenciais

1. Vá em **Settings** → **API**
2. Copie:
   - **Project URL**: `https://xxx.supabase.co`
   - **anon/public key**: `eyJhbGci...`

## ☁️ Passo 2: Deploy no Vercel

### 2.1 Preparar Repositório

```bash
# Fazer commit das alterações
git add .
git commit -m "feat: preparar para deploy online"
git push origin feature/deploy-vercel-supabase
```

### 2.2 Importar no Vercel

1. Acesse [vercel.com](https://vercel.com)
2. Clique em **Add New** → **Project**
3. Importe seu repositório do GitHub
4. Escolha a branch `feature/deploy-vercel-supabase`

### 2.3 Configurar Variáveis de Ambiente

Na seção **Environment Variables**, adicione:

| Nome | Valor | Descrição |
|------|-------|-----------|
| `SUPABASE_URL` | `https://xxx.supabase.co` | URL do seu projeto Supabase |
| `SUPABASE_KEY` | `eyJhbGci...` | Chave pública do Supabase |
| `SECRET_KEY` | `[gere uma chave aleatória]` | Para sessions Flask |

**Gerar SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

### 2.4 Deploy

1. Clique em **Deploy**
2. Aguarde o build (~2-3 minutos)
3. Acesse a URL gerada: `https://seu-app.vercel.app` 🎉

## 🔑 Passo 3: Configurar Gemini API

### 3.1 Obter API Key

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Clique em **Create API Key**
3. Copie a chave gerada

### 3.2 Configurar no Sistema

1. Acesse seu app no Vercel
2. Clique em **⚙️ Configurações**
3. Cole a API Key do Gemini
4. Clique em **💾 Salvar**

## ✅ Passo 4: Testar

### 4.1 Testar Ligações

1. Vá para a página inicial
2. Registre uma ligação de teste
3. Verifique se aparece na lista
4. Teste filtros e busca

### 4.2 Testar IA

1. Na página inicial, digite uma pergunta no chat
2. Verifique se a IA responde
3. Teste o chat full-screen

### 4.3 Verificar Supabase

1. Volte ao Supabase
2. Vá em **Table Editor**
3. Veja se os dados estão sendo salvos nas tabelas:
   - `ligacoes`
   - `conversas_ia`
   - `user_configs`

## 🔧 Troubleshooting

### Erro: "Supabase não configurado"

- Verifique se as variáveis `SUPABASE_URL` e `SUPABASE_KEY` estão corretas no Vercel
- Faça um **Redeploy** após adicionar variáveis

### Erro: "IA não responde"

- Verifique se a API Key do Gemini foi configurada
- Teste a API Key no [Google AI Studio](https://makersuite.google.com)
- Verifique o console do navegador (F12) para erros

### Erro: "Dados não salvam"

- Verifique se as tabelas foram criadas corretamente no Supabase
- Veja os logs no Vercel (**Deployments** → seu deploy → **Logs**)
- Verifique Row Level Security (RLS) no Supabase

### Build falha no Vercel

- Verifique se `requirements.txt` está correto
- Veja os logs de build no Vercel
- Certifique-se de que `vercel.json` está presente

## 📊 Monitoramento

### Vercel

- **Analytics**: Ver quantas pessoas acessam
- **Logs**: Ver erros em tempo real
- **Speed Insights**: Ver performance

### Supabase

- **Table Editor**: Ver dados salvos
- **Database**: Ver uso de armazenamento
- **API Logs**: Ver requisições

## 💰 Limites Gratuitos

### Vercel (Hobby Plan)
- ✅ 100 GB de largura de banda/mês
- ✅ Builds ilimitados
- ✅ Subdomínio vercel.app gratuito
- ✅ HTTPS automático

### Supabase (Free Tier)
- ✅ 500 MB de banco de dados
- ✅ 1 GB de armazenamento de arquivos
- ✅ 2 GB de largura de banda/mês
- ✅ 50.000 usuários ativos mensais

### Google Gemini
- ✅ 60 requisições/minuto
- ✅ 1.500 requisições/dia
- ✅ Totalmente gratuito (Flash model)

## 🚀 Próximos Passos

1. Configure um domínio personalizado no Vercel
2. Ative autenticação com Supabase Auth
3. Configure backups automáticos
4. Adicione analytics personalizado
5. Configure alertas de erro

## 📞 Suporte

Se tiver problemas:

1. Verifique a [documentação do Vercel](https://vercel.com/docs)
2. Verifique a [documentação do Supabase](https://supabase.com/docs)
3. Abra uma [issue no GitHub](https://github.com/robinCardoso/GestaoLigacoes-IA/issues)

---

**Sucesso! 🎉 Seu sistema está online e pronto para uso!**

