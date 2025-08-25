<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-25T16:41:17+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hk"
}
-->
# 數據倫理簡介

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| 數據科學倫理 - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

我們都是生活在數據化世界中的數據公民。

市場趨勢顯示，到2022年，每三家大型組織中就有一家會通過線上[市場和交易所](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)購買和出售數據。作為**應用程式開發者**，我們會發現將數據驅動的洞察力和算法驅動的自動化整合到日常用戶體驗中變得更加容易和便宜。然而，隨著人工智能的普及，我們也需要了解這些算法在大規模應用中可能引發的[武器化](https://www.youtube.com/watch?v=TQHs8SA1qpk)危害。

趨勢還顯示，到2025年，我們將創造和消耗超過[180澤字節](https://www.statista.com/statistics/871513/worldwide-data-created/)的數據。作為**數據科學家**，這讓我們能夠前所未有地接觸到個人數據。這意味著我們可以建立用戶的行為檔案，並以某些方式影響決策，從而創造一種[自由選擇的幻覺](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)，同時可能引導用戶朝向我們偏好的結果。這也引發了關於數據隱私和用戶保護的更廣泛問題。

數據倫理現在是數據科學和工程的_必要防護措施_，幫助我們減少數據驅動行動可能帶來的潛在危害和意外後果。[Gartner人工智能技術成熟度曲線](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)指出，數字倫理、負責任的人工智能和人工智能治理是推動人工智能_民主化_和_工業化_的主要趨勢。

![Gartner人工智能技術成熟度曲線 - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

在本課程中，我們將探索數據倫理這個迷人的領域——從核心概念和挑戰，到案例研究和應用人工智能概念（如治理），幫助在處理數據和人工智能的團隊和組織中建立倫理文化。

## [課前測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## 基本定義

讓我們先了解一些基本術語。

「倫理」一詞源自[希臘詞「ethikos」](https://en.wikipedia.org/wiki/Ethics)（及其根詞「ethos」），意為_品格或道德本質_。

**倫理**是指在社會中指導我們行為的共同價值觀和道德原則。倫理不是基於法律，而是基於廣泛接受的「對與錯」的規範。然而，倫理考量可以影響企業治理倡議和政府法規，從而創造更多遵守的激勵措施。

**數據倫理**是一個[新的倫理分支](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)，研究和評估與_數據、算法及相關實踐_相關的道德問題。在這裡，**「數據」**聚焦於生成、記錄、策劃、處理、傳播、共享和使用的行動，**「算法」**聚焦於人工智能、代理、機器學習和機器人，**「實踐」**聚焦於負責任的創新、編程、黑客行為和倫理守則等主題。

**應用倫理**是[道德考量的實際應用](https://en.wikipedia.org/wiki/Applied_ethics)。它是積極調查_現實世界行動、產品和流程_中的倫理問題，並採取糾正措施以確保這些行動與我們定義的倫理價值保持一致。

**倫理文化**是關於[將應用倫理_付諸實踐_](https://hbr.org/2019/05/how-to-design-an-ethical-organization)，確保我們的倫理原則和實踐在整個組織中以一致且可擴展的方式被採用。成功的倫理文化會定義全組織的倫理原則，提供有意義的遵守激勵措施，並通過鼓勵和放大期望的行為來加強倫理規範。

## 倫理概念

在本節中，我們將討論數據倫理中的**共同價值觀**（原則）和**倫理挑戰**（問題），並探索**案例研究**，幫助你在現實世界的背景中理解這些概念。

### 1. 倫理原則

每個數據倫理策略都始於定義_倫理原則_——描述可接受行為並指導數據和人工智能項目中合規行動的「共同價值觀」。你可以在個人或團隊層面定義這些原則。然而，大多數大型組織會在企業層面定義並一致執行的_倫理人工智能_使命聲明或框架中概述這些原則。

**例子：** 微軟的[負責任人工智能](https://www.microsoft.com/en-us/ai/responsible-ai)使命聲明寫道：_「我們致力於推動以倫理原則為基礎的人工智能發展，將人放在首位」_——並在以下框架中確定了六個倫理原則：

![微軟的負責任人工智能](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

讓我們簡要探討這些原則。_透明性_和_問責性_是其他原則的基礎價值觀，因此我們從這裡開始：

* [**問責性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)使實踐者對其數據和人工智能操作以及遵守這些倫理原則負責。
* [**透明性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)確保數據和人工智能行動對用戶是_可理解的_（可解釋的），並解釋決策背後的原因和內容。
* [**公平性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)——確保人工智能公平對待_所有人_，解決數據和系統中的系統性或隱性社會技術偏見。
* [**可靠性與安全性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——確保人工智能以_一致性_的方式行事，並減少潛在危害或意外後果。
* [**隱私與安全**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——關注數據來源，並為用戶提供_數據隱私及相關保護_。
* [**包容性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)——旨在有意設計人工智能解決方案，並使其適應_廣泛的人類需求_和能力。

> 🚨 想想你的數據倫理使命聲明可能是什麼。探索其他組織的倫理人工智能框架——以下是[IBM](https://www.ibm.com/cloud/learn/ai-ethics)、[Google](https://ai.google/principles)和[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/)的例子。他們有哪些共同的價值觀？這些原則如何與他們所運營的人工智能產品或行業相關？

### 2. 倫理挑戰

一旦我們定義了倫理原則，下一步就是評估我們的數據和人工智能行動是否符合這些共同價值觀。思考你的行動可以分為兩類：_數據收集_和_算法設計_。

在數據收集方面，行動可能涉及**個人數據**或可識別的個人信息（PII），這些信息可以識別活著的個人。這包括[多樣化的非個人數據項目](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)，這些數據_共同_識別一個人。倫理挑戰可能涉及_數據隱私_、_數據所有權_以及相關主題，如_知情同意_和_用戶的知識產權_。

在算法設計方面，行動將涉及收集和策劃**數據集**，然後使用它們來訓練和部署**數據模型**，以在現實世界的背景中預測結果或自動化決策。倫理挑戰可能來自_數據集偏見_、_數據質量_問題、_不公平性_和算法中的_誤導性_，包括一些系統性問題。

在這兩種情況下，倫理挑戰突出了我們的行動可能與共同價值觀發生衝突的領域。為了檢測、減輕、最小化或消除這些問題，我們需要針對行動提出道德「是/否」問題，然後根據需要採取糾正措施。讓我們看看一些倫理挑戰及其引發的道德問題：

#### 2.1 數據所有權

數據收集通常涉及可識別數據主體的個人數據。[數據所有權](https://permission.io/blog/data-ownership)是關於與數據的創建、處理和傳播相關的_控制_和[用戶權利](https://permission.io/blog/data-ownership)。

需要提出的道德問題包括：
* 誰擁有數據？（用戶或組織）
* 數據主體擁有哪些權利？（例如：訪問、刪除、可攜性）
* 組織擁有哪些權利？（例如：糾正惡意用戶評論）

#### 2.2 知情同意

[知情同意](https://legaldictionary.net/informed-consent/)指用戶在充分了解相關事實（包括目的、潛在風險和替代方案）的情況下同意某項行動（如數據收集）。

需要探討的問題包括：
* 用戶（數據主體）是否授權數據捕獲和使用？
* 用戶是否理解捕獲數據的目的？
* 用戶是否理解參與可能帶來的潛在風險？

#### 2.3 知識產權

[知識產權](https://en.wikipedia.org/wiki/Intellectual_property)指由人類創造的無形產物，可能對個人或企業具有_經濟價值_。

需要探討的問題包括：
* 收集的數據是否對用戶或企業具有經濟價值？
* **用戶**是否擁有知識產權？
* **組織**是否擁有知識產權？
* 如果存在這些權利，我們如何保護它們？

#### 2.4 數據隱私

[數據隱私](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/)或信息隱私指保護用戶隱私和身份，尤其是與可識別個人信息相關的部分。

需要探討的問題包括：
* 用戶的（個人）數據是否防止黑客攻擊和洩漏？
* 用戶的數據是否僅限授權用戶和情境訪問？
* 用戶的匿名性是否在數據共享或傳播時得到保護？
* 用戶是否可以從匿名數據集中被重新識別？

#### 2.5 被遺忘的權利

[被遺忘的權利](https://en.wikipedia.org/wiki/Right_to_be_forgotten)或[刪除權](https://www.gdpreu.org/right-to-be-forgotten/)為用戶提供額外的個人數據保護。具體而言，它賦予用戶在特定情況下要求刪除或移除個人數據的權利，允許他們在網上重新開始，而不受過去行為的影響。

需要探討的問題包括：
* 系統是否允許數據主體請求刪除？
* 用戶撤回同意是否應觸發自動刪除？
* 是否存在未經同意或非法手段收集的數據？
* 我們是否符合政府對數據隱私的法規？

#### 2.6 數據集偏見

數據集或[收集偏見](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)指選擇_非代表性_的數據子集進行算法開發，可能導致對不同群體的結果不公平。偏見類型包括選擇或抽樣偏見、志願者偏見和工具偏見。

需要探討的問題包括：
* 我們是否招募了代表性數據主體？
* 我們是否測試了收集或策劃的數據集以檢測各種偏見？
* 我們是否能減輕或消除發現的偏見？

#### 2.7 數據質量

[數據質量](https://lakefs.io/data-quality-testing/)檢查用於開發算法的策劃數據集的有效性，確保特徵和記錄符合人工智能目的所需的準確性和一致性要求。

需要探討的問題包括：
* 我們是否捕獲了適合我們用例的有效_特徵_？
* 數據是否在不同數據源中_一致地_捕獲？
* 數據集是否_完整_，涵蓋多樣化的條件或場景？
* 捕獲的信息是否_準確_反映了現實？

#### 2.8 算法公平性
[算法公平性](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) 是檢查算法設計是否系統性地對特定數據群體進行歧視，從而導致在資源分配（_allocation_，即資源被拒絕或剝奪）和服務質量（_quality of service_，即人工智能對某些群體的準確性不如對其他群體）方面的[潛在傷害](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)。

需要探討的問題包括：
 * 我們是否評估了模型在不同群體和條件下的準確性？
 * 我們是否仔細檢查了系統可能帶來的傷害（例如，刻板印象）？
 * 我們是否可以修正數據或重新訓練模型以減輕已識別的傷害？

探索像 [AI 公平性檢查清單](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) 這樣的資源以了解更多。

#### 2.9 錯誤呈現

[數據錯誤呈現](https://www.sciencedirect.com/topics/computer-science/misrepresentation) 是指我們是否以欺騙性的方式傳達來自誠實報告數據的洞察，以支持某種期望的敘述。

需要探討的問題包括：
 * 我們是否報告了不完整或不準確的數據？
 * 我們是否以誤導性的方式可視化數據，從而得出錯誤結論？
 * 我們是否使用選擇性的統計技術來操縱結果？
 * 是否存在其他可能提供不同結論的解釋？

#### 2.10 自由選擇

[自由選擇的假象](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) 是指系統的“選擇架構”使用決策算法來引導人們選擇某種偏好的結果，同時表面上給予他們選擇和控制的權利。這些[黑暗模式](https://www.darkpatterns.org/)可能對用戶造成社會和經濟上的傷害。由於用戶的決策會影響行為檔案，這些行為可能進一步驅動未來的選擇，從而放大或延續這些傷害的影響。

需要探討的問題包括：
 * 用戶是否理解做出該選擇的影響？
 * 用戶是否了解（替代）選擇及其各自的優缺點？
 * 用戶是否可以在事後撤銷自動化或受影響的選擇？

### 3. 案例研究

將這些倫理挑戰放在現實世界的背景中，研究案例有助於了解當忽視這些倫理問題時，對個人和社會可能造成的傷害和後果。

以下是一些例子：

| 倫理挑戰 | 案例研究  | 
|--- |--- |
| **知情同意** | 1972年 - [塔斯基吉梅毒研究](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 參與研究的非裔美國男性被承諾提供免費醫療服務，但研究人員欺騙他們，未告知其診斷或治療的可用性。許多受試者因此死亡，其伴侶或子女也受到影響；該研究持續了40年。 | 
| **數據隱私** | 2007年 - [Netflix數據獎](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) 向研究人員提供了_50000名用戶的1000萬條匿名電影評分_，以改進推薦算法。然而，研究人員能夠將匿名數據與外部數據集（例如IMDb評論）中的個人身份數據相關聯，實際上“去匿名化”了一些Netflix用戶。|
| **數據收集偏差** | 2013年 - 波士頓市[開發了Street Bump](https://www.boston.gov/transportation/street-bump)，一款讓市民報告坑洞的應用，幫助城市獲取更好的道路數據以解決問題。然而，[低收入群體的人更少擁有汽車和手機](https://hbr.org/2013/04/the-hidden-biases-in-big-data)，使得他們的道路問題在該應用中不可見。開發者與學者合作解決_公平性和數字鴻溝_問題。 |
| **算法公平性** | 2018年 - MIT [Gender Shades研究](http://gendershades.org/overview.html) 評估了性別分類AI產品的準確性，揭示了對女性和有色人種準確性不足的問題。一個[2019年Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) 似乎給女性提供的信用額度低於男性。這兩個案例都說明了算法偏差導致的社會經濟傷害問題。|
| **數據錯誤呈現** | 2020年 - [喬治亞州公共衛生部發布的COVID-19圖表](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) 似乎通過非時間順序的x軸排序誤導公眾對確診病例趨勢的理解。這說明了通過可視化技巧進行的錯誤呈現。 |
| **自由選擇的假象** | 2020年 - 學習應用[ABCmouse支付了1000萬美元以解決FTC投訴](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/)，家長被迫支付無法取消的訂閱費用。這說明了選擇架構中的黑暗模式，導致用戶做出潛在有害的選擇。 |
| **數據隱私與用戶權利** | 2021年 - Facebook [數據洩露](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 導致5.3億用戶數據洩露，最終支付了50億美元的和解金給FTC。然而，它拒絕通知用戶洩露事件，違反了用戶對數據透明性和訪問的權利。 |

想了解更多案例研究？查看以下資源：
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 涵蓋多個行業的倫理困境。
* [數據科學倫理課程](https://www.coursera.org/learn/data-science-ethics#syllabus) - 探討標誌性案例研究。
* [問題出在哪裡](https://deon.drivendata.org/examples/) - Deon清單中的案例示例。

> 🚨 想想你見過的案例研究——你是否曾經遇到過或受到過類似倫理挑戰的影響？你能想到至少一個其他案例來說明我們在本節中討論的倫理挑戰嗎？

## 應用倫理

我們已經討論了倫理概念、挑戰以及現實世界中的案例研究。但我們如何開始在項目中_應用_倫理原則和實踐？我們又如何_實現_這些實踐以改進治理？讓我們來探討一些現實世界的解決方案：

### 1. 專業守則

專業守則為組織提供了一種選擇，通過“激勵”成員支持其倫理原則和使命聲明。守則是專業行為的_道德指導方針_，幫助員工或成員做出符合組織原則的決策。它的有效性取決於成員的自願遵守；然而，許多組織提供額外的獎勵和懲罰來激勵成員遵守。

示例包括：

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) 倫理守則
 * [數據科學協會](http://datascienceassn.org/code-of-conduct.html) 行為守則（創建於2013年）
 * [ACM倫理與專業行為守則](https://www.acm.org/code-of-ethics)（自1993年起）

> 🚨 你是否屬於某個專業工程或數據科學組織？探索他們的網站，看看是否定義了專業倫理守則。這些守則說明了他們的倫理原則嗎？他們如何“激勵”成員遵守守則？

### 2. 倫理檢查清單

雖然專業守則定義了從業者所需的_倫理行為_，但它們在執行方面[存在已知的局限性](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，特別是在大規模項目中。因此，許多數據科學專家[提倡使用檢查清單](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)，這些清單可以將原則與實踐**聯繫起來**，以更具決定性和可操作的方式。

檢查清單將問題轉化為“是/否”任務，可以被操作化，並作為標準產品發布工作流程的一部分進行跟蹤。

示例包括：
 * [Deon](https://deon.drivendata.org/) - 一個通用的數據倫理檢查清單，基於[行業建議](https://deon.drivendata.org/#checklist-citations)創建，並提供命令行工具以便於集成。
 * [隱私審核清單](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 從法律和社會曝光的角度提供信息處理實踐的一般指導。
 * [AI公平性檢查清單](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - 由AI從業者創建，用於支持公平性檢查的採用和集成到AI開發週期中。
 * [數據與AI倫理的22個問題](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 更開放的框架，結構化用於設計、實施和組織背景下的倫理問題初步探索。

### 3. 倫理法規

倫理是關於定義共同價值觀並_自願_做正確的事情。**合規**是指在法律規定的情況下_遵守法律_。**治理**則廣泛涵蓋了組織運營中為了執行倫理原則和遵守既定法律的所有方式。

如今，治理在組織內部有兩種形式。首先，它是關於定義**倫理AI**原則並建立實踐，以在組織內的所有AI相關項目中實現採用。其次，它是關於遵守其運營地區的所有政府規定的**數據保護法規**。

數據保護和隱私法規的示例：

 * `1974年`，[美國隱私法案](https://www.justice.gov/opcl/privacy-act-1974) - 規範_聯邦政府_對個人信息的收集、使用和披露。
 * `1996年`，[美國健康保險攜帶與責任法案（HIPAA）](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 保護個人健康數據。
 * `1998年`，[美國兒童在線隱私保護法案（COPPA）](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 保護13歲以下兒童的數據隱私。
 * `2018年`，[通用數據保護條例（GDPR）](https://gdpr-info.eu/) - 提供用戶權利、數據保護和隱私。
 * `2018年`，[加州消費者隱私法案（CCPA）](https://www.oag.ca.gov/privacy/ccpa) - 賦予消費者更多對其（個人）數據的_權利_。
 * `2021年`，中國[個人信息保護法](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) 剛剛通過，成為全球最強的在線數據隱私法規之一。

> 🚨 歐盟定義的GDPR（通用數據保護條例）仍然是當今最具影響力的數據隱私法規之一。你知道它還定義了[8項用戶權利](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)來保護公民的數字隱私和個人數據嗎？了解這些權利是什麼以及它們為什麼重要。

### 4. 倫理文化

需要注意的是，_合規_（僅僅滿足“法律條文”的要求）與解決[系統性問題](https://www.coursera.org/learn/data-science-ethics/home/week/4)（如僵化、信息不對稱和分配不公平）之間仍然存在無形的差距，而這些問題可能加速AI的武器化。

後者需要[協作方式來定義倫理文化](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)，以在行業內部建立情感聯繫和一致的共同價值觀。這需要在組織內部[正式化數據倫理文化](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/)——允許_任何人_ [拉動安燈繩](https://en.wikipedia.org/wiki/Andon_(manufacturing))（在過程早期提出倫理問題），並將_倫理評估_（例如，在招聘中）作為AI項目團隊組建的核心標準。

---
## [課後測驗](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## 回顧與自學 

課程和書籍有助於理解核心倫理概念和挑戰，而案例研究和工具則有助於在現實世界中應用倫理實踐。以下是一些入門資源：

* [機器學習初學者](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - 來自Microsoft的公平性課程。
* [負責任人工智能的原則](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - Microsoft Learn 提供的免費學習路徑。
* [倫理與數據科學](https://resources.oreilly.com/examples/0636920203964) - O'Reilly 電子書 (M. Loukides, H. Mason 等人著)
* [數據科學倫理](https://www.coursera.org/learn/data-science-ethics#syllabus) - 密歇根大學提供的線上課程。
* [倫理解構](https://ethicsunwrapped.utexas.edu/case-studies) - 德州大學的案例研究。

# 作業

[撰寫一個數據倫理案例研究](assignment.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。