<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T16:45:11+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "br"
}
-->
# Exibindo dados de aeroportos

Você recebeu um [banco de dados](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) baseado em [SQLite](https://sqlite.org/index.html) que contém informações sobre aeroportos. O esquema está exibido abaixo. Você usará a [extensão SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) no [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) para exibir informações sobre os aeroportos de diferentes cidades.

## Instruções

Para começar a tarefa, você precisará realizar algumas etapas. Será necessário instalar algumas ferramentas e baixar o banco de dados de exemplo.

### Configure seu sistema

Você pode usar o Visual Studio Code e a extensão SQLite para interagir com o banco de dados.

1. Acesse [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) e siga as instruções para instalar o Visual Studio Code
1. Instale a [extensão SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) conforme instruído na página do Marketplace

### Baixe e abra o banco de dados

Em seguida, você fará o download e abrirá o banco de dados.

1. Baixe o [arquivo do banco de dados no GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) e salve-o em um diretório
1. Abra o Visual Studio Code
1. Abra o banco de dados na extensão SQLite selecionando **Ctrl-Shift-P** (ou **Cmd-Shift-P** em um Mac) e digitando `SQLite: Open database`
1. Selecione **Choose database from file** e abra o arquivo **airports.db** que você baixou anteriormente
1. Após abrir o banco de dados (você não verá uma atualização na tela), crie uma nova janela de consulta selecionando **Ctrl-Shift-P** (ou **Cmd-Shift-P** em um Mac) e digitando `SQLite: New query`

Depois de aberto, a nova janela de consulta pode ser usada para executar instruções SQL no banco de dados. Você pode usar o comando **Ctrl-Shift-Q** (ou **Cmd-Shift-Q** em um Mac) para executar consultas no banco de dados.

> [!NOTE] Para mais informações sobre a extensão SQLite, você pode consultar a [documentação](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Esquema do banco de dados

O esquema de um banco de dados é o design e a estrutura de suas tabelas. O banco de dados **airports** possui duas tabelas: `cities`, que contém uma lista de cidades no Reino Unido e na Irlanda, e `airports`, que contém a lista de todos os aeroportos. Como algumas cidades podem ter vários aeroportos, foram criadas duas tabelas para armazenar as informações. Neste exercício, você usará joins para exibir informações de diferentes cidades.

| Cidades          |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Aeroportos                      |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK para id em **Cidades**) |

## Tarefa

Crie consultas para retornar as seguintes informações:

1. todos os nomes de cidades na tabela `Cities`
1. todas as cidades na Irlanda na tabela `Cities`
1. todos os nomes de aeroportos com suas respectivas cidades e países
1. todos os aeroportos em Londres, Reino Unido

## Rubrica

| Exemplary | Adequate | Needs Improvement |
| --------- | -------- | ----------------- |

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.