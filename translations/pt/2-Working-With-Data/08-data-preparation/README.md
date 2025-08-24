<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-23T23:26:27+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "pt"
}
-->
# Trabalhar com Dados: Preparação de Dados

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Preparação de Dados - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

## [Questionário Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Dependendo da sua origem, os dados brutos podem conter algumas inconsistências que dificultam a análise e modelagem. Em outras palavras, esses dados podem ser categorizados como "sujos" e precisarão ser limpos. Esta lição foca em técnicas para limpar e transformar os dados, lidando com desafios como dados ausentes, imprecisos ou incompletos. Os tópicos abordados nesta lição utilizam Python e a biblioteca Pandas e serão [demonstrados no notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) dentro deste diretório.

## A importância de limpar os dados

- **Facilidade de uso e reutilização**: Quando os dados estão devidamente organizados e normalizados, é mais fácil pesquisá-los, utilizá-los e compartilhá-los com outras pessoas.

- **Consistência**: A ciência de dados frequentemente exige trabalhar com mais de um conjunto de dados, onde conjuntos de diferentes fontes precisam ser combinados. Garantir que cada conjunto de dados individual tenha uma padronização comum assegura que os dados continuem úteis quando todos forem mesclados em um único conjunto.

- **Precisão do modelo**: Dados que foram limpos melhoram a precisão dos modelos que dependem deles.

## Objetivos e estratégias comuns de limpeza

- **Explorar um conjunto de dados**: A exploração de dados, que será abordada em uma [lição futura](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), pode ajudá-lo a identificar dados que precisam ser limpos. Observar visualmente os valores dentro de um conjunto de dados pode definir expectativas sobre como o restante será ou fornecer uma ideia dos problemas que podem ser resolvidos. A exploração pode envolver consultas básicas, visualizações e amostragem.

- **Formatação**: Dependendo da origem, os dados podem ter inconsistências na forma como são apresentados. Isso pode causar problemas na busca e representação dos valores, onde eles são vistos dentro do conjunto de dados, mas não são devidamente representados em visualizações ou resultados de consultas. Problemas comuns de formatação envolvem resolver espaços em branco, datas e tipos de dados. Resolver problemas de formatação geralmente depende das pessoas que estão utilizando os dados. Por exemplo, os padrões de apresentação de datas e números podem variar de país para país.

- **Duplicações**: Dados que possuem mais de uma ocorrência podem produzir resultados imprecisos e geralmente devem ser removidos. Isso pode ocorrer frequentemente ao combinar dois ou mais conjuntos de dados. No entanto, há casos em que duplicações em conjuntos de dados combinados contêm informações adicionais que podem precisar ser preservadas.

- **Dados ausentes**: Dados ausentes podem causar imprecisões, bem como resultados fracos ou tendenciosos. Às vezes, isso pode ser resolvido com um "recarregamento" dos dados, preenchendo os valores ausentes com cálculos e código como Python, ou simplesmente removendo o valor e os dados correspondentes. Existem várias razões para os dados estarem ausentes, e as ações tomadas para resolver esses valores ausentes podem depender de como e por que eles desapareceram.

## Explorando informações de DataFrame
> **Objetivo de aprendizagem:** Ao final desta subseção, você deve estar confortável em encontrar informações gerais sobre os dados armazenados em DataFrames do pandas.

