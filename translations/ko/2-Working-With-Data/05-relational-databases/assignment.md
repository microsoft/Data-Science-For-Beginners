<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:53:46+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ko"
}
-->
# 공항 데이터 표시

[SQLite](https://sqlite.org/index.html)를 기반으로 구축된 [데이터베이스](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)가 제공되었으며, 이 데이터베이스에는 공항에 대한 정보가 포함되어 있습니다. 아래에 스키마가 표시되어 있습니다. [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)에서 [SQLite 확장](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)을 사용하여 다양한 도시의 공항 정보를 표시합니다.

## 지침

과제를 시작하려면 몇 가지 단계를 수행해야 합니다. 약간의 도구를 설치하고 샘플 데이터베이스를 다운로드해야 합니다.

### 시스템 설정

Visual Studio Code와 SQLite 확장을 사용하여 데이터베이스와 상호작용할 수 있습니다.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)으로 이동하여 Visual Studio Code를 설치하는 지침을 따르세요.
1. [SQLite 확장](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)을 Marketplace 페이지의 지침에 따라 설치하세요.

### 데이터베이스 다운로드 및 열기

다음으로 데이터베이스를 다운로드하고 엽니다.

1. [GitHub에서 데이터베이스 파일](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db)을 다운로드하여 디렉토리에 저장하세요.
1. Visual Studio Code를 엽니다.
1. **Ctl-Shift-P** (Mac에서는 **Cmd-Shift-P**)를 선택하고 `SQLite: Open database`를 입력하여 SQLite 확장에서 데이터베이스를 엽니다.
1. **Choose database from file**을 선택하고 이전에 다운로드한 **airports.db** 파일을 엽니다.
1. 데이터베이스를 열면 화면에 업데이트가 표시되지 않지만, **Ctl-Shift-P** (Mac에서는 **Cmd-Shift-P**)를 선택하고 `SQLite: New query`를 입력하여 새 쿼리 창을 만듭니다.

데이터베이스가 열리면 새 쿼리 창을 사용하여 데이터베이스에 대해 SQL 문을 실행할 수 있습니다. **Ctl-Shift-Q** (Mac에서는 **Cmd-Shift-Q**) 명령을 사용하여 데이터베이스에 대해 쿼리를 실행할 수 있습니다.

> [!NOTE] 
> SQLite 확장에 대한 자세한 내용은 [문서](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)를 참조하세요.

## 데이터베이스 스키마

데이터베이스의 스키마는 테이블 설계와 구조를 나타냅니다. **airports** 데이터베이스에는 두 개의 테이블이 있습니다. `cities`는 영국과 아일랜드의 도시 목록을 포함하고 있으며, `airports`는 모든 공항 목록을 포함하고 있습니다. 일부 도시에는 여러 공항이 있을 수 있으므로 정보를 저장하기 위해 두 개의 테이블이 생성되었습니다. 이 연습에서는 조인을 사용하여 다양한 도시의 정보를 표시합니다.

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

## 과제

다음 정보를 반환하는 쿼리를 작성하세요:

1. `Cities` 테이블의 모든 도시 이름
1. `Cities` 테이블에서 아일랜드의 모든 도시
1. 도시와 국가와 함께 모든 공항 이름
1. 영국 런던의 모든 공항

## 평가 기준

| 우수 | 적절 | 개선 필요 |
| ---- | ---- | -------- |

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.