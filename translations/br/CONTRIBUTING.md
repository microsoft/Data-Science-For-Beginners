<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:54:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "br"
}
-->
# Contribuindo para Ciência de Dados para Iniciantes

Obrigado pelo seu interesse em contribuir para o currículo de Ciência de Dados para Iniciantes! Agradecemos contribuições da comunidade.

## Índice

- [Código de Conduta](../..)
- [Como Posso Contribuir?](../..)
- [Primeiros Passos](../..)
- [Diretrizes de Contribuição](../..)
- [Processo de Pull Request](../..)
- [Diretrizes de Estilo](../..)
- [Acordo de Licença de Contribuidor](../..)

## Código de Conduta

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Para mais informações, veja as [Perguntas Frequentes sobre o Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/)  
ou entre em contato pelo e-mail [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer dúvidas ou comentários adicionais.

## Como Posso Contribuir?

### Relatar Bugs

Antes de criar relatórios de bugs, verifique os problemas existentes para evitar duplicatas. Ao criar um relatório de bug, inclua o máximo de detalhes possível:

- **Use um título claro e descritivo**
- **Descreva os passos exatos para reproduzir o problema**
- **Forneça exemplos específicos** (trechos de código, capturas de tela)
- **Descreva o comportamento observado e o esperado**
- **Inclua detalhes do seu ambiente** (SO, versão do Python, navegador)

### Sugerir Melhorias

Sugestões de melhorias são bem-vindas! Ao sugerir melhorias:

- **Use um título claro e descritivo**
- **Forneça uma descrição detalhada da melhoria sugerida**
- **Explique por que essa melhoria seria útil**
- **Liste quaisquer recursos semelhantes em outros projetos, se aplicável**

### Contribuir para a Documentação

Melhorias na documentação são sempre apreciadas:

- **Corrigir erros de digitação e gramática**
- **Melhorar a clareza das explicações**
- **Adicionar documentação ausente**
- **Atualizar informações desatualizadas**
- **Adicionar exemplos ou casos de uso**

### Contribuir com Código

Aceitamos contribuições de código, incluindo:

- **Novas lições ou exercícios**
- **Correções de bugs**
- **Melhorias em notebooks existentes**
- **Novos conjuntos de dados ou exemplos**
- **Aprimoramentos no aplicativo de quiz**

## Primeiros Passos

### Pré-requisitos

Antes de contribuir, certifique-se de ter:

1. Uma conta no GitHub
2. Git instalado no seu sistema
3. Python 3.7+ e Jupyter instalados
4. Node.js e npm (para contribuições no aplicativo de quiz)
5. Familiaridade com a estrutura do currículo

Veja [INSTALLATION.md](INSTALLATION.md) para instruções detalhadas de configuração.

### Fork e Clone

1. **Faça um fork do repositório** no GitHub  
2. **Clone seu fork** localmente:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Adicione o remoto upstream**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Criar um Branch

Crie um novo branch para seu trabalho:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Convenções de nomenclatura de branch:  
- `feature/` - Novos recursos ou lições  
- `fix/` - Correções de bugs  
- `docs/` - Alterações na documentação  
- `refactor/` - Refatoração de código  

## Diretrizes de Contribuição

### Para Conteúdo de Lições

Ao contribuir com lições ou modificar as existentes:

1. **Siga a estrutura existente**:  
   - README.md com o conteúdo da lição  
   - Notebook Jupyter com exercícios  
   - Tarefa (se aplicável)  
   - Link para quizzes pré e pós-lição  

2. **Inclua os seguintes elementos**:  
   - Objetivos de aprendizado claros  
   - Explicações passo a passo  
   - Exemplos de código com comentários  
   - Exercícios para prática  
   - Links para recursos adicionais  

3. **Garanta acessibilidade**:  
   - Use linguagem clara e simples  
   - Forneça texto alternativo para imagens  
   - Inclua comentários no código  
   - Considere diferentes estilos de aprendizado  

### Para Notebooks Jupyter

1. **Limpe todas as saídas** antes de fazer o commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Inclua células de markdown** com explicações  

3. **Use formatação consistente**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Teste completamente seu notebook** antes de enviar  

### Para Código Python

Siga as diretrizes de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```
  

### Para Contribuições no Aplicativo de Quiz

Ao modificar o aplicativo de quiz:

1. **Teste localmente**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Execute o linter**:  
   ```bash
   npm run lint
   ```
  
3. **Construa com sucesso**:  
   ```bash
   npm run build
   ```
  
4. **Siga o guia de estilo do Vue.js** e os padrões existentes  

### Para Traduções

Ao adicionar ou atualizar traduções:

1. Siga a estrutura na pasta `translations/`  
2. Use o código do idioma como nome da pasta (ex.: `pt` para Português)  
3. Mantenha a mesma estrutura de arquivos da versão em inglês  
4. Atualize os links dos quizzes para incluir o parâmetro de idioma: `?loc=pt`  
5. Teste todos os links e a formatação  

## Processo de Pull Request

### Antes de Enviar

1. **Atualize seu branch** com as alterações mais recentes:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Teste suas alterações**:  
   - Execute todos os notebooks modificados  
   - Teste o aplicativo de quiz, se modificado  
   - Verifique se todos os links funcionam  
   - Confira erros de ortografia e gramática  

3. **Faça commit das suas alterações**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Escreva mensagens de commit claras:  
   - Use tempo presente ("Adiciona recurso" em vez de "Adicionou recurso")  
   - Use modo imperativo ("Mover cursor para..." em vez de "Move cursor para...")  
   - Limite a primeira linha a 72 caracteres  
   - Referencie problemas e pull requests quando relevante  

4. **Envie para seu fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Criando o Pull Request

1. Acesse o [repositório](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Clique em "Pull requests" → "New pull request"  
3. Clique em "compare across forks"  
4. Selecione seu fork e branch  
5. Clique em "Create pull request"  

### Formato do Título do PR

Use títulos claros e descritivos seguindo este formato:  
```
[Component] Brief description
```
  
Exemplos:  
- `[Lesson 7] Corrigir erro de importação no notebook Python`  
- `[Quiz App] Adicionar tradução para alemão`  
- `[Docs] Atualizar README com novos pré-requisitos`  
- `[Fix] Corrigir caminho de dados na lição de visualização`  

### Descrição do PR

Inclua na descrição do seu PR:

- **O que**: Quais alterações você fez?  
- **Por que**: Por que essas alterações são necessárias?  
- **Como**: Como você implementou as alterações?  
- **Testes**: Como você testou as alterações?  
- **Capturas de tela**: Inclua capturas de tela para alterações visuais  
- **Problemas relacionados**: Link para problemas relacionados (ex.: "Fixes #123")  

### Processo de Revisão

1. **Verificações automáticas** serão executadas no seu PR  
2. **Os mantenedores revisarão** sua contribuição  
3. **Aborde o feedback** fazendo commits adicionais  
4. Uma vez aprovado, um **mantenedor fará o merge** do seu PR  

### Após o Merge do Seu PR

1. Exclua seu branch:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Atualize seu fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Diretrizes de Estilo

### Markdown

- Use níveis de cabeçalho consistentes  
- Inclua linhas em branco entre seções  
- Use blocos de código com especificadores de linguagem:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Adicione texto alternativo às imagens: `![Texto alternativo](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.br.png)`  
- Mantenha os comprimentos das linhas razoáveis (cerca de 80-100 caracteres)  

### Python

- Siga o guia de estilo PEP 8  
- Use nomes de variáveis significativos  
- Adicione docstrings às funções  
- Inclua dicas de tipo quando apropriado:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Siga o guia de estilo do Vue.js 2  
- Use a configuração do ESLint fornecida  
- Escreva componentes modulares e reutilizáveis  
- Adicione comentários para lógica complexa  

### Organização de Arquivos

- Mantenha arquivos relacionados juntos  
- Use nomes de arquivos descritivos  
- Siga a estrutura de diretórios existente  
- Não faça commit de arquivos desnecessários (.DS_Store, .pyc, node_modules, etc.)  

## Acordo de Licença de Contribuidor

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA), declarando que você tem o direito de, e realmente concede a nós os direitos de usar sua contribuição. Para detalhes, visite  
https://cla.microsoft.com.

Quando você enviar um pull request, um CLA-bot determinará automaticamente se você precisa fornecer um CLA e decorará o PR adequadamente (ex.: etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez em todos os repositórios que usam nosso CLA.

## Dúvidas?

- Confira nosso [Canal Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Junte-se à nossa [comunidade no Discord](https://aka.ms/ds4beginners/discord)  
- Revise os [problemas existentes](https://github.com/microsoft/Data-Science-For-Beginners/issues) e [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Obrigado!

Suas contribuições tornam este currículo melhor para todos. Obrigado por dedicar seu tempo para contribuir!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.