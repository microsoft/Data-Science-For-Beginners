<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-25T17:40:08+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "ja"
}
-->
# クイズ

これらのクイズは、データサイエンスカリキュラム（https://aka.ms/datascience-beginners）の講義前後に行うクイズです。

## 翻訳されたクイズセットを追加する

翻訳されたクイズを追加するには、`assets/translations`フォルダ内に対応するクイズ構造を作成してください。オリジナルのクイズは`assets/translations/en`にあります。クイズは複数のグループに分かれています。適切なクイズセクションに番号を合わせるようにしてください。このカリキュラムには合計40個のクイズがあり、番号は0から始まります。

翻訳を編集した後、翻訳フォルダ内の`index.js`ファイルを編集し、`en`の規則に従ってすべてのファイルをインポートしてください。

次に、`assets/translations`内の`index.js`ファイルを編集して、新しい翻訳ファイルをインポートします。

その後、このアプリ内の`App.vue`のドロップダウンを編集し、言語を追加します。ローカライズされた略語を言語フォルダ名と一致させてください。

最後に、翻訳されたレッスン内のすべてのクイズリンクを編集し、ローカライズをクエリパラメータとして含めるようにします。例: `?loc=fr`。

## プロジェクトセットアップ

```
npm install
```

### 開発用のコンパイルとホットリロード

```
npm run serve
```

### 本番用のコンパイルと最小化

```
npm run build
```

### ファイルのリントと修正

```
npm run lint
```

### 設定のカスタマイズ

[Configuration Reference](https://cli.vuejs.org/config/)を参照してください。

クレジット: このクイズアプリのオリジナルバージョンに感謝します: https://github.com/arpan45/simple-quiz-vue

## Azureへのデプロイ

以下は、始めるためのステップバイステップガイドです：

1. GitHubリポジトリをフォークする  
静的ウェブアプリのコードをGitHubリポジトリに保存してください。このリポジトリをフォークします。

2. Azure Static Web Appを作成する  
- [Azureアカウント](http://azure.microsoft.com)を作成します。  
- [Azureポータル](https://portal.azure.com)にアクセスします。  
- 「リソースの作成」をクリックし、「Static Web App」を検索します。  
- 「作成」をクリックします。

3. Static Web Appを構成する  
- 基本設定:  
  - サブスクリプション: Azureサブスクリプションを選択します。  
  - リソースグループ: 新しいリソースグループを作成するか、既存のものを使用します。  
  - 名前: 静的ウェブアプリの名前を入力します。  
  - リージョン: ユーザーに最も近いリージョンを選択します。

- #### デプロイメントの詳細:  
  - ソース: 「GitHub」を選択します。  
  - GitHubアカウント: AzureにGitHubアカウントへのアクセスを許可します。  
  - 組織: GitHubの組織を選択します。  
  - リポジトリ: 静的ウェブアプリを含むリポジトリを選択します。  
  - ブランチ: デプロイするブランチを選択します。

- #### ビルドの詳細:  
  - ビルドプリセット: アプリが構築されているフレームワークを選択します（例: React, Angular, Vueなど）。  
  - アプリの場所: アプリコードが含まれるフォルダを指定します（例: ルートの場合は/）。  
  - APIの場所: APIがある場合、その場所を指定します（オプション）。  
  - 出力の場所: ビルド出力が生成されるフォルダを指定します（例: buildまたはdist）。

4. レビューと作成  
設定を確認し、「作成」をクリックします。Azureが必要なリソースを設定し、リポジトリにGitHub Actionsワークフローを作成します。

5. GitHub Actionsワークフロー  
Azureはリポジトリ内に自動的にGitHub Actionsワークフロー（.github/workflows/azure-static-web-apps-<name>.yml）を作成します。このワークフローがビルドとデプロイプロセスを処理します。

6. デプロイの監視  
GitHubリポジトリの「Actions」タブに移動します。  
ワークフローが実行中であることが確認できます。このワークフローは静的ウェブアプリをAzureにビルドおよびデプロイします。  
ワークフローが完了すると、提供されたAzure URLでアプリが公開されます。

### ワークフローファイルの例

以下は、GitHub Actionsワークフローファイルの例です：  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "quiz-app" # App source code path
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### 追加リソース  
- [Azure Static Web Apps ドキュメント](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions ドキュメント](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。