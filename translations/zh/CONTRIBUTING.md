<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:29:57+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "zh"
}
-->
# 贡献《数据科学入门》

感谢您对《数据科学入门》课程的贡献兴趣！我们欢迎社区的贡献。

## 目录

- [行为准则](../..)
- [我如何贡献？](../..)
- [入门指南](../..)
- [贡献指南](../..)
- [拉取请求流程](../..)
- [样式指南](../..)
- [贡献者许可协议](../..)

## 行为准则

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
有关更多信息，请参阅 [行为准则常见问题](https://opensource.microsoft.com/codeofconduct/faq/) 或通过 [opencode@microsoft.com](mailto:opencode@microsoft.com) 联系我们提出其他问题或意见。

## 我如何贡献？

### 报告错误

在创建错误报告之前，请检查现有问题以避免重复。当您创建错误报告时，请尽可能提供详细信息：

- **使用清晰且描述性的标题**
- **描述重现问题的具体步骤**
- **提供具体示例**（代码片段、截图）
- **描述您观察到的行为以及您的期望**
- **包括您的环境详细信息**（操作系统、Python版本、浏览器）

### 提出改进建议

我们欢迎改进建议！提出建议时：

- **使用清晰且描述性的标题**
- **提供建议改进的详细描述**
- **解释为什么此改进会有用**
- **列出其他项目中的类似功能（如果适用）**

### 贡献文档

文档改进总是受到欢迎：

- **修复拼写和语法错误**
- **提高解释的清晰度**
- **补充缺失的文档**
- **更新过时的信息**
- **添加示例或使用案例**

### 贡献代码

我们欢迎以下代码贡献：

- **新的课程或练习**
- **错误修复**
- **改进现有的笔记本**
- **新的数据集或示例**
- **测验应用程序的改进**

## 入门指南

### 前提条件

在贡献之前，请确保您已具备以下条件：

1. 一个 GitHub 账户
2. 您的系统上已安装 Git
3. 安装了 Python 3.7+ 和 Jupyter
4. 安装了 Node.js 和 npm（用于测验应用程序贡献）
5. 熟悉课程结构

请参阅 [INSTALLATION.md](INSTALLATION.md) 获取详细的设置说明。

### Fork 和克隆

1. **在 GitHub 上 Fork 仓库**
2. **本地克隆您的 Fork**：
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **添加上游远程仓库**：
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### 创建分支

为您的工作创建一个新分支：

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

分支命名约定：
- `feature/` - 新功能或课程
- `fix/` - 错误修复
- `docs/` - 文档更改
- `refactor/` - 代码重构

## 贡献指南

### 对课程内容的贡献

贡献课程或修改现有课程时：

1. **遵循现有结构**：
   - README.md 包含课程内容
   - Jupyter 笔记本包含练习
   - 作业（如果适用）
   - 链接到前测和后测

2. **包括以下元素**：
   - 清晰的学习目标
   - 分步解释
   - 带注释的代码示例
   - 练习以供实践
   - 额外资源的链接

3. **确保可访问性**：
   - 使用清晰、简单的语言
   - 为图片提供替代文本
   - 包含代码注释
   - 考虑不同的学习风格

### 对 Jupyter 笔记本的贡献

1. **在提交之前清除所有输出**：
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **包含带解释的 Markdown 单元格**

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

4. **在提交之前完全测试您的笔记本**

### 对 Python 代码的贡献

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 样式指南：

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

### 对测验应用程序的贡献

修改测验应用程序时：

1. **本地测试**：
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **运行代码检查工具**：
   ```bash
   npm run lint
   ```

3. **成功构建**：
   ```bash
   npm run build
   ```

4. **遵循 Vue.js 样式指南**和现有模式

### 对翻译的贡献

添加或更新翻译时：

1. 遵循 `translations/` 文件夹中的结构
2. 使用语言代码作为文件夹名称（例如，法语为 `fr`）
3. 保持与英文版本相同的文件结构
4. 更新测验链接以包含语言参数：`?loc=fr`
5. 测试所有链接和格式

## 拉取请求流程

### 提交之前

1. **使用最新更改更新您的分支**：
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **测试您的更改**：
   - 运行所有修改过的笔记本
   - 测试测验应用程序（如果已修改）
   - 验证所有链接是否有效
   - 检查拼写和语法错误

3. **提交您的更改**：
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   编写清晰的提交消息：
   - 使用现在时态（“添加功能”而不是“已添加功能”）
   - 使用命令式语气（“移动光标到...”而不是“光标移动到...”）
   - 限制第一行为 72 个字符
   - 在相关时引用问题和拉取请求

4. **推送到您的 Fork**：
   ```bash
   git push origin feature/your-feature-name
   ```

### 创建拉取请求

1. 转到 [仓库](https://github.com/microsoft/Data-Science-For-Beginners)
2. 点击“Pull requests” → “New pull request”
3. 点击“compare across forks”
4. 选择您的 Fork 和分支
5. 点击“Create pull request”

### PR 标题格式

使用清晰、描述性的标题，遵循以下格式：

```
[Component] Brief description
```

示例：
- `[Lesson 7] 修复 Python 笔记本导入错误`
- `[Quiz App] 添加德语翻译`
- `[Docs] 更新 README，添加新前提条件`
- `[Fix] 修正可视化课程中的数据路径`

### PR 描述

在您的 PR 描述中包括：

- **内容**：您做了哪些更改？
- **原因**：为什么需要这些更改？
- **方法**：您如何实现这些更改？
- **测试**：您如何测试这些更改？
- **截图**：对于视觉更改，请包含截图
- **相关问题**：链接到相关问题（例如，“Fixes #123”）

### 审核流程

1. **自动检查**将运行在您的 PR 上
2. **维护者将审核**您的贡献
3. **根据反馈**进行额外提交
4. 一旦获得批准，**维护者将合并**您的 PR

### PR 合并后

1. 删除您的分支：
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

## 样式指南

### Markdown

- 使用一致的标题级别
- 在章节之间添加空行
- 使用带语言标识符的代码块：
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- 为图片添加替代文本：`![Alt text](../../translated_images/zh/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- 保持合理的行长度（约 80-100 个字符）

### Python

- 遵循 PEP 8 样式指南
- 使用有意义的变量名
- 为函数添加文档字符串
- 在适当的地方添加类型提示：
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- 遵循 Vue.js 2 样式指南
- 使用提供的 ESLint 配置
- 编写模块化、可重用的组件
- 为复杂逻辑添加注释

### 文件组织

- 将相关文件放在一起
- 使用描述性的文件名
- 遵循现有的目录结构
- 不要提交不必要的文件（如 .DS_Store、.pyc、node_modules 等）

## 贡献者许可协议

本项目欢迎贡献和建议。大多数贡献需要您同意贡献者许可协议 (CLA)，声明您有权并实际授予我们使用您的贡献的权利。详情请访问 https://cla.microsoft.com。

当您提交拉取请求时，CLA-bot 会自动确定您是否需要提供 CLA，并适当装饰 PR（例如，标签、评论）。只需按照机器人提供的说明操作即可。您只需在所有使用我们 CLA 的仓库中执行一次此操作。

## 有问题？

- 查看我们的 [Discord 频道 #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- 加入我们的 [Discord 社区](https://aka.ms/ds4beginners/discord)
- 查看现有的 [问题](https://github.com/microsoft/Data-Science-For-Beginners/issues) 和 [拉取请求](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## 感谢！

您的贡献使这门课程对所有人都更好。感谢您抽出时间贡献！

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。