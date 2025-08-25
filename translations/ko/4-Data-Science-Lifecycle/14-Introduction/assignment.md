<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "564445c39ad29a491abcb9356fc4d47d",
  "translation_date": "2025-08-25T17:45:20+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/assignment.md",
  "language_code": "ko"
}
-->
# 데이터셋 평가하기

한 고객이 뉴욕시에서 택시 고객의 계절별 소비 습관을 조사하는 데 도움을 요청했습니다.

그들은 다음 질문에 대한 답을 알고 싶어합니다: **뉴욕시의 옐로우 택시 승객은 겨울과 여름 중 어느 계절에 운전사에게 더 많은 팁을 주는가?**

귀하의 팀은 데이터 과학 생명주기의 [캡처 단계](Readme.md#Capturing)에 있으며, 귀하는 데이터셋을 처리하는 책임을 맡고 있습니다. 탐색을 위해 노트북과 [데이터](../../../../data/taxi.csv)가 제공되었습니다.

이 디렉터리에는 [노트북](../../../../4-Data-Science-Lifecycle/14-Introduction/notebook.ipynb)이 있으며, 이는 [뉴욕시 택시 및 리무진 위원회](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets)의 옐로우 택시 여행 데이터를 Python을 사용하여 로드합니다. 택시 데이터 파일은 텍스트 편집기나 Excel과 같은 스프레드시트 소프트웨어에서도 열 수 있습니다.

## 지침

- 이 데이터셋의 데이터가 질문에 답하는 데 도움이 될 수 있는지 평가하세요.
- [뉴욕시 오픈 데이터 카탈로그](https://data.cityofnewyork.us/browse?sortBy=most_accessed&utf8=%E2%9C%93)를 탐색하여 고객의 질문에 답하는 데 잠재적으로 도움이 될 추가 데이터셋을 식별하세요.
- 문제를 더 잘 이해하고 명확히 하기 위해 고객에게 물어볼 3가지 질문을 작성하세요.

데이터에 대한 추가 정보를 얻으려면 [데이터셋 사전](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)과 [사용자 가이드](https://www1.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf)를 참조하세요.

## 평가 기준

우수 | 적절 | 개선 필요
--- | --- | --- |

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.