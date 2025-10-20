# 🖥️ Instalação para Desktop - Versão Executável

## 📌 Duas Formas de Usar

### ⚡ Opção 1: MAIS FÁCIL - Usando o Script BAT (Recomendado)

**Não precisa criar executável! Basta clicar duas vezes!**

1. **Certifique-se que o Python está instalado:**
   - Baixe em: https://www.python.org/downloads/
   - **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação

2. **Clique duas vezes no arquivo:**
   ```
   INICIAR.bat
   ```

3. **Pronto!** 
   - O script instalará automaticamente as dependências (na primeira vez)
   - Abrirá o navegador automaticamente
   - Sistema pronto para uso!

4. **Criar atalho no Desktop (opcional):**
   - Clique com botão direito em `INICIAR.bat`
   - "Enviar para" → "Área de trabalho (criar atalho)"
   - Agora você pode iniciar com 1 clique!

---

### 🏗️ Opção 2: Criar Executável Standalone (.exe)

**Para criar uma versão que NÃO precisa do Python instalado:**

#### Passo 1: Preparar o Ambiente

```bash
# Instalar dependências (incluindo PyInstaller)
pip install -r requirements.txt
```

#### Passo 2: Criar o Executável

**Forma Automática (Recomendada):**
```bash
python criar_executavel.py
```

**Forma Manual:**
```bash
pyinstaller --name=GestaoLigacoes --onefile --windowed --add-data="templates;templates" app.py
```

#### Passo 3: Localizar o Executável

O executável estará em:
```
dist/GestaoLigacoes.exe
```

#### Passo 4: Distribuir

**Para distribuir para outros computadores:**

1. Copie a pasta `dist` inteira
2. Os arquivos criados automaticamente ficarão ao lado do .exe:
   - `ligacoes.json` - Dados das ligações
   - `config.json` - Configurações (API Key salva aqui)

3. **O executável pode ser usado em qualquer Windows 10/11 sem precisar instalar Python!**

---

## 🎯 Comparação das Opções

| Característica | Script BAT | Executável .exe |
|----------------|------------|-----------------|
| **Facilidade** | ⭐⭐⭐⭐⭐ Muito fácil | ⭐⭐⭐ Médio |
| **Requer Python** | ✅ Sim | ❌ Não |
| **Tamanho** | ~1 KB | ~15-30 MB |
| **Velocidade inicialização** | Rápido | Mais rápido |
| **Distribuir para outros** | ❌ Precisa Python | ✅ Funciona direto |
| **Atualizar** | ✅ Muito fácil | ⚠️ Recriar .exe |

---

## 🎨 Personalização

### Adicionar Ícone Personalizado ao Executável

1. **Crie ou baixe um ícone (.ico):**
   - Tamanho recomendado: 256x256 pixels
   - Formato: .ico

2. **Salve como:** `icone.ico` na pasta do projeto

3. **Recrie o executável com:**
   ```bash
   pyinstaller --name=GestaoLigacoes --onefile --windowed --add-data="templates;templates" --icon=icone.ico app.py
   ```

### Criar Instalador (Avançado)

Para criar um instalador tipo "setup.exe", use **Inno Setup**:

1. **Baixe Inno Setup:**
   - https://jrsoftware.org/isdl.php

2. **Crie um script .iss básico:**

```iss
[Setup]
AppName=Sistema de Gestão de Ligações com IA
AppVersion=1.0
DefaultDirName={autopf}\GestaoLigacoes
DefaultGroupName=Gestão de Ligações
OutputDir=.
OutputBaseFilename=Instalador_GestaoLigacoes

[Files]
Source: "dist\GestaoLigacoes.exe"; DestDir: "{app}"
Source: "README.md"; DestDir: "{app}"
Source: "COMO_USAR.md"; DestDir: "{app}"

[Icons]
Name: "{group}\Gestão de Ligações"; Filename: "{app}\GestaoLigacoes.exe"
Name: "{autodesktop}\Gestão de Ligações"; Filename: "{app}\GestaoLigacoes.exe"
```

3. **Compile o script no Inno Setup**
4. **Resultado:** `Instalador_GestaoLigacoes.exe`

---

## 🚀 Atalho no Desktop (Qualquer Opção)

### Para o Script BAT:
1. Clique com botão direito em `INICIAR.bat`
2. "Criar atalho"
3. Arraste o atalho para o Desktop
4. (Opcional) Renomeie para "📞 Gestão de Ligações"

### Para o Executável:
1. Vá até `dist/GestaoLigacoes.exe`
2. Clique com botão direito
3. "Enviar para" → "Área de trabalho (criar atalho)"

---

## 🔧 Solução de Problemas

### Script BAT não funciona
- **Erro "Python não encontrado":**
  - Reinstale o Python marcando "Add to PATH"
  - Ou adicione manualmente ao PATH

- **Erro ao instalar dependências:**
  ```bash
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

### Executável não inicia
- **Antivírus bloqueando:**
  - Adicione exceção para o arquivo
  - PyInstaller às vezes é detectado como falso positivo

- **Erro "Failed to execute script":**
  - Certifique-se que a pasta `templates` foi incluída
  - Recrie o executável com o comando completo

- **Porta 5000 em uso:**
  - Feche outros programas que possam usar essa porta
  - Ou modifique a porta no `app.py`

### Dados não salvam
- Verifique se tem permissão de escrita na pasta
- Execute como administrador (botão direito → "Executar como administrador")

---

## 📦 Distribuição Profissional

**Se quiser distribuir para clientes:**

1. **Crie uma pasta de distribuição:**
   ```
   GestaoLigacoes_v1.0/
   ├── GestaoLigacoes.exe
   ├── README.md
   ├── COMO_USAR.md
   └── ligacoes.exemplo.json
   ```

2. **Compacte em .zip:**
   - Nome: `GestaoLigacoes_v1.0_Windows.zip`

3. **Inclua instruções:**
   - Como usar
   - Como obter API Key do Gemini
   - Como instalar Ollama (opcional)

---

## 💡 Recomendação Final

**Para uso pessoal:** Use o **Script BAT** (INICIAR.bat)
- Mais fácil
- Mais rápido de atualizar
- Menor tamanho

**Para distribuir:** Crie o **Executável .exe**
- Funciona sem Python
- Mais profissional
- Plug-and-play

---

## 🎯 Começar Agora

**Opção mais fácil (2 cliques):**
1. Duplo clique em `INICIAR.bat`
2. Aguarde abrir o navegador
3. Comece a usar! 🚀

**Dúvidas?** Consulte o README.md completo!

