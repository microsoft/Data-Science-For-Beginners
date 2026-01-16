<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1441550a0d789796b2821e04f7f4cc94",
  "translation_date": "2025-08-27T10:06:27+00:00",
  "source_file": "3-Data-Visualization/README.md",
  "language_code": "mo"
}
-->
# 視覺化

![一隻蜜蜂停在薰衣草花上](../../../translated_images/mo/bee.0aa1d91132b12e3a8994b9ca12816d05ce1642010d9b8be37f8d37365ba845cf.jpg)
> 照片由 <a href="https://unsplash.com/@jenna2980?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jenna Lee</a> 提供，來源於 <a href="https://unsplash.com/s/photos/bees-in-a-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

視覺化數據是數據科學家最重要的任務之一。圖片勝過千言萬語，視覺化可以幫助你識別數據中的各種有趣部分，例如峰值、異常值、分組、趨勢等，這些都能幫助你理解數據背後的故事。

在這五節課中，你將探索來自自然的數據，並使用各種技術創建有趣且美麗的視覺化。

| 主題編號 | 主題 | 相關課程 | 作者 |
| :-----------: | :--: | :-----------: | :----: |
| 1. | 數量視覺化 | <ul> <li> [Python](09-visualization-quantities/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/09-visualization-quantities) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 2. | 分佈視覺化 | <ul> <li> [Python](10-visualization-distributions/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/10-visualization-distributions) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 3. | 比例視覺化 | <ul> <li> [Python](11-visualization-proportions/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 4. | 關係視覺化 | <ul> <li> [Python](12-visualization-relationships/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 5. | 創建有意義的視覺化 | <ul> <li> [Python](13-meaningful-visualizations/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |

### 致謝

這些視覺化課程由 [Jen Looper](https://twitter.com/jenlooper)、[Jasleen Sondhi](https://github.com/jasleen101010) 和 [Vidushi Gupta](https://github.com/Vidushi-Gupta) 用 🌸 精心編寫。

🍯 美國蜂蜜生產數據來源於 Jessica Li 在 [Kaggle](https://www.kaggle.com/jessicali9530/honey-production) 的項目。該 [數據](https://usda.library.cornell.edu/concern/publications/rn301137d) 來自 [美國農業部](https://www.nass.usda.gov/About_NASS/index.php)。

🍄 蘑菇數據同樣來源於 [Kaggle](https://www.kaggle.com/hatterasdunton/mushroom-classification-updated-dataset)，由 Hatteras Dunton 修訂。該數據集包括描述假設樣本，對應於 Agaricus 和 Lepiota 家族中 23 種有鰓蘑菇。蘑菇信息取自《Audubon Society Field Guide to North American Mushrooms》（1981）。該數據集於 1987 年捐贈給 UCI ML 27。

🦆 明尼蘇達州鳥類數據來自 [Kaggle](https://www.kaggle.com/hannahcollins/minnesota-birds)，由 Hannah Collins 從 [Wikipedia](https://en.wikipedia.org/wiki/List_of_birds_of_Minnesota) 抓取。

所有這些數據集均以 [CC0: Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/) 授權。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。