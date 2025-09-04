<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T13:28:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ko"
}
-->
# 데이터 작업: 관계형 데이터베이스

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| 데이터 작업: 관계형 데이터베이스 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

여러분은 과거에 정보를 저장하기 위해 스프레드시트를 사용해본 적이 있을 것입니다. 스프레드시트는 행과 열로 구성되어 있으며, 행에는 정보(또는 데이터)가, 열에는 그 정보에 대한 설명(때로는 메타데이터라고도 함)이 포함됩니다. 관계형 데이터베이스는 테이블의 행과 열이라는 핵심 원칙을 기반으로 구축되며, 여러 테이블에 걸쳐 정보를 분산시킬 수 있습니다. 이를 통해 더 복잡한 데이터를 다룰 수 있고, 중복을 피하며, 데이터를 탐색하는 방식에 유연성을 제공합니다. 이제 관계형 데이터베이스의 개념을 살펴보겠습니다.

## [강의 전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## 모든 것은 테이블에서 시작됩니다

관계형 데이터베이스의 핵심은 테이블입니다. 스프레드시트와 마찬가지로, 테이블은 열과 행의 모음입니다. 행은 우리가 다루고자 하는 데이터나 정보를 포함하며, 예를 들어 도시 이름이나 강수량 같은 데이터를 저장합니다. 열은 저장된 데이터를 설명합니다.

도시에 대한 정보를 저장하기 위해 테이블을 시작해 봅시다. 도시 이름과 국가를 저장한다고 가정해 보겠습니다. 이를 다음과 같은 테이블에 저장할 수 있습니다:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

**City**, **Country**, **Population**이라는 열 이름이 저장된 데이터를 설명하며, 각 행은 하나의 도시에 대한 정보를 포함하고 있습니다.

## 단일 테이블 접근 방식의 한계

위의 테이블은 여러분에게 꽤 익숙하게 보일 것입니다. 이제 우리의 데이터베이스에 연간 강수량(단위: 밀리미터) 데이터를 추가해 보겠습니다. 2018년, 2019년, 2020년 데이터를 추가한다고 가정해 봅시다. 도쿄의 데이터를 추가하면 다음과 같을 것입니다:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

이 테이블에서 무엇을 발견할 수 있나요? 도시 이름과 국가를 반복적으로 중복 저장하고 있다는 점을 알 수 있습니다. 이는 많은 저장 공간을 차지할 수 있으며, 불필요한 중복입니다. 결국 도쿄라는 도시는 우리가 관심 있는 단 하나의 이름만 가지고 있습니다.

그렇다면 다른 방법을 시도해 봅시다. 각 연도에 대해 새로운 열을 추가해 보겠습니다:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

이 방식은 행 중복을 피할 수 있지만, 몇 가지 다른 문제를 야기합니다. 새로운 연도가 추가될 때마다 테이블 구조를 수정해야 합니다. 또한, 데이터가 증가함에 따라 연도를 열로 사용하는 방식은 값을 검색하고 계산하는 데 더 어려움을 줄 수 있습니다.

이것이 바로 여러 테이블과 관계가 필요한 이유입니다. 데이터를 분리함으로써 중복을 피하고 데이터를 다루는 방식에 더 많은 유연성을 가질 수 있습니다.

## 관계의 개념

데이터로 돌아가서 어떻게 데이터를 분리할지 결정해 봅시다. 도시 이름과 국가를 저장하려면, 이를 하나의 테이블에 저장하는 것이 가장 적합할 것입니다.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

하지만 다음 테이블을 생성하기 전에 각 도시를 참조하는 방법을 결정해야 합니다. 특정 행을 식별하는 데 사용되는 식별자, ID 또는 (기술적 데이터베이스 용어로) 기본 키(primary key)가 필요합니다. 기본 키는 테이블에서 특정 행을 식별하는 데 사용되는 값입니다. 이는 값 자체(예: 도시 이름)를 기반으로 할 수도 있지만, 거의 항상 숫자나 다른 식별자를 사용하는 것이 좋습니다. ID는 변경되지 않아야 하며, 변경될 경우 관계가 깨질 수 있기 때문입니다. 대부분의 경우 기본 키 또는 ID는 자동으로 생성된 숫자일 것입니다.

> ✅ 기본 키는 종종 PK로 약어화됩니다.

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ 이 강의에서는 "id"와 "기본 키"라는 용어를 서로 교환하여 사용합니다. 여기서 설명하는 개념은 나중에 탐구할 DataFrame에도 적용됩니다. DataFrame은 "기본 키"라는 용어를 사용하지 않지만, 매우 유사한 방식으로 작동한다는 것을 알게 될 것입니다.

