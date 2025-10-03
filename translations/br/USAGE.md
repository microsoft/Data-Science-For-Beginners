<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:01:14+00:00",
  "source_file": "USAGE.md",
  "language_code": "br"
}
-->
# Guia de Uso

Este guia fornece exemplos e fluxos de trabalho comuns para usar o currículo de Ciência de Dados para Iniciantes.

## Índice

- [Como Usar Este Currículo](../..)
- [Trabalhando com as Lições](../..)
- [Trabalhando com Jupyter Notebooks](../..)
- [Usando o Aplicativo de Quiz](../..)
- [Fluxos de Trabalho Comuns](../..)
- [Dicas para Autodidatas](../..)
- [Dicas para Professores](../..)

## Como Usar Este Currículo

Este currículo foi projetado para ser flexível e pode ser usado de várias maneiras:

- **Aprendizado autônomo**: Trabalhe nas lições de forma independente, no seu próprio ritmo
- **Instrução em sala de aula**: Use como um curso estruturado com orientação
- **Grupos de estudo**: Aprenda colaborativamente com colegas
- **Formato de workshop**: Sessões intensivas de aprendizado de curto prazo

## Trabalhando com as Lições

Cada lição segue uma estrutura consistente para maximizar o aprendizado:

### Estrutura da Lição

1. **Quiz pré-lição**: Teste seus conhecimentos existentes
2. **Sketchnote** (Opcional): Resumo visual dos conceitos principais
3. **Vídeo** (Opcional): Conteúdo de vídeo complementar
4. **Lição escrita**: Conceitos principais e explicações
5. **Jupyter Notebook**: Exercícios práticos de codificação
6. **Tarefa**: Pratique o que aprendeu
7. **Quiz pós-lição**: Reforce sua compreensão

### Exemplo de Fluxo de Trabalho para uma Lição

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Trabalhando com Jupyter Notebooks

### Iniciando o Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Executando Células do Notebook

1. **Executar uma célula**: Pressione `Shift + Enter` ou clique no botão "Run"
2. **Executar todas as células**: Selecione "Cell" → "Run All" no menu
3. **Reiniciar kernel**: Selecione "Kernel" → "Restart" se encontrar problemas

### Exemplo: Trabalhando com Dados em um Notebook

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Salvando Seu Trabalho

- O Jupyter salva automaticamente periodicamente
- Salve manualmente: Pressione `Ctrl + S` (ou `Cmd + S` no macOS)
- Seu progresso é salvo no arquivo `.ipynb`

## Usando o Aplicativo de Quiz

### Executando o Aplicativo de Quiz Localmente

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Realizando os Quizzes

1. Os quizzes pré-lição estão vinculados no início de cada lição
2. Os quizzes pós-lição estão vinculados no final de cada lição
3. Cada quiz tem 3 perguntas
4. Os quizzes são projetados para reforçar o aprendizado, não para testar exaustivamente

### Numeração dos Quizzes

- Os quizzes são numerados de 0 a 39 (40 quizzes no total)
- Cada lição geralmente tem um quiz pré e pós
- Os URLs dos quizzes incluem o número do quiz: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Fluxos de Trabalho Comuns

### Fluxo de Trabalho 1: Caminho para Iniciantes

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Fluxo de Trabalho 2: Aprendizado Específico por Tópico

Se você estiver interessado em um tópico específico:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Fluxo de Trabalho 3: Aprendizado Baseado em Projetos

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Fluxo de Trabalho 4: Ciência de Dados na Nuvem

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Dicas para Autodidatas

### Mantenha-se Organizado

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Pratique Regularmente

- Reserve tempo dedicado diariamente ou semanalmente
- Complete pelo menos uma lição por semana
- Revise lições anteriores periodicamente

### Engaje-se com a Comunidade

- Junte-se à [comunidade no Discord](https://aka.ms/ds4beginners/discord)
- Participe do canal #Data-Science-for-Beginners no Discord [Discussões no Discord](https://aka.ms/ds4beginners/discord)
- Compartilhe seu progresso e faça perguntas

### Construa Seus Próprios Projetos

Após concluir as lições, aplique os conceitos em projetos pessoais:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Dicas para Professores

### Configuração da Sala de Aula

1. Revise [for-teachers.md](for-teachers.md) para orientações detalhadas
2. Configure um ambiente compartilhado (GitHub Classroom ou Codespaces)
3. Estabeleça um canal de comunicação (Discord, Slack ou Teams)

### Planejamento de Lições

**Cronograma sugerido de 10 semanas:**

- **Semana 1-2**: Introdução (Lições 1-4)
- **Semana 3-4**: Trabalhando com Dados (Lições 5-8)
- **Semana 5-6**: Visualização de Dados (Lições 9-13)
- **Semana 7-8**: Ciclo de Vida da Ciência de Dados (Lições 14-16)
- **Semana 9**: Ciência de Dados na Nuvem (Lições 17-19)
- **Semana 10**: Aplicações Reais & Projetos Finais (Lição 20)

### Executando Docsify para Acesso Offline

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Avaliação de Tarefas

- Revise os notebooks dos alunos para exercícios concluídos
- Verifique a compreensão por meio das pontuações dos quizzes
- Avalie os projetos finais usando os princípios do ciclo de vida da ciência de dados

### Criando Tarefas

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Trabalhando Offline

### Baixar Recursos

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Executar Documentação Localmente

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Executar Aplicativo de Quiz Localmente

```bash
cd quiz-app
npm run serve
```

## Acessando Conteúdo Traduzido

As traduções estão disponíveis em mais de 40 idiomas:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Cada tradução mantém a mesma estrutura da versão em inglês.

## Recursos Adicionais

### Continue Aprendendo

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Caminhos de aprendizado adicionais
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Recursos para estudantes
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Fórum da comunidade

### Currículos Relacionados

- [AI para Iniciantes](https://aka.ms/ai-beginners)
- [ML para Iniciantes](https://aka.ms/ml-beginners)
- [Desenvolvimento Web para Iniciantes](https://aka.ms/webdev-beginners)
- [IA Generativa para Iniciantes](https://aka.ms/genai-beginners)

## Obtendo Ajuda

- Consulte [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para problemas comuns
- Pesquise [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Junte-se ao nosso [Discord](https://aka.ms/ds4beginners/discord)
- Revise [CONTRIBUTING.md](CONTRIBUTING.md) para relatar problemas ou contribuir

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.