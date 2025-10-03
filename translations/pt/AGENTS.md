<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:15:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pt"
}
-->
# AGENTS.md

## Visão Geral do Projeto

Data Science for Beginners é um currículo abrangente de 10 semanas e 20 lições, criado pelos Microsoft Azure Cloud Advocates. Este repositório é um recurso de aprendizagem que ensina conceitos fundamentais de ciência de dados através de lições baseadas em projetos, incluindo notebooks Jupyter, questionários interativos e tarefas práticas.

**Principais Tecnologias:**
- **Jupyter Notebooks**: Meio principal de aprendizagem utilizando Python 3
- **Bibliotecas Python**: pandas, numpy, matplotlib para análise e visualização de dados
- **Vue.js 2**: Aplicação de questionários (pasta quiz-app)
- **Docsify**: Gerador de sites de documentação para acesso offline
- **Node.js/npm**: Gestão de pacotes para componentes JavaScript
- **Markdown**: Todo o conteúdo das lições e documentação

**Arquitetura:**
- Repositório educacional multilíngue com extensas traduções
- Estruturado em módulos de lições (1-Introdução até 6-Ciência-de-Dados-no-Mundo-Real)
- Cada lição inclui README, notebooks, tarefas e questionários
- Aplicação de questionários Vue.js independente para avaliações pré/pós-lição
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

### Configuração da Aplicação de Questionários
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
3. Abra os ficheiros `.ipynb` para realizar os exercícios
4. Os notebooks são autossuficientes, com explicações e células de código
5. A maioria dos notebooks utiliza pandas, numpy e matplotlib - certifique-se de que estão instalados

### Estrutura das Lições
Cada lição geralmente contém:
- `README.md` - Conteúdo principal da lição com teoria e exemplos
- `notebook.ipynb` - Exercícios práticos em Jupyter Notebook
- `assignment.ipynb` ou `assignment.md` - Tarefas práticas
- Pasta `solution/` - Notebooks e códigos de solução
- Pasta `images/` - Materiais visuais de suporte

### Desenvolvimento da Aplicação de Questionários
- Aplicação Vue.js 2 com recarregamento automático durante o desenvolvimento
- Questionários armazenados em `quiz-app/src/assets/translations/`
- Cada idioma tem a sua própria pasta de tradução (en, fr, es, etc.)
- A numeração dos questionários começa em 0 e vai até 39 (40 questionários no total)

### Adicionando Traduções
- Traduções vão para a pasta `translations/` na raiz do repositório
- Cada idioma tem uma estrutura completa de lições espelhada do inglês
- Tradução automatizada via GitHub Actions (co-op-translator.yml)

## Instruções de Teste

### Teste da Aplicação de Questionários
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
- Verifique se os ficheiros de dados estão acessíveis e se os resultados são gerados corretamente
- Confirme que as visualizações são renderizadas corretamente

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
- Use nomes de variáveis claros que expliquem os dados analisados
- Inclua células Markdown com explicações antes das células de código
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
- Use componentes de ficheiro único Vue (.vue files)
- Mantenha uma arquitetura baseada em componentes
- Execute `npm run lint` antes de submeter alterações

