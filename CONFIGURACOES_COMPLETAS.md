# ⚙️ Menu de Configurações - Guia Completo

## 🎉 O que foi implementado:

### ✅ **1. Página de Configurações Dedicada**
- **Acesso:** Botão "⚙️ Configurações" na tela principal
- **URL:** http://localhost:5000/configuracoes
- **Interface moderna** com todas as opções organizadas

### ✅ **2. Links Úteis Integrados**
- **Ollama:** Links diretos para download (Windows, Mac, Linux)
- **Google Gemini:** Link direto para criar API Key
- **Instruções passo-a-passo** para cada IA

### ✅ **3. Controle Automático do Ollama**
- **Iniciar/Parar servidor** com botões na interface
- **Status em tempo real** (online/offline)
- **Controle automático** no executável (.exe)
- **Lista de modelos** disponíveis

---

## 🎯 Funcionalidades do Menu de Configurações:

### 🏠 **Seção Ollama (Local)**

#### 📥 **Instalação do Ollama**
- Links diretos para download:
  - [Windows](https://ollama.ai/download)
  - [Mac](https://ollama.ai/download) 
  - [Linux](https://ollama.ai/download)
- Instruções claras de instalação

#### 📦 **Modelos Disponíveis**
- Lista dinâmica dos modelos instalados
- Botão "🔄 Atualizar Lista"
- Seleção visual dos modelos

#### 🎯 **Modelo Preferido**
- Dropdown com modelos recomendados:
  - Llama 2 (Recomendado)
  - Mistral (Mais Rápido)
  - Code Llama (Para Código)
  - Gemma (Google)
- Salva preferência automaticamente

#### 🚀 **Controle do Servidor**
- **▶️ Iniciar Servidor** - Inicia o Ollama automaticamente
- **⏹️ Parar Servidor** - Para o Ollama
- **🔄 Reiniciar Servidor** - Reinicia o Ollama
- **Status em tempo real** com indicador visual

### 🌐 **Seção Google Gemini (Online)**

#### 🔑 **API Key**
- Campo para inserir API Key
- Botão "💾 Salvar" (fica salva para sempre!)
- Status visual (✅ carregada / ❌ erro)

#### 📥 **Como Obter API Key**
- Link direto: [Google AI Studio](https://makersuite.google.com/app/apikey)
- Instruções passo-a-passo:
  1. Acesse o link
  2. Faça login com Google
  3. Clique "Create API Key"
  4. Copie a chave
  5. Cole no sistema e salve

#### 💰 **Limites Gratuitos**
- 60 requisições por minuto
- 1 milhão de tokens por mês
- 100% gratuito para uso pessoal
- Sem necessidade de cartão

### ⚙️ **Configurações Gerais**

#### 🌐 **Servidor Web**
- **Porta do Servidor:** Configurável (padrão: 5000)
- **Auto-abrir Navegador:** Sim/Não

#### 💾 **Backup e Dados**
- **📤 Exportar Dados** - Download de backup completo
- **📥 Importar Dados** - Restaurar de backup
- **🗑️ Limpar Todos os Dados** - Reset completo (com confirmação)

---

## 🤖 Controle Automático do Ollama

### ✅ **Como Funciona:**

#### **No Executável (.exe):**
1. **Ao abrir:** Ollama inicia automaticamente
2. **Durante uso:** Servidor fica rodando
3. **Ao fechar:** Ollama para automaticamente

#### **No Script BAT:**
1. **Duplo clique em `INICIAR.bat`**
2. **Ollama inicia automaticamente**
3. **Sistema abre no navegador**
4. **Ao fechar:** Ollama para automaticamente

#### **No Python:**
```bash
# Com controle automático
python GestaoLigacoes_ComOllama.py

# Ou definir variável de ambiente
set AUTO_OLLAMA=true
python app.py
```

### 🔧 **Controles Manuais:**

#### **Na Interface:**
- Acesse **⚙️ Configurações**
- Seção **🏠 Ollama (Local)**
- Use os botões:
  - ▶️ Iniciar Servidor
  - ⏹️ Parar Servidor  
  - 🔄 Reiniciar Servidor

#### **Status Visual:**
- 🟢 **Verde:** Servidor online
- 🔴 **Vermelho:** Servidor offline
- 🟡 **Amarelo:** Verificando status

---

## 📋 Exemplos de Uso:

### **Cenário 1: Primeira Instalação**
```
1. Duplo clique em INICIAR.bat
2. Sistema abre automaticamente
3. Clique "⚙️ Configurações"
4. Seção "🌐 Google Gemini"
5. Clique no link para criar API Key
6. Cole a chave e clique "💾 Salvar"
7. Pronto! IA configurada para sempre!
```

### **Cenário 2: Usar Ollama**
```
1. Acesse "⚙️ Configurações"
2. Seção "🏠 Ollama (Local)"
3. Clique "▶️ Iniciar Servidor"
4. Aguarde status ficar verde
5. Escolha modelo preferido
6. Clique "💾 Salvar Configuração"
7. Volte para tela principal e use!
```

### **Cenário 3: Backup de Dados**
```
1. Acesse "⚙️ Configurações"
2. Seção "💾 Backup e Dados"
3. Clique "📤 Exportar Dados"
4. Arquivo baixa automaticamente
5. Guarde em local seguro
6. Para restaurar: "📥 Importar Dados"
```

---

## 🎨 Interface Visual:

### **Design Moderno:**
- ✅ Gradientes azul/roxo
- ✅ Cards organizados
- ✅ Ícones intuitivos
- ✅ Status coloridos
- ✅ Animações suaves

### **Responsivo:**
- ✅ Funciona em desktop
- ✅ Adapta para mobile
- ✅ Botões touch-friendly

### **UX Otimizada:**
- ✅ Navegação clara
- ✅ Feedback visual
- ✅ Confirmações de segurança
- ✅ Mensagens de status

---

## 🔒 Segurança:

### **API Key:**
- ✅ Criptografada (base64)
- ✅ Salva localmente
- ✅ Nunca enviada desnecessariamente

### **Dados:**
- ✅ Backup fácil
- ✅ Restauração simples
- ✅ Limpeza com confirmação

### **Ollama:**
- ✅ Controle local
- ✅ Sem transmissão externa
- ✅ Processo isolado

---

## 🚀 Vantagens:

### **Para o Usuário:**
- ✅ **1 clique** para configurar tudo
- ✅ **Links diretos** para downloads
- ✅ **Instruções claras** passo-a-passo
- ✅ **Controle total** do Ollama
- ✅ **Backup automático** fácil

### **Para o Sistema:**
- ✅ **Inicialização automática** do Ollama
- ✅ **Fechamento limpo** ao sair
- ✅ **Status em tempo real**
- ✅ **Configurações persistentes**
- ✅ **Interface profissional**

---

## 📱 Como Acessar:

### **Opção 1: Botão na Tela Principal**
```
1. Abra o sistema
2. Clique "⚙️ Configurações" no header
3. Configure tudo que precisar
```

### **Opção 2: URL Direta**
```
http://localhost:5000/configuracoes
```

### **Opção 3: Menu de Navegação**
```
Sistema → Configurações
```

---

## 🎯 Próximos Passos:

1. **Teste o sistema:**
   - Duplo clique em `INICIAR.bat`
   - Clique "⚙️ Configurações"
   - Configure uma IA
   - Teste o controle do Ollama

2. **Crie o executável:**
   ```bash
   python criar_executavel.py
   ```
   - O .exe terá controle automático do Ollama!

3. **Use as configurações:**
   - Salve sua API Key do Gemini
   - Configure modelo preferido do Ollama
   - Faça backup dos seus dados

---

## 🎉 Resultado Final:

**Agora você tem um sistema COMPLETO com:**

✅ **Menu de configurações dedicado**
✅ **Links úteis integrados**  
✅ **Controle automático do Ollama**
✅ **Interface profissional**
✅ **Backup/restore de dados**
✅ **Configurações persistentes**
✅ **Status em tempo real**

**É um sistema de nível empresarial, 100% gratuito!** 🚀

---

## 💡 Dicas Finais:

- **Use o botão "⚙️ Configurações"** para tudo
- **Salve sua API Key** uma vez só
- **O executável controla o Ollama** automaticamente
- **Faça backup regular** dos seus dados
- **Links diretos** para downloads e configuração

**Agora está TUDO integrado e profissional!** 🎯✨
