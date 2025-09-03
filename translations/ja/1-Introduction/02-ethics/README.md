<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:02:54+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "ja"
}
-->
# データ倫理の導入

|![ [(@sketchthedocs)](https://sketchthedocs.dev) によるスケッチノート ](../../sketchnotes/02-Ethics.png)|
|:---:|
| データサイエンス倫理 - _[@nitya](https://twitter.com/nitya) によるスケッチノート_ |

---

私たちはデータ化された世界に生きるデータ市民です。

市場の動向によると、2022年までに大規模な組織の3分の1がオンラインの[マーケットプレイスや取引所](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/)を通じてデータを売買するようになると言われています。**アプリ開発者**として、データ駆動型の洞察やアルゴリズム駆動型の自動化を日常のユーザー体験に統合することが、より簡単かつ安価になります。しかし、AIが広く普及するにつれて、そのようなアルゴリズムが大規模に[武器化](https://www.youtube.com/watch?v=TQHs8SA1qpk)されることで生じる潜在的な害についても理解する必要があります。

また、2025年までに[180ゼタバイト](https://www.statista.com/statistics/871513/worldwide-data-created/)以上のデータを生成・消費するという予測もあります。**データサイエンティスト**として、これにより個人データへのアクセスがかつてないほど容易になります。これにより、ユーザーの行動プロファイルを構築し、[自由選択の錯覚](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)を作り出しながら、ユーザーを私たちが望む結果に誘導することが可能になります。しかし、これによりデータプライバシーやユーザー保護に関する広範な問題も浮上します。

データ倫理は、データサイエンスやエンジニアリングにおける潜在的な害や意図しない結果を最小限に抑えるための_必要なガードレール_です。[GartnerのAIハイプサイクル](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/)は、デジタル倫理、責任あるAI、AIガバナンスに関連するトレンドを、AIの_民主化_と_産業化_を推進する主要なメガトレンドとして特定しています。

![GartnerのAIハイプサイクル - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

このレッスンでは、データ倫理の魅力的な分野を探求します。基本的な概念や課題から、ケーススタディやガバナンスのような応用AIの概念まで、データやAIを扱うチームや組織に倫理文化を確立する方法を学びます。

## [講義前のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## 基本的な定義

まずは基本的な用語を理解することから始めましょう。

「倫理」という言葉は、[ギリシャ語の「ethikos」](https://en.wikipedia.org/wiki/Ethics)（その語源である「ethos」）に由来し、_性格や道徳的性質_を意味します。

**倫理**とは、社会における行動を支配する共有価値観や道徳的原則のことです。倫理は法律ではなく、「正しい vs. 間違っている」という広く受け入れられた規範に基づいています。しかし、倫理的な考慮事項は、企業統治の取り組みや政府規制に影響を与え、コンプライアンスのインセンティブを増やすことがあります。

**データ倫理**は、_データ、アルゴリズム、対応する実践_に関連する道徳的問題を「研究し評価する」[新しい倫理の分野](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1)です。ここで、**「データ」**は生成、記録、キュレーション、処理、普及、共有、使用に関連する行動に焦点を当て、**「アルゴリズム」**はAI、エージェント、機械学習、ロボットに焦点を当て、**「実践」**は責任あるイノベーション、プログラミング、ハッキング、倫理コードなどのトピックに焦点を当てます。

**応用倫理**は、_現実世界の行動、製品、プロセス_の文脈で倫理的問題を積極的に調査し、定義された倫理的価値観に一致するように是正措置を講じる[道徳的考慮事項の実践的応用](https://en.wikipedia.org/wiki/Applied_ethics)です。

**倫理文化**は、組織全体で倫理的原則と実践が一貫して拡張可能な方法で採用されるようにするために、応用倫理を[_運用化_](https://hbr.org/2019/05/how-to-design-an-ethical-organization)することです。成功する倫理文化は、組織全体の倫理的原則を定義し、コンプライアンスに対する意味のあるインセンティブを提供し、望ましい行動を奨励し増幅することで、組織のあらゆるレベルで倫理規範を強化します。

## 倫理の概念

このセクションでは、データ倫理における**共有価値観**（原則）や**倫理的課題**（問題）について議論し、これらの概念を現実世界の文脈で理解するための**ケーススタディ**を探求します。

### 1. 倫理原則

すべてのデータ倫理戦略は、_倫理原則_を定義することから始まります。これは、データとAIプロジェクトにおける許容される行動を記述し、コンプライアンス行動を導く「共有価値観」です。これらは個人やチームレベルで定義することができます。しかし、ほとんどの大規模な組織では、これらを企業レベルで定義され、すべてのチームで一貫して施行される_倫理的AI_ミッションステートメントやフレームワークにまとめています。

**例:** Microsoftの[責任あるAI](https://www.microsoft.com/en-us/ai/responsible-ai)ミッションステートメントは、_「人々を第一に考える倫理原則によって推進されるAIの進歩にコミットしています」_と述べており、以下の6つの倫理原則を特定しています：

![Microsoftの責任あるAI](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

これらの原則を簡単に見てみましょう。_透明性_と_責任_は他の原則の基盤となる価値観であるため、まずそこから始めます：

* [**責任**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)は、実践者がデータとAIの運用に対して_責任_を持ち、これらの倫理原則に準拠することを保証します。
* [**透明性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)は、データとAIの行動がユーザーにとって_理解可能_（解釈可能）であり、決定の背後にある内容と理由を説明することを保証します。
* [**公平性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)は、AIが_すべての人々_を公平に扱い、データやシステムにおける体系的または暗黙的な社会技術的バイアスに対処することに焦点を当てます。
* [**信頼性と安全性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)は、AIが定義された価値観に_一貫して_従い、潜在的な害や意図しない結果を最小限に抑えることを保証します。
* [**プライバシーとセキュリティ**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)は、データの系譜を理解し、ユーザーに_データプライバシーと関連する保護_を提供することに焦点を当てます。
* [**包括性**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)は、AIソリューションを意図的に設計し、_幅広い人間のニーズ_と能力に対応するように適応させることに焦点を当てます。

> 🚨 あなたのデータ倫理ミッションステートメントはどのようなものになるでしょうか。他の組織の倫理的AIフレームワークを探求してみましょう。例えば、[IBM](https://www.ibm.com/cloud/learn/ai-ethics)、[Google](https://ai.google/principles)、[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/)の例があります。これらの共有価値観にはどのような共通点がありますか？これらの原則は、それぞれのAI製品や業界にどのように関連していますか？

### 2. 倫理的課題

倫理原則を定義した後、次のステップは、データとAIの行動がこれらの共有価値観と一致しているかどうかを評価することです。行動を_データ収集_と_アルゴリズム設計_の2つのカテゴリーで考えてみましょう。

データ収集では、行動は**個人データ**や個人を特定できる情報（PII）を含む可能性があります。これには、個人を_集合的に_特定する[多様な非個人データ](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en)が含まれます。倫理的課題は、_データプライバシー_、_データ所有権_、および_インフォームドコンセント_や_知的財産権_などの関連トピックに関連する可能性があります。

アルゴリズム設計では、行動は**データセット**を収集・キュレーションし、それを使用して**データモデル**をトレーニング・展開し、現実世界の文脈で結果を予測したり意思決定を自動化したりすることに関連します。倫理的課題は、_データセットのバイアス_、_データ品質_の問題、_不公平性_、およびアルゴリズムの_誤表現_に関連する可能性があります。これには、体系的な問題も含まれることがあります。

どちらの場合も、倫理的課題は、行動が共有価値観と衝突する可能性のある領域を強調します。これらの懸念を検出、緩和、最小化、または排除するためには、行動に関連する道徳的な「はい/いいえ」の質問を行い、必要に応じて是正措置を講じる必要があります。倫理的課題とそれが提起する道徳的質問をいくつか見てみましょう：

#### 2.1 データ所有権

データ収集は、データ主体を特定できる個人データを含むことがよくあります。[データ所有権](https://permission.io/blog/data-ownership)は、データの生成、処理、普及に関連する_コントロール_と[_ユーザー権利_](https://permission.io/blog/data-ownership)に関するものです。

道徳的な質問は以下の通りです：
 * データの所有者は誰ですか？（ユーザーまたは組織）
 * データ主体にはどのような権利がありますか？（例：アクセス、消去、移植性）
 * 組織にはどのような権利がありますか？（例：悪意のあるユーザーレビューの修正）

#### 2.2 インフォームドコンセント

[インフォームドコンセント](https://legaldictionary.net/informed-consent/)は、ユーザーが目的、潜在的なリスク、代替案を含む関連事実を_完全に理解_した上で、行動（例：データ収集）に同意する行為を定義します。

ここで探求する質問は：
 * ユーザー（データ主体）はデータの収集と使用に許可を与えましたか？
 * ユーザーはそのデータが収集された目的を理解しましたか？
 * ユーザーは参加による潜在的なリスクを理解しましたか？

#### 2.3 知的財産

[知的財産](https://en.wikipedia.org/wiki/Intellectual_property)は、人間の創意工夫から生まれた無形の創造物であり、個人や企業にとって_経済的価値_を持つ可能性があります。

ここで探求する質問は：
 * 収集されたデータはユーザーや企業にとって経済的価値を持っていましたか？
 * **ユーザー**には知的財産がありますか？
 * **組織**には知的財産がありますか？
 * これらの権利が存在する場合、それらをどのように保護していますか？

#### 2.4 データプライバシー

[データプライバシー](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/)または情報プライバシーは、個人を特定できる情報に関して、ユーザーのプライバシーを維持し、ユーザーの身元を保護することを指します。

ここで探求する質問は：
 * ユーザーの（個人）データはハッキングや漏洩から保護されていますか？
 * ユーザーのデータは許可されたユーザーや文脈にのみアクセス可能ですか？
 * データが共有または普及される際にユーザーの匿名性は維持されていますか？
 * 匿名化されたデータセットからユーザーを特定することは可能ですか？

#### 2.5 忘れられる権利

[忘れられる権利](https://en.wikipedia.org/wiki/Right_to_be_forgotten)または[消去権](https://www.gdpreu.org/right-to-be-forgotten/)は、ユーザーに追加の個人データ保護を提供します。具体的には、特定の状況下でインターネット検索やその他の場所から個人データの削除または除去を要求する権利をユーザーに与え、過去の行動がユーザーに不利に働かないようにします。

ここで探求する質問は：
 * システムはデータ主体が消去を要求することを許可していますか？
 * ユーザーの同意の撤回が自動消去を引き起こすべきですか？
 * データは同意なしまたは違法な手段で収集されましたか？
 * データプライバシーに関する政府規制に準拠していますか？

#### 2.6 データセットのバイアス

データセットまたは[収集バイアス](http://researcharticles.com/index.php/bias-in-data-collection-in-research/)は、アルゴリズム開発のために_非代表的な_データのサブセットを選択することで、さまざまなグループに対する結果の公平性に潜在的な影響を与えることを指します。バイアスの種類には、選択またはサンプリングバイアス、ボランティアバイアス、機器バイアスがあります。

ここで探求する質問は：
 * 代表的なデータ主体のセットを募集しましたか？
 * 収集またはキュレーションされたデータセットをさまざまなバイアスについてテストしましたか？
 * 発見されたバイアスを緩和または除去することは可能ですか？

#### 
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) は、アルゴリズム設計が特定のデータ主体のサブグループに対して体系的に差別を行い、_資源配分_（そのグループに対して資源が拒否または保留される場合）や_サービスの質_（AIが特定のサブグループに対して他のグループほど正確でない場合）における[潜在的な害](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml)を引き起こすかどうかを確認するものです。

ここで検討すべき質問は以下の通りです：
 * 多様なサブグループや条件に対してモデルの精度を評価しましたか？
 * ステレオタイプ化などの潜在的な害についてシステムを精査しましたか？
 * 特定された害を軽減するためにデータを修正したりモデルを再学習させることは可能ですか？

[AI Fairness チェックリスト](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA)などのリソースを探求して、さらに学びましょう。

#### 2.9 誤表現

[データの誤表現](https://www.sciencedirect.com/topics/computer-science/misrepresentation)とは、正直に報告されたデータから得られた洞察を、望ましいストーリーを支持するために欺瞞的に伝えていないかどうかを問うことです。

ここで検討すべき質問は以下の通りです：
 * 不完全または不正確なデータを報告していませんか？
 * 誤解を招く結論を導くような方法でデータを視覚化していませんか？
 * 結果を操作するために選択的な統計手法を使用していませんか？
 * 別の結論を提供する可能性のある代替説明はありませんか？

#### 2.10 自由選択

[自由選択の錯覚](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice)は、システムの「選択アーキテクチャ」が意思決定アルゴリズムを使用して、ユーザーに選択肢やコントロールを与えているように見せながら、好ましい結果を取るよう促す場合に発生します。これらの[ダークパターン](https://www.darkpatterns.org/)は、ユーザーに社会的および経済的な害を引き起こす可能性があります。ユーザーの意思決定は行動プロファイルに影響を与えるため、これらの行動は将来の選択を促進または拡大する可能性があります。

ここで検討すべき質問は以下の通りです：
 * ユーザーはその選択をすることの影響を理解していましたか？
 * ユーザーは（代替の）選択肢とそれぞれの利点と欠点を認識していましたか？
 * ユーザーは自動化された選択や影響を受けた選択を後で取り消すことができますか？

### 3. ケーススタディ

これらの倫理的課題を現実世界の文脈で考えるには、倫理違反が見過ごされた場合に個人や社会に与える潜在的な害や結果を強調するケーススタディを検討することが役立ちます。

以下はいくつかの例です：

| 倫理的課題 | ケーススタディ  | 
|--- |--- |
| **インフォームドコンセント** | 1972年 - [タスキーギ梅毒研究](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - 研究に参加したアフリカ系アメリカ人男性は無料の医療を約束されましたが、研究者によって診断や治療の利用可能性について知らされずに欺かれました。多くの被験者が死亡し、パートナーや子供にも影響が及びました。この研究は40年間続きました。 | 
| **データプライバシー** |  2007年 - [Netflixデータ賞](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/)は、研究者に_50Kの顧客からの10Mの匿名化された映画ランキング_を提供し、推薦アルゴリズムを改善することを目的としていました。しかし、研究者は匿名化されたデータを外部データセット（例：IMDbコメント）と関連付けることで、一部のNetflix加入者を「匿名解除」することができました。|
| **収集バイアス**  | 2013年 - ボストン市は[Street Bump](https://www.boston.gov/transportation/street-bump)というアプリを開発し、市民が道路の穴を報告できるようにし、市が問題を特定して修正するためのより良い道路データを提供しました。しかし、[低所得層の人々は車や電話へのアクセスが少ない](https://hbr.org/2013/04/the-hidden-biases-in-big-data)ため、このアプリでは彼らの道路問題が見えなくなっていました。開発者は公平性のために_公平なアクセスとデジタル格差_の問題に取り組むために学者と協力しました。 |
| **アルゴリズムの公平性**  | 2018年 - MITの[Gender Shades Study](http://gendershades.org/overview.html)は、性別分類AI製品の精度を評価し、女性や有色人種に対する精度のギャップを明らかにしました。[2019年のApple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/)は、男性よりも女性に少ないクレジットを提供しているように見えました。どちらもアルゴリズムバイアスが社会経済的な害を引き起こす問題を示しています。|
| **データの誤表現** | 2020年 - [ジョージア州公衆衛生局はCOVID-19のチャートを公開](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening)し、確認されたケースの傾向について市民を誤解させるような非時系列のx軸を使用しました。これは視覚化トリックによる誤表現を示しています。 |
| **自由選択の錯覚** | 2020年 - 学習アプリ[ABCmouseはFTCの苦情を解決するために$10Mを支払った](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/)ケースでは、親がキャンセルできないサブスクリプションを支払うように追い込まれました。これは、ユーザーが潜在的に有害な選択肢に誘導されるダークパターンを示しています。 |
| **データプライバシーとユーザーの権利** | 2021年 - Facebookの[データ漏洩](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users)では、530Mのユーザーのデータが漏洩し、FTCに$5Bの和解金を支払う結果となりました。しかし、漏洩についてユーザーに通知することを拒否し、データの透明性とアクセスに関するユーザーの権利を侵害しました。 |

さらにケーススタディを探求したいですか？以下のリソースをチェックしてください：
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - 多様な業界における倫理的ジレンマ。
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - 重要なケーススタディを探求。
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - Deonチェックリストと例。

> 🚨 あなたが見たケーススタディについて考えてみてください。あなたの人生で似たような倫理的課題を経験したり影響を受けたりしたことはありますか？このセクションで議論した倫理的課題を示す少なくとも1つの別のケーススタディを思いつくことができますか？

## 応用倫理

倫理の概念、課題、そして現実世界の文脈でのケーススタディについて話しました。しかし、プロジェクトで倫理的な原則や実践を_適用_するにはどうすればよいでしょうか？また、これらの実践をより良いガバナンスのために_運用化_するにはどうすればよいでしょうか？いくつかの現実的な解決策を探ってみましょう：

### 1. プロフェッショナルコード

プロフェッショナルコードは、組織がメンバーに倫理的原則やミッションステートメントを支持するよう「奨励」するための選択肢を提供します。コードはプロフェッショナルな行動のための_道徳的ガイドライン_であり、従業員やメンバーが組織の原則に沿った意思決定を行うのを助けます。これらはメンバーの自主的な遵守に依存しますが、多くの組織はメンバーの遵守を促進するために追加の報酬や罰則を提供しています。

例：
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) 倫理コード
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) 行動規範（2013年作成）
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics)（1993年以降）

> 🚨 あなたはプロフェッショナルなエンジニアリングやデータサイエンスの組織に所属していますか？そのサイトを探して、プロフェッショナルな倫理コードを定義しているかどうかを確認してください。それは彼らの倫理的原則について何を示していますか？メンバーにコードを遵守させるためにどのように「奨励」しているのでしょうか？

### 2. 倫理チェックリスト

プロフェッショナルコードは実践者に必要な_倫理的行動_を定義しますが、大規模プロジェクトにおける[既知の制限](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)があります。その代わりに、多くのデータサイエンスの専門家は[チェックリスト](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md)を提唱しており、これにより**原則を実践に結び付ける**ことがより決定論的かつ実行可能になります。

チェックリストは質問を「はい/いいえ」のタスクに変換し、運用化することができ、標準的な製品リリースワークフローの一部として追跡可能になります。

例：
 * [Deon](https://deon.drivendata.org/) - [業界の推奨事項](https://deon.drivendata.org/#checklist-citations)から作成された汎用データ倫理チェックリストで、コマンドラインツールを使用して簡単に統合可能。
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - 法的および社会的な露出の観点から情報処理の一般的なガイダンスを提供。
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI開発サイクルに公平性チェックを統合するためにAI実践者によって作成。
 * [データとAIの倫理に関する22の質問](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - 設計、実装、組織的な文脈での倫理的問題の初期探求のために構造化されたよりオープンなフレームワーク。

### 3. 倫理規制

倫理は共有価値を定義し、自発的に正しいことを行うことに関するものです。**コンプライアンス**は、定義されている場合に法律を遵守することに関するものです。**ガバナンス**は、組織が倫理的原則を強制し、確立された法律を遵守するために運営するすべての方法を広くカバーします。

今日、ガバナンスは組織内で2つの形態を取ります。まず、**倫理的AI**原則を定義し、組織内のすべてのAI関連プロジェクトにわたって採用を運用化する実践を確立することです。次に、組織が運営する地域のすべての政府が定めた**データ保護規制**を遵守することです。

データ保護とプライバシー規制の例：

 * `1974年`、[米国プライバシー法](https://www.justice.gov/opcl/privacy-act-1974) - _連邦政府_による個人情報の収集、使用、開示を規制。
 * `1996年`、[米国医療保険の携行性と責任に関する法律（HIPAA）](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - 個人の健康データを保護。
 * `1998年`、[米国児童オンラインプライバシー保護法（COPPA）](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - 13歳未満の子供のデータプライバシーを保護。
 * `2018年`、[一般データ保護規則（GDPR）](https://gdpr-info.eu/) - ユーザーの権利、データ保護、プライバシーを提供。
 * `2018年`、[カリフォルニア消費者プライバシー法（CCPA）](https://www.oag.ca.gov/privacy/ccpa) - 消費者に（個人）データに関するより多くの_権利_を提供。
 * `2021年`、中国の[個人情報保護法](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - 世界で最も強力なオンラインデータプライバシー規制の1つを作成。

> 🚨 欧州連合が定義したGDPR（一般データ保護規則）は、今日最も影響力のあるデータプライバシー規制の1つです。これが市民のデジタルプライバシーと個人データを保護するために[8つのユーザー権利](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr)を定義していることを知っていましたか？これらが何であるか、そしてなぜ重要なのかを学びましょう。

### 4. 倫理文化

_コンプライアンス_（「法律の文言」を満たすために十分なことを行うこと）と[体系的な問題](https://www.coursera.org/learn/data-science-ethics/home/week/4)（硬直化、情報の非対称性、分配の不公平性など）に対処することの間には、依然として無形のギャップがあります。これらの問題はAIの武器化を加速させる可能性があります。

後者には、業界内で_組織全体_で一貫した共有価値と感情的なつながりを構築する[倫理文化を定義するための協力的アプローチ](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f)が必要です。これには、組織内でより[正式化されたデータ倫理文化](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/)を構築することが求められます。これにより、_誰でも_（プロセスの早い段階で倫理的懸念を提起するために）[アンドンコードを引く](https://en.wikipedia.org/wiki/Andon_(manufacturing))ことができ、AIプロジェクトのチーム形成において_倫理的評価_（例：採用時）が重要な基準とな
* [責任あるAIの原則](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - Microsoft Learnによる無料学習パス。
* [倫理とデータサイエンス](https://resources.oreilly.com/examples/0636920203964) - O'Reillyの電子書籍 (M. Loukides, H. Mason 他)
* [データサイエンス倫理](https://www.coursera.org/learn/data-science-ethics#syllabus) - ミシガン大学によるオンラインコース。
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - テキサス大学によるケーススタディ。

# 課題

[データ倫理のケーススタディを書く](assignment.md)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。