### Documentação em Markdown
- Use uma hierarquia clara de cabeçalhos (# ## ### etc.)
- Inclua blocos de código com especificadores de linguagem
- Adicione texto alternativo para imagens
- Ligue a lições e recursos relacionados
- Mantenha comprimentos de linha razoáveis para facilitar a leitura

### Organização de Ficheiros
- Conteúdo das lições em pastas numeradas (01-definindo-ciencia-de-dados, etc.)
- Soluções em subpastas dedicadas `solution/`
- Traduções espelham a estrutura em inglês na pasta `translations/`
- Mantenha os ficheiros de dados na pasta `data/` ou em pastas específicas das lições

## Construção e Implantação

### Implantação da Aplicação de Questionários
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Implantação em Azure Static Web Apps
A aplicação quiz-app pode ser implantada no Azure Static Web Apps:
1. Crie um recurso Azure Static Web App
2. Conecte ao repositório GitHub
3. Configure as definições de construção:
   - Localização da aplicação: `quiz-app`
   - Localização de saída: `dist`
4. O fluxo de trabalho do GitHub Actions fará a implantação automática ao fazer push

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
- O Codespaces configura automaticamente o ambiente Python e Node.js
- Abra o repositório no Codespace via interface do GitHub
- Todas as dependências são instaladas automaticamente

## Diretrizes para Pull Requests

### Antes de Submeter
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
  - `[Aplicação de Questionários] Adicionar tradução para alemão`
  - `[Documentação] Atualizar README com novos pré-requisitos`

### Verificações Necessárias
- Certifique-se de que todo o código é executado sem erros
- Verifique se os notebooks são executados completamente
- Confirme que as aplicações Vue.js são construídas com sucesso
- Verifique se os links da documentação funcionam
- Teste a aplicação de questionários se modificada
- Confirme que as traduções mantêm uma estrutura consistente

### Diretrizes de Contribuição
- Siga o estilo e os padrões de código existentes
- Adicione comentários explicativos para lógica complexa
- Atualize a documentação relevante
- Teste alterações em diferentes módulos de lições, se aplicável
- Consulte o ficheiro CONTRIBUTING.md

## Notas Adicionais

### Bibliotecas Comuns Utilizadas
- **pandas**: Manipulação e análise de dados
- **numpy**: Computação numérica
- **matplotlib**: Visualização e criação de gráficos
- **seaborn**: Visualização estatística de dados (algumas lições)
- **scikit-learn**: Aprendizagem de máquina (lições avançadas)

### Trabalhando com Ficheiros de Dados
- Ficheiros de dados localizados na pasta `data/` ou em diretórios específicos das lições
- A maioria dos notebooks espera ficheiros de dados em caminhos relativos
- Ficheiros CSV são o formato de dados principal
- Algumas lições utilizam JSON para exemplos de dados não relacionais

### Suporte Multilíngue
- Mais de 40 traduções de idiomas via GitHub Actions automatizado
- Fluxo de trabalho de tradução em `.github/workflows/co-op-translator.yml`
- Traduções na pasta `translations/` com códigos de idioma
- Traduções de questionários em `quiz-app/src/assets/translations/`

### Opções de Ambiente de Desenvolvimento
1. **Desenvolvimento Local**: Instale Python, Jupyter, Node.js localmente
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo na nuvem
3. **Contêineres de Desenvolvimento do VS Code**: Desenvolvimento local baseado em contêineres
4. **Binder**: Inicie notebooks na nuvem (se configurado)

### Diretrizes de Conteúdo das Lições
- Cada lição é independente, mas constrói conceitos anteriores
- Questionários pré-lição testam conhecimentos prévios
- Questionários pós-lição reforçam o aprendizado
- Tarefas oferecem prática prática
- Sketchnotes fornecem resumos visuais

### Resolução de Problemas Comuns

**Problemas com o Kernel do Jupyter:**
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
- Confirme a compatibilidade da versão do Python (recomenda-se Python 3.7+)
- Certifique-se de que o ambiente virtual está ativado

**Docsify Não Carrega:**
- Verifique se está a servir a partir da raiz do repositório
- Confirme que o ficheiro `index.html` existe
- Certifique-se de que há acesso de rede adequado (porta 3000)

### Considerações de Desempenho
- Conjuntos de dados grandes podem demorar a carregar nos notebooks
- A renderização de visualizações pode ser lenta para gráficos complexos
- O servidor de desenvolvimento Vue.js permite recarregamento rápido para iteração
- As construções de produção são otimizadas e minificadas

### Notas de Segurança
- Não devem ser comprometidos dados sensíveis ou credenciais
- Use variáveis de ambiente para quaisquer chaves de API em lições na nuvem
- Lições relacionadas ao Azure podem exigir credenciais de conta Azure
- Mantenha as dependências atualizadas para correções de segurança

## Contribuindo com Traduções
- Traduções automatizadas geridas via GitHub Actions
- Correções manuais são bem-vindas para melhorar a precisão das traduções
- Siga a estrutura de pastas de tradução existente
- Atualize os links dos questionários para incluir o parâmetro de idioma: `?loc=fr`
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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.