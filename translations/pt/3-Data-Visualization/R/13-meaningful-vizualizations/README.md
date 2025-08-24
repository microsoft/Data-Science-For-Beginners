<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-24T01:20:23+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "pt"
}
-->
# Criando Visualizações Significativas

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Visualizações Significativas - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

> "Se torturares os dados por tempo suficiente, eles confessarão qualquer coisa" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Uma das habilidades básicas de um cientista de dados é a capacidade de criar uma visualização de dados significativa que ajude a responder às perguntas que você possa ter. Antes de visualizar os seus dados, é necessário garantir que eles foram limpos e preparados, como foi feito em lições anteriores. Depois disso, pode-se começar a decidir a melhor forma de apresentar os dados.

Nesta lição, você revisará:

1. Como escolher o tipo de gráfico certo  
2. Como evitar gráficos enganosos  
3. Como trabalhar com cores  
4. Como estilizar os seus gráficos para melhorar a legibilidade  
5. Como criar soluções de gráficos animados ou em 3D  
6. Como construir uma visualização criativa  

## [Questionário Pré-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Escolha o tipo de gráfico certo

Em lições anteriores, você experimentou criar vários tipos de visualizações de dados interessantes usando Matplotlib e Seaborn. De forma geral, você pode selecionar o [tipo certo de gráfico](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) para a pergunta que está fazendo utilizando esta tabela:

| Necessidade:               | Deve usar:                     |
| -------------------------- | ------------------------------ |
| Mostrar tendências ao longo do tempo | Linha                          |
| Comparar categorias         | Barra, Pizza                   |
| Comparar totais             | Pizza, Barra Empilhada         |
| Mostrar relações            | Dispersão, Linha, Facet, Linha Dupla |
| Mostrar distribuições       | Dispersão, Histograma, Caixa   |
| Mostrar proporções          | Pizza, Donut, Waffle           |

> ✅ Dependendo da composição dos seus dados, pode ser necessário convertê-los de texto para numérico para que um determinado gráfico seja suportado.

## Evite enganos

Mesmo que um cientista de dados escolha o gráfico certo para os dados certos, existem muitas maneiras de apresentar os dados de forma a provar um ponto, muitas vezes às custas de comprometer os próprios dados. Há inúmeros exemplos de gráficos e infográficos enganosos!

