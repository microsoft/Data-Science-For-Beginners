<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:16:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "br"
}
-->
# AGENTS.md

## Visão Geral do Projeto

Data Science for Beginners é um currículo abrangente de 10 semanas e 20 lições criado pelos Advocates de Nuvem da Microsoft Azure. O repositório é um recurso de aprendizado que ensina conceitos fundamentais de ciência de dados por meio de lições baseadas em projetos, incluindo notebooks Jupyter, quizzes interativos e tarefas práticas.

**Principais Tecnologias:**
- **Jupyter Notebooks**: Meio principal de aprendizado usando Python 3
- **Bibliotecas Python**: pandas, numpy, matplotlib para análise e visualização de dados
- **Vue.js 2**: Aplicativo de quiz (pasta quiz-app)
- **Docsify**: Gerador de site de documentação para acesso offline
- **Node.js/npm**: Gerenciamento de pacotes para componentes JavaScript
- **Markdown**: Todo o conteúdo das lições e documentação

**Arquitetura:**
- Repositório educacional multilíngue com extensas traduções
- Estruturado em módulos de lições (1-Introdução até 6-Ciência-de-Dados-na-Prática)
- Cada lição inclui README, notebooks, tarefas e quizzes
- Aplicativo de quiz Vue.js independente para avaliações pré/pós-lição
- Suporte para GitHub Codespaces e contêineres de desenvolvimento do VS Code

## Comandos de Configuração

