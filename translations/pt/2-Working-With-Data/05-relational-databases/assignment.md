<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:54:50+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "pt"
}
-->
# Exibindo dados de aeroportos

Foi fornecida uma [base de dados](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) construída em [SQLite](https://sqlite.org/index.html) que contém informações sobre aeroportos. O esquema está exibido abaixo. Você usará a [extensão SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) no [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) para exibir informações sobre os aeroportos de diferentes cidades.

## Instruções

Para começar a tarefa, será necessário realizar alguns passos. Você precisará instalar algumas ferramentas e fazer o download da base de dados de exemplo.

### Configure o seu sistema

Você pode usar o Visual Studio Code e a extensão SQLite para interagir com a base de dados.

1. Acesse [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) e siga as instruções para instalar o Visual Studio Code
1. Instale a extensão [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) conforme instruído na página do Marketplace

### Faça o download e abra a base de dados

Em seguida, faça o download e abra a base de dados.

1. Faça o download do [arquivo da base de dados no GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) e salve-o em um diretório
1. Abra o Visual Studio Code
1. Abra a base de dados na extensão SQLite selecionando **Ctl-Shift-P** (ou **Cmd-Shift-P** em um Mac) e digitando `SQLite: Open database`
1. Selecione **Choose database from file** e abra o arquivo **airports.db** que você baixou anteriormente
1. Após abrir a base de dados (não haverá uma atualização visível na tela), crie uma nova janela de consulta selecionando **Ctl-Shift-P** (ou **Cmd-Shift-P** em um Mac) e digitando `SQLite: New query`

Uma vez aberta, a nova janela de consulta pode ser usada para executar instruções SQL contra a base de dados. Você pode usar o comando **Ctl-Shift-Q** (ou **Cmd-Shift-Q** em um Mac) para executar consultas na base de dados.

> [!NOTE] 
> Para mais informações sobre a extensão SQLite, você pode consultar a [documentação](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Esquema da base de dados

O esquema de uma base de dados é o design e a estrutura das suas tabelas. A base de dados **airports** possui duas tabelas, `cities`, que contém uma lista de cidades no Reino Unido e na Irlanda, e `airports`, que contém a lista de todos os aeroportos. Como algumas cidades podem ter múltiplos aeroportos, foram criadas duas tabelas para armazenar as informações. Neste exercício, você usará joins para exibir informações de diferentes cidades.

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

## Tarefa

Crie consultas para retornar as seguintes informações:

1. todos os nomes de cidades na tabela `Cities`
1. todas as cidades na Irlanda na tabela `Cities`
1. todos os nomes de aeroportos com suas respectivas cidades e países
1. todos os aeroportos em Londres, Reino Unido

## Rubrica

| Exemplar   | Adequado   | Precisa Melhorar |
| ---------- | ---------- | ---------------- |

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.