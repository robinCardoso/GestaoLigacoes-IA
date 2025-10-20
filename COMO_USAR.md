# 🎯 Guia Rápido de Uso

## Início Rápido (3 passos)

### 1️⃣ Instalar
```bash
pip install -r requirements.txt
```

### 2️⃣ Iniciar
```bash
python app.py
```

### 3️⃣ Acessar
Abra o navegador em: **http://localhost:5000**

---

## 🤖 Configuração das IAs

### Opção 1: Ollama (Recomendado para Privacidade)

**Instalação do Ollama:**

1. **Windows:**
   - Baixe: https://ollama.ai/download/windows
   - Execute o instalador
   
2. **Instale um modelo (escolha um):**
```bash
# Llama 2 (recomendado, bom equilíbrio)
ollama pull llama2

# Mistral (mais rápido)
ollama pull mistral

# Gemma (do Google)
ollama pull gemma
```

3. **Inicie o servidor:**
```bash
ollama serve
```
Deixe esta janela aberta!

4. **No sistema:** Selecione "Ollama" e escolha o modelo

---

### Opção 2: Google Gemini (Sem Instalação)

1. **Obter API Key (grátis):**
   - Acesse: https://makersuite.google.com/app/apikey
   - Faça login com Google
   - Clique em "Create API Key"
   - Copie a chave gerada

2. **No sistema:**
   - Selecione "Google Gemini"
   - Cole a API Key no campo
   - Pronto!

---

## 💬 Exemplos Práticos de Uso

### Registrar uma Ligação

```
Cliente: João Silva
Data: 17/10/2025
Duração: 25 minutos
Assuntos: Renovação de contrato, aumento de usuários
Notas: Cliente demonstrou interesse em expandir de 50 para 100 usuários.
       Mencionou preocupação com custos. Pediu proposta até sexta.
Próximos Passos: Enviar proposta comercial com desconto progressivo
```

### Perguntas para a IA

**Análise Geral:**
- "Quais clientes estão com renovação pendente?"
- "Liste os 3 principais problemas mencionados pelos clientes"
- "Que oportunidades de upsell foram identificadas?"

**Análise Específica:**
- "Resuma todas as conversas com o João Silva"
- "O que o cliente XYZ precisa com urgência?"
- "Quais foram os assuntos da última ligação com Maria?"

**Insights Estratégicos:**
- "Que padrões você identifica nas objeções de preço?"
- "Quais clientes mencionaram a concorrência?"
- "Liste clientes que podem estar em risco de cancelamento"

---

## 🎨 Dicas de Uso

### ✅ Boas Práticas

1. **Seja detalhado nas notas:** Quanto mais informação, melhores os insights da IA
2. **Registre logo após a ligação:** Enquanto a memória está fresca
3. **Use o filtro de cliente:** Para análises específicas mais precisas
4. **Experimente ambas as IAs:** Veja qual te atende melhor

### 📊 Maximize os Insights

**Ao registrar, inclua:**
- ✅ Sentimento do cliente (satisfeito, preocupado, irritado)
- ✅ Objeções mencionadas
- ✅ Interesse em novos produtos/serviços
- ✅ Prazos importantes
- ✅ Concorrentes citados
- ✅ Decisores envolvidos

**Perguntas poderosas para a IA:**
- "Analise o nível de satisfação dos clientes"
- "Identifique sinais de churn (cancelamento)"
- "Que features foram mais solicitadas?"
- "Compare as necessidades do cliente A vs B"

---

## ⚡ Atalhos

- **Enter no chat:** Envia mensagem
- **Filtro vazio:** IA analisa TODAS as ligações
- **Filtro preenchido:** IA analisa apenas 1 cliente

---

## 🔥 Casos de Uso

### Para Vendas
- Identificar oportunidades de cross-sell
- Rastrear objeções comuns
- Preparar reuniões com contexto completo

### Para Customer Success
- Monitorar satisfação do cliente
- Identificar clientes em risco
- Planejar ações proativas

### Para Gestão
- Analisar tendências
- Identificar problemas recorrentes
- Tomar decisões baseadas em dados

---

## 🚨 Solução Rápida de Problemas

| Problema | Solução |
|----------|---------|
| Ollama não conecta | Execute `ollama serve` em um terminal |
| Modelo não aparece | Execute `ollama pull llama2` |
| Gemini dá erro | Verifique se a API Key está correta |
| Porta em uso | Mude a porta no `app.py` (última linha) |
| Chat não responde | Verifique a IA selecionada e configurada |

---

## 📞 Dúvidas?

Leia o **README.md** completo para mais detalhes!

