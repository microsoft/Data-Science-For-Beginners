<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "67076ed50f54e7d26ba1ba378d6078f1",
  "translation_date": "2025-08-24T12:54:32+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "ja"
}
-->
# 現実世界におけるデータサイエンス

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               現実世界におけるデータサイエンス - _スケッチノート by [@nitya](https://twitter.com/nitya)_               |

この学習の旅もいよいよ終盤に差し掛かっています！

私たちはデータサイエンスと倫理の定義から始め、データ分析と可視化のためのさまざまなツールや技術を探求し、データサイエンスのライフサイクルをレビューし、クラウドコンピューティングサービスを活用してデータサイエンスのワークフローをスケールアップおよび自動化する方法を見てきました。そこで、皆さんはこう思っているかもしれません：「これらの学びを現実世界の文脈にどう結びつければいいの？」

このレッスンでは、業界におけるデータサイエンスの現実的な応用を探り、研究、デジタル人文学、持続可能性といった具体的な例を掘り下げます。また、学生プロジェクトの機会を見て、学びを続けるための役立つリソースで締めくくります！

## 講義前クイズ

[講義前クイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/38)

## データサイエンス + 業界

AIの民主化のおかげで、開発者はAI駆動の意思決定やデータ駆動の洞察をユーザー体験や開発ワークフローに設計・統合することが以前よりも容易になっています。以下は、業界全体でデータサイエンスが「応用」されているいくつかの例です：

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) は、検索語とインフルエンザの流行を関連付けるためにデータサイエンスを使用しました。このアプローチには欠点がありましたが、データ駆動型の医療予測の可能性（および課題）についての認識を高めました。

 * [UPSのルート予測](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPSがデータサイエンスと機械学習を使用して、天候条件、交通パターン、配達期限などを考慮した最適な配達ルートを予測する方法を説明しています。

 * [NYCタクシールートの可視化](http://chriswhong.github.io/nyctaxi/) - [情報公開法](https://chriswhong.com/open-data/foil_nyc_taxi/)を使用して収集されたデータを活用し、NYCタクシーの日常を可視化しました。これにより、タクシーが忙しい都市をどのように移動し、どれだけの収益を上げ、24時間ごとの移動時間がどのようになっているかを理解することができます。

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - 毎日数百万件のUberの乗車データ（乗車・降車地点、移動時間、好まれるルートなど）を使用して、価格設定、安全性、不正検出、ナビゲーションの意思決定を支援するデータ分析ツールを構築しています。

 * [スポーツ分析](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - _予測分析_（チームや選手の分析 - [マネーボール](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/)を思い浮かべてください - やファン管理）と_データ可視化_（チームやファンダッシュボード、ゲームなど）に焦点を当てています。タレントスカウティング、スポーツ賭博、在庫/会場管理などに応用されています。

 * [銀行業界におけるデータサイエンス](https://data-flair.training/blogs/data-science-in-banking/) - リスクモデリングや不正検出、顧客セグメンテーション、リアルタイム予測、レコメンダーシステムなど、金融業界におけるデータサイエンスの価値を強調しています。予測分析は、[信用スコア](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit)のような重要な指標にも役立っています。

 * [医療におけるデータサイエンス](https://data-flair.training/blogs/data-science-in-healthcare/) - 医療画像（例：MRI、X線、CTスキャン）、ゲノミクス（DNA配列解析）、薬剤開発（リスク評価、成功予測）、予測分析（患者ケアと供給物流）、疾病追跡と予防などの応用を強調しています。

![現実世界におけるデータサイエンスの応用](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) 画像提供: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

この図は、データサイエンス技術を応用する他の分野と例を示しています。他の応用例を探りたいですか？以下の[レビューと自己学習](../../../../6-Data-Science-In-Wild/20-Real-World-Examples)セクションをチェックしてください。

## データサイエンス + 研究

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンスと研究 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

現実世界の応用がスケールの大きい業界ユースケースに焦点を当てる一方で、_研究_の応用やプロジェクトは以下の2つの観点から有用です：

* _イノベーションの機会_ - 次世代アプリケーションのための高度な概念の迅速なプロトタイピングとユーザー体験のテストを探求します。
* _展開の課題_ - 現実世界の文脈でデータサイエンステクノロジーが引き起こす可能性のある害や意図しない結果を調査します。

学生にとって、これらの研究プロジェクトはトピックの理解を深め、興味のある分野で活動する関連する人々やチームとの意識や関与を広げる学習と協力の機会を提供します。それでは、研究プロジェクトはどのようなもので、どのように影響を与えるのでしょうか？

1つの例として、[MIT Gender Shades Study](http://gendershades.org/overview.html) を見てみましょう。これはJoy Buolamwini（MIT Media Labs）による研究で、Timnit Gebru（当時Microsoft Research所属）との共著による[代表的な研究論文](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)が含まれています。この研究は以下に焦点を当てています：

 * **何を:** この研究プロジェクトの目的は、_性別や肌の色に基づく自動顔分析アルゴリズムとデータセットに存在するバイアスを評価すること_でした。
 * **なぜ:** 顔分析は、法執行機関、空港のセキュリティ、採用システムなどの分野で使用されており、不正確な分類（例：バイアスによる）は、影響を受ける個人やグループに経済的および社会的な害を引き起こす可能性があります。バイアスを理解し、それを排除または軽減することは、公平性を確保するために重要です。
 * **どのように:** 研究者たちは、既存のベンチマークが主に肌の色が明るい被験者を使用していることを認識し、性別と肌の色で_よりバランスの取れた_新しいデータセット（1000以上の画像）を作成しました。このデータセットを使用して、3つの性別分類製品（Microsoft、IBM、Face++）の精度を評価しました。

結果として、全体的な分類精度は良好でしたが、さまざまなサブグループ間でエラー率に顕著な違いが見られました。特に、**女性や肌の色が濃い人々に対する誤分類**が高く、バイアスの存在を示していました。

**主な成果:** データサイエンスには_代表的なデータセット_（バランスの取れたサブグループ）と_包括的なチーム_（多様な背景）が必要であり、AIソリューションにおけるバイアスを早期に認識し、排除または軽減することが重要であるという認識を高めました。このような研究努力は、多くの組織がAI製品とプロセスの公平性を向上させるための_責任あるAI_の原則と実践を定義する上で重要な役割を果たしています。

**Microsoftの関連研究努力について学びたいですか？**

* [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) をチェックしてみてください。
* [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) の学生プロジェクトを探ってみてください。
* [Fairlearn](https://fairlearn.org/) プロジェクトや[責任あるAI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)の取り組みをチェックしてください。

## データサイエンス + 人文学

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンスとデジタル人文学 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

デジタル人文学は、「計算手法と人文学的探求を組み合わせた実践とアプローチの集合」と[定義されています](https://digitalhumanities.stanford.edu/about-dh-stanford)。[スタンフォードのプロジェクト](https://digitalhumanities.stanford.edu/projects)（例：「歴史の再起動」や「詩的思考」）は、[デジタル人文学とデータサイエンス](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science)の関連性を示しており、ネットワーク分析、情報可視化、空間およびテキスト分析といった技術が、歴史的および文学的データセットを再検討し、新たな洞察や視点を引き出すのに役立つことを強調しています。

*この分野でプロジェクトを探求し、拡張してみたいですか？*

["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) をチェックしてみてください。これは[Jen Looper](https://twitter.com/jenlooper)による素晴らしい例で、データサイエンスを使用して馴染みのある詩を再検討し、新しい文脈でその意味や作者の貢献を再評価する方法を問うものです。例えば、_詩のトーンや感情を分析することで、その詩が書かれた季節を予測できるか_、そしてそれがその期間中の作者の精神状態について何を教えてくれるのか？

この質問に答えるために、データサイエンスライフサイクルのステップをたどります：
 * [`データ取得`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - 分析のための関連データセットを収集します。選択肢には、API（例：[Poetry DB API](https://poetrydb.org/index.html)）を使用するか、[Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)のようなウェブページをスクレイピングする（例：[Scrapy](https://scrapy.org/)を使用）方法があります。
 * [`データクリーニング`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - テキストをフォーマット、サニタイズ、簡略化する方法を、Visual Studio CodeやMicrosoft Excelのような基本ツールを使用して説明します。
 * [`データ分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - Pythonパッケージ（pandas、numpy、matplotlibなど）を使用してデータを整理し、可視化するためにデータセットを「ノートブック」にインポートする方法を説明します。
 * [`感情分析`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - Text Analyticsのようなクラウドサービスを統合し、[Power Automate](https://flow.microsoft.com/en-us/)のようなローコードツールを使用してデータ処理ワークフローを自動化する方法を説明します。

このワークフローを使用して、詩の感情に対する季節の影響を探り、作者に対する独自の視点を形成することができます。ぜひ試してみてください。そして、ノートブックを拡張して他の質問を投げかけたり、新しい方法でデータを可視化してみてください！

> [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) のツールを使用して、これらの探求を進めることができます。

## データサイエンス + 持続可能性

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              データサイエンスと持続可能性 - _スケッチノート by [@nitya](https://twitter.com/nitya)_              |

[2030年持続可能な開発アジェンダ](https://sdgs.un.org/2030agenda) - 2015年にすべての国連加盟国によって採択されたこのアジェンダは、気候変動の影響や地球の劣化から**地球を守る**ことに焦点を当てた17の目標を掲げています。[Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) の取り組みは、これらの目標をサポートし、技術ソリューションを活用してより持続可能な未来を構築する方法を探求しています。その中で、[4つの目標](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - 2030年までにカーボンネガティブ、水ポジティブ、ゼロ廃棄物、生物多様性を達成することに焦点を当てています。

これらの課題にスケーラブルかつタイムリーに取り組むには、クラウド規模の思考と大規模なデータが必要です。[Planetary Computer](https://planetarycomputer.microsoft.com/) の取り組みは、データサイエンティストや開発者を支援するために以下の4つのコンポーネントを提供しています：

 * [データカタログ](https://planetarycomputer.microsoft.com/catalog) - 地球システムデータのペタバイト規模のデータセット（無料＆Azureホスト）。
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - ユーザーが空間と時間を超えて関連データを検索するのを支援。
 * [ハブ](https://planetarycomputer.microsoft.com/docs/overview/environment/) - 科学者が大規
**Planetary Computerプロジェクトは現在プレビュー中です（2021年9月時点）** - データサイエンスを活用して持続可能性の解決策に貢献する方法をご紹介します。

* 探索を開始し、仲間とつながるために[アクセスをリクエスト](https://planetarycomputer.microsoft.com/account/request)してください。
* サポートされているデータセットやAPIを理解するために[ドキュメントを探索](https://planetarycomputer.microsoft.com/docs/overview/about)してください。
* [エコシステムモニタリング](https://analytics-lab.org/ecosystemmonitoring/)のようなアプリケーションを探索し、アプリケーションのアイデアにインスピレーションを得てください。

気候変動や森林破壊といった分野で、データ可視化を活用して関連する洞察を明らかにしたり強調したりする方法を考えてみてください。また、洞察を活用して、より持続可能な生活を促す行動変容を生み出す新しいユーザー体験を作り出す方法についても考えてみましょう。

## データサイエンス + 学生

私たちはこれまで、産業界や研究における実際の応用例について話し、デジタル人文学や持続可能性におけるデータサイエンスの応用例を探ってきました。それでは、データサイエンス初心者としてスキルを磨き、専門知識を共有するにはどうすればよいでしょうか？

以下は、学生向けのデータサイエンスプロジェクトの例です。ぜひ参考にしてください。

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects)では、以下のようなトピックを探求するGitHubの[プロジェクト](https://github.com/msr-ds3)があります：
    - [警察の武力行使における人種的偏見](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [ニューヨーク市地下鉄システムの信頼性](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [物質文化のデジタル化：Sirkapにおける社会経済的分布の探求](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom)氏とClaremontのチームによるプロジェクトで、[ArcGIS StoryMaps](https://storymaps.arcgis.com/)を使用しています。

## 🚀 チャレンジ

初心者向けのデータサイエンスプロジェクトを推奨する記事を探してみましょう。例えば、[これらの50のトピックエリア](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/)や[これらの21のプロジェクトアイデア](https://www.intellspot.com/data-science-project-ideas)、または[ソースコード付きの16のプロジェクト](https://data-flair.training/blogs/data-science-project-ideas/)などがあります。これらを分解して再構築してみてください。そして、学びの過程をブログに書き、洞察を私たちと共有するのを忘れないでください。

## 講義後のクイズ

[講義後のクイズ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/39)

## 復習と自己学習

さらにユースケースを探求したいですか？以下の関連する記事をご覧ください：
* [17のデータサイエンスの応用例](https://builtin.com/data-science/data-science-applications-examples) - 2021年7月
* [現実世界における11の驚くべきデータサイエンスの応用](https://myblindbird.com/data-science-applications-real-world/) - 2021年5月
* [現実世界のデータサイエンス](https://towardsdatascience.com/data-science-in-the-real-world/home) - 記事コレクション
* データサイエンスの応用： [教育](https://data-flair.training/blogs/data-science-in-education/)、[農業](https://data-flair.training/blogs/data-science-in-agriculture/)、[金融](https://data-flair.training/blogs/data-science-in-finance/)、[映画](https://data-flair.training/blogs/data-science-at-movies/)など。

## 課題

[Planetary Computerのデータセットを探索する](assignment.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。