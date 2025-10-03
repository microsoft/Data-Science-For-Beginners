<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:07:53+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tw"
}
-->
# AGENTS.md

## 專案概述

《初學者的數據科學》是一個由 Microsoft Azure Cloud Advocates 創建的全面性 10 週、20 課課程。此存儲庫是一個學習資源，通過基於項目的課程教授基礎數據科學概念，包括 Jupyter 筆記本、互動測驗和實作練習。

**主要技術：**
- **Jupyter 筆記本**：使用 Python 3 作為主要學習媒介
- **Python 庫**：pandas、numpy、matplotlib 用於數據分析和可視化
- **Vue.js 2**：測驗應用程式（quiz-app 資料夾）
- **Docsify**：離線存取的文件站點生成器
- **Node.js/npm**：JavaScript 元件的套件管理
- **Markdown**：所有課程內容和文件

**架構：**
- 多語言教育存儲庫，提供廣泛的翻譯
- 結構化為課程模組（1-Introduction 至 6-Data-Science-In-Wild）
- 每課包含 README、筆記本、作業和測驗
- 獨立的 Vue.js 測驗應用程式，用於課前/課後評估
- 支援 GitHub Codespaces 和 VS Code 開發容器

## 設置指令

### 存儲庫設置
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python 環境設置
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 測驗應用程式設置
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify 文件伺服器
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### 可視化項目設置
針對像 meaningful-visualizations（第 13 課）這樣的可視化項目：
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## 開發工作流程

### 使用 Jupyter 筆記本
1. 在存儲庫根目錄啟動 Jupyter：`jupyter notebook`
2. 導航到所需的課程資料夾
3. 打開 `.ipynb` 文件進行練習
4. 筆記本是自包含的，包含解釋和代碼單元
5. 大多數筆記本使用 pandas、numpy 和 matplotlib，請確保已安裝這些庫

### 課程結構
每課通常包含：
- `README.md` - 主要課程內容，包含理論和範例
- `notebook.ipynb` - 實作 Jupyter 筆記本練習
- `assignment.ipynb` 或 `assignment.md` - 練習作業
- `solution/` 資料夾 - 解答筆記本和代碼
- `images/` 資料夾 - 支援的視覺材料

### 測驗應用程式開發
- Vue.js 2 應用程式，開發期間支援熱重載
- 測驗存儲於 `quiz-app/src/assets/translations/`
- 每種語言有自己的翻譯資料夾（en、fr、es 等）
- 測驗編號從 0 開始，最多到 39（共 40 個測驗）

### 添加翻譯
- 翻譯存放於存儲庫根目錄的 `translations/` 資料夾
- 每種語言的課程結構與英文完全鏡像
- 通過 GitHub Actions 自動翻譯（co-op-translator.yml）

## 測試指導

### 測驗應用程式測試
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### 筆記本測試
- 筆記本沒有自動化測試框架
- 手動驗證：按順序運行所有單元以確保無錯誤
- 確認數據文件可訪問且輸出正確生成
- 檢查可視化是否正確渲染

### 文件測試
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### 代碼質量檢查
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## 代碼風格指南

### Python（Jupyter 筆記本）
- 遵循 PEP 8 代碼風格指南
- 使用清晰的變數名稱，說明正在分析的數據
- 在代碼單元之前包含解釋的 Markdown 單元
- 代碼單元應專注於單一概念或操作
- 使用 pandas 進行數據操作，matplotlib 進行可視化
- 常見的導入模式：
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- 遵循 Vue.js 2 風格指南和最佳實踐
- ESLint 配置於 `quiz-app/package.json`
- 使用 Vue 單文件元件（.vue 文件）
- 維持基於元件的架構
- 提交更改前運行 `npm run lint`

### Markdown 文件
- 使用清晰的標題層次結構（# ## ### 等）
- 包含帶語言指定的代碼塊
- 為圖片添加替代文字
- 鏈接相關課程和資源
- 保持合理的行長以提高可讀性

### 文件組織
- 課程內容存放於編號資料夾（01-defining-data-science 等）
- 解答存放於專用的 `solution/` 子資料夾
- 翻譯在 `translations/` 資料夾中鏡像英文結構
- 數據文件存放於 `data/` 或課程專用資料夾

## 構建和部署

### 測驗應用程式部署
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure 靜態 Web 應用部署
測驗應用程式可部署到 Azure 靜態 Web 應用：
1. 創建 Azure 靜態 Web 應用資源
2. 連接到 GitHub 存儲庫
3. 配置構建設置：
   - 應用位置：`quiz-app`
   - 輸出位置：`dist`
