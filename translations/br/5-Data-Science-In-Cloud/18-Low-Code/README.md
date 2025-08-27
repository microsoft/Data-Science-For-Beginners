<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "14b2a7f1c63202920bd98eeb913f5614",
  "translation_date": "2025-08-27T17:43:02+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "br"
}
-->
# Ciência de Dados na Nuvem: O caminho "Low code/No code"

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Ciência de Dados na Nuvem: Low Code - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Índice:

- [Ciência de Dados na Nuvem: O caminho "Low code/No code"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Quiz Pré-Aula](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Introdução](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 O que é o Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 O Projeto de Previsão de Insuficiência Cardíaca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 O Conjunto de Dados de Insuficiência Cardíaca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Treinamento Low code/No code de um modelo no Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Criar um workspace no Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Recursos de Computação](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Escolhendo as opções certas para seus recursos de computação](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Criando um cluster de computação](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Carregando o Conjunto de Dados](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Treinamento Low code/No code com AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Implantação Low code/No code do modelo e consumo do endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Implantação do modelo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Consumo do endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Desafio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Quiz Pós-Aula](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Revisão e Autoestudo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Tarefa](../../../../5-Data-Science-In-Cloud/18-Low-Code)

## [Quiz Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/34)
## 1. Introdução
### 1.1 O que é o Azure Machine Learning?

A plataforma de nuvem Azure oferece mais de 200 produtos e serviços projetados para ajudar você a criar novas soluções. Cientistas de dados gastam muito esforço explorando e pré-processando dados, além de testar vários tipos de algoritmos de treinamento de modelos para produzir modelos precisos. Essas tarefas consomem tempo e frequentemente utilizam de forma ineficiente hardware de computação caro.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) é uma plataforma baseada em nuvem para construir e operar soluções de aprendizado de máquina no Azure. Ela inclui uma ampla gama de recursos e capacidades que ajudam cientistas de dados a preparar dados, treinar modelos, publicar serviços preditivos e monitorar seu uso. Mais importante, ela aumenta a eficiência ao automatizar muitas das tarefas demoradas associadas ao treinamento de modelos; e permite o uso de recursos de computação baseados na nuvem que escalam de forma eficaz para lidar com grandes volumes de dados, incorrendo em custos apenas quando realmente utilizados.

O Azure ML fornece todas as ferramentas que desenvolvedores e cientistas de dados precisam para seus fluxos de trabalho de aprendizado de máquina. Isso inclui:

- **Azure Machine Learning Studio**: um portal web no Azure Machine Learning para opções de treinamento, implantação, automação, rastreamento e gerenciamento de ativos com pouco ou nenhum código. O estúdio se integra ao SDK do Azure Machine Learning para uma experiência contínua.
- **Jupyter Notebooks**: prototipagem rápida e teste de modelos de aprendizado de máquina.
- **Azure Machine Learning Designer**: permite arrastar e soltar módulos para construir experimentos e, em seguida, implantar pipelines em um ambiente de baixo código.
- **Interface de AutoML**: automatiza tarefas iterativas de desenvolvimento de modelos de aprendizado de máquina, permitindo construir modelos com alta escala, eficiência e produtividade, mantendo a qualidade do modelo.
- **Rotulagem de Dados**: uma ferramenta assistida de aprendizado de máquina para rotular dados automaticamente.
- **Extensão de aprendizado de máquina para o Visual Studio Code**: fornece um ambiente de desenvolvimento completo para construir e gerenciar projetos de aprendizado de máquina.
- **CLI de aprendizado de máquina**: fornece comandos para gerenciar recursos do Azure ML a partir da linha de comando.
- **Integração com frameworks de código aberto** como PyTorch, TensorFlow, Scikit-learn e muitos outros para treinar, implantar e gerenciar o processo de aprendizado de máquina de ponta a ponta.
- **MLflow**: uma biblioteca de código aberto para gerenciar o ciclo de vida de seus experimentos de aprendizado de máquina. **MLFlow Tracking** é um componente do MLflow que registra e rastreia métricas de execução de treinamento e artefatos de modelo, independentemente do ambiente do experimento.

### 1.2 O Projeto de Previsão de Insuficiência Cardíaca:

