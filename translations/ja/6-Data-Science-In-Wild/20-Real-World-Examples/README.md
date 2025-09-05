<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T12:54:34+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "ja"
}
-->
# 現実世界におけるデータサイエンス

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               現実世界におけるデータサイエンス - _スケッチノート by [@nitya](https://twitter.com/nitya)_               |

学習の旅もいよいよ終盤です！

私たちはデータサイエンスと倫理の定義から始まり、データ分析と可視化のためのさまざまなツールと技術を探り、データサイエンスのライフサイクルをレビューし、クラウドコンピューティングサービスを使ったデータサイエンスワークフローの拡張と自動化について学びました。そこで、次の疑問が浮かぶかもしれません: _「これらの学びを現実世界の文脈にどう結びつければいいの？」_

このレッスンでは、業界におけるデータサイエンスの現実的な応用を探り、研究、デジタル人文学、持続可能性の具体的な例を掘り下げます。また、学生プロジェクトの機会を紹介し、学習の旅を続けるための役立つリソースで締めくくります！

## 講義前クイズ

## [講義前クイズ](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## データサイエンス + 業界

AIの民主化のおかげで、開発者はAI駆動の意思決定やデータ駆動の洞察をユーザー体験や開発ワークフローに設計・統合することが以前よりも容易になっています。以下は、業界全体でデータサイエンスが「応用」されている現実的な例のいくつかです:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) は検索語とインフルエンザの傾向を関連付けるためにデータサイエンスを使用しました。このアプローチには欠点がありましたが、データ駆動型の医療予測の可能性（および課題）についての認識を高めました。

 * [UPSのルート予測](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPSがデータサイエンスと機械学習を使用して、天候条件、交通パターン、配達期限などを考慮した最適な配達ルートを予測する方法を説明しています。

 * [NYCタクシーのルート可視化](http://chriswhong.github.io/nyctaxi/) - [情報公開法](https://chriswhong.com/open-data/foil_nyc_taxi/) を使用して収集されたデータを活用し、NYCタクシーの日常を可視化。忙しい都市をどのように移動し、どれだけの収益を上げ、各24時間の間にどれだけの時間を費やしているかを理解するのに役立ちます。

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - 毎日数百万件のUberの乗車データ（ピックアップ＆ドロップオフの場所、乗車時間、好まれるルートなど）を活用して、価格設定、安全性、不正検出、ナビゲーションの意思決定を支援するデータ分析ツールを構築。

 * [スポーツ分析](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - _予測分析_（チームや選手の分析 - [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) を想像してください - およびファン管理）と _データ可視化_（チーム＆ファンダッシュボード、ゲームなど）に焦点を当て、才能スカウト、スポーツ賭博、在庫/会場管理などの応用例を提供。

 * [銀行業界におけるデータサイエンス](https://data-flair.training/blogs/data-science-in-banking/) - リスクモデリングや不正検出から顧客セグメンテーション、リアルタイム予測、レコメンダーシステムまで、金融業界におけるデータサイエンスの価値を強調。予測分析は、[信用スコア](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit) のような重要な指標を推進。

 * [医療におけるデータサイエンス](https://data-flair.training/blogs/data-science-in-healthcare/) - 医療画像（例: MRI、X線、CTスキャン）、ゲノミクス（DNA配列解析）、薬剤開発（リスク評価、成功予測）、予測分析（患者ケア＆供給物流）、疾病追跡＆予防などの応用例を強調。

![現実世界におけるデータサイエンスの応用](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) 画像提供: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

この図は、データサイエンス技術を応用する他の分野と例を示しています。他の応用例を探りたいですか？以下の [レビュー＆自己学習](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) セクションをチェックしてください。

## データサイエンス + 研究

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンス＆研究 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

現実世界の応用はしばしば業界の大規模なユースケースに焦点を当てますが、_研究_ の応用とプロジェクトは以下の2つの観点から有益です:

* _イノベーションの機会_ - 次世代アプリケーションのための高度な概念の迅速なプロトタイピングとユーザー体験のテストを探る。
* _展開の課題_ - 現実世界の文脈でデータサイエンス技術が引き起こす可能性のある害や意図しない結果を調査。

学生にとって、これらの研究プロジェクトは学習と協力の機会を提供し、トピックの理解を深め、関連する分野で活動する人々やチームとの認識と関与を広げることができます。それでは、研究プロジェクトはどのようなものか、そしてそれがどのように影響を与えることができるのかを見てみましょう。

一例として、Joy Buolamwini（MIT Media Labs）による [MIT Gender Shades Study](http://gendershades.org/overview.html) を見てみましょう。この研究は、Timnit Gebru（当時Microsoft Research所属）との共著による[代表的な研究論文](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)を伴い、以下に焦点を当てました:

 * **何を:** 研究プロジェクトの目的は、_性別と肌の色に基づく自動顔分析アルゴリズムとデータセットに存在するバイアスを評価すること_ でした。
 * **なぜ:** 顔分析は、法執行機関、空港のセキュリティ、採用システムなどの分野で使用されており、不正確な分類（例: バイアスによる）が影響を受ける個人やグループに経済的および社会的な害を引き起こす可能性があります。バイアスを理解し、それを排除または軽減することは、公平な使用の鍵です。
 * **どのように:** 研究者は、既存のベンチマークが主に肌の色が明るい被験者を使用していることを認識し、性別と肌の色でよりバランスの取れた新しいデータセット（1000以上の画像）を作成しました。このデータセットを使用して、3つの性別分類製品（Microsoft、IBM、Face++）の精度を評価しました。

結果は、全体的な分類精度は良好であるものの、さまざまなサブグループ間でエラー率に顕著な違いがあることを示しました。特に、**性別誤認識**が女性や肌の色が濃い人々で高く、バイアスを示唆していました。

**主な成果:** データサイエンスには、より_代表的なデータセット_（バランスの取れたサブグループ）と、より_包括的なチーム_（多様な背景）が必要であり、AIソリューションでのバイアスを早期に認識し排除または軽減することが重要であるという認識を高めました。このような研究努力は、多くの組織がAI製品とプロセスの公平性を向上させるための_責任あるAI_ の原則と実践を定義する上で重要です。

**Microsoftの関連研究努力について学びたいですか？**

* [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) の人工知能に関するプロジェクトをチェックしてください。
* [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) の学生プロジェクトを探ってみてください。
* [Fairlearn](https://fairlearn.org/) プロジェクトと [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) イニシアチブをチェックしてください。

## データサイエンス + 人文学

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンス＆デジタル人文学 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

デジタル人文学は、「計算方法と人文学的探求を組み合わせた実践とアプローチの集合」と[定義されています](https://digitalhumanities.stanford.edu/about-dh-stanford)。[スタンフォードのプロジェクト](https://digitalhumanities.stanford.edu/projects) では、_「歴史の再起動」_ や _「詩的思考」_ のような例が示されており、[デジタル人文学とデータサイエンス](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) の関連性を強調しています。これらは、ネットワーク分析、情報可視化、空間およびテキスト分析などの技術を活用し、歴史的および文学的データセットを再検討して新たな洞察や視点を得ることを目的としています。

*この分野でプロジェクトを探求し拡張したいですか？*

["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) をチェックしてください。これは、[Jen Looper](https://twitter.com/jenlooper) による素晴らしい例で、データサイエンスを使って馴染みのある詩を再検討し、その意味や作者の貢献を新しい文脈で評価する方法を問うものです。例えば、_詩のトーンや感情を分析することで、その詩が書かれた季節を予測できるか_ - そしてそれが関連する期間における作者の精神状態について何を教えてくれるのか？

その質問に答えるために、データサイエンスライフサイクルのステップをたどります:
 * [`データ取得`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - 分析のための関連データセットを収集します。API（例: [Poetry DB API](https://poetrydb.org/index.html)）を使用するか、ウェブページをスクレイピング（例: [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)）するオプションがあります。
 * [`データクリーニング`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - テキストをフォーマット、整理、簡素化する方法を基本ツール（Visual Studio CodeやMicrosoft Excelなど）を使って説明します。
 * [`データ分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - データセットを「ノートブック」にインポートし、Pythonパッケージ（pandas、numpy、matplotlibなど）を使用してデータを整理・可視化する方法を説明します。
 * [`感情分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - Text Analyticsのようなクラウドサービスを統合し、[Power Automate](https://flow.microsoft.com/en-us/) のようなローコードツールを使用して自動データ処理ワークフローを実現する方法を説明します。

このワークフローを使用して、詩の感情に季節が与える影響を探り、作者に対する独自の視点を形成することができます。ぜひ試してみてください - その後、ノートブックを拡張して他の質問を投げかけたり、新しい方法でデータを可視化してみてください！

> [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) のツールを使ってこれらの探求を進めることができます。

## データサイエンス + 持続可能性

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンス＆持続可能性 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

[2030年持続可能な開発のためのアジェンダ](https://sdgs.un.org/2030agenda) - 2015年にすべての国連加盟国によって採択されたこのアジェンダは、**気候変動の影響から地球を保護する**ことに焦点を当てた目標を含む17の目標を特定しています。[Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) イニシアチブはこれらの目標を支援し、技術ソリューションを活用してより持続可能な未来を構築する方法を探ることで、[4つの目標](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) に焦点を当てています - 2030年までに炭素ネガティブ、水ポジティブ、ゼロ廃棄物、生物多様性を実現すること。

これらの課題にスケーラブルかつタイムリーに取り組むには、クラウドスケールの思考と大規模なデータが必要です。[Planetary Computer](https://planetarycomputer.microsoft.com/) イニシアチブは、データサイエンティストや開発者を支援するために以下の4つのコンポーネントを提供しています:

 * [データカタログ](https://planetarycomputer.microsoft.com/catalog) - 地球システムデータのペタバイト（無料＆Azureホスト）。
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - 空間と時間を超えて関連データを検索するためのAPI。
 * [ハブ](https://planetarycomputer.microsoft.com/docs/overview/environment/) - 科学者が大規模な地理空間データセットを処理するための管理環境。
 * [アプリケーション](https://planetarycomputer.microsoft.com/applications) - 持続可能性の洞
**現在、Planetary Computerプロジェクトはプレビュー段階です（2021年9月時点）** - データサイエンスを活用して持続可能性の解決策に貢献する方法をご紹介します。

* [アクセスをリクエスト](https://planetarycomputer.microsoft.com/account/request)して、探索を開始し、仲間とつながりましょう。
* [ドキュメントを探索](https://planetarycomputer.microsoft.com/docs/overview/about)して、サポートされているデータセットやAPIを理解しましょう。
* [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/)のようなアプリケーションを探索して、アプリケーションのアイデアにインスピレーションを得ましょう。

気候変動や森林破壊といった分野で、データ可視化を活用して関連する洞察を明らかにしたり、強調したりする方法を考えてみてください。また、洞察を活用して、より持続可能な生活を促す行動変容を促進する新しいユーザー体験を生み出す方法についても考えてみましょう。

## データサイエンス + 学生

私たちは、産業界や研究における実際の応用について話し合い、デジタル人文学や持続可能性におけるデータサイエンスの応用例を探求しました。それでは、データサイエンス初心者としてスキルを磨き、専門知識を共有するにはどうすればよいでしょうか？

以下は、学生向けのデータサイエンスプロジェクトの例です。ぜひ参考にしてください。

 * [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects)では、以下のようなトピックを探求するGitHubの[プロジェクト](https://github.com/msr-ds3)があります：
    - [警察の武力行使における人種的偏見](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [ニューヨーク市地下鉄システムの信頼性](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [物質文化のデジタル化：Sirkapにおける社会経済的分布の探求](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom)氏とClaremontのチームによるプロジェクトで、[ArcGIS StoryMaps](https://storymaps.arcgis.com/)を使用。

## 🚀 チャレンジ

初心者向けのデータサイエンスプロジェクトを推奨する記事を探してみましょう。例えば、[これらの50のトピックエリア](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/)や[これらの21のプロジェクトアイデア](https://www.intellspot.com/data-science-project-ideas)、[ソースコード付きの16のプロジェクト](https://data-flair.training/blogs/data-science-project-ideas/)などがあります。これらを分解して再構築してみてください。そして、学習の過程をブログに書き、私たちと洞察を共有するのを忘れないでください。

## 講義後のクイズ

## [講義後のクイズ](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## 復習と自己学習

さらにユースケースを探求したいですか？以下の関連する記事をご覧ください：
 * [17のデータサイエンスの応用例](https://builtin.com/data-science/data-science-applications-examples) - 2021年7月
 * [現実世界における11の驚くべきデータサイエンスの応用](https://myblindbird.com/data-science-applications-real-world/) - 2021年5月
 * [現実世界のデータサイエンス](https://towardsdatascience.com/data-science-in-the-real-world/home) - 記事コレクション
 * データサイエンスの応用： [教育](https://data-flair.training/blogs/data-science-in-education/)、[農業](https://data-flair.training/blogs/data-science-in-agriculture/)、[金融](https://data-flair.training/blogs/data-science-in-finance/)、[映画](https://data-flair.training/blogs/data-science-at-movies/)など。

## 課題

[Planetary Computerのデータセットを探索する](assignment.md)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。