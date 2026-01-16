<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:35:59+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# 初心者向けデータサイエンスへの貢献

初心者向けデータサイエンスカリキュラムへの貢献に興味を持っていただきありがとうございます！コミュニティからの貢献を歓迎します。

## 目次

- [行動規範](../..)
- [どのように貢献できますか？](../..)
- [始め方](../..)
- [貢献ガイドライン](../..)
- [プルリクエストのプロセス](../..)
- [スタイルガイドライン](../..)
- [貢献者ライセンス契約](../..)

## 行動規範

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)を採用しています。
詳細については、[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)をご覧いただくか、追加の質問やコメントがある場合は[opencode@microsoft.com](mailto:opencode@microsoft.com)までお問い合わせください。

## どのように貢献できますか？

### バグの報告

バグ報告を作成する前に、既存の問題を確認して重複を避けてください。バグ報告を作成する際は、できるだけ詳細を含めてください：

- **明確でわかりやすいタイトルを使用**
- **問題を再現するための正確な手順を記述**
- **具体的な例を提供**（コードスニペット、スクリーンショットなど）
- **観察した動作と期待した動作を記述**
- **環境の詳細を含める**（OS、Pythonのバージョン、ブラウザなど）

### 改善提案

改善提案を歓迎します！改善提案を行う際は：

- **明確でわかりやすいタイトルを使用**
- **提案する改善の詳細な説明を提供**
- **この改善が有用である理由を説明**
- **他のプロジェクトでの類似機能があればリストアップ**

### ドキュメントへの貢献

ドキュメントの改善は常に歓迎されます：

- **誤字や文法の修正**
- **説明の明確化**
- **不足しているドキュメントの追加**
- **古い情報の更新**
- **例やユースケースの追加**

### コードへの貢献

以下のコード貢献を歓迎します：

- **新しいレッスンや演習**
- **バグ修正**
- **既存のノートブックの改善**
- **新しいデータセットや例**
- **クイズアプリケーションの改善**

## 始め方

### 必要条件

貢献する前に以下を確認してください：

1. GitHubアカウント
2. システムにGitがインストールされていること
3. Python 3.7以上とJupyterがインストールされていること
4. Node.jsとnpm（クイズアプリへの貢献の場合）
5. カリキュラム構造への理解

詳細なセットアップ手順については[INSTALLATION.md](INSTALLATION.md)をご覧ください。

### フォークとクローン

1. **GitHubでリポジトリをフォーク**
2. **フォークをローカルにクローン**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **アップストリームリモートを追加**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### ブランチを作成

作業用の新しいブランチを作成します：

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

ブランチ命名規則：
- `feature/` - 新しい機能やレッスン
- `fix/` - バグ修正
- `docs/` - ドキュメントの変更
- `refactor/` - コードのリファクタリング

## 貢献ガイドライン

### レッスン内容について

レッスンを貢献する場合や既存のレッスンを変更する場合：

1. **既存の構造に従う**：
   - レッスン内容を含むREADME.md
   - 演習を含むJupyterノートブック
   - 課題（該当する場合）
   - 事前および事後クイズへのリンク

2. **以下の要素を含める**：
   - 明確な学習目標
   - ステップバイステップの説明
   - コメント付きのコード例
   - 練習用の演習
   - 追加のリソースへのリンク

3. **アクセシビリティを確保**：
   - 明確で簡潔な言葉を使用
   - 画像に代替テキストを提供
   - コードコメントを含める
   - 異なる学習スタイルを考慮

### Jupyterノートブックについて

1. **コミット前にすべての出力をクリア**:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **説明付きのMarkdownセルを含める**

3. **一貫したフォーマットを使用**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **ノートブックを完全にテスト**してから提出

### Pythonコードについて

