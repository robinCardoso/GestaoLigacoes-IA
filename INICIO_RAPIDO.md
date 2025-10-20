# ⚡ Início Rápido - 3 Opções

## 🎯 Escolha a forma mais fácil para você:

---

## ✨ Opção 1: SUPER FÁCIL - Clique Duplo! (Recomendado)

### Windows:
```
1. Duplo clique em: INICIAR.bat
2. Aguarde o navegador abrir
3. Pronto! 🎉
```

### Criar Atalho no Desktop:
- Botão direito em `INICIAR.bat` → "Criar atalho"
- Arraste para o Desktop
- Renomeie para "📞 Gestão de Ligações"

---

## 🐍 Opção 2: Python Direto

```bash
# Instalar dependências (apenas primeira vez)
pip install -r requirements.txt

# Iniciar (escolha um):
python iniciar.py    # Abre navegador automaticamente
python app.py        # Forma tradicional
```

---

## 💻 Opção 3: Executável Standalone (.exe)

**Criar uma vez, usar sempre sem Python:**

```bash
# Criar o executável
python criar_executavel.py

# Usar
dist/GestaoLigacoes.exe
```

**Vantagem:** Pode distribuir para outros PCs sem Python!

---

## 🤖 Configurar IA (Escolha 1):

### Opção A: Google Gemini (Mais Fácil)
1. Acesse: https://makersuite.google.com/app/apikey
2. Crie uma API Key gratuita
3. No sistema: Selecione "Gemini" 
4. Cole a chave e clique "💾 Salvar"
5. **✨ Pronto! A chave fica salva para sempre!**

### Opção B: Ollama (Privado)
```bash
# 1. Instalar: https://ollama.ai/download
# 2. Baixar modelo
ollama pull llama2
# 3. Iniciar
ollama serve
```

---

## 📝 Primeiro Uso

1. **Registre uma ligação:**
   - Preencha o formulário
   - Clique "Salvar"

2. **Teste a IA:**
   - Selecione Gemini ou Ollama
   - Pergunte: "Resuma todas as ligações"
   - Veja a mágica acontecer! ✨

---

## 🎬 Exemplo Completo

```
1. Duplo clique em INICIAR.bat
   ↓
2. Sistema abre em http://localhost:5000
   ↓
3. Registre sua primeira ligação:
   - Cliente: João Silva
   - Data: Hoje
   - Notas: "Cliente quer renovar contrato"
   ↓
4. Clique em "Gemini"
   ↓
5. Cole sua API Key e clique "Salvar"
   ↓
6. Pergunte: "O que o João precisa?"
   ↓
7. IA responde com análise completa! 🎉
```

---

## 💡 Dicas

- ✅ API Key do Gemini fica **salva automaticamente**
- ✅ Seus dados ficam em `ligacoes.json` (faça backup!)
- ✅ Use o filtro de cliente para análises específicas
- ✅ Quanto mais detalhada a nota, melhor a análise da IA

---

## 🆘 Problemas?

| Problema | Solução |
|----------|---------|
| Python não encontrado | Instale: https://www.python.org/downloads/ |
| Porta 5000 em uso | Mude a porta no `app.py` (última linha) |
| Ollama não conecta | Execute `ollama serve` em outro terminal |
| Gemini dá erro | Verifique se a API Key está correta |

---

## 📚 Quer Saber Mais?

- **README.md** - Documentação completa
- **COMO_USAR.md** - Guia detalhado com exemplos
- **INSTALACAO_DESKTOP.md** - Criar executável e instalador

---

## 🚀 COMEÇAR AGORA:

**Windows:**
```
Duplo clique → INICIAR.bat
```

**Outros:**
```bash
pip install -r requirements.txt
python iniciar.py
```

**Simples assim!** 🎉

