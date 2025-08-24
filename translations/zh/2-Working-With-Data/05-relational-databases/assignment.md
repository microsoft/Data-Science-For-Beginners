<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-24T12:02:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "zh"
}
-->
# 显示机场数据

您已获得一个基于 [SQLite](https://sqlite.org/index.html) 的 [数据库](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)，其中包含有关机场的信息。数据库的模式如下所示。您将使用 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) 中的 [SQLite 扩展](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) 来显示不同城市机场的信息。

## 指导说明

要开始完成任务，您需要执行几个步骤。您需要安装一些工具并下载示例数据库。

### 设置您的系统

您可以使用 Visual Studio Code 和 SQLite 扩展来与数据库交互。

1. 访问 [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)，按照说明安装 Visual Studio Code
1. 按照 Marketplace 页面上的说明安装 [SQLite 扩展](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

### 下载并打开数据库

接下来，您将下载并打开数据库。

1. 从 [GitHub 下载数据库文件](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)，并将其保存到一个目录中
1. 打开 Visual Studio Code
1. 在 SQLite 扩展中打开数据库，按下 **Ctl-Shift-P**（Mac 上为 **Cmd-Shift-P**），然后输入 `SQLite: Open database`
1. 选择 **Choose database from file**，然后打开您之前下载的 **airports.db** 文件
1. 打开数据库后（屏幕上不会显示更新），通过按下 **Ctl-Shift-P**（Mac 上为 **Cmd-Shift-P**），然后输入 `SQLite: New query` 来创建一个新的查询窗口

打开后，新的查询窗口可用于对数据库运行 SQL 语句。您可以使用命令 **Ctl-Shift-Q**（Mac 上为 **Cmd-Shift-Q**）来对数据库运行查询。

> [!NOTE] 有关 SQLite 扩展的更多信息，您可以查阅 [文档](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## 数据库模式

数据库的模式是其表的设计和结构。**airports** 数据库有两个表：`cities` 表包含英国和爱尔兰的城市列表，`airports` 表包含所有机场的列表。由于某些城市可能有多个机场，因此创建了两个表来存储信息。在本练习中，您将使用连接来显示不同城市的信息。

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## 任务

创建查询以返回以下信息：

1. `Cities` 表中的所有城市名称
1. `Cities` 表中所有位于爱尔兰的城市
1. 所有机场名称及其所在城市和国家
1. 所有位于英国伦敦的机场

## 评分标准

| 卓越       | 合格       | 需要改进   |
| --------- | --------- | --------- |

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。