[PEP 8](https://www.python.org/dev/peps/pep-0008/)スタイルガイドに従ってください：

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```

### クイズアプリへの貢献について

クイズアプリケーションを変更する場合：

1. **ローカルでテスト**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **リンターを実行**:
   ```bash
   npm run lint
   ```

3. **正常にビルド**:
   ```bash
   npm run build
   ```

4. **Vue.jsスタイルガイド**と既存のパターンに従う

### 翻訳について

翻訳を追加または更新する場合：

1. `translations/`フォルダー内の構造に従う
2. フォルダー名として言語コードを使用（例：フランス語の場合は`fr`）
3. 英語版と同じファイル構造を維持
4. クイズリンクに言語パラメータを追加：`?loc=fr`
5. すべてのリンクとフォーマットをテスト

## プルリクエストのプロセス

### 提出前

1. **最新の変更でブランチを更新**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **変更をテスト**：
   - 変更したノートブックをすべて実行
   - クイズアプリをテスト（変更した場合）
   - すべてのリンクが機能することを確認
   - スペルと文法のエラーをチェック

3. **変更をコミット**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   明確なコミットメッセージを書く：
   - 現在形を使用（例："Add feature"、"Added feature"ではない）
   - 命令形を使用（例："Move cursor to..."、"Moves cursor to..."ではない）
   - 最初の行を72文字以内に制限
   - 関連する問題やプルリクエストを参照

4. **フォークにプッシュ**:
   ```bash
   git push origin feature/your-feature-name
   ```

### プルリクエストの作成

1. [リポジトリ](https://github.com/microsoft/Data-Science-For-Beginners)に移動
2. 「Pull requests」→「New pull request」をクリック
3. 「compare across forks」をクリック
4. 自分のフォークとブランチを選択
5. 「Create pull request」をクリック

### PRタイトルのフォーマット

以下のフォーマットに従った明確で説明的なタイトルを使用：

```
[Component] Brief description
```

例：
- `[Lesson 7] Fix Python notebook import error`
- `[Quiz App] Add German translation`
- `[Docs] Update README with new prerequisites`
- `[Fix] Correct data path in visualization lesson`

### PR説明

PR説明には以下を含めてください：

- **何を**：どのような変更を行ったか
- **なぜ**：これらの変更が必要な理由
- **どのように**：変更をどのように実装したか
- **テスト**：変更をどのようにテストしたか
- **スクリーンショット**：視覚的な変更がある場合はスクリーンショットを含める
- **関連する問題**：関連する問題へのリンク（例："Fixes #123"）

### レビューのプロセス

1. **自動チェック**がPRで実行されます
2. **メンテナーが貢献をレビュー**します
3. **フィードバックに対応**して追加のコミットを行います
4. 承認されると、**メンテナーがPRをマージ**します

### PRがマージされた後

1. ブランチを削除：
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. フォークを更新：
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## スタイルガイドライン

### Markdown

- 一貫した見出しレベルを使用
- セクション間に空行を含める
- 言語指定付きのコードブロックを使用：
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- 画像に代替テキストを追加：`![Alt text](../../translated_images/ja/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- 行の長さを適度に保つ（約80〜100文字）

### Python

- PEP 8スタイルガイドに従う
- 意味のある変数名を使用
- 関数にドックストリングを追加
- 適切な場所に型ヒントを含める：
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Vue.js 2スタイルガイドに従う
- 提供されたESLint構成を使用
- モジュール化された再利用可能なコンポーネントを書く
- 複雑なロジックにはコメントを追加

### ファイルの整理

- 関連するファイルをまとめる
- 説明的なファイル名を使用
- 既存のディレクトリ構造に従う
- 不要なファイルをコミットしない（.DS_Store、.pyc、node_modulesなど）

## 貢献者ライセンス契約

このプロジェクトは貢献と提案を歓迎します。ほとんどの貢献には、貢献者ライセンス契約（CLA）に同意する必要があります。これにより、貢献を使用する権利を私たちに与えることができます。詳細については、https://cla.microsoft.com をご覧ください。

プルリクエストを送信すると、CLAボットが自動的にCLAが必要かどうかを判断し、適切にPRを装飾します（例：ラベル、コメント）。ボットの指示に従うだけで、すべてのリポジトリでこれを一度だけ行えば済みます。

## 質問がありますか？

- [Discord Channel #data-science-for-beginners](https://aka.ms/ds4beginners/discord)をご確認ください
- [Discordコミュニティ](https://aka.ms/ds4beginners/discord)に参加してください
- 既存の[問題](https://github.com/microsoft/Data-Science-For-Beginners/issues)や[プルリクエスト](https://github.com/microsoft/Data-Science-For-Beginners/pulls)を確認してください

## ありがとうございます！

あなたの貢献がこのカリキュラムをより良いものにします。貢献していただきありがとうございます！

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。原文書の母国語版を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当方は責任を負いません。