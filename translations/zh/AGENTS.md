<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:05:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "zh"
}
-->
# AGENTS.md

## 项目概述

《数据科学入门》是由 Microsoft Azure Cloud Advocates 创建的一个全面的10周、20课时的课程。该仓库是一个学习资源，通过基于项目的课程教授数据科学的基础概念，包括 Jupyter 笔记本、互动测验和实践作业。

**关键技术：**
- **Jupyter 笔记本**：使用 Python 3 的主要学习媒介
- **Python 库**：pandas、numpy、matplotlib 用于数据分析和可视化
- **Vue.js 2**：测验应用程序（quiz-app 文件夹）
- **Docsify**：离线访问的文档站点生成器
- **Node.js/npm**：JavaScript 组件的包管理
- **Markdown**：所有课程内容和文档

**架构：**
- 多语言教育仓库，提供广泛的翻译
- 结构化为课程模块（从1-Introduction到6-Data-Science-In-Wild）
- 每节课包括 README、笔记本、作业和测验
- 独立的 Vue.js 测验应用程序，用于课前/课后评估
- 支持 GitHub Codespaces 和 VS Code 开发容器

## 设置命令

### 仓库设置
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python 环境设置
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 测验应用程序设置
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

### Docsify 文档服务器
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### 可视化项目设置
对于像 meaningful-visualizations（第13课）这样的可视化项目：
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


## 开发工作流程

### 使用 Jupyter 笔记本
1. 在仓库根目录启动 Jupyter：`jupyter notebook`
2. 导航到所需的课程文件夹
3. 打开 `.ipynb` 文件以完成练习
4. 笔记本是自包含的，包含解释和代码单元
5. 大多数笔记本使用 pandas、numpy 和 matplotlib - 确保这些库已安装

### 课程结构
每节课通常包括：
- `README.md` - 主要课程内容，包含理论和示例
- `notebook.ipynb` - 实践 Jupyter 笔记本练习
- `assignment.ipynb` 或 `assignment.md` - 实践作业
- `solution/` 文件夹 - 解决方案笔记本和代码
- `images/` 文件夹 - 支持的视觉材料

### 测验应用程序开发
- 使用 Vue.js 2 的应用程序，开发期间支持热重载
- 测验存储在 `quiz-app/src/assets/translations/` 中
- 每种语言都有自己的翻译文件夹（en, fr, es 等）
- 测验编号从0开始，总计40个测验

### 添加翻译
- 翻译存储在仓库根目录的 `translations/` 文件夹中
- 每种语言的课程结构与英文完全镜像
- 通过 GitHub Actions 自动翻译（co-op-translator.yml）

## 测试说明

### 测验应用程序测试
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### 笔记本测试
- 笔记本没有自动化测试框架
- 手动验证：按顺序运行所有单元，确保没有错误
- 验证数据文件是否可访问，输出是否正确生成
- 检查可视化是否正确渲染

### 文档测试
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### 代码质量检查
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## 代码风格指南

### Python（Jupyter 笔记本）
- 遵循 PEP 8 风格指南编写 Python 代码
- 使用清晰的变量名，解释所分析的数据
- 在代码单元之前包含解释性的 Markdown 单元
- 代码单元专注于单一概念或操作
- 使用 pandas 进行数据操作，matplotlib 进行可视化
- 常见导入模式：
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- 遵循 Vue.js 2 风格指南和最佳实践
- ESLint 配置在 `quiz-app/package.json` 中
- 使用 Vue 单文件组件（.vue 文件）
- 维护基于组件的架构
- 提交更改前运行 `npm run lint`

### Markdown 文档
- 使用清晰的标题层次结构（# ## ### 等）
- 包含带语言说明符的代码块
- 为图片添加替代文本
- 链接相关课程和资源
- 保持合理的行长度以提高可读性

### 文件组织
- 课程内容存储在编号文件夹中（01-defining-data-science 等）
- 解决方案存储在专用的 `solution/` 子文件夹中
- 翻译在 `translations/` 文件夹中镜像英文结构
- 数据文件存储在 `data/` 或课程特定文件夹中

## 构建和部署

### 测验应用程序部署
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure 静态 Web 应用部署
测验应用程序可以部署到 Azure 静态 Web 应用：
1. 创建 Azure 静态 Web 应用资源
2. 连接到 GitHub 仓库
3. 配置构建设置：
   - 应用位置：`quiz-app`
   - 输出位置：`dist`
