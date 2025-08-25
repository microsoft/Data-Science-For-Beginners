<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-25T17:39:35+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "hk"
}
-->
# 測驗

這些測驗是數據科學課程的課前和課後測驗，課程網址：https://aka.ms/datascience-beginners

## 添加翻譯的測驗集

要添加測驗翻譯，請在 `assets/translations` 文件夾中創建相應的測驗結構。原始測驗位於 `assets/translations/en`。測驗分為幾個組別。請確保編號與正確的測驗部分對齊。整個課程共有 40 個測驗，編號從 0 開始。

編輯翻譯後，請編輯翻譯文件夾中的 index.js 文件，按照 `en` 中的約定導入所有文件。

接著，編輯 `assets/translations` 中的 `index.js` 文件以導入新的翻譯文件。

然後，編輯此應用中的 `App.vue` 文件中的下拉選單，添加您的語言。將本地化縮寫與您的語言文件夾名稱匹配。

最後，編輯翻譯課程中的所有測驗鏈接（如果存在），以包含本地化查詢參數，例如：`?loc=fr`。

## 項目設置

```
npm install
```

### 編譯並熱重載以進行開發

```
npm run serve
```

### 編譯並壓縮以進行生產環境

```
npm run build
```

### 檢查並修復文件

```
npm run lint
```

### 自定義配置

請參閱 [配置參考](https://cli.vuejs.org/config/)。

致謝：感謝此測驗應用的原始版本：https://github.com/arpan45/simple-quiz-vue

## 部署到 Azure

以下是幫助您開始的逐步指南：

1. Fork GitHub 儲存庫  
確保您的靜態網頁應用程式代碼在您的 GitHub 儲存庫中。Fork 此儲存庫。

2. 創建 Azure 靜態網頁應用  
- 創建 [Azure 帳戶](http://azure.microsoft.com)  
- 前往 [Azure 入口網站](https://portal.azure.com)  
- 點擊“創建資源”，然後搜索“靜態網頁應用”。  
- 點擊“創建”。

3. 配置靜態網頁應用  
- 基本信息：  
  - 訂閱：選擇您的 Azure 訂閱。  
  - 資源組：創建新的資源組或使用現有的資源組。  
  - 名稱：為您的靜態網頁應用提供一個名稱。  
  - 地區：選擇最接近您的用戶的地區。

- #### 部署詳情：  
  - 資源：選擇“GitHub”。  
  - GitHub 帳戶：授權 Azure 訪問您的 GitHub 帳戶。  
  - 組織：選擇您的 GitHub 組織。  
  - 儲存庫：選擇包含靜態網頁應用的儲存庫。  
  - 分支：選擇您要部署的分支。

- #### 構建詳情：  
  - 構建預設：選擇您的應用所使用的框架（例如 React、Angular、Vue 等）。  
  - 應用位置：指定包含應用代碼的文件夾（例如，如果在根目錄，則為 /）。  
  - API 位置：如果有 API，請指定其位置（可選）。  
  - 輸出位置：指定生成構建輸出的文件夾（例如 build 或 dist）。

4. 審核並創建  
審核您的設置並點擊“創建”。Azure 會設置必要的資源並在您的儲存庫中創建 GitHub Actions 工作流程。

5. GitHub Actions 工作流程  
Azure 會自動在您的儲存庫中創建 GitHub Actions 工作流程文件（.github/workflows/azure-static-web-apps-<name>.yml）。此工作流程將處理構建和部署過程。

6. 監控部署  
前往 GitHub 儲存庫中的“Actions”標籤。  
您應該看到一個工作流程正在運行。此工作流程將構建並部署您的靜態網頁應用到 Azure。  
工作流程完成後，您的應用將在提供的 Azure URL 上線。

### 示例工作流程文件

以下是 GitHub Actions 工作流程文件的示例：  
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

### 其他資源  
- [Azure 靜態網頁應用文檔](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions 文檔](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。