Não há dúvida de que criar e construir projetos é a melhor maneira de testar suas habilidades e conhecimentos. Nesta lição, vamos explorar duas maneiras diferentes de construir um projeto de ciência de dados para a previsão de ataques de insuficiência cardíaca no Azure ML Studio, através de Low code/No code e do Azure ML SDK, conforme mostrado no esquema a seguir:

![project-schema](../../../../translated_images/project-schema.736f6e403f321eb48d10242b3f4334dc6ccf0eabef8ff87daf52b89781389fcb.br.png)

Cada abordagem tem seus próprios prós e contras. O método Low code/No code é mais fácil para começar, pois envolve a interação com uma interface gráfica (GUI), sem necessidade de conhecimento prévio de código. Esse método permite testar rapidamente a viabilidade do projeto e criar um POC (Prova de Conceito). No entanto, à medida que o projeto cresce e precisa estar pronto para produção, não é viável criar recursos por meio de GUI. É necessário automatizar programaticamente tudo, desde a criação de recursos até a implantação de um modelo. É aqui que o conhecimento do uso do Azure ML SDK se torna crucial.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Conhecimento de código | Não necessário  | Necessário                |
| Tempo de desenvolvimento | Rápido e fácil  | Depende da experiência com código |
| Pronto para produção | Não               | Sim                       |

### 1.3 O Conjunto de Dados de Insuficiência Cardíaca:

As doenças cardiovasculares (DCVs) são a principal causa de morte no mundo, representando 31% de todas as mortes globalmente. Fatores de risco ambientais e comportamentais, como uso de tabaco, dieta não saudável e obesidade, inatividade física e uso nocivo de álcool, podem ser usados como características para modelos de estimativa. Ser capaz de estimar a probabilidade de desenvolvimento de uma DCV pode ser muito útil para prevenir ataques em pessoas de alto risco.

O Kaggle disponibilizou publicamente um [conjunto de dados de insuficiência cardíaca](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), que usaremos neste projeto. Você pode baixar o conjunto de dados agora. Este é um conjunto de dados tabular com 13 colunas (12 características e 1 variável alvo) e 299 linhas.

|    | Nome da variável          | Tipo            | Descrição                                               | Exemplo           |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 1  | age                       | numérico        | Idade do paciente                                       | 25                |
| 2  | anaemia                   | booleano        | Redução de glóbulos vermelhos ou hemoglobina           | 0 ou 1            |
| 3  | creatinine_phosphokinase  | numérico        | Nível da enzima CPK no sangue                          | 542               |
| 4  | diabetes                  | booleano        | Se o paciente tem diabetes                             | 0 ou 1            |
| 5  | ejection_fraction         | numérico        | Percentual de sangue que sai do coração a cada contração | 45                |
| 6  | high_blood_pressure       | booleano        | Se o paciente tem hipertensão                          | 0 ou 1            |
| 7  | platelets                 | numérico        | Plaquetas no sangue                                    | 149000            |
| 8  | serum_creatinine          | numérico        | Nível de creatinina sérica no sangue                   | 0.5               |
| 9  | serum_sodium              | numérico        | Nível de sódio sérico no sangue                        | jun               |
| 10 | sex                       | booleano        | Mulher ou homem                                        | 0 ou 1            |
| 11 | smoking                   | booleano        | Se o paciente fuma                                     | 0 ou 1            |
| 12 | time                      | numérico        | Período de acompanhamento (dias)                       | 4                 |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Alvo]        | booleano        | Se o paciente morre durante o período de acompanhamento | 0 ou 1            |

Depois de obter o conjunto de dados, podemos começar o projeto no Azure.

