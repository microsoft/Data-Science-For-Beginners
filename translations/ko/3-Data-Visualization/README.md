<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1441550a0d789796b2821e04f7f4cc94",
  "translation_date": "2025-08-25T17:58:20+00:00",
  "source_file": "3-Data-Visualization/README.md",
  "language_code": "ko"
}
-->
# 시각화

![라벤더 꽃 위의 벌](../../../translated_images/bee.0aa1d91132b12e3a8994b9ca12816d05ce1642010d9b8be37f8d37365ba845cf.ko.jpg)
> 사진 제공: <a href="https://unsplash.com/@jenna2980?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jenna Lee</a> on <a href="https://unsplash.com/s/photos/bees-in-a-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

데이터 시각화는 데이터 과학자에게 가장 중요한 작업 중 하나입니다. "이미지는 천 마디 말보다 강하다"는 말처럼, 시각화는 데이터의 스파이크, 이상치, 그룹화, 경향 등 흥미로운 부분을 식별하는 데 도움을 주며, 데이터가 전달하려는 이야기를 이해하는 데 큰 도움을 줍니다.

이 다섯 가지 강의에서는 자연에서 얻은 데이터를 탐구하고 다양한 기법을 사용하여 흥미롭고 아름다운 시각화를 만들어 볼 것입니다.

| 주제 번호 | 주제 | 연결된 강의 | 저자 |
| :-----------: | :--: | :-----------: | :----: |
| 1. | 수량 시각화 | <ul> <li> [Python](09-visualization-quantities/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/09-visualization-quantities) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 2. | 분포 시각화 | <ul> <li> [Python](10-visualization-distributions/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/10-visualization-distributions) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 3. | 비율 시각화 | <ul> <li> [Python](11-visualization-proportions/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 4. | 관계 시각화 | <ul> <li> [Python](12-visualization-relationships/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 5. | 의미 있는 시각화 만들기 | <ul> <li> [Python](13-meaningful-visualizations/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |

### 크레딧

이 시각화 강의는 🌸 [Jen Looper](https://twitter.com/jenlooper), [Jasleen Sondhi](https://github.com/jasleen101010), [Vidushi Gupta](https://github.com/Vidushi-Gupta)가 작성했습니다.

🍯 미국 꿀 생산 데이터는 Jessica Li의 [Kaggle](https://www.kaggle.com/jessicali9530/honey-production) 프로젝트에서 가져왔습니다. 이 [데이터](https://usda.library.cornell.edu/concern/publications/rn301137d)는 [미국 농무부](https://www.nass.usda.gov/About_NASS/index.php)에서 제공한 자료를 기반으로 합니다.

🍄 버섯 데이터는 Hatteras Dunton이 수정한 [Kaggle](https://www.kaggle.com/hatterasdunton/mushroom-classification-updated-dataset)에서 가져왔습니다. 이 데이터셋은 Agaricus와 Lepiota 계열의 23종의 주름버섯에 해당하는 가상의 샘플 설명을 포함하고 있습니다. 데이터는 The Audubon Society Field Guide to North American Mushrooms (1981)에서 발췌되었으며, 1987년 UCI ML 27에 기증되었습니다.

🦆 미네소타 새 데이터는 [Kaggle](https://www.kaggle.com/hannahcollins/minnesota-birds)에서 가져왔으며, Hannah Collins가 [Wikipedia](https://en.wikipedia.org/wiki/List_of_birds_of_Minnesota)에서 스크랩한 자료입니다.

이 모든 데이터셋은 [CC0: Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/) 라이선스로 제공됩니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.