도시 테이블을 생성했으니 이제 강수량 데이터를 저장해 봅시다. 도시의 전체 정보를 중복 저장하는 대신, ID를 사용할 수 있습니다. 새로 생성된 테이블에도 *id* 열이 있어야 하며, 모든 테이블에는 ID 또는 기본 키가 있어야 합니다.

### rainfall

| rainfall_id | city_id | Year | Amount |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

새로 생성된 **rainfall** 테이블의 **city_id** 열을 주목하세요. 이 열은 **cities** 테이블의 ID를 참조하는 값을 포함하고 있습니다. 기술적 관계형 데이터 용어로, 이를 **외래 키**(foreign key)라고 합니다. 이는 다른 테이블의 기본 키입니다. 간단히 참조 또는 포인터라고 생각하면 됩니다. **city_id** 1은 도쿄를 참조합니다.

> [!NOTE] 외래 키는 종종 FK로 약어화됩니다.

## 데이터 검색

데이터를 두 개의 테이블로 분리했으니, 데이터를 어떻게 검색할 수 있을지 궁금할 것입니다. MySQL, SQL Server 또는 Oracle과 같은 관계형 데이터베이스를 사용하는 경우, SQL(Structured Query Language)이라는 언어를 사용할 수 있습니다. SQL(때로는 "시퀄"이라고 발음)은 관계형 데이터베이스에서 데이터를 검색하고 수정하는 데 사용되는 표준 언어입니다.

데이터를 검색하려면 `SELECT` 명령을 사용합니다. 기본적으로, **보고 싶은 열을 선택(SELECT)** 하고, **그 열이 포함된 테이블로부터(FROM)** 가져옵니다. 도시 이름만 표시하려면 다음과 같은 쿼리를 사용할 수 있습니다:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT`는 열을 나열하는 곳이고, `FROM`은 테이블을 나열하는 곳입니다.

> [NOTE] SQL 구문은 대소문자를 구분하지 않습니다. 즉, `select`와 `SELECT`는 동일한 의미를 가집니다. 그러나 사용하는 데이터베이스 유형에 따라 열과 테이블은 대소문자를 구분할 수 있습니다. 따라서 프로그래밍에서는 항상 모든 것을 대소문자를 구분하는 것처럼 다루는 것이 모범 사례입니다. SQL 쿼리를 작성할 때 일반적인 관례는 키워드를 모두 대문자로 작성하는 것입니다.

위의 쿼리는 모든 도시를 표시합니다. 뉴질랜드에 있는 도시만 표시하고 싶다고 가정해 봅시다. 필터가 필요합니다. SQL 키워드는 `WHERE`이며, "어떤 조건이 참인 경우"를 의미합니다.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## 데이터 결합

지금까지는 단일 테이블에서 데이터를 검색했습니다. 이제 **cities**와 **rainfall**의 데이터를 결합하고 싶습니다. 이는 *조인(join)*을 통해 이루어집니다. 두 테이블 사이에 연결을 만들어 각 테이블의 열 값을 매칭합니다.

우리의 예에서는 **rainfall**의 **city_id** 열과 **cities**의 **city_id** 열을 매칭할 것입니다. 이를 통해 강수량 값을 해당 도시와 연결합니다. 우리가 수행할 조인의 유형은 *내부(inner)* 조인이라고 하며, 다른 테이블과 매칭되지 않는 행은 표시되지 않습니다. 우리의 경우 모든 도시에 강수량 데이터가 있으므로 모든 데이터가 표시될 것입니다.

2019년의 모든 도시 강수량 데이터를 검색해 봅시다.

단계를 나누어 진행하겠습니다. 첫 번째 단계는 **city_id** 열을 기준으로 데이터를 결합하는 것입니다.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

결합하려는 두 열과 **city_id**를 기준으로 테이블을 조인하고 싶다는 점을 강조했습니다. 이제 `WHERE` 문을 추가하여 2019년 데이터만 필터링합니다.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## 요약

관계형 데이터베이스는 정보를 여러 테이블로 나누고 이를 다시 결합하여 표시 및 분석하는 데 중점을 둡니다. 이를 통해 계산을 수행하거나 데이터를 조작하는 데 높은 유연성을 제공합니다. 관계형 데이터베이스의 핵심 개념과 두 테이블 간의 조인을 수행하는 방법을 살펴보았습니다.

## 🚀 도전 과제

인터넷에는 수많은 관계형 데이터베이스가 존재합니다. 위에서 배운 기술을 사용하여 데이터를 탐색해 보세요.

## 강의 후 퀴즈

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ds/)

## 복습 및 자기 학습

SQL 및 관계형 데이터베이스 개념을 계속 탐구할 수 있는 여러 리소스가 [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum)에 제공됩니다.

- [관계형 데이터 개념 설명](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL로 쿼리 시작하기](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL은 SQL의 한 버전입니다)
- [Microsoft Learn의 SQL 콘텐츠](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## 과제

[과제 제목](assignment.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  