4. GitHub Actions 工作流将在推送时自动部署

### 文档站点
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- 仓库包含开发容器配置
- Codespaces 自动设置 Python 和 Node.js 环境
- 通过 GitHub UI 打开仓库中的 Codespace
- 所有依赖项自动安装

## 拉取请求指南

### 提交前
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR 标题格式
- 使用清晰、描述性的标题
- 格式：`[组件] 简短描述`
- 示例：
  - `[第7课] 修复 Python 笔记本导入错误`
  - `[测验应用] 添加德语翻译`
  - `[文档] 更新 README，添加新前置条件`

### 必要检查
- 确保所有代码运行无错误
- 验证笔记本完全执行
- 确认 Vue.js 应用程序成功构建
- 检查文档链接是否有效
- 如果修改了测验应用程序，请进行测试
- 验证翻译保持一致的结构

### 贡献指南
- 遵循现有代码风格和模式
- 为复杂逻辑添加解释性注释
- 更新相关文档
- 如果适用，跨不同课程模块测试更改
- 查看 CONTRIBUTING.md 文件

## 附加说明

### 常用库
- **pandas**：数据操作和分析
- **numpy**：数值计算
- **matplotlib**：数据可视化和绘图
- **seaborn**：统计数据可视化（部分课程）
- **scikit-learn**：机器学习（高级课程）

### 使用数据文件
- 数据文件位于 `data/` 文件夹或课程特定目录中
- 大多数笔记本期望数据文件在相对路径中
- CSV 文件是主要的数据格式
- 部分课程使用 JSON 作为非关系数据示例

### 多语言支持
- 通过 GitHub Actions 提供40多种语言翻译
- 翻译工作流在 `.github/workflows/co-op-translator.yml` 中
- 翻译存储在 `translations/` 文件夹中，使用语言代码命名
- 测验翻译存储在 `quiz-app/src/assets/translations/` 中

### 开发环境选项
1. **本地开发**：本地安装 Python、Jupyter、Node.js
2. **GitHub Codespaces**：基于云的即时开发环境
3. **VS Code 开发容器**：基于本地容器的开发
4. **Binder**：在云中启动笔记本（如果已配置）

### 课程内容指南
- 每节课是独立的，但建立在之前的概念之上
- 课前测验测试先前知识
- 课后测验巩固学习
- 作业提供实践练习
- Sketchnotes 提供视觉总结

### 常见问题排查

**Jupyter 内核问题：**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm 安装失败：**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**笔记本导入错误：**
- 验证所有必需库是否已安装
- 检查 Python 版本兼容性（推荐 Python 3.7+）
- 确保虚拟环境已激活

**Docsify 无法加载：**
- 验证是否从仓库根目录提供服务
- 检查 `index.html` 是否存在
- 确保网络访问正常（端口 3000）

### 性能注意事项
- 大型数据集可能需要时间加载到笔记本中
- 复杂图表的可视化渲染可能较慢
- Vue.js 开发服务器支持热重载以快速迭代
- 生产构建经过优化和压缩

### 安全注意事项
- 不应提交敏感数据或凭据
- 在云课程中使用环境变量存储任何 API 密钥
- 与 Azure 相关的课程可能需要 Azure 账户凭据
- 保持依赖项更新以获取安全补丁

## 贡献翻译
- 通过 GitHub Actions 管理自动翻译
- 欢迎手动修正以提高翻译准确性
- 遵循现有翻译文件夹结构
- 更新测验链接以包含语言参数：`?loc=fr`
- 测试翻译课程以确保正确渲染

## 相关资源
- 主课程：https://aka.ms/datascience-beginners
- Microsoft Learn：https://docs.microsoft.com/learn/
- 学生中心：https://docs.microsoft.com/learn/student-hub
- 讨论论坛：https://github.com/microsoft/Data-Science-For-Beginners/discussions
- 其他 Microsoft 课程：ML for Beginners, AI for Beginners, Web Dev for Beginners

## 项目维护
- 定期更新以保持内容最新
- 欢迎社区贡献
- 在 GitHub 上跟踪问题
- 由课程维护者审查 PR
- 每月内容审查和更新

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。