### Configuração do Repositório
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Configuração do Ambiente Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Configuração do Aplicativo de Quiz
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Servidor de Documentação Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Configuração de Projetos de Visualização
Para projetos de visualização como meaningful-visualizations (lição 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Fluxo de Trabalho de Desenvolvimento

### Trabalhando com Jupyter Notebooks
1. Inicie o Jupyter na raiz do repositório: `jupyter notebook`
2. Navegue até a pasta da lição desejada
3. Abra os arquivos `.ipynb` para realizar os exercícios
4. Os notebooks são autossuficientes, com explicações e células de código
5. A maioria dos notebooks utiliza pandas, numpy e matplotlib - certifique-se de que estão instalados

### Estrutura das Lições
Cada lição geralmente contém:
- `README.md` - Conteúdo principal da lição com teoria e exemplos
- `notebook.ipynb` - Exercícios práticos no Jupyter Notebook
- `assignment.ipynb` ou `assignment.md` - Tarefas práticas
- Pasta `solution/` - Notebooks e códigos de solução
- Pasta `images/` - Materiais visuais de suporte

### Desenvolvimento do Aplicativo de Quiz
- Aplicativo Vue.js 2 com recarregamento automático durante o desenvolvimento
- Quizzes armazenados em `quiz-app/src/assets/translations/`
- Cada idioma tem sua própria pasta de tradução (en, fr, es, etc.)
- A numeração dos quizzes começa em 0 e vai até 39 (40 quizzes no total)

### Adicionando Traduções
- Traduções vão na pasta `translations/` na raiz do repositório
- Cada idioma tem a estrutura completa das lições espelhada do inglês
- Tradução automatizada via GitHub Actions (co-op-translator.yml)

## Instruções de Teste

### Teste do Aplicativo de Quiz
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Teste de Notebooks
- Não existe um framework de teste automatizado para notebooks
- Validação manual: Execute todas as células em sequência para garantir que não há erros
- Verifique se os arquivos de dados estão acessíveis e os resultados são gerados corretamente
- Certifique-se de que as visualizações são renderizadas corretamente

### Teste de Documentação
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Verificações de Qualidade de Código
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Diretrizes de Estilo de Código

### Python (Jupyter Notebooks)
- Siga as diretrizes de estilo PEP 8 para código Python
- Use nomes de variáveis claros que expliquem os dados sendo analisados
- Inclua células markdown com explicações antes das células de código
- Mantenha as células de código focadas em conceitos ou operações únicas
- Use pandas para manipulação de dados, matplotlib para visualização
- Padrão comum de importação:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Siga o guia de estilo e as melhores práticas do Vue.js 2
- Configuração do ESLint em `quiz-app/package.json`
- Use componentes Vue de arquivo único (.vue files)
- Mantenha uma arquitetura baseada em componentes
- Execute `npm run lint` antes de enviar alterações

### Documentação Markdown
- Use uma hierarquia clara de cabeçalhos (# ## ### etc.)
- Inclua blocos de código com especificadores de linguagem
- Adicione texto alternativo para imagens
- Link para lições e recursos relacionados
- Mantenha os comprimentos das linhas razoáveis para facilitar a leitura

### Organização de Arquivos
- Conteúdo das lições em pastas numeradas (01-defining-data-science, etc.)
- Soluções em subpastas dedicadas `solution/`
- Traduções espelham a estrutura em inglês na pasta `translations/`
- Mantenha os arquivos de dados na pasta `data/` ou em pastas específicas de lições

## Construção e Implantação

### Implantação do Aplicativo de Quiz
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Implantação em Azure Static Web Apps
O quiz-app pode ser implantado no Azure Static Web Apps:
1. Crie um recurso Azure Static Web App
2. Conecte ao repositório GitHub
3. Configure as configurações de build:
   - Localização do aplicativo: `quiz-app`
   - Localização de saída: `dist`
4. O workflow do GitHub Actions fará a implantação automática ao enviar alterações

### Site de Documentação
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- O repositório inclui configuração de contêiner de desenvolvimento
- Codespaces configura automaticamente o ambiente Python e Node.js
- Abra o repositório no Codespace via interface do GitHub
- Todas as dependências são instaladas automaticamente

## Diretrizes para Pull Requests

### Antes de Enviar
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formato do Título do PR
- Use títulos claros e descritivos
- Formato: `[Componente] Breve descrição`
- Exemplos:
  - `[Lição 7] Corrigir erro de importação no notebook Python`
  - `[Aplicativo de Quiz] Adicionar tradução em alemão`
  - `[Docs] Atualizar README com novos pré-requisitos`

### Verificações Necessárias
- Certifique-se de que todo o código funciona sem erros
- Verifique se os notebooks executam completamente
- Confirme que os aplicativos Vue.js são construídos com sucesso
- Verifique se os links da documentação funcionam
- Teste o aplicativo de quiz se modificado
- Confirme que as traduções mantêm uma estrutura consistente

### Diretrizes de Contribuição
- Siga o estilo e os padrões de código existentes
- Adicione comentários explicativos para lógica complexa
- Atualize a documentação relevante
- Teste alterações em diferentes módulos de lições, se aplicável
- Revise o arquivo CONTRIBUTING.md

## Notas Adicionais

### Bibliotecas Comuns Utilizadas
- **pandas**: Manipulação e análise de dados
- **numpy**: Computação numérica
- **matplotlib**: Visualização e plotagem de dados
- **seaborn**: Visualização estatística de dados (algumas lições)
- **scikit-learn**: Aprendizado de máquina (lições avançadas)

### Trabalhando com Arquivos de Dados
- Arquivos de dados localizados na pasta `data/` ou em diretórios específicos de lições
- A maioria dos notebooks espera arquivos de dados em caminhos relativos
- Arquivos CSV são o formato de dados principal
- Algumas lições utilizam JSON para exemplos de dados não relacionais

### Suporte Multilíngue
- Mais de 40 traduções de idiomas via GitHub Actions automatizado
- Workflow de tradução em `.github/workflows/co-op-translator.yml`
- Traduções na pasta `translations/` com códigos de idioma
- Traduções de quizzes em `quiz-app/src/assets/translations/`

### Opções de Ambiente de Desenvolvimento
1. **Desenvolvimento Local**: Instale Python, Jupyter, Node.js localmente
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo baseado em nuvem
3. **Contêineres de Desenvolvimento do VS Code**: Desenvolvimento local baseado em contêiner
4. **Binder**: Inicie notebooks na nuvem (se configurado)

### Diretrizes de Conteúdo das Lições
- Cada lição é independente, mas constrói conceitos anteriores
- Quizzes pré-lição testam conhecimento prévio
- Quizzes pós-lição reforçam o aprendizado
- Tarefas fornecem prática prática
- Sketchnotes fornecem resumos visuais

### Solução de Problemas Comuns

**Problemas com Kernel do Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Falhas na Instalação do npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Erros de Importação em Notebooks:**
- Verifique se todas as bibliotecas necessárias estão instaladas
- Confira a compatibilidade da versão do Python (recomendado Python 3.7+)
- Certifique-se de que o ambiente virtual está ativado

**Docsify Não Carregando:**
- Verifique se você está servindo a partir da raiz do repositório
- Confira se o arquivo `index.html` existe
- Certifique-se de que há acesso adequado à rede (porta 3000)

### Considerações de Desempenho
- Conjuntos de dados grandes podem levar tempo para carregar nos notebooks
- A renderização de visualizações pode ser lenta para gráficos complexos
- O servidor de desenvolvimento Vue.js permite recarregamento rápido para iteração rápida
- Builds de produção são otimizados e minificados

### Notas de Segurança
- Nenhum dado sensível ou credenciais deve ser enviado
- Use variáveis de ambiente para quaisquer chaves de API em lições na nuvem
- Lições relacionadas ao Azure podem exigir credenciais de conta Azure
- Mantenha as dependências atualizadas para patches de segurança

## Contribuindo com Traduções
- Traduções automatizadas gerenciadas via GitHub Actions
- Correções manuais são bem-vindas para precisão das traduções
- Siga a estrutura de pastas de tradução existente
- Atualize os links dos quizzes para incluir o parâmetro de idioma: `?loc=fr`
- Teste as lições traduzidas para garantir a renderização adequada

## Recursos Relacionados
- Currículo principal: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Fórum de Discussão: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Outros currículos da Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Manutenção do Projeto
- Atualizações regulares para manter o conteúdo atual
- Contribuições da comunidade são bem-vindas
- Problemas rastreados no GitHub
- PRs revisados pelos mantenedores do currículo
- Revisões e atualizações de conteúdo mensais

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.