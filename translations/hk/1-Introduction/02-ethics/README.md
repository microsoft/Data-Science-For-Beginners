<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T16:08:44+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hk"
}
-->
# 數據倫理簡介

|![由 [(@sketchthedocs)](https://sketchthedocs.dev) 繪製的速寫筆記](../../sketchnotes/02-Ethics.png)|
|:---:|
| 數據科學倫理 - _由 [@nitya](https://twitter.com/nitya) 繪製的速寫筆記_ |

---

我們都是生活在數據化世界中的數據公民。

市場趨勢顯示，到2022年，三分之一的大型組織將通過在線[市場和交易所](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)購買和出售數據。作為**應用程式開發者**，我們將更容易、更便宜地將數據驅動的洞察力和算法驅動的自動化整合到日常用戶體驗中。但隨著人工智能的普及，我們也需要了解這些算法在大規模應用中可能造成的[武器化](https://www.youtube.com/watch?v=TQHs8SA1qpk)危害。

趨勢顯示，到2025年，我們將生成和消耗超過[180澤字節](https://www.statista.com/statistics/871513/worldwide-data-created/)的數據。對於**數據科學家**來說，這種信息爆炸提供了前所未有的個人和行為數據的訪問權。這使得我們能夠建立詳細的用戶檔案並微妙地影響決策——通常以促進[自由選擇的幻覺](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/)的方式進行。雖然這可以用來引導用戶朝向偏好的結果，但也引發了關於數據隱私、自主性以及算法影響的倫理界限的關鍵問題。

數據倫理現在是數據科學和工程的_必要防護欄_，幫助我們減少數據驅動行動可能帶來的潛在危害和意外後果。[Gartner人工智能技術成熟度曲線](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)指出，數字倫理、負責任的人工智能和人工智能治理是推動人工智能_民主化_和_工業化_的主要趨勢。

![Gartner 2020人工智能技術成熟度曲線](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

在本課程中，我們將探索數據倫理的迷人領域——從核心概念和挑戰，到案例研究和應用人工智能概念（如治理），幫助在處理數據和人工智能的團隊和組織中建立倫理文化。

## [課前測驗](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## 基本定義

讓我們先了解一些基本術語。

"倫理"一詞源自[希臘詞 "ethikos"](https://en.wikipedia.org/wiki/Ethics)（及其根詞 "ethos"），意指_品格或道德本質_。

**倫理**是指在社會中規範我們行為的共同價值觀和道德原則。倫理並非基於法律，而是基於廣泛接受的"對與錯"的標準。然而，倫理考量可以影響公司治理倡議和政府法規，從而創造更多遵守的激勵措施。

**數據倫理**是一個[新興的倫理分支](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)，研究和評估與_數據、算法及相關實踐_相關的道德問題。在這裡，**"數據"**側重於生成、記錄、策劃、處理、傳播、共享和使用的行動，**"算法"**側重於人工智能、代理、機器學習和機器人，**"實踐"**側重於負責任的創新、編程、黑客行為和倫理守則等主題。

**應用倫理**是[道德考量的實際應用](https://en.wikipedia.org/wiki/Applied_ethics)。它是積極調查_現實世界行動、產品和流程_中的倫理問題，並採取糾正措施以確保這些行動與我們定義的倫理價值保持一致的過程。

**倫理文化**是關於[_操作化_應用倫理](https://hbr.org/2019/05/how-to-design-an-ethical-organization)，確保我們的倫理原則和實踐在整個組織中以一致且可擴展的方式被採用。成功的倫理文化定義了全組織的倫理原則，提供有意義的遵守激勵措施，並通過鼓勵和放大期望的行為來加強倫理規範。

## 倫理概念

在本節中，我們將討論**共同價值觀**（原則）和**倫理挑戰**（問題）等數據倫理概念，並探索**案例研究**，幫助您在現實世界的背景中理解這些概念。

### 1. 倫理原則

每個數據倫理策略都始於定義_倫理原則_——描述可接受行為並指導合規行動的"共同價值觀"，用於我們的數據和人工智能項目。您可以在個人或團隊層面定義這些原則。然而，大多數大型組織會在公司層面定義並一致執行的_倫理人工智能_使命聲明或框架中概述這些原則。

**示例：** 微軟的[負責任人工智能](https://www.microsoft.com/en-us/ai/responsible-ai)使命聲明寫道：_"我們致力於推動以倫理原則為基礎的人工智能發展，將人放在首位"_，並在以下框架中確定了6個倫理原則：

![微軟的負責任人工智能](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

讓我們簡要探討這些原則。_透明性_和_問責性_是其他原則的基礎價值觀，因此我們從這裡開始：

* [**問責性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)使實踐者對其數據和人工智能操作以及遵守這些倫理原則負責。
* [**透明性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)確保數據和人工智能行動對用戶是_可理解的_（可解釋的），解釋決策背後的內容和原因。
* [**公平性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)——確保人工智能公平對待_所有人_，解決數據和系統中的任何系統性或隱性社會技術偏見。
* [**可靠性與安全性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——確保人工智能以_一致性_的方式行事，減少潛在危害或意外後果。
* [**隱私與安全**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——關於理解數據來源，並為用戶提供_數據隱私及相關保護_。
* [**包容性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——旨在有意設計人工智能解決方案，並使其適應_廣泛的人類需求_和能力。

> 🚨 想一想您的數據倫理使命聲明可能是什麼。探索其他組織的倫理人工智能框架——以下是[IBM](https://www.ibm.com/cloud/learn/ai-ethics)、[Google](https://ai.google/principles)和[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/)的示例。他們有哪些共同的價值觀？這些原則如何與他們所運營的人工智能產品或行業相關？

### 2. 倫理挑戰

一旦我們定義了倫理原則，下一步就是評估我們的數據和人工智能行動是否與這些共同價值觀一致。思考您的行動可以分為兩類：_數據收集_和_算法設計_。

在數據收集方面，行動可能涉及**個人數據**或可識別的個人信息（PII），這些信息可以識別活著的個人。這包括[多樣化的非個人數據項目](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)，這些數據_共同_識別一個個體。倫理挑戰可能涉及_數據隱私_、_數據所有權_以及相關主題，如_知情同意_和用戶的_知識產權權利_。

在算法設計方面，行動將涉及收集和策劃**數據集**，然後使用它們來訓練和部署**數據模型**，以在現實世界的背景中預測結果或自動化決策。倫理挑戰可能源於_數據集偏差_、_數據質量_問題、_不公平性_以及算法中的_誤導性_——包括一些系統性問題。

在這兩種情況下，倫理挑戰突出了我們的行動可能與共同價值觀發生衝突的領域。為了檢測、減輕、最小化或消除這些問題，我們需要針對我們的行動提出道德的"是/否"問題，然後根據需要採取糾正措施。讓我們看看一些倫理挑戰及其引發的道德問題：

#### 2.1 數據所有權

數據收集通常涉及可以識別數據主體的個人數據。[數據所有權](https://permission.io/blog/data-ownership)是關於與數據的創建、處理和傳播相關的_控制_和[_用戶權利_](https://permission.io/blog/data-ownership)。

需要提出的道德問題包括：
 * 誰擁有數據？（用戶或組織）
 * 數據主體擁有哪些權利？（例如：訪問、刪除、可攜性）
 * 組織擁有哪些權利？（例如：糾正惡意用戶評論）

#### 2.2 知情同意

[知情同意](https://legaldictionary.net/informed-consent/)指的是用戶在充分了解相關事實（包括目的、潛在風險和替代方案）的情況下同意某項行動（如數據收集）。

需要探討的問題包括：
 * 用戶（數據主體）是否允許數據的捕獲和使用？
 * 用戶是否理解捕獲數據的目的？
 * 用戶是否理解參與可能帶來的潛在風險？

#### 2.3 知識產權

[知識產權](https://en.wikipedia.org/wiki/Intellectual_property)指的是由人類創造的無形產物，可能對個人或企業具有_經濟價值_。

需要探討的問題包括：
 * 收集的數據是否對用戶或企業具有經濟價值？
 * **用戶**是否擁有知識產權？
 * **組織**是否擁有知識產權？
 * 如果存在這些權利，我們如何保護它們？

#### 2.4 數據隱私

[數據隱私](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/)或信息隱私指的是在涉及可識別個人信息時，保護用戶隱私和身份。

需要探討的問題包括：
 * 用戶的（個人）數據是否免受黑客攻擊和洩漏？
 * 用戶的數據是否僅對授權用戶和上下文可訪問？
 * 在共享或傳播數據時，是否保護了用戶的匿名性？
 * 用戶是否可以從匿名數據集中被去識別？

#### 2.5 被遺忘的權利

[被遺忘的權利](https://en.wikipedia.org/wiki/Right_to_be_forgotten)或[刪除權](https://www.gdpreu.org/right-to-be-forgotten/)為用戶提供額外的個人數據保護。具體而言，它賦予用戶在特定情況下要求從互聯網搜索和其他位置刪除或移除個人數據的權利，_讓他們在網上重新開始，而不受過去行動的影響_。

需要探討的問題包括：
 * 系統是否允許數據主體請求刪除？
 * 用戶撤回同意是否應觸發自動刪除？
 * 是否在未經同意或非法手段下收集了數據？
 * 我們是否符合政府對數據隱私的法規？

#### 2.6 數據集偏差

數據集或[收集偏差](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)指的是為算法開發選擇了_非代表性_的數據子集，可能導致對不同群體的結果不公平。偏差類型包括選擇或抽樣偏差、志願者偏差和工具偏差。

需要探討的問題包括：
 * 我們是否招募了代表性數據主體？
 * 我們是否測試了收集或策劃的數據集以檢測各種偏差？
 * 我們是否能減輕或消除發現的偏差？

#### 2.7 數據質量

[數據質量](https://lakefs.io/data-quality-testing/)檢查用於開發算法的策劃數據集的有效性，確保特徵和記錄符合人工智能目的所需的準確性和一致性要求。

需要探討的問題包括：
 * 我們是否捕獲了適合用例的有效_特徵_？
 * 數據是否在不同數據源中_一致性_地捕獲？
 * 數據集是否在不同條件或場景下_完整_？
* 是否準確捕捉信息以反映現實？

#### 2.8 演算法公平性

[演算法公平性](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f)檢查演算法設計是否系統性地對特定數據主體的子群體造成歧視，導致在資源分配（即資源被拒絕或扣留）和服務質量（即人工智能對某些子群體的準確性不如其他群體）方面的[潛在傷害](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)。

需要探討的問題包括：
* 我們是否評估了模型在不同子群體和條件下的準確性？
* 我們是否仔細檢查了系統的潛在傷害（例如刻板印象）？
* 我們是否可以修正數據或重新訓練模型以減輕已識別的傷害？

探索像[AI公平性檢查清單](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA)這樣的資源以了解更多。

#### 2.9 錯誤表述

[數據錯誤表述](https://www.sciencedirect.com/topics/computer-science/misrepresentation)是指我們是否以欺騙的方式傳達來自誠實報告數據的洞察，以支持某種期望的敘述。

需要探討的問題包括：
* 我們是否報告了不完整或不準確的數據？
* 我們是否以誤導性結論的方式可視化數據？
* 我們是否使用選擇性統計技術來操縱結果？
* 是否存在可能提供不同結論的替代解釋？

#### 2.10 自由選擇

[自由選擇的幻覺](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)發生在系統的“選擇架構”使用決策演算法來引導人們選擇偏好的結果，同時看似給予他們選擇和控制權。這些[黑暗模式](https://www.darkpatterns.org/)可能對用戶造成社會和經濟上的傷害。由於用戶的決策會影響行為檔案，這些行動可能會驅動未來的選擇，進一步放大或延伸這些傷害的影響。

需要探討的問題包括：
* 用戶是否理解做出該選擇的影響？
* 用戶是否了解（替代）選擇及其各自的利弊？
* 用戶是否可以在後期逆轉自動化或受影響的選擇？

### 3. 案例研究

為了將這些倫理挑戰置於現實世界的背景中，研究案例研究有助於了解當忽視這些倫理問題時，對個人和社會可能造成的傷害和後果。

以下是一些例子：

| 倫理挑戰 | 案例研究 | 
|--- |--- |
| **知情同意** | 1972年 - [塔斯基吉梅毒研究](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 參與研究的非裔美國男性被承諾提供免費醫療服務，但研究人員欺騙了受試者，未告知其診斷或治療的可用性。許多受試者死亡，其伴侶或子女受到影響；研究持續了40年。 | 
| **數據隱私** | 2007年 - [Netflix數據獎](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/)向研究人員提供了_10M匿名化的50K客戶電影評分_以改進推薦演算法。然而，研究人員能夠將匿名數據與外部數據集（例如IMDb評論）中的個人身份數據相關聯，實際上“去匿名化”了一些Netflix訂閱者。|
| **收集偏差** | 2013年 - 波士頓市[開發了Street Bump](https://www.boston.gov/transportation/street-bump)，一款讓市民報告坑洞的應用程式，幫助城市獲得更好的道路數據以發現和修復問題。然而，[低收入群體的人們較少擁有汽車和手機](https://hbr.org/2013/04/the-hidden-biases-in-big-data)，使得他們的道路問題在此應用程式中不可見。開發者與學者合作解決公平性問題，例如_公平訪問和數字鴻溝_。|
| **演算法公平性** | 2018年 - MIT [Gender Shades研究](http://gendershades.org/overview.html)評估了性別分類AI產品的準確性，揭示了對女性和有色人種準確性方面的差距。一個[2019年Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/)似乎給女性提供的信用額度低於男性。這兩個例子都說明了演算法偏差導致的社會經濟傷害問題。|
| **數據錯誤表述** | 2020年 - [喬治亞州公共衛生部發布COVID-19圖表](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening)，似乎通過非時間順序的x軸排列誤導公民關於確診病例趨勢的理解。這說明了通過可視化技巧進行的錯誤表述。|
| **自由選擇的幻覺** | 2020年 - 學習應用程式[ABCmouse支付了$10M以解決FTC投訴](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/)，家長被困於無法取消的訂閱付款中。這說明了選擇架構中的黑暗模式，導致用戶被引導做出可能有害的選擇。|
| **數據隱私與用戶權利** | 2021年 - Facebook [數據洩露](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users)洩露了530M用戶的數據，導致向FTC支付了$5B的和解金。然而，它拒絕通知用戶洩露事件，違反了用戶關於數據透明性和訪問的權利。|

想探索更多案例研究？查看以下資源：
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 涵蓋多個行業的倫理困境。
* [數據科學倫理課程](https://www.coursera.org/learn/data-science-ethics#syllabus) - 探索標誌性案例研究。
* [問題出在哪裡](https://deon.drivendata.org/examples/) - Deon清單中的示例。

> 🚨 回想你所見過的案例研究——你是否曾經經歷過或受到類似倫理挑戰的影響？你能否想到至少一個其他案例研究來說明我們在本節中討論的倫理挑戰之一？

## 應用倫理

我們已經討論了倫理概念、挑戰以及在現實世界中的案例研究。但我們如何開始在項目中_應用_倫理原則和實踐？以及如何_實現_這些實踐以改善治理？讓我們探索一些現實世界的解決方案：

### 1. 專業守則

專業守則為組織提供了一種選擇，通過“激勵”成員支持其倫理原則和使命聲明。守則是專業行為的_道德指南_，幫助員工或成員做出符合其組織原則的決策。守則的效力取決於成員的自願遵守；然而，許多組織提供額外的獎勵和懲罰以激勵成員遵守。

示例包括：

* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/)倫理守則
* [數據科學協會](http://datascienceassn.org/code-of-conduct.html)行為守則（創建於2013年）
* [ACM倫理守則與專業行為守則](https://www.acm.org/code-of-ethics)（自1993年起）

> 🚨 你是否屬於某個專業工程或數據科學組織？探索其網站，查看是否定義了專業倫理守則。這些守則說明了哪些倫理原則？他們如何“激勵”成員遵守守則？

### 2. 倫理清單

雖然專業守則定義了從業者所需的_倫理行為_，但它們在執行方面[存在已知的局限性](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，特別是在大型項目中。因此，許多數據科學專家[提倡使用清單](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，這些清單可以**將原則與實踐**更具決定性地聯繫起來。

清單將問題轉化為“是/否”任務，可以操作化，並允許它們作為標準產品發布工作流程的一部分進行跟蹤。

示例包括：
* [Deon](https://deon.drivendata.org/) - 一個通用數據倫理清單，由[行業建議](https://deon.drivendata.org/#checklist-citations)創建，並配有命令行工具以便於集成。
* [隱私審核清單](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 從法律和社會暴露的角度提供信息處理實踐的一般指導。
* [AI公平性清單](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - 由AI從業者創建，以支持公平性檢查的採用和集成到AI開發周期中。
* [數據與AI倫理的22個問題](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 更開放式的框架，結構化以初步探索設計、實施和組織背景中的倫理問題。

### 3. 倫理法規

倫理是關於定義共享價值並_自願_做正確的事情。**合規**是指_遵守法律_（如果有定義）。**治理**則涵蓋了組織運作以執行倫理原則並遵守既定法律的所有方式。

今天，治理在組織內部有兩種形式。首先，它是關於定義**倫理AI**原則並建立實踐以操作化採用，涵蓋組織內所有與AI相關的項目。其次，它是關於遵守所有政府規定的**數據保護法規**，適用於其運營的地區。

數據保護和隱私法規的示例：

* `1974年`，[美國隱私法案](https://www.justice.gov/opcl/privacy-act-1974) - 規範_聯邦政府_收集、使用和披露個人信息。
* `1996年`，[美國健康保險流通與責任法案（HIPAA）](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 保護個人健康數據。
* `1998年`，[美國兒童在線隱私保護法案（COPPA）](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 保護13歲以下兒童的數據隱私。
* `2018年`，[通用數據保護法規（GDPR）](https://gdpr-info.eu/) - 提供用戶權利、數據保護和隱私。
* `2018年`，[加州消費者隱私法案（CCPA）](https://www.oag.ca.gov/privacy/ccpa) - 賦予消費者更多關於其（個人）數據的_權利_。
* `2021年`，中國[個人信息保護法](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/)剛剛通過，創造了全球最強的在線數據隱私法規之一。

> 🚨 歐盟定義的GDPR（通用數據保護法規）仍然是今天最具影響力的數據隱私法規之一。你知道它還定義了[8項用戶權利](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)以保護公民的數字隱私和個人數據嗎？了解這些權利是什麼以及它們為什麼重要。

### 4. 倫理文化

注意，_合規_（僅僅做到符合“法律條文”）與解決[系統性問題](https://www.coursera.org/learn/data-science-ethics/home/week/4)（例如僵化、信息不對稱和分配不公平）之間仍然存在無形的差距，這些問題可能加速AI的武器化。

後者需要[協作方式來定義倫理文化](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)，在行業內部建立情感聯繫和一致的共享價值。這需要在組織內部建立更[正式化的數據倫理文化](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/)——允許_任何人_拉動[安燈繩](https://en.wikipedia.org/wiki/Andon_(manufacturing))（在過程早期提出倫理問題），並將_倫理評估_（例如在招聘中）作為AI項目團隊組建的核心標準。

---
## [課後測驗](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## 回顧與自學

課程和書籍有助於理解核心倫理概念和挑戰，而案例研究和工具有助於在現實世界中應用倫理實踐。以下是一些入門資源。
* [機器學習入門](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - 來自 Microsoft 的公平性課程。
* [負責任人工智能的原則](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - Microsoft Learn 提供的免費學習路徑。
* [倫理與數據科學](https://resources.oreilly.com/examples/0636920203964) - O'Reilly 電子書 (M. Loukides, H. Mason 等人著)
* [數據科學倫理](https://www.coursera.org/learn/data-science-ethics#syllabus) - 密歇根大學提供的線上課程。
* [倫理解讀](https://ethicsunwrapped.utexas.edu/case-studies) - 來自德州大學的案例研究。

# 作業

[撰寫數據倫理案例研究](assignment.md)

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。