4. GitHub Actions 工作流程會在推送時自動部署

### 文件站點
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- 存儲庫包含開發容器配置
- Codespaces 自動設置 Python 和 Node.js 環境
- 通過 GitHub UI 打開存儲庫中的 Codespace
- 所有依賴項自動安裝

## 拉取請求指南

### 提交前
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR 標題格式
- 使用清晰、描述性的標題
- 格式：`[元件] 簡短描述`
- 範例：
  - `[Lesson 7] 修復 Python 筆記本導入錯誤`
  - `[Quiz App] 添加德語翻譯`
  - `[Docs] 更新 README，新增前置條件`

### 必要檢查
- 確保所有代碼無錯誤運行
- 驗證筆記本完整執行
- 確認 Vue.js 應用程式成功構建
- 檢查文件鏈接是否正常
- 測試修改的測驗應用程式
- 確認翻譯保持一致結構

### 貢獻指南
- 遵循現有代碼風格和模式
- 為複雜邏輯添加解釋性註解
- 更新相關文件
- 在不同課程模組中測試更改（如適用）
- 查看 CONTRIBUTING.md 文件

## 附加說明

### 常用庫
- **pandas**：數據操作和分析
- **numpy**：數值計算
- **matplotlib**：數據可視化和繪圖
- **seaborn**：統計數據可視化（部分課程）
- **scikit-learn**：機器學習（進階課程）

### 使用數據文件
- 數據文件存放於 `data/` 資料夾或課程專用目錄
- 大多數筆記本期望數據文件位於相對路徑
- CSV 文件是主要數據格式
- 部分課程使用 JSON 作為非關聯數據範例

### 多語言支援
- 通過 GitHub Actions 提供 40+ 語言翻譯
- 翻譯工作流程位於 `.github/workflows/co-op-translator.yml`
- 翻譯存放於 `translations/` 資料夾，使用語言代碼命名
- 測驗翻譯存放於 `quiz-app/src/assets/translations/`

### 開發環境選項
1. **本地開發**：本地安裝 Python、Jupyter、Node.js
2. **GitHub Codespaces**：基於雲端的即時開發環境
3. **VS Code 開發容器**：基於容器的本地開發
4. **Binder**：在雲端啟動筆記本（如已配置）

### 課程內容指南
- 每課是獨立的，但建立在之前概念之上
- 課前測驗測試先前知識
- 課後測驗加強學習
- 作業提供實作練習
- Sketchnotes 提供視覺摘要

### 常見問題排查

**Jupyter 核心問題：**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm 安裝失敗：**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**筆記本導入錯誤：**
- 確認已安裝所有必要庫
- 檢查 Python 版本兼容性（建議使用 Python 3.7+）
- 確保虛擬環境已啟動

**Docsify 無法加載：**
- 確認您從存儲庫根目錄提供服務
- 檢查 `index.html` 是否存在
- 確保網絡訪問正常（端口 3000）

### 性能考量
- 大型數據集可能需要較長時間加載到筆記本中
- 複雜圖表的可視化渲染可能較慢
- Vue.js 開發伺服器啟用熱重載以快速迭代
- 生產構建已優化並縮小

### 安全注意事項
- 不應提交敏感數據或憑證
- 在雲端課程中使用環境變數存儲 API 密鑰
- 與 Azure 相關的課程可能需要 Azure 帳戶憑證
- 保持依賴項更新以獲得安全修補

## 翻譯貢獻
- 通過 GitHub Actions 管理自動翻譯
- 歡迎手動修正以提高翻譯準確性
- 遵循現有翻譯資料夾結構
- 更新測驗鏈接以包含語言參數：`?loc=fr`
- 測試翻譯課程以確保正確渲染

## 相關資源
- 主課程：https://aka.ms/datascience-beginners
- Microsoft Learn：https://docs.microsoft.com/learn/
- 學生中心：https://docs.microsoft.com/learn/student-hub
- 討論論壇：https://github.com/microsoft/Data-Science-For-Beginners/discussions
- 其他 Microsoft 課程：ML for Beginners、AI for Beginners、Web Dev for Beginners

## 專案維護
- 定期更新以保持內容最新
- 歡迎社群貢獻
- 問題在 GitHub 上追蹤
- PR 由課程維護者審核
- 每月進行內容審查和更新

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。