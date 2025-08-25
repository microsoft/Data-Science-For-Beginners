<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bb17a440fdabf0823105136a5b81029",
  "translation_date": "2025-08-25T16:06:18+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者のためのデータサイエンス - カリキュラム

Azure Cloud Advocates at Microsoftは、データサイエンスに関する10週間、20レッスンのカリキュラムを提供します。各レッスンには、事前・事後のクイズ、レッスンを完了するための手順書、解答例、課題が含まれています。このプロジェクトベースの学習方法により、新しいスキルを実践的に学ぶことができます。

**著者の皆さんに感謝します:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 特別な感謝 🙏 を以下の[Microsoft Student Ambassador](https://studentambassadors.microsoft.com/)の著者、レビュアー、コンテンツ貢献者の皆さんに:** Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![ [(@sketchthedocs)](https://sketchthedocs.dev) によるスケッチノート](./sketchnotes/00-Title.png)|
|:---:|
| 初心者のためのデータサイエンス - _[@nitya](https://twitter.com/nitya) によるスケッチノート_ |

## お知らせ - 新しい生成AIカリキュラムがリリースされました！

生成AIに関する12レッスンのカリキュラムをリリースしました。以下の内容を学べます：

- プロンプトとプロンプトエンジニアリング
- テキストと画像アプリの生成
- 検索アプリ

いつものように、レッスン、課題、知識チェック、チャレンジが含まれています。

ぜひご覧ください：

> https://aka.ms/genai-beginners

# 学生の皆さんへ

以下のリソースから始めましょう：

- [Student Hubページ](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) このページでは、初心者向けリソース、学生向けパック、さらには無料の認定試験バウチャーを取得する方法が見つかります。このページをブックマークして、定期的にチェックしてください。コンテンツは少なくとも月に一度更新されます。
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) グローバルな学生アンバサダーコミュニティに参加しましょう。これがMicrosoftへの道になるかもしれません。

# 始めに

> **教師の皆さん**: このカリキュラムの使用方法について[いくつかの提案](for-teachers.md)を含めています。フィードバックは[ディスカッションフォーラム](https://github.com/microsoft/Data-Science-For-Beginners/discussions)でお待ちしています！

> **[学生の皆さん](https://aka.ms/student-page)**: このカリキュラムを自分で使用するには、リポジトリ全体をフォークし、事前クイズから始めて演習を完了してください。その後、レクチャーを読み、残りの活動を完了します。解答コードをコピーするのではなく、レッスンを理解しながらプロジェクトを作成することをお勧めします。ただし、解答コードは各プロジェクト指向のレッスンの/solutionsフォルダーにあります。また、友達と勉強グループを作り、一緒にコンテンツを進めるのも良いアイデアです。さらに学びたい場合は、[Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)をお勧めします。

## チーム紹介

[![プロモーションビデオ](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "プロモーションビデオ")

**Gif作成者** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 上の画像をクリックして、このプロジェクトと作成者についてのビデオをご覧ください！

## 教育方針

このカリキュラムを構築する際、プロジェクトベースであることと頻繁なクイズを含むことの2つの教育方針を採用しました。このシリーズの終わりまでに、学生はデータサイエンスの基本原則（倫理的概念、データ準備、データの操作方法、データ可視化、データ分析、データサイエンスの実際の使用例など）を学びます。

さらに、授業前の低リスクなクイズは、学生がトピックを学ぶ意図を設定し、授業後のクイズはさらなる記憶定着を確保します。このカリキュラムは柔軟で楽しいものとして設計されており、全体または一部を受講することができます。プロジェクトは小規模なものから始まり、10週間のサイクルの終わりには徐々に複雑になります。

> [行動規範](CODE_OF_CONDUCT.md)、[貢献ガイドライン](CONTRIBUTING.md)、[翻訳ガイドライン](TRANSLATIONS.md)をご覧ください。建設的なフィードバックをお待ちしています！

## 各レッスンには以下が含まれます：

- オプションのスケッチノート
- オプションの補足ビデオ
- レッスン前のウォームアップクイズ
- 書面によるレッスン
- プロジェクトベースのレッスンの場合、プロジェクトの構築方法に関するステップバイステップガイド
- 知識チェック
- チャレンジ
- 補足資料
- 課題
- レッスン後のクイズ

> **クイズについての注意**: すべてのクイズはQuiz-Appフォルダーに含まれており、合計40個の3問クイズがあります。レッスン内からリンクされていますが、クイズアプリはローカルで実行するか、Azureにデプロイすることができます。`quiz-app`フォルダーの指示に従ってください。クイズは徐々にローカライズされています。

## レッスン一覧

|![ [(@sketchthedocs)](https://sketchthedocs.dev) によるスケッチノート](./sketchnotes/00-Roadmap.png)|
|:---:|
| 初心者のためのデータサイエンス: ロードマップ - _[@nitya](https://twitter.com/nitya) によるスケッチノート_ |

| レッスン番号 | トピック | レッスングループ | 学習目標 | リンクされたレッスン | 著者 |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | データサイエンスの定義 | [イントロダクション](1-Introduction/README.md) | データサイエンスの基本概念と、それが人工知能、機械学習、大規模データとどのように関連しているかを学ぶ。 | [レッスン](1-Introduction/01-defining-data-science/README.md) [ビデオ](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | データサイエンスの倫理 | [イントロダクション](1-Introduction/README.md) | データ倫理の概念、課題、フレームワーク。 | [レッスン](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | データの定義 | [イントロダクション](1-Introduction/README.md) | データの分類方法とその一般的なソース。 | [レッスン](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | 統計と確率の入門 | [イントロダクション](1-Introduction/README.md) | データを理解するための確率と統計の数学的手法。 | [レッスン](1-Introduction/04-stats-and-probability/README.md) [ビデオ](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | リレーショナルデータの操作 | [データの操作](2-Working-With-Data/README.md) | リレーショナルデータの概要と、SQL（Structured Query Language）を使用したリレーショナルデータの探索と分析の基本。 | [レッスン](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) |
| 06 | NoSQLデータの操作 | [データの操作](2-Working-With-Data/README.md) | 非リレーショナルデータの概要、そのさまざまな種類、およびドキュメントデータベースの探索と分析の基本。 | [レッスン](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique) |
| 07 | Pythonの操作 | [データの操作](2-Working-With-Data/README.md) | Pandasなどのライブラリを使用したデータ探索のためのPythonの基本。Pythonプログラミングの基礎的な理解が推奨されます。 | [レッスン](2-Working-With-Data/07-python/README.md) [ビデオ](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | データ準備 | [データの取り扱い](2-Working-With-Data/README.md) | 欠損、不正確、不完全なデータの課題に対処するためのデータのクリーニングと変換技術に関するトピック。 | [レッスン](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | 数量の可視化 | [データ可視化](3-Data-Visualization/README.md) | Matplotlibを使用して鳥のデータを可視化する方法を学ぶ 🦆 | [レッスン](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | データ分布の可視化 | [データ可視化](3-Data-Visualization/README.md) | 区間内の観測値や傾向を可視化する。 | [レッスン](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | 比率の可視化 | [データ可視化](3-Data-Visualization/README.md) | 離散的およびグループ化された割合を可視化する。 | [レッスン](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | 関係性の可視化 | [データ可視化](3-Data-Visualization/README.md) | データセット間やその変数間の接続や相関を可視化する。 | [レッスン](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | 意味のある可視化 | [データ可視化](3-Data-Visualization/README.md) | 問題解決や洞察を効果的にするための価値ある可視化を作成する技術とガイド。 | [レッスン](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | データサイエンスライフサイクルの概要 | [ライフサイクル](4-Data-Science-Lifecycle/README.md) | データサイエンスライフサイクルとその最初のステップであるデータの取得と抽出の概要。 | [レッスン](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | 分析 | [ライフサイクル](4-Data-Science-Lifecycle/README.md) | データサイエンスライフサイクルのこのフェーズでは、データを分析する技術に焦点を当てる。 | [レッスン](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | コミュニケーション | [ライフサイクル](4-Data-Science-Lifecycle/README.md) | データサイエンスライフサイクルのこのフェーズでは、意思決定者が理解しやすい形でデータから得られた洞察を提示することに焦点を当てる。 | [レッスン](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | クラウドでのデータサイエンス | [クラウドデータ](5-Data-Science-In-Cloud/README.md) | クラウドでのデータサイエンスとその利点を紹介する一連のレッスン。 | [レッスン](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) と [Maud](https://twitter.com/maudstweets) |
| 18 | クラウドでのデータサイエンス | [クラウドデータ](5-Data-Science-In-Cloud/README.md) | ローコードツールを使用したモデルのトレーニング。 | [レッスン](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) と [Maud](https://twitter.com/maudstweets) |
| 19 | クラウドでのデータサイエンス | [クラウドデータ](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studioを使用したモデルのデプロイ。 | [レッスン](5-Data-Science-In-Cloud/19-Azure/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) と [Maud](https://twitter.com/maudstweets) |
| 20 | 実世界でのデータサイエンス | [実世界](6-Data-Science-In-Wild/README.md) | 実世界でのデータサイエンス主導のプロジェクト。 | [レッスン](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

このサンプルをCodespaceで開く手順は以下の通りです：
1. Codeドロップダウンメニューをクリックし、Open with Codespacesオプションを選択します。
2. ペインの下部にある+ New codespaceを選択します。
詳細については、[GitHubのドキュメント](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)をご覧ください。

## VSCode Remote - Containers
VSCodeのRemote - Containers拡張機能を使用して、ローカルマシンでこのリポジトリをコンテナ内で開く手順は以下の通りです：

1. 開発コンテナを初めて使用する場合は、[開始ガイド](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)で必要条件（例：Dockerのインストール）を確認してください。

このリポジトリを使用するには、以下のいずれかの方法を選択できます：

**注意**: 内部的には、Remote-Containers: **Clone Repository in Container Volume...** コマンドを使用して、ソースコードをローカルファイルシステムではなくDockerボリュームにクローンします。[ボリューム](https://docs.docker.com/storage/volumes/)はコンテナデータを永続化するための推奨メカニズムです。

または、ローカルにクローンまたはダウンロードしたリポジトリを開く：

- このリポジトリをローカルファイルシステムにクローンします。
- F1キーを押して、**Remote-Containers: Open Folder in Container...** コマンドを選択します。
- クローンしたフォルダを選択し、コンテナが起動するのを待って試してみてください。

## オフラインアクセス

[Docsify](https://docsify.js.org/#/)を使用して、このドキュメントをオフラインで実行できます。このリポジトリをフォークし、[Docsifyをインストール](https://docsify.js.org/#/quickstart)してから、このリポジトリのルートフォルダで`docsify serve`と入力してください。ウェブサイトはローカルホストのポート3000で提供されます：`localhost:3000`。

> 注意：Docsifyではノートブックはレンダリングされません。そのため、ノートブックを実行する必要がある場合は、Pythonカーネルを使用してVS Codeで別途実行してください。

## ヘルプ募集中！

カリキュラムの全部または一部を翻訳したい場合は、[翻訳ガイド](TRANSLATIONS.md)をご覧ください。

## その他のカリキュラム

私たちのチームは他にもカリキュラムを制作しています！以下をご覧ください：

- [Generative AI for Beginners](https://aka.ms/genai-beginners)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI with JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative AI with Java](https://aka.ms/genaijava)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101) 
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners)
- [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。