## 2. Treinamento Low code/No code de um modelo no Azure ML Studio
### 2.1 Criar um workspace no Azure ML
Para treinar um modelo no Azure ML, você precisa primeiro criar um workspace no Azure ML. O workspace é o recurso de nível superior para o Azure Machine Learning, fornecendo um local centralizado para trabalhar com todos os artefatos que você cria ao usar o Azure Machine Learning. O workspace mantém um histórico de todas as execuções de treinamento, incluindo logs, métricas, saídas e um instantâneo de seus scripts. Você usa essas informações para determinar qual execução de treinamento produz o melhor modelo. [Saiba mais](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Recomenda-se usar o navegador mais atualizado compatível com seu sistema operacional. Os seguintes navegadores são suportados:

- Microsoft Edge (O novo Microsoft Edge, versão mais recente. Não o Microsoft Edge legado)
- Safari (versão mais recente, apenas para Mac)
- Chrome (versão mais recente)
- Firefox (versão mais recente)

Para usar o Azure Machine Learning, crie um workspace em sua assinatura do Azure. Você pode então usar este workspace para gerenciar dados, recursos de computação, código, modelos e outros artefatos relacionados às suas cargas de trabalho de aprendizado de máquina.

> **_NOTA:_** Sua assinatura do Azure será cobrada por uma pequena quantidade de armazenamento de dados enquanto o workspace do Azure Machine Learning existir em sua assinatura, então recomendamos que você exclua o workspace do Azure Machine Learning quando não estiver mais usando.

1. Faça login no [portal do Azure](https://ms.portal.azure.com/) usando as credenciais da Microsoft associadas à sua assinatura do Azure.
2. Selecione **＋Criar um recurso**
   
   ![workspace-1](../../../../translated_images/workspace-1.ac8694d60b073ed1ae8333d71244dc8a9b3e439d54593724f98f1beefdd27b08.br.png)

   Pesquise por Machine Learning e selecione o tile Machine Learning.

   ![workspace-2](../../../../translated_images/workspace-2.ae7c486db8796147075e4a56566aa819827dd6c4c8d18d64590317c3be625f17.br.png)

   Clique no botão criar.

   ![workspace-3](../../../../translated_images/workspace-3.398ca4a5858132cce584db9df10c5a011cd9075eb182e647a77d5cac01771eea.br.png)

   Preencha as configurações da seguinte forma:
   - Assinatura: Sua assinatura do Azure
   - Grupo de recursos: Crie ou selecione um grupo de recursos
   - Nome do workspace: Insira um nome único para seu workspace
   - Região: Selecione a região geográfica mais próxima de você
   - Conta de armazenamento: Observe a nova conta de armazenamento padrão que será criada para seu workspace
   - Cofre de chaves: Observe o novo cofre de chaves padrão que será criado para seu workspace
   - Application Insights: Observe o novo recurso Application Insights padrão que será criado para seu workspace
   - Registro de contêiner: Nenhum (um será criado automaticamente na primeira vez que você implantar um modelo em um contêiner)

    ![workspace-4](../../../../translated_images/workspace-4.bac87f6599c4df63e624fc2608990f965887bee551d9dedc71c687b43b986b6a.br.png)

   - Clique em criar + revisar e, em seguida, no botão criar.
3. Aguarde a criação do seu workspace (isso pode levar alguns minutos). Depois, acesse-o no portal. Você pode encontrá-lo através do serviço Azure Machine Learning.
4. Na página de visão geral do seu workspace, inicie o Azure Machine Learning Studio (ou abra uma nova aba do navegador e navegue para https://ml.azure.com), e faça login no Azure Machine Learning Studio usando sua conta Microsoft. Se solicitado, selecione seu diretório e assinatura do Azure, e seu workspace do Azure Machine Learning.
   
![workspace-5](../../../../translated_images/workspace-5.a6eb17e0a5e6420018b08bdaf3755ce977f96f1df3ea363d2476a9dce7e15adb.br.png)

5. No Azure Machine Learning Studio, alterne o ícone ☰ no canto superior esquerdo para visualizar as várias páginas da interface. Você pode usar essas páginas para gerenciar os recursos do seu workspace.

![workspace-6](../../../../translated_images/workspace-6.8dd81fe841797ee17f8f73916769576260b16c4e17e850d277a49db35fd74a15.br.png)

Você pode gerenciar seu workspace usando o portal do Azure, mas para cientistas de dados e engenheiros de operações de aprendizado de máquina, o Azure Machine Learning Studio fornece uma interface de usuário mais focada para gerenciar os recursos do workspace.

### 2.2 Recursos de Computação

Recursos de Computação são recursos baseados na nuvem nos quais você pode executar processos de treinamento de modelos e exploração de dados. Existem quatro tipos de recursos de computação que você pode criar:

- **Instâncias de Computação**: Estações de trabalho de desenvolvimento que cientistas de dados podem usar para trabalhar com dados e modelos. Isso envolve a criação de uma Máquina Virtual (VM) e o lançamento de uma instância de notebook. Você pode então treinar um modelo chamando um cluster de computação a partir do notebook.
- **Clusters de Computação**: Clusters escaláveis de VMs para processamento sob demanda de código de experimentos. Você precisará disso ao treinar um modelo. Clusters de computação também podem empregar recursos especializados de GPU ou CPU.
- **Clusters de Inferência**: Alvos de implantação para serviços preditivos que usam seus modelos treinados.
- **Attached Compute**: Links para recursos de computação existentes no Azure, como Máquinas Virtuais ou clusters do Azure Databricks.

#### 2.2.1 Escolhendo as opções certas para seus recursos de computação

Alguns fatores-chave devem ser considerados ao criar um recurso de computação, e essas escolhas podem ser decisões críticas.

**Você precisa de CPU ou GPU?**

Uma CPU (Unidade Central de Processamento) é o circuito eletrônico que executa instruções de um programa de computador. Uma GPU (Unidade de Processamento Gráfico) é um circuito eletrônico especializado que pode executar código relacionado a gráficos em uma taxa muito alta.

A principal diferença entre a arquitetura de CPU e GPU é que uma CPU é projetada para lidar com uma ampla gama de tarefas rapidamente (medida pela velocidade do clock da CPU), mas é limitada na simultaneidade das tarefas que podem estar em execução. GPUs são projetadas para computação paralela e, portanto, são muito melhores em tarefas de aprendizado profundo.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Menos caro                              | Mais caro                  |
| Nível mais baixo de simultaneidade      | Nível mais alto de simultaneidade |
| Mais lento no treinamento de modelos de aprendizado profundo | Ótimo para aprendizado profundo |

**Tamanho do Cluster**

Clusters maiores são mais caros, mas resultarão em melhor capacidade de resposta. Portanto, se você tem tempo, mas não muito dinheiro, deve começar com um cluster pequeno. Por outro lado, se você tem dinheiro, mas pouco tempo, deve começar com um cluster maior.

**Tamanho da VM**

Dependendo das suas restrições de tempo e orçamento, você pode variar o tamanho da RAM, disco, número de núcleos e velocidade do clock. Aumentar todos esses parâmetros será mais caro, mas resultará em melhor desempenho.

**Instâncias Dedicadas ou de Baixa Prioridade?**

Uma instância de baixa prioridade significa que ela é interrompível: essencialmente, a Microsoft Azure pode pegar esses recursos e atribuí-los a outra tarefa, interrompendo um trabalho. Uma instância dedicada, ou não interrompível, significa que o trabalho nunca será encerrado sem sua permissão. 
Esta é outra consideração de tempo versus dinheiro, já que instâncias interrompíveis são menos caras do que dedicadas.

#### 2.2.2 Criando um cluster de computação

No [workspace do Azure ML](https://ml.azure.com/) que criamos anteriormente, vá para computação e você poderá ver os diferentes recursos de computação que acabamos de discutir (ou seja, instâncias de computação, clusters de computação, clusters de inferência e computação vinculada). Para este projeto, precisaremos de um cluster de computação para o treinamento do modelo. No Studio, clique no menu "Compute", depois na aba "Compute cluster" e clique no botão "+ New" para criar um cluster de computação.

![22](../../../../translated_images/cluster-1.b78cb630bb543729b11f60c34d97110a263f8c27b516ba4dc47807b3cee5579f.br.png)

1. Escolha suas opções: Dedicado vs Baixa prioridade, CPU ou GPU, tamanho da VM e número de núcleos (você pode manter as configurações padrão para este projeto).
2. Clique no botão Next.

![23](../../../../translated_images/cluster-2.ea30cdbc9f926bb9e05af3fdbc1f679811c796dc2a6847f935290aec15526e88.br.png)

3. Dê ao cluster um nome de computação.
4. Escolha suas opções: Número mínimo/máximo de nós, segundos ociosos antes de reduzir, acesso SSH. Note que, se o número mínimo de nós for 0, você economizará dinheiro quando o cluster estiver ocioso. Note que quanto maior o número de nós máximos, mais curto será o treinamento. O número máximo de nós recomendado é 3.  
5. Clique no botão "Create". Este passo pode levar alguns minutos.

![29](../../../../translated_images/cluster-3.8a334bc070ec173a329ce5abd2a9d727542e83eb2347676c9af20f2c8870b3e7.br.png)

Incrível! Agora que temos um cluster de computação, precisamos carregar os dados no Azure ML Studio.

### 2.3 Carregando o Conjunto de Dados

1. No [workspace do Azure ML](https://ml.azure.com/) que criamos anteriormente, clique em "Datasets" no menu à esquerda e clique no botão "+ Create dataset" para criar um conjunto de dados. Escolha a opção "From local files" e selecione o conjunto de dados do Kaggle que baixamos anteriormente.
   
   ![24](../../../../translated_images/dataset-1.e86ab4e10907a6e9c2a72577b51db35f13689cb33702337b8b7032f2ef76dac2.br.png)

2. Dê ao seu conjunto de dados um nome, um tipo e uma descrição. Clique em Next. Faça o upload dos dados a partir dos arquivos. Clique em Next.
   
   ![25](../../../../translated_images/dataset-2.f58de1c435d5bf9ccb16ccc5f5d4380eb2b50affca85cfbf4f97562bdab99f77.br.png)

3. No Schema, altere o tipo de dados para Boolean para os seguintes recursos: anaemia, diabetes, high blood pressure, sex, smoking e DEATH_EVENT. Clique em Next e clique em Create.
   
   ![26](../../../../translated_images/dataset-3.58db8c0eb783e89236a02bbce5bb4ba808d081a87d994d5284b1ae59928c95bf.br.png)

Ótimo! Agora que o conjunto de dados está no lugar e o cluster de computação foi criado, podemos começar o treinamento do modelo!

### 2.4 Treinamento com pouco ou nenhum código usando AutoML

O desenvolvimento tradicional de modelos de aprendizado de máquina é intensivo em recursos, requer conhecimento significativo do domínio e tempo para produzir e comparar dezenas de modelos. 
O aprendizado de máquina automatizado (AutoML) é o processo de automatizar as tarefas iterativas e demoradas do desenvolvimento de modelos de aprendizado de máquina. Ele permite que cientistas de dados, analistas e desenvolvedores construam modelos de aprendizado de máquina com alta escala, eficiência e produtividade, mantendo a qualidade do modelo. Isso reduz o tempo necessário para obter modelos de aprendizado de máquina prontos para produção, com grande facilidade e eficiência. [Saiba mais](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. No [workspace do Azure ML](https://ml.azure.com/) que criamos anteriormente, clique em "Automated ML" no menu à esquerda e selecione o conjunto de dados que você acabou de carregar. Clique em Next.

   ![27](../../../../translated_images/aml-1.67281a85d3a1e2f34eb367b2d0f74e1039d13396e510f363cd8766632106d1ec.br.png)

2. Insira um novo nome de experimento, a coluna alvo (DEATH_EVENT) e o cluster de computação que criamos. Clique em Next.
   
   ![28](../../../../translated_images/aml-2.c9fb9cffb39ccbbe21ab9810ae937195d41a489744e15cff2b8477ed4dcae1ec.br.png)

3. Escolha "Classification" e clique em Finish. Este passo pode levar entre 30 minutos e 1 hora, dependendo do tamanho do seu cluster de computação.
    
    ![30](../../../../translated_images/aml-3.a7952e4295f38cc6cdb0c7ed6dc71ea756b7fb5697ec126bc1220f87c5fa9231.br.png)

4. Quando a execução estiver concluída, clique na aba "Automated ML", clique na sua execução e clique no Algoritmo no cartão "Best model summary".
    
    ![31](../../../../translated_images/aml-4.7a627e09cb6f16d0aa246059d9faee3d1725cc4258d0c8df15e801f73afc7e2c.br.png)

Aqui você pode ver uma descrição detalhada do melhor modelo que o AutoML gerou. Você também pode explorar outros modelos gerados na aba Models. Reserve alguns minutos para explorar os modelos na aba Explanations (preview). Depois de escolher o modelo que deseja usar (aqui escolheremos o melhor modelo selecionado pelo AutoML), veremos como podemos implantá-lo.

## 3. Implantação do modelo com pouco ou nenhum código e consumo do endpoint
### 3.1 Implantação do modelo

A interface de aprendizado de máquina automatizado permite que você implante o melhor modelo como um serviço web em alguns passos. A implantação é a integração do modelo para que ele possa fazer previsões com base em novos dados e identificar áreas potenciais de oportunidade. Para este projeto, a implantação em um serviço web significa que aplicativos médicos poderão consumir o modelo para fazer previsões ao vivo sobre o risco de seus pacientes terem um ataque cardíaco.

Na descrição do melhor modelo, clique no botão "Deploy".
    
![deploy-1](../../../../translated_images/deploy-1.ddad725acadc84e34553c3d09e727160faeb32527a9fb8b904c0f99235a34bb6.br.png)

15. Dê um nome, uma descrição, tipo de computação (Azure Container Instance), habilite a autenticação e clique em Deploy. Este passo pode levar cerca de 20 minutos para ser concluído. O processo de implantação envolve várias etapas, incluindo registrar o modelo, gerar recursos e configurá-los para o serviço web. Uma mensagem de status aparece em Deploy status. Selecione Refresh periodicamente para verificar o status da implantação. Ele estará implantado e funcionando quando o status for "Healthy".

![deploy-2](../../../../translated_images/deploy-2.94dbb13f239086473aa4bf814342fd40483d136849b080f02bafbb995383940e.br.png)

16. Depois de implantado, clique na aba Endpoint e clique no endpoint que você acabou de implantar. Aqui você pode encontrar todos os detalhes que precisa saber sobre o endpoint.

![deploy-3](../../../../translated_images/deploy-3.fecefef070e8ef3b28e802326d107f61ac4e672d20bf82d05f78d025f9e6c611.br.png)

Incrível! Agora que temos um modelo implantado, podemos começar o consumo do endpoint.

### 3.2 Consumo do endpoint

Clique na aba "Consume". Aqui você pode encontrar o endpoint REST e um script Python na opção de consumo. Reserve um tempo para ler o código Python.

Este script pode ser executado diretamente da sua máquina local e consumirá seu endpoint.

![35](../../../../translated_images/consumption-1.700abd196452842a020c7d745908637a6e4c5c50494ad1217be80e283e0de154.br.png)

Reserve um momento para verificar estas 2 linhas de código:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
A variável `url` é o endpoint REST encontrado na aba de consumo e a variável `api_key` é a chave primária também encontrada na aba de consumo (somente no caso de você ter habilitado a autenticação). É assim que o script pode consumir o endpoint.

18. Executando o script, você deve ver a seguinte saída:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
Isso significa que a previsão de falha cardíaca para os dados fornecidos é verdadeira. Isso faz sentido porque, se você olhar mais de perto os dados gerados automaticamente no script, tudo está em 0 e falso por padrão. Você pode alterar os dados com o seguinte exemplo de entrada:

```python
data = {
    "data":
    [
        {
            'age': "0",
            'anaemia': "false",
            'creatinine_phosphokinase': "0",
            'diabetes': "false",
            'ejection_fraction': "0",
            'high_blood_pressure': "false",
            'platelets': "0",
            'serum_creatinine': "0",
            'serum_sodium': "0",
            'sex': "false",
            'smoking': "false",
            'time': "0",
        },
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}
```
O script deve retornar:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Parabéns! Você acabou de consumir o modelo implantado e treinado no Azure ML!

> **_NOTA:_** Quando terminar o projeto, não se esqueça de excluir todos os recursos.
## 🚀 Desafio

Observe atentamente as explicações e os detalhes do modelo que o AutoML gerou para os melhores modelos. Tente entender por que o melhor modelo é melhor do que os outros. Quais algoritmos foram comparados? Quais são as diferenças entre eles? Por que o melhor está tendo um desempenho superior neste caso?

## [Quiz Pós-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/35)

## Revisão e Autoestudo

Nesta lição, você aprendeu como treinar, implantar e consumir um modelo para prever o risco de falha cardíaca de forma Low code/No code na nuvem. Se ainda não fez isso, aprofunde-se nas explicações do modelo que o AutoML gerou para os melhores modelos e tente entender por que o melhor modelo é superior aos outros.

Você pode explorar mais sobre AutoML com pouco ou nenhum código lendo esta [documentação](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Tarefa

[Projeto de Ciência de Dados com pouco ou nenhum código no Azure ML](assignment.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.