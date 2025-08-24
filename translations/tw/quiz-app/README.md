<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-24T13:14:42+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "tw"
}
-->
# 測驗

這些測驗是數據科學課程的課前和課後測驗，課程網址為：https://aka.ms/datascience-beginners

## 新增翻譯測驗集

要新增測驗翻譯，請在 `assets/translations` 資料夾中建立相應的測驗結構。原始測驗位於 `assets/translations/en`。測驗分為多個組別。請確保編號與正確的測驗部分對齊。整個課程共有 40 個測驗，編號從 0 開始。

完成翻譯後，編輯翻譯資料夾中的 `index.js` 文件，按照 `en` 中的慣例導入所有文件。

接著，編輯 `assets/translations` 中的 `index.js` 文件以導入新的翻譯文件。

然後，編輯此應用中的 `App.vue` 文件中的下拉選單，新增您的語言。將本地化縮寫與您的語言資料夾名稱匹配。

最後，編輯翻譯課程中的所有測驗連結（如果存在），以包含本地化查詢參數，例如：`?loc=fr`。

## 專案設置

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

### 自訂配置

請參閱 [配置參考](https://cli.vuejs.org/config/)。

致謝：感謝此測驗應用的原始版本：https://github.com/arpan45/simple-quiz-vue

## 部署到 Azure

以下是幫助您開始的逐步指南：

1. Fork GitHub 儲存庫  
確保您的靜態網頁應用程式代碼位於您的 GitHub 儲存庫中。Fork 此儲存庫。

2. 建立 Azure 靜態網頁應用程式  
- 建立 [Azure 帳戶](http://azure.microsoft.com)  
- 前往 [Azure 入口網站](https://portal.azure.com)  
- 點擊「建立資源」，搜尋「靜態網頁應用程式」。  
- 點擊「建立」。  

3. 配置靜態網頁應用程式  
- 基本設定：  
  - 訂閱：選擇您的 Azure 訂閱。  
  - 資源群組：建立新的資源群組或使用現有的資源群組。  
  - 名稱：為您的靜態網頁應用程式提供一個名稱。  
  - 地區：選擇最接近您的使用者的地區。  

- #### 部署詳情：  
  - 原始碼：選擇「GitHub」。  
  - GitHub 帳戶：授權 Azure 訪問您的 GitHub 帳戶。  
  - 組織：選擇您的 GitHub 組織。  
  - 儲存庫：選擇包含靜態網頁應用程式的儲存庫。  
  - 分支：選擇您要部署的分支。  

- #### 建置詳情：  
  - 建置預設：選擇您的應用程式所使用的框架（例如：React、Angular、Vue 等）。  
  - 應用程式位置：指定包含應用程式代碼的資料夾（例如：/ 如果在根目錄）。  
  - API 位置：如果有 API，指定其位置（可選）。  
  - 輸出位置：指定建置輸出生成的資料夾（例如：build 或 dist）。  

4. 檢查並建立  
檢查您的設置並點擊「建立」。Azure 會設置必要的資源並在您的儲存庫中建立 GitHub Actions 工作流程。

5. GitHub Actions 工作流程  
Azure 會自動在您的儲存庫中建立 GitHub Actions 工作流程文件（.github/workflows/azure-static-web-apps-<name>.yml）。此工作流程將處理建置和部署過程。

6. 監控部署  
前往 GitHub 儲存庫中的「Actions」標籤。  
您應該會看到一個工作流程正在運行。此工作流程將建置並部署您的靜態網頁應用程式到 Azure。  
工作流程完成後，您的應用程式將在提供的 Azure URL 上線。

### 範例工作流程文件

以下是 GitHub Actions 工作流程文件的範例：  
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
- [Azure 靜態網頁應用程式文件](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions 文件](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。