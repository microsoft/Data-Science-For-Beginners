<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:19:15+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "pt"
}
-->
# Guia de Instalação

Este guia irá ajudá-lo a configurar o seu ambiente para trabalhar com o currículo de Ciência de Dados para Iniciantes.

## Índice

- [Pré-requisitos](../..)
- [Opções de Início Rápido](../..)
- [Instalação Local](../..)
- [Verificar a Instalação](../..)

## Pré-requisitos

Antes de começar, deve ter:

- Familiaridade básica com linha de comandos/terminal
- Uma conta GitHub (gratuita)
- Conexão estável à internet para a configuração inicial

## Opções de Início Rápido

### Opção 1: GitHub Codespaces (Recomendado para Iniciantes)

A forma mais fácil de começar é com o GitHub Codespaces, que fornece um ambiente de desenvolvimento completo no seu navegador.

1. Navegue até ao [repositório](https://github.com/microsoft/Data-Science-For-Beginners)
2. Clique no menu suspenso **Code**
3. Selecione o separador **Codespaces**
4. Clique em **Create codespace on main**
5. Aguarde enquanto o ambiente é inicializado (2-3 minutos)

O seu ambiente está agora pronto com todas as dependências pré-instaladas!

### Opção 2: Desenvolvimento Local

Para trabalhar no seu próprio computador, siga as instruções detalhadas abaixo.

## Instalação Local

### Passo 1: Instalar Git

O Git é necessário para clonar o repositório e acompanhar as suas alterações.

**Windows:**
- Faça o download em [git-scm.com](https://git-scm.com/download/win)
- Execute o instalador com as configurações padrão

**macOS:**
- Instale via Homebrew: `brew install git`
- Ou faça o download em [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Passo 2: Clonar o Repositório

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Passo 3: Instalar Python e Jupyter

É necessário Python 3.7 ou superior para as lições de ciência de dados.

**Windows:**
1. Faça o download do Python em [python.org](https://www.python.org/downloads/)
2. Durante a instalação, marque "Add Python to PATH"
3. Verifique a instalação:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Passo 4: Configurar o Ambiente Python

Recomenda-se usar um ambiente virtual para manter as dependências isoladas.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Passo 5: Instalar Pacotes Python

Instale as bibliotecas necessárias para ciência de dados:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Passo 6: Instalar Node.js e npm (Para a Aplicação de Questionários)

A aplicação de questionários requer Node.js e npm.

**Windows/macOS:**
- Faça o download em [nodejs.org](https://nodejs.org/) (recomenda-se a versão LTS)
- Execute o instalador

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Passo 7: Instalar Dependências da Aplicação de Questionários

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Passo 8: Instalar Docsify (Opcional)

Para acesso offline à documentação:

```bash
npm install -g docsify-cli
```

## Verificar a Instalação

### Testar Python e Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

O seu navegador deve abrir com a interface do Jupyter. Agora pode navegar até ao ficheiro `.ipynb` de qualquer lição.

### Testar a Aplicação de Questionários

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

A aplicação de questionários deve estar disponível em `http://localhost:8080` (ou outro porto, caso o 8080 esteja ocupado).

### Testar o Servidor de Documentação

```bash
# From the root directory of the repository
docsify serve
```

A documentação deve estar disponível em `http://localhost:3000`.

## Usar Contêineres de Desenvolvimento do VS Code

Se tiver o Docker instalado, pode usar os Contêineres de Desenvolvimento do VS Code:

1. Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instale o [Visual Studio Code](https://code.visualstudio.com/)
3. Instale a extensão [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Abra o repositório no VS Code
5. Pressione `F1` e selecione "Remote-Containers: Reopen in Container"
6. Aguarde enquanto o contêiner é construído (apenas na primeira vez)

## Próximos Passos

- Explore o [README.md](README.md) para uma visão geral do currículo
- Leia o [USAGE.md](USAGE.md) para fluxos de trabalho e exemplos comuns
- Consulte o [TROUBLESHOOTING.md](TROUBLESHOOTING.md) se encontrar problemas
- Revise o [CONTRIBUTING.md](CONTRIBUTING.md) se quiser contribuir

## Obter Ajuda

Se encontrar problemas:

1. Consulte o guia [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Pesquise problemas existentes no [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Junte-se à nossa [comunidade no Discord](https://aka.ms/ds4beginners/discord)
4. Crie um novo problema com informações detalhadas sobre o seu problema

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.