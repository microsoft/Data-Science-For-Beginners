<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:37:47+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "br"
}
-->
# Guia de Solução de Problemas

Este guia fornece soluções para problemas comuns que você pode encontrar ao trabalhar com o currículo de Ciência de Dados para Iniciantes.

## Índice

- [Problemas com Python e Jupyter](../..)
- [Problemas com Pacotes e Dependências](../..)
- [Problemas com Jupyter Notebook](../..)
- [Problemas com o Aplicativo de Quiz](../..)
- [Problemas com Git e GitHub](../..)
- [Problemas com a Documentação Docsify](../..)
- [Problemas com Dados e Arquivos](../..)
- [Problemas de Desempenho](../..)
- [Obtendo Ajuda Adicional](../..)

## Problemas com Python e Jupyter

### Python Não Encontrado ou Versão Errada

**Problema:** `python: command not found` ou versão errada do Python

**Solução:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Solução para Windows:**
1. Reinstale o Python em [python.org](https://www.python.org/)
2. Durante a instalação, marque "Add Python to PATH"
3. Reinicie seu terminal/prompt de comando

### Problemas de Ativação do Ambiente Virtual

**Problema:** O ambiente virtual não ativa

**Solução:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Verifique a ativação:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problemas com o Kernel do Jupyter

**Problema:** "Kernel não encontrado" ou "Kernel continua morrendo"

**Solução:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problema:** Versão errada do Python no Jupyter

**Solução:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problemas com Pacotes e Dependências

### Erros de Importação

**Problema:** `ModuleNotFoundError: No module named 'pandas'` (ou outros pacotes)

**Solução:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Falhas na Instalação com Pip

**Problema:** `pip install` falha com erros de permissão

**Solução:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problema:** `pip install` falha com erros de certificado SSL

**Solução:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Conflitos de Versão de Pacotes

**Problema:** Versões incompatíveis de pacotes

**Solução:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Problemas com Jupyter Notebook

### Jupyter Não Inicia

**Problema:** Comando `jupyter notebook` não encontrado

**Solução:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Não Carrega ou Não Salva

**Problema:** "Notebook falhou ao carregar" ou erros ao salvar

**Solução:**

1. Verifique as permissões do arquivo
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Verifique se há corrupção no arquivo
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Limpe o cache do Jupyter
```bash
jupyter notebook --clear-cache
```

### Célula Não Executa

**Problema:** Célula travada em "In [*]" ou demora muito

**Solução:**

1. **Interrompa o kernel**: Clique no botão "Interrupt" ou pressione `I, I`
2. **Reinicie o kernel**: Menu Kernel → Restart
3. **Verifique loops infinitos** no seu código
4. **Limpe a saída**: Cell → All Output → Clear

### Gráficos Não Aparecem

**Problema:** Gráficos do `matplotlib` não aparecem no notebook

**Solução:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa para gráficos interativos:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problemas com o Aplicativo de Quiz

### npm install Falha

**Problema:** Erros durante `npm install`

**Solução:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Aplicativo de Quiz Não Inicia

**Problema:** `npm run serve` falha

**Solução:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Porta Já em Uso

**Problema:** "Porta 8080 já está em uso"

**Solução:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Quiz Não Carrega ou Página em Branco

**Problema:** O aplicativo de quiz carrega, mas mostra uma página em branco

**Solução:**

1. Verifique erros no console do navegador (F12)
2. Limpe o cache e os cookies do navegador
3. Tente outro navegador
4. Certifique-se de que o JavaScript está habilitado
5. Verifique se bloqueadores de anúncios estão interferindo

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problemas com Git e GitHub

### Git Não Reconhecido

**Problema:** `git: command not found`

**Solução:**

**Windows:**
- Instale o Git em [git-scm.com](https://git-scm.com/)
- Reinicie o terminal após a instalação

**macOS:**

> **Nota:** Se você não tiver o Homebrew instalado, siga as instruções em [https://brew.sh/](https://brew.sh/) para instalá-lo primeiro.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Falha ao Clonar

**Problema:** `git clone` falha com erros de autenticação

**Solução:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permissão Negada (publickey)

**Problema:** Autenticação com chave SSH falha

**Solução:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Problemas com a Documentação Docsify

### Comando Docsify Não Encontrado

**Problema:** `docsify: command not found`

**Solução:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Documentação Não Carrega

**Problema:** Docsify serve, mas o conteúdo não carrega

**Solução:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Imagens Não Aparecem

**Problema:** Imagens mostram ícone de link quebrado

**Solução:**

1. Verifique se os caminhos das imagens são relativos
2. Certifique-se de que os arquivos de imagem existem no repositório
3. Limpe o cache do navegador
4. Verifique se as extensões dos arquivos correspondem (sensível a maiúsculas/minúsculas em alguns sistemas)

## Problemas com Dados e Arquivos

### Erros de Arquivo Não Encontrado

**Problema:** `FileNotFoundError` ao carregar dados

**Solução:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### Erros ao Ler CSV

**Problema:** Erros ao ler arquivos CSV

**Solução:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Erros de Memória com Grandes Conjuntos de Dados

**Problema:** `MemoryError` ao carregar arquivos grandes

**Solução:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Problemas de Desempenho

### Desempenho Lento do Notebook

**Problema:** Notebooks executam muito lentamente

**Solução:**

1. **Reinicie o kernel e limpe a saída**
   - Kernel → Restart & Clear Output

2. **Feche notebooks não utilizados**

3. **Otimize o código:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Amostre grandes conjuntos de dados:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Navegador Travando

**Problema:** Navegador trava ou fica sem resposta

**Solução:**

1. Feche abas não utilizadas
2. Limpe o cache do navegador
3. Aumente a memória do navegador (Chrome: `chrome://settings/system`)
4. Use o JupyterLab em vez disso:
```bash
pip install jupyterlab
jupyter lab
```

## Obtendo Ajuda Adicional

### Antes de Pedir Ajuda

1. Consulte este guia de solução de problemas
2. Pesquise [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Revise [INSTALLATION.md](INSTALLATION.md) e [USAGE.md](USAGE.md)
4. Tente buscar a mensagem de erro online

### Como Pedir Ajuda

Ao criar um problema ou pedir ajuda, inclua:

1. **Sistema Operacional**: Windows, macOS ou Linux (qual distribuição)
2. **Versão do Python**: Execute `python --version`
3. **Mensagem de Erro**: Copie a mensagem de erro completa
4. **Passos para Reproduzir**: O que você fez antes de o erro ocorrer
5. **O que Você Já Tentou**: Soluções que você já tentou

**Exemplo:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Recursos da Comunidade

- **GitHub Issues**: [Crie um problema](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Participe da nossa comunidade](https://aka.ms/ds4beginners/discord)
- **Discussões**: [Discussões no GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Fóruns de Q&A](https://docs.microsoft.com/answers/)

### Documentação Relacionada

- [INSTALLATION.md](INSTALLATION.md) - Instruções de configuração
- [USAGE.md](USAGE.md) - Como usar o currículo
- [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir
- [README.md](README.md) - Visão geral do projeto

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.