[![Como Gráficos Mentem por Alberto Cairo](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Como gráficos mentem")

> 🎥 Clique na imagem acima para assistir a uma palestra sobre gráficos enganosos

Este gráfico inverte o eixo X para mostrar o oposto da verdade, com base na data:

![gráfico ruim 1](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-1.png)

[Este gráfico](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) é ainda mais enganoso, pois o olhar é atraído para a direita, levando à conclusão de que, ao longo do tempo, os casos de COVID diminuíram nos vários condados. Na verdade, se você observar atentamente as datas, verá que elas foram reorganizadas para criar essa falsa tendência de queda.

![gráfico ruim 2](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-2.jpg)

Este exemplo notório usa cores E um eixo Y invertido para enganar: em vez de concluir que as mortes por armas de fogo aumentaram após a aprovação de uma legislação favorável às armas, o olhar é induzido a pensar o oposto:

![gráfico ruim 3](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-3.jpg)

Este gráfico estranho mostra como a proporção pode ser manipulada, de forma hilária:

![gráfico ruim 4](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-4.jpg)

Comparar o incomparável é outro truque duvidoso. Existe um [site maravilhoso](https://tylervigen.com/spurious-correlations) sobre 'correlações espúrias', exibindo 'fatos' que correlacionam coisas como a taxa de divórcio no Maine e o consumo de margarina. Um grupo no Reddit também coleta os [usos feios](https://www.reddit.com/r/dataisugly/top/?t=all) de dados.

É importante entender como o olhar pode ser facilmente enganado por gráficos enganosos. Mesmo que a intenção do cientista de dados seja boa, a escolha de um tipo ruim de gráfico, como um gráfico de pizza com muitas categorias, pode ser enganosa.

## Cor

Você viu no gráfico 'violência armada na Flórida' acima como a cor pode adicionar uma camada adicional de significado aos gráficos, especialmente aqueles que não foram projetados usando bibliotecas como ggplot2 e RColorBrewer, que vêm com várias bibliotecas e paletas de cores validadas. Se estiver criando um gráfico manualmente, estude um pouco sobre a [teoria das cores](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Esteja ciente, ao projetar gráficos, de que a acessibilidade é um aspecto importante da visualização. Alguns dos seus utilizadores podem ser daltônicos - o seu gráfico é exibido corretamente para utilizadores com deficiências visuais?

Tenha cuidado ao escolher cores para o seu gráfico, pois elas podem transmitir significados que você não pretende. As 'senhoras de rosa' no gráfico de 'altura' acima transmitem um significado distintamente 'feminino', que adiciona ao caráter bizarro do próprio gráfico.

Embora o [significado das cores](https://colormatters.com/color-symbolism/the-meanings-of-colors) possa variar em diferentes partes do mundo e tenda a mudar de acordo com o tom, de forma geral, os significados incluem:

| Cor    | Significado          |
| ------ | -------------------- |
| vermelho | poder               |
| azul    | confiança, lealdade  |
| amarelo | felicidade, cautela  |
| verde   | ecologia, sorte, inveja |
| roxo    | felicidade           |
| laranja | vibração             |

Se você for encarregado de criar um gráfico com cores personalizadas, certifique-se de que os seus gráficos sejam acessíveis e que as cores escolhidas coincidam com o significado que você deseja transmitir.

## Estilizando os seus gráficos para legibilidade

Gráficos não são significativos se não forem legíveis! Reserve um momento para considerar o dimensionamento da largura e altura do seu gráfico para que ele se ajuste bem aos seus dados. Se uma variável (como os 50 estados) precisar ser exibida, mostre-os verticalmente no eixo Y, se possível, para evitar um gráfico com rolagem horizontal.

Rotule os seus eixos, forneça uma legenda, se necessário, e ofereça tooltips para melhor compreensão dos dados.

Se os seus dados forem textuais e extensos no eixo X, você pode inclinar o texto para melhorar a legibilidade. O [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) oferece gráficos em 3D, se os seus dados suportarem. Visualizações de dados sofisticadas podem ser produzidas com ele.

![gráficos 3D](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/3d.png)

## Exibição de gráficos animados e em 3D

Algumas das melhores visualizações de dados hoje em dia são animadas. Shirley Wu criou visualizações incríveis com D3, como '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', onde cada flor é uma visualização de um filme. Outro exemplo para o Guardian é 'bussed out', uma experiência interativa que combina visualizações com Greensock e D3, além de um formato de artigo narrativo, para mostrar como Nova York lida com o problema dos sem-abrigo, enviando pessoas para fora da cidade.

![busing](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/busing.png)

> "Bussed Out: How America Moves its Homeless" do [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualizações por Nadieh Bremer & Shirley Wu

Embora esta lição não seja suficiente para ensinar em profundidade essas poderosas bibliotecas de visualização, experimente usar D3 em uma aplicação Vue.js com uma biblioteca para exibir uma visualização do livro "Ligações Perigosas" como uma rede social animada.

> "Les Liaisons Dangereuses" é um romance epistolar, ou seja, um romance apresentado como uma série de cartas. Escrito em 1782 por Choderlos de Laclos, conta a história das manobras sociais cruéis e moralmente corruptas de dois protagonistas da aristocracia francesa do final do século XVIII, o Visconde de Valmont e a Marquesa de Merteuil. Ambos encontram seu fim trágico, mas não sem causar um grande dano social. O romance se desenrola como uma série de cartas escritas para várias pessoas em seus círculos, tramando vingança ou simplesmente para causar problemas. Crie uma visualização dessas cartas para descobrir os principais personagens da narrativa, visualmente.

Você completará uma aplicação web que exibirá uma visão animada dessa rede social. Ela usa uma biblioteca criada para gerar uma [visualização de uma rede](https://github.com/emiliorizzo/vue-d3-network) usando Vue.js e D3. Quando a aplicação estiver em execução, você poderá mover os nós na tela para reorganizar os dados.

![liaisons](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/liaisons.png)

## Projeto: Crie um gráfico para mostrar uma rede usando D3.js

> Esta pasta da lição inclui uma pasta `solution` onde você pode encontrar o projeto concluído, para sua referência.

1. Siga as instruções no arquivo README.md na raiz da pasta starter. Certifique-se de que o NPM e o Node.js estão instalados na sua máquina antes de instalar as dependências do projeto.

2. Abra a pasta `starter/src`. Você encontrará uma pasta `assets` onde há um arquivo .json com todas as cartas do romance, numeradas, com anotações de 'para' e 'de'.

3. Complete o código em `components/Nodes.vue` para habilitar a visualização. Procure o método chamado `createLinks()` e adicione o seguinte loop aninhado.

Percorra o objeto .json para capturar os dados 'para' e 'de' das cartas e construa o objeto `links` para que a biblioteca de visualização possa consumi-lo:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Execute a sua aplicação a partir do terminal (npm run serve) e aproveite a visualização!

## 🚀 Desafio

Faça uma pesquisa na internet para descobrir visualizações enganosas. Como o autor engana o utilizador, e isso é intencional? Tente corrigir as visualizações para mostrar como elas deveriam ser.

## [Questionário Pós-Aula](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Revisão e Estudo Individual

Aqui estão alguns artigos para ler sobre visualizações de dados enganosas:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Dê uma olhada nestas visualizações interessantes de ativos e artefatos históricos:

https://handbook.pubpub.org/

Leia este artigo sobre como a animação pode melhorar as suas visualizações:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Tarefa

[Crie a sua própria visualização personalizada](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.