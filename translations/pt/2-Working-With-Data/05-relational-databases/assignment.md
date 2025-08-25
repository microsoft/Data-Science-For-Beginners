<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-24T20:55:46+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "pt"
}
-->
# Exibindo dados de aeroportos

Foi-lhe fornecida uma [base de dados](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) construída em [SQLite](https://sqlite.org/index.html) que contém informações sobre aeroportos. O esquema está exibido abaixo. Irá utilizar a [extensão SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) no [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) para exibir informações sobre os aeroportos de diferentes cidades.

## Instruções

Para começar a tarefa, precisará realizar alguns passos. Será necessário instalar algumas ferramentas e descarregar a base de dados de exemplo.

### Configurar o seu sistema

Pode usar o Visual Studio Code e a extensão SQLite para interagir com a base de dados.

1. Aceda a [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) e siga as instruções para instalar o Visual Studio Code
1. Instale a [extensão SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) conforme indicado na página do Marketplace

### Descarregar e abrir a base de dados

De seguida, descarregue e abra a base de dados.

1. Descarregue o [ficheiro da base de dados no GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) e guarde-o numa pasta
1. Abra o Visual Studio Code
1. Abra a base de dados na extensão SQLite selecionando **Ctl-Shift-P** (ou **Cmd-Shift-P** num Mac) e escrevendo `SQLite: Open database`
1. Selecione **Choose database from file** e abra o ficheiro **airports.db** que descarregou anteriormente
1. Após abrir a base de dados (não verá uma atualização no ecrã), crie uma nova janela de consulta selecionando **Ctl-Shift-P** (ou **Cmd-Shift-P** num Mac) e escrevendo `SQLite: New query`

Depois de aberta, a nova janela de consulta pode ser usada para executar instruções SQL na base de dados. Pode usar o comando **Ctl-Shift-Q** (ou **Cmd-Shift-Q** num Mac) para executar consultas na base de dados.

> [!NOTE] Para mais informações sobre a extensão SQLite, pode consultar a [documentação](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Esquema da base de dados

O esquema de uma base de dados é o design e a estrutura das suas tabelas. A base de dados **airports** tem duas tabelas, `cities`, que contém uma lista de cidades no Reino Unido e na Irlanda, e `airports`, que contém a lista de todos os aeroportos. Como algumas cidades podem ter vários aeroportos, foram criadas duas tabelas para armazenar as informações. Neste exercício, irá usar joins para exibir informações de diferentes cidades.

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
1. todos os nomes de aeroportos com as respetivas cidades e países
1. todos os aeroportos em Londres, Reino Unido

## Rubrica

| Exemplar  | Adequado | Precisa de Melhorias |
| --------- | -------- | -------------------- |

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.