Depois de carregar seus dados no pandas, é provável que eles estejam em um DataFrame (consulte a [lição anterior](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) para uma visão detalhada). No entanto, se o conjunto de dados no seu DataFrame tiver 60.000 linhas e 400 colunas, como começar a entender com o que você está lidando? Felizmente, o [pandas](https://pandas.pydata.org/) fornece ferramentas convenientes para rapidamente obter informações gerais sobre um DataFrame, além das primeiras e últimas linhas.

Para explorar essa funcionalidade, vamos importar a biblioteca Python scikit-learn e usar um conjunto de dados icônico: o **conjunto de dados Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Para começar, o método `info()` é usado para imprimir um resumo do conteúdo presente em um `DataFrame`. Vamos dar uma olhada neste conjunto de dados para ver o que temos:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
A partir disso, sabemos que o conjunto de dados *Iris* tem 150 entradas em quatro colunas sem entradas nulas. Todos os dados estão armazenados como números de ponto flutuante de 64 bits.

- **DataFrame.head()**: Em seguida, para verificar o conteúdo real do `DataFrame`, usamos o método `head()`. Vamos ver como as primeiras linhas do nosso `iris_df` se parecem:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Por outro lado, para verificar as últimas linhas do `DataFrame`, usamos o método `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Conclusão:** Apenas olhando para os metadados sobre as informações em um DataFrame ou para as primeiras e últimas linhas, você pode ter uma ideia imediata sobre o tamanho, formato e conteúdo dos dados com os quais está lidando.

## Lidando com Dados Ausentes
> **Objetivo de aprendizagem:** Ao final desta subseção, você deve saber como substituir ou remover valores nulos de DataFrames.

Na maioria das vezes, os conjuntos de dados que você deseja usar (ou precisa usar) têm valores ausentes. Como os dados ausentes são tratados envolve escolhas sutis que podem afetar sua análise final e os resultados no mundo real.

O pandas lida com valores ausentes de duas maneiras. A primeira, que você já viu em seções anteriores, é `NaN`, ou Not a Number. Este é, na verdade, um valor especial que faz parte da especificação IEEE de ponto flutuante e é usado apenas para indicar valores de ponto flutuante ausentes.

Para valores ausentes que não sejam de ponto flutuante, o pandas usa o objeto `None` do Python. Embora possa parecer confuso encontrar dois tipos diferentes de valores que essencialmente dizem a mesma coisa, há razões programáticas sólidas para essa escolha de design e, na prática, isso permite que o pandas ofereça um bom compromisso para a grande maioria dos casos. Apesar disso, tanto `None` quanto `NaN` possuem restrições que você precisa ter em mente em relação ao modo como podem ser usados.

Confira mais sobre `NaN` e `None` no [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detectando valores nulos**: No `pandas`, os métodos `isnull()` e `notnull()` são suas principais ferramentas para detectar dados nulos. Ambos retornam máscaras booleanas sobre seus dados. Usaremos `numpy` para valores `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Observe atentamente o resultado. Alguma coisa te surpreende? Embora `0` seja um nulo aritmético, ele é, no entanto, um número inteiro válido e o pandas o trata como tal. `''` é um pouco mais sutil. Embora o tenhamos usado na Seção 1 para representar um valor de string vazio, ele é, no entanto, um objeto de string e não uma representação de nulo para o pandas.

Agora, vamos inverter isso e usar esses métodos de uma maneira mais parecida com a prática. Você pode usar máscaras booleanas diretamente como um índice de ``Series`` ou ``DataFrame``, o que pode ser útil ao tentar trabalhar com valores ausentes (ou presentes) isolados.

> **Conclusão**: Tanto os métodos `isnull()` quanto `notnull()` produzem resultados semelhantes quando usados em `DataFrame`s: eles mostram os resultados e o índice desses resultados, o que será extremamente útil ao lidar com seus dados.

- **Removendo valores nulos**: Além de identificar valores ausentes, o pandas fornece um meio conveniente de remover valores nulos de `Series` e `DataFrame`s. (Particularmente em conjuntos de dados grandes, muitas vezes é mais aconselhável simplesmente remover valores ausentes [NA] da sua análise do que lidar com eles de outras maneiras.) Para ver isso em ação, vamos voltar ao `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Observe que isso deve se parecer com sua saída de `example3[example3.notnull()]`. A diferença aqui é que, em vez de apenas indexar os valores mascarados, `dropna` removeu esses valores ausentes da `Series` `example1`.

Como os `DataFrame`s têm duas dimensões, eles oferecem mais opções para remover dados.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Você reparou que o pandas converteu duas das colunas para ponto flutuante para acomodar os `NaN`s?)

Você não pode remover um único valor de um `DataFrame`, então precisa remover linhas ou colunas inteiras. Dependendo do que você está fazendo, pode querer fazer uma coisa ou outra, e o pandas oferece opções para ambas. Como na ciência de dados as colunas geralmente representam variáveis e as linhas representam observações, é mais provável que você remova linhas de dados; a configuração padrão para `dropna()` é remover todas as linhas que contêm quaisquer valores nulos:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Se necessário, você pode remover valores NA de colunas. Use `axis=1` para fazer isso:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Observe que isso pode remover muitos dados que você pode querer manter, particularmente em conjuntos de dados menores. E se você quiser apenas remover linhas ou colunas que contenham vários ou até mesmo todos os valores nulos? Você especifica essas configurações em `dropna` com os parâmetros `how` e `thresh`.

Por padrão, `how='any'` (se quiser verificar por si mesmo ou ver quais outros parâmetros o método possui, execute `example4.dropna?` em uma célula de código). Você pode, alternativamente, especificar `how='all'` para remover apenas linhas ou colunas que contenham todos os valores nulos. Vamos expandir nosso exemplo de `DataFrame` para ver isso em ação.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

O parâmetro `thresh` oferece um controle mais refinado: você define o número de valores *não nulos* que uma linha ou coluna precisa ter para ser mantida:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Aqui, a primeira e última linha foram removidas, porque contêm apenas dois valores não nulos.

- **Preenchendo valores nulos**: Dependendo do seu conjunto de dados, às vezes faz mais sentido preencher valores nulos com valores válidos do que removê-los. Você poderia usar `isnull` para fazer isso diretamente, mas isso pode ser trabalhoso, especialmente se você tiver muitos valores para preencher. Como essa é uma tarefa tão comum na ciência de dados, o pandas fornece `fillna`, que retorna uma cópia da `Series` ou `DataFrame` com os valores ausentes substituídos por um de sua escolha. Vamos criar outra `Series` de exemplo para ver como isso funciona na prática.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Você pode preencher todas as entradas nulas com um único valor, como `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Você pode **preencher para frente** valores nulos, ou seja, usar o último valor válido para preencher um nulo:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Você também pode **preencher para trás** para propagar o próximo valor válido para trás e preencher um nulo:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Como você pode imaginar, isso funciona da mesma forma com `DataFrame`s, mas você também pode especificar um `axis` ao longo do qual preencher valores nulos. Usando novamente o `example2` anteriormente utilizado:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Observe que, quando um valor anterior não está disponível para preenchimento para frente, o valor nulo permanece.
> **Conclusão:** Existem várias formas de lidar com valores em falta nos seus conjuntos de dados. A estratégia específica que utiliza (removê-los, substituí-los ou até mesmo como os substitui) deve ser ditada pelas particularidades desses dados. Quanto mais trabalhar e interagir com conjuntos de dados, melhor será a sua capacidade de lidar com valores em falta.

## Remoção de dados duplicados

> **Objetivo de aprendizagem:** No final desta subseção, deverá sentir-se confortável a identificar e remover valores duplicados de DataFrames.

Além de dados em falta, é comum encontrar dados duplicados em conjuntos de dados do mundo real. Felizmente, o `pandas` oferece uma forma simples de detetar e remover entradas duplicadas.

- **Identificar duplicados: `duplicated`**: Pode identificar facilmente valores duplicados utilizando o método `duplicated` no pandas, que devolve uma máscara booleana indicando se uma entrada num `DataFrame` é duplicada de uma anterior. Vamos criar outro exemplo de `DataFrame` para ver isto em ação.  
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```  
|      |letters|numbers|  
|------|-------|-------|  
|0     |A      |1      |  
|1     |B      |2      |  
|2     |A      |1      |  
|3     |B      |3      |  
|4     |B      |3      |  

```python
example4.duplicated()
```  
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```  

- **Remover duplicados: `drop_duplicates`:** devolve simplesmente uma cópia dos dados para os quais todos os valores `duplicated` são `False`:  
```python
example4.drop_duplicates()
```  
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```  

Tanto `duplicated` como `drop_duplicates` consideram por padrão todas as colunas, mas pode especificar que examinem apenas um subconjunto de colunas no seu `DataFrame`:  
```python
example4.drop_duplicates(['letters'])
```  
```
letters	numbers
0	A	1
1	B	2
```  

> **Conclusão:** Remover dados duplicados é uma parte essencial de quase todos os projetos de ciência de dados. Dados duplicados podem alterar os resultados das suas análises e fornecer resultados imprecisos!

## 🚀 Desafio

Todo o material discutido está disponível como um [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Além disso, há exercícios após cada secção, experimente-os!

## [Questionário Pós-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)

## Revisão e Autoestudo

Existem muitas formas de descobrir e abordar a preparação dos seus dados para análise e modelação, e a limpeza dos dados é um passo importante que requer uma experiência prática. Experimente estes desafios do Kaggle para explorar técnicas que esta lição não abordou.

- [Desafio de Limpeza de Dados: Análise de Datas](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Desafio de Limpeza de Dados: Escalar e Normalizar Dados](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)

## Tarefa

[Avaliação de Dados de um Formulário](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.