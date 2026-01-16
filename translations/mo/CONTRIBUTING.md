<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:31:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "mo"
}
-->
# 貢獻《初學者的數據科學》

感謝您對《初學者的數據科學》課程的貢獻感興趣！我們歡迎社群的貢獻。

## 目錄

- [行為準則](../..)
- [我可以如何貢獻？](../..)
- [開始使用](../..)
- [貢獻指南](../..)
- [拉取請求流程](../..)
- [風格指南](../..)
- [貢獻者許可協議](../..)

## 行為準則

本專案採用了 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱 [行為準則 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或聯繫 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出其他問題或意見。

## 我可以如何貢獻？

### 回報錯誤

在建立錯誤報告之前，請檢查現有的問題以避免重複。當您建立錯誤報告時，請提供盡可能多的細節：

- **使用清晰且描述性的標題**
- **描述重現問題的具體步驟**
- **提供具體範例**（程式碼片段、截圖）
- **描述您觀察到的行為以及您預期的行為**
- **包含您的環境細節**（作業系統、Python版本、瀏覽器）

### 建議改進

我們歡迎改進建議！提出改進建議時：

- **使用清晰且描述性的標題**
- **提供詳細的建議改進描述**
- **解釋為什麼這項改進會有用**
- **列出其他專案中類似的功能（如果適用）**

### 貢獻文件

我們非常感謝文件的改進：

- **修正拼寫和語法錯誤**
- **提高解釋的清晰度**
- **補充缺失的文件**
- **更新過時的資訊**
- **添加範例或使用案例**

### 貢獻程式碼

我們歡迎程式碼貢獻，包括：

- **新的課程或練習**
- **錯誤修正**
- **改進現有的筆記本**
- **新增數據集或範例**
- **測驗應用程式的改進**

## 開始使用

### 先決條件

在貢獻之前，請確保您已具備以下條件：

1. 一個 GitHub 帳號
2. 您的系統已安裝 Git
3. 安裝了 Python 3.7+ 和 Jupyter
4. 安裝了 Node.js 和 npm（用於測驗應用程式的貢獻）
5. 熟悉課程結構

請參閱 [INSTALLATION.md](INSTALLATION.md) 以獲取詳細的設置說明。

### Fork 和 Clone

1. **在 GitHub 上 Fork 此倉庫**
2. **在本地 Clone 您的 Fork**：
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **添加上游遠端**：
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### 建立分支

為您的工作建立一個新分支：

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

分支命名規範：
- `feature/` - 新功能或課程
- `fix/` - 錯誤修正
- `docs/` - 文件更改
- `refactor/` - 程式碼重構

## 貢獻指南

### 關於課程內容

當貢獻課程或修改現有課程時：

1. **遵循現有結構**：
   - README.md 包含課程內容
   - Jupyter 筆記本包含練習
   - 作業（如果適用）
   - 連結到前測和後測

2. **包含以下元素**：
   - 清晰的學習目標
   - 步驟式的解釋
   - 帶有註解的程式碼範例
   - 練習題以供練習
   - 額外資源的連結

3. **確保可訪問性**：
   - 使用清晰、簡單的語言
   - 為圖片提供替代文字
   - 包含程式碼註解
   - 考慮不同的學習風格

### 關於 Jupyter 筆記本

1. **在提交之前清除所有輸出**：
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **包含帶有解釋的 Markdown 單元格**

3. **使用一致的格式**：
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **在提交之前完整測試您的筆記本**

### 關於 Python 程式碼

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 風格指南：

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

### 關於測驗應用程式的貢獻

修改測驗應用程式時：

1. **在本地測試**：
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **運行 linter**：
   ```bash
   npm run lint
   ```

3. **成功構建**：
   ```bash
   npm run build
   ```

4. **遵循 Vue.js 風格指南** 和現有模式

### 關於翻譯

新增或更新翻譯時：

1. 遵循 `translations/` 資料夾中的結構
2. 使用語言代碼作為資料夾名稱（例如，法語使用 `fr`）
3. 維持與英文版本相同的檔案結構
4. 更新測驗連結以包含語言參數：`?loc=fr`
5. 測試所有連結和格式

## 拉取請求流程

### 提交之前

1. **使用最新更改更新您的分支**：
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **測試您的更改**：
   - 運行所有修改過的筆記本
   - 測試測驗應用程式（如果有修改）
   - 確保所有連結正常工作
   - 檢查拼寫和語法錯誤

3. **提交您的更改**：
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   撰寫清晰的提交訊息：
   - 使用現在式（例如 "Add feature" 而非 "Added feature"）
   - 使用命令式語氣（例如 "Move cursor to..." 而非 "Moves cursor to..."）
   - 第一行限制在 72 個字元內
   - 參考相關問題和拉取請求（如果適用）

4. **推送到您的 Fork**：
   ```bash
   git push origin feature/your-feature-name
   ```

### 建立拉取請求

1. 前往 [倉庫](https://github.com/microsoft/Data-Science-For-Beginners)
2. 點擊 "Pull requests" → "New pull request"
3. 點擊 "compare across forks"
4. 選擇您的 Fork 和分支
5. 點擊 "Create pull request"

### PR 標題格式

使用清晰、描述性的標題，遵循以下格式：

```
[Component] Brief description
```

範例：
- `[Lesson 7] Fix Python notebook import error`
- `[Quiz App] Add German translation`
- `[Docs] Update README with new prerequisites`
- `[Fix] Correct data path in visualization lesson`

### PR 描述

在您的 PR 描述中包含：

- **What**：您做了哪些更改？
- **Why**：為什麼需要這些更改？
- **How**：您如何實現這些更改？
- **Testing**：您如何測試這些更改？
- **Screenshots**：對於視覺更改，請包含截圖
- **Related Issues**：連結相關問題（例如 "Fixes #123"）

### 審核流程

1. **自動檢查** 將在您的 PR 上運行
2. **維護者將審核** 您的貢獻
3. **根據反饋進行修改**，提交額外的更改
4. 一旦獲得批准，**維護者將合併** 您的 PR

### PR 合併後

1. 刪除您的分支：
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. 更新您的 Fork：
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## 風格指南

### Markdown

- 使用一致的標題層級
- 在各部分之間添加空行
- 使用帶有語言指定的程式碼塊：
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- 為圖片添加替代文字：`![Alt text](../../translated_images/mo/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- 保持合理的行長度（約 80-100 字元）

### Python

- 遵循 PEP 8 風格指南
- 使用有意義的變數名稱
- 為函數添加文檔字符串
- 在適當的地方包含類型提示：
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- 遵循 Vue.js 2 風格指南
- 使用提供的 ESLint 配置
- 撰寫模組化、可重用的元件
- 為複雜邏輯添加註解

### 檔案組織

- 將相關檔案放在一起
- 使用描述性的檔案名稱
- 遵循現有的目錄結構
- 不要提交不必要的檔案（例如 .DS_Store、.pyc、node_modules 等）

## 貢獻者許可協議

本專案歡迎貢獻和建議。大多數貢獻需要您同意貢獻者許可協議 (CLA)，聲明您有權並實際授予我們使用您的貢獻的權利。詳情請訪問 https://cla.microsoft.com。

當您提交拉取請求時，CLA 機器人將自動判斷您是否需要提供 CLA，並適當地標記 PR（例如，標籤、評論）。只需按照機器人提供的指示操作即可。您只需在使用我們的 CLA 的所有倉庫中執行一次此操作。

## 有問題嗎？

- 查看我們的 [Discord 頻道 #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- 加入我們的 [Discord 社群](https://aka.ms/ds4beginners/discord)
- 查看現有的 [問題](https://github.com/microsoft/Data-Science-For-Beginners/issues) 和 [拉取請求](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## 感謝！

您的貢獻讓這個課程對每個人都更有幫助。感謝您花時間貢獻！

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。