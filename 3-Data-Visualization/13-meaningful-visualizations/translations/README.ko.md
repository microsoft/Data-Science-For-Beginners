# Making Meaningful Visualizations
# 의미 있는 시각화 만들기

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Meaningful Visualizations - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |
| 의미 있는 시각화 -_제작자: [@nitya](https://twitter.com/nitya)_ |

> "If you torture the data long enough, it will confess to anything" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)
> "데이터를 충분히 오래 고문하면, 그것은 무엇이든 자백할 것입니다." [Ronald Coase] (https://en.wikiquote.org/wiki/Ronald_Coase)

One of the basic skills of a data scientist is the ability to create a meaningful data visualization that helps answer questions you might have. Prior to visualizing your data, you need to ensure that it has been cleaned and prepared, as you did in prior lessons. After that, you can start deciding how best to present the data.
데이터 과학자의 기본 기술 중 하나는 사용자가 가질 수 있는 질문에 대답하는 데 도움이 되는 의미 있는 데이터 시각화를 만드는 능력입니다. 데이터를 시각화하기 전에 이전 학습에서와 같이 데이터를 정리하고 준비해야 합니다. 그런 다음 데이터를 가장 잘 표시할 방법을 결정할 수 있습니다.

In this lesson, you will review:
이 과정에서는 다음을 복습합니다:

1. How to choose the right chart type
2. How to avoid deceptive charting
3. How to work with color
4. How to style your charts for readability
5. How to build animated or 3D charting solutions
6. How to build a creative visualization
1. 올바른 차트 유형을 선택하는 방법
2. 기만적인 차트 작성을 피하는 방법
3. 컬러로 작업하는 방법
4. 가독성을 위해 차트를 스타일링하는 방법
5. 애니메이션 또는 3D 차트 작성 솔루션을 구축하는 방법
6. 창의적 시각화를 만드는 방법

## [Pre-Lecture Quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/24)
## [사전 강의 퀴즈](https://red-water-0103e7a0f.azurestaticapps.net/quiz/24)

## Choose the right chart type
## 올바른 차트 유형 선택

In previous lessons, you experimented with building all kinds of interesting data visualizations using Matplotlib and Seaborn for charting. In general, you can select the [right kind of chart](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) for the question you are asking using this table:
이전 과정에서는 차트 작성을 위해 Matplotlib와 Seaborn을 사용하여 모든 종류의 흥미로운 데이터 시각화를 구축하는 실험을 했습니다. 일반적으로 다음 표를 사용하여 [적절한 유형의 차트](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/)를 선택할 수 있습니다:

| You need to:               | You should use:                 |
| -------------------------- | ------------------------------- |
| Show data trends over time | Line                            |
| Compare categories         | Bar, Pie                        |
| Compare totals             | Pie, Stacked Bar                |
| Show relationships         | Scatter, Line, Facet, Dual Line |
| Show distributions         | Scatter, Histogram, Box         |
| Show proportions           | Pie, Donut, Waffle              |

> ✅ Depending on the makeup of your data, you might need to convert it from text to numeric to get a given chart to support it.
> ✅ 데이터의 구성에 따라 텍스트에서 숫자로 변환해야 데이터를 지원할 수 있는 차트를 얻을 수 있습니다.

## Avoid deception
## 속임수를 피하라

Even if a data scientist is careful to choose the right chart for the right data, there are plenty of ways that data can be displayed in a way to prove a point, often at the cost of undermining the data itself. There are many examples of deceptive charts and infographics!
데이터 과학자가 올바른 데이터에 대한 올바른 차트를 선택하기 위해 주의를 기울인다고 해도, 데이터 자체를 손상시키는 대가를 치르고라도, 요점을 입증하는 방법으로 데이터를 표시할 수 있는 방법은 얼마든지 있습니다. 기만적인 차트와 인포그래픽의 예는 많습니다!

[![How Charts Lie by Alberto Cairo](./images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")
[![알베르토 카이로의 차트 눕기](..images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "차트 눕기"

> 🎥 Click the image above for a conference talk about deceptive charts
> 🎥 위 이미지를 클릭하면 기만적인 차트에 대한 컨퍼런스 토크가 나옵니다.

This chart reverses the X axis to show the opposite of the truth, based on date:
이 차트는 날짜를 기준으로 X축을 반전시켜 진실의 반대 방향을 보여줍니다:

![bad chart 1](images/bad-chart-1.png)
![나쁜 차트 1](images/bad-chart-1.png)

[This chart](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) is even more deceptive, as the eye is drawn to the right to conclude that, over time, COVID cases have declined in the various counties. In fact, if you look closely at the dates, you find that they have been rearranged to give that deceptive downward trend.
[이 차트](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg)는 시간이 지남에 따라 다양한 카운티에서 COVID 사례가 감소했다고 결론을 내릴 수 있는 권리에 주목하기 때문에 훨씬 더 기만적이다. 사실, 만약 여러분이 날짜를 자세히 본다면, 여러분은 그것들이 기만적인 하향 추세를 주기 위해 재배열되었다는 것을 발견할 것입니다.

![bad chart 2](images/bad-chart-2.jpg)
![나쁜 차트 2](images/bad-chart-2.jpg)

This notorious example uses color AND a flipped Y axis to deceive: instead of concluding that gun deaths spiked after the passage of gun-friendly legislation, in fact the eye is fooled to think that the opposite is true:
이 악명 높은 예는 색깔과 뒤집힌 Y축을 사용하여 속인다: 총기 친화적인 법안이 통과된 후 총기 사망률이 급증했다고 결론짓는 대신, 사실 그 반대라고 생각하는 것은 눈을 속인다:

![bad chart 3](images/bad-chart-3.jpg)
![나쁜 차트 3](images/bad-chart-3.jpg)

This strange chart shows how proportion can be manipulated, to hilarious effect:
이 이상한 차트는 비율을 조작하여 우스꽝스러운 효과를 얻을 수 있습니다:

![bad chart 4](images/bad-chart-4.jpg)
![나쁜 차트 4](images/bad-chart-4.jpg)

Comparing the incomparable is yet another shady trick. There is a [wonderful web site](https://tylervigen.com/spurious-correlations) all about 'spurious correlations' displaying 'facts' correlating things like the divorce rate in Maine and the consumption of margarine. A Reddit group also collects the [ugly uses](https://www.reddit.com/r/dataisugly/top/?t=all) of data.
비교할 수 없는 것을 비교하는 것은 또 다른 음흉한 속임수이다. 메인주의 이혼율과 마가린 소비와 같은 '비교적 상관관계'를 보여주는 [정보 웹사이트](https://tylervigen.com/spurious-correlations)가 있다. Reddit 그룹은 또한 데이터의 [사용량](https://www.reddit.com/r/dataisugly/top/?t=all)을 수집합니다.

It's important to understand how easily the eye can be fooled by deceptive charts. Even if the data scientist's intention is good, the choice of a bad type of chart, such as a pie chart showing too many categories, can be deceptive.
눈이 얼마나 쉽게 기만적인 도표에 속아 넘어갈 수 있는지 이해하는 것이 중요하다. 데이터 과학자의 의도가 좋더라도 너무 많은 범주를 보여주는 파이 차트와 같은 잘못된 유형의 차트를 선택하는 것은 기만적일 수 있습니다.

## Color
## 색상

You saw in the 'Florida gun violence' chart above how color can provide an additional layer of meaning to charts, especially ones not designed using libraries such as Matplotlib and Seaborn which come with various vetted color libraries and palettes. If you are making a chart by hand, do a little study of [color theory](https://colormatters.com/color-and-design/basic-color-theory)
당신은 '플로리다 총기 폭력' 차트에서 색상이 차트에 어떻게 추가적인 의미 층을 제공할 수 있는지 보았으며, 특히 다양한 컬러 라이브러리와 팔레트가 제공되는 Matplotlib과 Seaborn과 같은 도서관을 사용하여 설계되지 않은 것을 보았습니다. 만약 여러분이 손으로 차트를 만들고 있다면, [색깔 이론]을 조금 연구해 보세요. https://colormatters.com/color-and-design/basic-color-theory)

> ✅ Be aware, when designing charts, that accessibility is an important aspect of visualization. Some of your users might be color blind - does your chart display well for users with visual impairments?
> ✅ 차트를 설계할 때 접근성은 시각화의 중요한 측면임을 유의해야 한다. 일부 사용자는 색맹일 수 있습니다. 당신의 차트는 시각 장애가 있는 사용자들에게 잘 표시됩니까?

Be careful when choosing colors for your chart, as color can convey meaning you might not intend. The 'pink ladies' in the 'height' chart above convey a distinctly 'feminine' ascribed meaning that adds to the bizarreness of the chart itself.
색상은 의도하지 않은 의미를 전달할 수 있으므로 차트에 사용할 색상을 선택할 때 주의하십시오. 위의 'height' 차트에 있는 'pink ladies'는 차트 자체의 기괴함을 더하는 뚜렷하게 '여성적인' 의미를 전달한다.

While [color meaning](https://colormatters.com/color-symbolism/the-meanings-of-colors) might be different in different parts of the world, and tend to change in meaning according to their shade. Generally speaking, color meanings include:
그러나 [color languation](https://colormatters.com/color-symbolism/the-meanings-of-colors)은 세계 각지에서 다를 수 있으며 색조에 따라 의미가 변하는 경향이 있다. 일반적으로 색상의 의미는 다음과 같다.

| Color  | Meaning             |
| ------ | ------------------- |
| red    | power               |
| blue   | trust, loyalty      |
| yellow | happiness, caution  |
| green  | ecology, luck, envy |
| purple | happiness           |
| orange | vibrance            |

If you are tasked with building a chart with custom colors, ensure that your charts are both accessible and the color you choose coincides with the meaning you are trying to convey.
사용자 지정 색을 사용하여 차트를 작성해야 하는 경우 차트에 액세스할 수 있고 선택한 색상이 전달하려는 의미와 일치하는지 확인하십시오.

## Styling your charts for readability
## 가독성을 위한 차트 스타일링

Charts are not meaningful if they are not readable! Take a moment to consider styling the width and height of your chart to scale well with your data. If one variable (such as all 50 states) need to be displayed, show them vertically on the Y axis if possible so as to avoid a horizontally-scrolling chart.
차트를 읽을 수 없으면 의미가 없습니다! 데이터에 맞게 잘 확장되도록 차트의 너비와 높이를 스타일링하는 것을 고려해 보십시오. 하나의 변수(예: 50개 상태 모두)를 표시해야 하는 경우 가로 스크롤 차트를 피하기 위해 가능하면 Y축에 세로로 표시합니다.

Label your axes, provide a legend if necessary, and offer tooltips for better comprehension of data.
축에 레이블을 지정하고 필요한 경우 범례를 제공하며 데이터를 더 잘 이해할 수 있도록 툴팁을 제공합니다.

If your data is textual and verbose on the X axis, you can angle the text for better readability. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) offers 3d plotting, if you data supports it. Sophisticated data visualizations can be produced using `mpl_toolkits.mplot3d`.
데이터가 텍스트이고 X축에 상세할 경우 텍스트를 더 잘 읽을 수 있도록 각도를 지정할 수 있습니다. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html)은 데이터가 지원하는 경우 3D 플로팅을 제공합니다. 'mpl_toolkits.mplot3d'를 사용하여 정교한 데이터 시각화를 생성할 수 있습니다.

![3d plots](images/3d.png)

## Animation and 3D chart display
## 애니메이션 및 3D 차트 표시

Some of the best data visualizations today are animated. Shirley Wu has amazing ones done with D3, such as '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', where each flower is a visualization of a movie. Another example for the Guardian is 'bussed out', an interactive experience combining visualizations with Greensock and D3 plus a scrollytelling article format to show how NYC handles its homeless problem by bussing people out of the city.
오늘날 최고의 데이터 시각화 중 일부는 애니메이션입니다. Shirley Wu는 D3로 놀라운 작업을 했습니다.
예를 들어 '[필름 플라워](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)',에서는 각각의 꽃이 영화의 시각화이다. 가디언의 또 다른 예는 '버스드 아웃'으로, Greensock 및 D3와 시각화를 결합한 대화형 체험과 NYC가 사람들을 도시 밖으로 내쫓아 노숙자 문제를 어떻게 처리하는지 보여주는 기사 형식을 포함한다.

![busing](images/busing.png)
![버스 수송](images/busing.png)

> "Bussed Out: How America Moves its Homeless" from [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualizations by Nadieh Bremer & Shirley Wu
> [가디언](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study))의 "버스드 아웃: 미국의 노숙자 이동 방법" Nadieh Bremer & Shirley Wu의 시각화

While this lesson is insufficient to go into depth to teach these powerful visualization libraries, try your hand at D3 in a Vue.js app using a library to display a visualization of the book "Dangerous Liaisons" as an animated social network.
이 교훈은 이러한 강력한 시각화 라이브러리를 가르치기에 충분하지 않지만, 애니메이션 소셜 네트워크로서 "위험한 관계"라는 책의 시각화를 표시하기 위해 라이브러리를 사용하여 Vue.js 앱의 D3에서 여러분의 손을 사용해 보십시오.

> "Les Liaisons Dangereuses" is an epistolary novel, or a novel presented as a series of letters. Written in 1782 by Choderlos de Laclos, it tells the story of the vicious, morally-bankrupt social maneuvers of two dueling protagonists of the French aristocracy in the late 18th century, the Vicomte de Valmont and the Marquise de Merteuil. Both meet their demise in the end but not without inflicting a great deal of social damage. The novel unfolds as a series of letters written to various people in their circles, plotting for revenge or simply to make trouble. Create a visualization of these letters to discover the major kingpins of the narrative, visually.
> "Les Liaisons Dangereuses"는 편지 소설 또는 일련의 편지로 표현된 소설이다. 1782년 Choderlos de Laclos에 의해 쓰여진 이 책은 18세기 후반 프랑스 귀족의 결투적인 두 주인공인 Vicomte de Valmont와 Marquise de Merteuil의 잔인하고 도덕적으로 타락한 사회적 책략에 대한 이야기를 들려준다. 둘 다 결국 그들의 죽음을 맞이하지만 큰 사회적 피해를 입히지 않고는 아니다. 이 소설은 복수의 음모를 꾸미거나 단순히 문제를 일으키기 위해 서클에 있는 다양한 사람들에게 쓴 일련의 편지들로 전개된다. 이 글자들을 시각화해서 이야기의 주요 킹핀을 시각적으로 발견하세요.

You will complete a web app that will display an animated view of this social network. It uses a library that was built to create a [visual of a network](https://github.com/emiliorizzo/vue-d3-network) using Vue.js and D3. When the app is running, you can pull the nodes around on the screen to shuffle the data around.
이 소셜 네트워크의 애니메이션 보기를 표시하는 웹 앱을 완료합니다. Vue.js 및 D3를 사용하여 [네트워크의 시각](https://github.com/emiliorizzo/vue-d3-network))을 만들기 위해 구축된 라이브러리를 사용합니다. 앱이 실행 중일 때 화면에서 노드를 당겨 데이터를 이리저리 섞을 수 있습니다.

![liaisons](images/liaisons.png)
![관계](images/liaisons.png)

## Project: Build a chart to show a network using D3.js
## 프로젝트: D3.js를 사용하여 네트워크를 표시할 차트 작성

> This lesson folder includes a `solution` folder where you can find the completed project, for your reference.
> 이 과정 폴더에는 완료된 프로젝트를 참조할 수 있는 '솔루션' 폴더가 포함되어 있습니다.

1. Follow the instructions in the README.md file in the starter folder's root. Make sure you have NPM and Node.js running on your machine before installing your project's dependencies.
1. 스타터 폴더의 루트에 있는 README.md 파일의 지침을 따릅니다. 프로젝트의 종속성을 설치하기 전에 시스템에서 NPM 및 Node.js가 실행 중인지 확인하십시오.

2. Open the `starter/src` folder. You'll discover an `assets` folder where you can find a .json file with all the letters from the novel, numbered, with a 'to' and 'from' annotation.
2. 'starter/src' 폴더를 엽니다. 당신은 소설의 모든 글자와 번호가 매겨진 .json 파일을 찾을 수 있는 assets 폴더를 발견할 것이다.

3. Complete the code in `components/Nodes.vue` to enable the visualization. Look for the method called `createLinks()` and add the following nested loop.
3. `components/Nodes.vue`를 사용하여 시각화를 활성화합니다. createLinks()라는 메서드를 찾아 다음과 같은 중첩 루프를 추가합니다.

Loop through the .json object to capture the 'to' and 'from' data for the letters and build up the `links` object so that the visualization library can consume it:
.json 객체를 루프하여 문자에 대한 'to' 및 'from' 데이터를 캡처하고 시각화 라이브러리가 사용할 수 있도록 'links' 객체를 구축합니다.

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

Run your app from the terminal (npm run serve) and enjoy the visualization!
터미널(npm run serve)에서 앱을 실행하고 시각화를 즐기십시오!

## 🚀 Challenge
## 🚀 도전

Take a tour of the internet to discover deceptive visualizations. How does the author fool the user, and is it intentional? Try correcting the visualizations to show how they should look.
인터넷을 둘러보고 기만적인 시각화를 찾아보세요. 저자는 어떻게 사용자를 속이고, 의도적인가? 시각화를 수정하여 어떻게 보여야 하는지 표시해 보십시오.

## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/25)
## [강의 후 퀴즈](https://red-water-0103e7a0f.azurestaticapps.net/quiz/25)

## Review & Self Study
## 리뷰 & 셀프 학습

Here are some articles to read about deceptive data visualization:
다음은 기만적인 데이터 시각화에 대한 몇 가지 기사입니다:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Take a look at these interest visualizations for historical assets and artifacts:
과거 자산 및 인공물에 대한 다음과 같은 관심 시각화를 살펴 보십시오.

https://handbook.pubpub.org/

Look through this article on how animation can enhance your visualizations:
이 기사를 통해 애니메이션이 시각화를 향상시키는 방법에 대해 알아보십시오:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Assignment
## 과제

[Build your own custom visualization](assignment.md)
[맞춤형 시각화 구축](assignment.md)
