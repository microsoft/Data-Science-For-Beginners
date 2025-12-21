<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T10:53:29+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ko"
}
-->
# 데이터 작업: 관계형 데이터베이스

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| 데이터 작업: 관계형 데이터베이스 - _스케치노트 by [@nitya](https://twitter.com/nitya)_ |

과거에 정보를 저장하기 위해 스프레드시트를 사용해본 적이 있을 것입니다. 행과 열의 집합이 있었고, 행에는 정보(또는 데이터)가 포함되어 있었으며, 열은 정보를 설명했습니다(때로는 메타데이터라고도 함). 관계형 데이터베이스는 테이블의 열과 행이라는 이 핵심 원칙을 기반으로 구축되어 여러 테이블에 걸쳐 정보를 분산시킬 수 있습니다. 이를 통해 더 복잡한 데이터를 다룰 수 있고, 중복을 피하며, 데이터를 탐색하는 방식에 유연성을 가질 수 있습니다. 관계형 데이터베이스의 개념을 살펴보겠습니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## 모든 것은 테이블에서 시작된다

관계형 데이터베이스의 핵심은 테이블입니다. 스프레드시트와 마찬가지로 테이블은 열과 행의 모음입니다. 행에는 우리가 작업하려는 데이터나 정보가 포함되어 있으며, 예를 들어 도시 이름이나 강수량 등이 있습니다. 열은 저장하는 데이터를 설명합니다.

도시에 대한 정보를 저장하는 테이블을 만들어 탐색을 시작해 봅시다. 이름과 국가부터 시작할 수 있습니다. 다음과 같이 테이블에 저장할 수 있습니다:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

**city**, **country**, **population**이라는 열 이름이 저장되는 데이터를 설명하며, 각 행은 한 도시의 정보를 담고 있음을 주목하세요.

## 단일 테이블 접근법의 한계

위 테이블이 비교적 익숙하게 느껴질 것입니다. 이제 성장하는 데이터베이스에 연간 강수량(밀리미터 단위)을 추가해 봅시다. 2018년, 2019년, 2020년에 초점을 맞춥니다. 도쿄에 대해 추가한다면 다음과 같을 수 있습니다:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

테이블에서 무엇을 발견했나요? 도시 이름과 국가가 반복되고 있음을 알 수 있습니다. 이는 상당한 저장 공간을 차지할 수 있으며, 여러 복사본을 가질 필요가 거의 없습니다. 결국 도쿄는 우리가 관심 있는 단 하나의 이름뿐입니다.

좋아요, 다른 방법을 시도해 봅시다. 각 연도에 대해 새 열을 추가해 봅시다:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

이 방법은 행 중복을 피하지만 몇 가지 다른 문제를 야기합니다. 새 연도가 생길 때마다 테이블 구조를 수정해야 합니다. 또한 데이터가 커질수록 연도를 열로 두는 것은 값을 검색하고 계산하는 데 더 어려움을 줍니다.

이 때문에 여러 테이블과 관계가 필요합니다. 데이터를 분리함으로써 중복을 피하고 데이터를 다루는 방식에 더 큰 유연성을 가질 수 있습니다.

## 관계의 개념

데이터로 돌아가서 어떻게 분리할지 결정해 봅시다. 도시의 이름과 국가를 저장하고 싶으므로, 이는 아마도 하나의 테이블에 가장 적합할 것입니다.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

하지만 다음 테이블을 만들기 전에 각 도시를 참조하는 방법을 알아야 합니다. 식별자, ID 또는 (기술적 데이터베이스 용어로) 기본 키가 필요합니다. 기본 키는 테이블에서 특정 행 하나를 식별하는 데 사용되는 값입니다. 이것이 값 자체(예: 도시 이름)를 기반으로 할 수도 있지만, 거의 항상 숫자나 다른 식별자여야 합니다. ID가 변경되면 관계가 깨지기 때문입니다. 대부분의 경우 기본 키 또는 ID는 자동 생성된 숫자일 것입니다.

> ✅ 기본 키는 종종 PK로 약칭됩니다

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ 이 강의에서는 "id"와 "기본 키"라는 용어를 혼용해서 사용합니다. 이 개념은 나중에 탐색할 DataFrame에도 적용됩니다. DataFrame은 "기본 키"라는 용어를 사용하지 않지만, 동작 방식은 매우 유사합니다.

cities 테이블을 만들었으니 강수량을 저장해 봅시다. 도시의 전체 정보를 중복하는 대신 ID를 사용할 수 있습니다. 새로 만든 테이블에도 *id* 열이 있어야 하며, 모든 테이블에는 id 또는 기본 키가 있어야 합니다.

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

새로 만든 **rainfall** 테이블 안의 **city_id** 열을 주목하세요. 이 열은 **cities** 테이블의 ID를 참조하는 값을 포함합니다. 기술적 관계형 데이터 용어로 이것을 **외래 키**라고 하며, 다른 테이블의 기본 키입니다. 단순히 참조나 포인터라고 생각하면 됩니다. **city_id** 1은 도쿄를 참조합니다.

> [!NOTE] 
> 외래 키는 종종 FK로 약칭됩니다

## 데이터 검색

데이터가 두 테이블로 분리되었으니, 어떻게 데이터를 검색하는지 궁금할 수 있습니다. MySQL, SQL Server, Oracle과 같은 관계형 데이터베이스를 사용하는 경우, SQL(Structured Query Language)이라는 언어를 사용할 수 있습니다. SQL(때로는 sequel로 발음)은 관계형 데이터베이스에서 데이터를 검색하고 수정하는 데 사용되는 표준 언어입니다.

데이터를 검색하려면 `SELECT` 명령을 사용합니다. 기본적으로, 보고 싶은 열을 **선택(SELECT)** 하고, 그 열이 포함된 테이블을 **FROM** 절에 명시합니다. 도시 이름만 표시하고 싶다면 다음과 같이 할 수 있습니다:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT`는 열을 나열하는 곳이고, `FROM`은 테이블을 나열하는 곳입니다.

> [!NOTE] 
> SQL 구문은 대소문자를 구분하지 않으므로 `select`와 `SELECT`는 동일합니다. 하지만 사용하는 데이터베이스 종류에 따라 열과 테이블 이름은 대소문자를 구분할 수 있습니다. 따라서 프로그래밍에서는 모든 것을 대소문자 구분하는 것으로 간주하는 것이 모범 사례입니다. SQL 쿼리를 작성할 때는 키워드를 모두 대문자로 쓰는 것이 일반적인 관례입니다.

위 쿼리는 모든 도시를 표시합니다. 뉴질랜드에 있는 도시만 표시하고 싶다고 가정해 봅시다. 필터가 필요합니다. SQL 키워드는 `WHERE`이며, "어떤 조건이 참인 경우"를 의미합니다.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## 데이터 조인

지금까지는 단일 테이블에서 데이터를 검색했습니다. 이제 **cities**와 **rainfall** 두 테이블의 데이터를 함께 가져오고 싶습니다. 이것을 *조인*이라고 합니다. 두 테이블 사이에 연결 고리를 만들고, 각 테이블의 열 값을 맞춥니다.

예제에서는 **rainfall**의 **city_id** 열과 **cities**의 **city_id** 열을 맞춥니다. 이렇게 하면 강수량 값이 해당 도시와 연결됩니다. 수행할 조인 유형은 *내부(inner)* 조인으로, 다른 테이블과 일치하지 않는 행은 표시되지 않습니다. 이 경우 모든 도시에 강수량 데이터가 있으므로 모두 표시됩니다.

모든 도시의 2019년 강수량을 검색해 봅시다.

단계별로 진행합니다. 첫 번째 단계는 조인할 열을 지정하여 데이터를 연결하는 것입니다 - 앞서 강조한 **city_id**입니다.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

원하는 두 열을 강조 표시했고, **city_id**로 테이블을 조인하려는 사실도 표시했습니다. 이제 `WHERE` 문을 추가하여 2019년 데이터만 필터링할 수 있습니다.

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

관계형 데이터베이스는 정보를 여러 테이블로 나누고, 이를 다시 결합하여 표시 및 분석하는 데 중점을 둡니다. 이를 통해 계산 수행 및 데이터 조작에 높은 유연성을 제공합니다. 관계형 데이터베이스의 핵심 개념과 두 테이블 간 조인 수행 방법을 살펴보았습니다.

## 🚀 도전 과제

인터넷에는 다양한 관계형 데이터베이스가 있습니다. 위에서 배운 기술을 사용하여 데이터를 탐색해 보세요.

## 강의 후 퀴즈

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## 복습 및 자기 주도 학습

SQL 및 관계형 데이터베이스 개념을 계속 탐구할 수 있는 여러 자료가 [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum)에 있습니다.

- [관계형 데이터 개념 설명](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Transact-SQL로 쿼리 시작하기](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL은 SQL의 한 버전입니다)
- [Microsoft Learn의 SQL 콘텐츠](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## 과제

[공항 데이터 표시](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->