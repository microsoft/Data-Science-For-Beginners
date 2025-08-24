<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fcc7547171f4530f159676dd73ed772e",
  "translation_date": "2025-08-24T13:23:33+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/assignment.md",
  "language_code": "ko"
}
-->
# 답을 탐구하기

이 문서는 이전 수업의 [과제](../14-Introduction/assignment.md)에서 이어지는 내용으로, 데이터 세트를 간단히 살펴보았습니다. 이제 데이터를 더 깊이 분석해 보겠습니다.

다시 한번, 고객이 알고 싶어 하는 질문은 다음과 같습니다: **뉴욕시의 옐로우 택시 승객들은 겨울과 여름 중 어느 계절에 운전사에게 더 많은 팁을 줄까요?**

여러분의 팀은 데이터 과학 생애 주기의 [분석](README.md) 단계에 있으며, 데이터 세트에 대한 탐색적 데이터 분석(EDA)을 수행하는 책임이 있습니다. 여러분에게는 2019년 1월과 7월의 200건의 택시 거래 데이터를 포함한 노트북과 데이터 세트가 제공되었습니다.

## 지침

이 디렉터리에는 [노트북](../../../../4-Data-Science-Lifecycle/15-analyzing/assignment.ipynb)과 [택시 및 리무진 위원회](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets)의 데이터가 포함되어 있습니다. 데이터에 대한 추가 정보를 얻으려면 [데이터 사전](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)과 [사용자 가이드](https://www1.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf)를 참조하세요.

이번 수업에서 배운 몇 가지 기법을 사용하여 노트북에서 직접 EDA를 수행하고(필요하면 셀을 추가하세요) 다음 질문에 답해 보세요:

- 팁 금액에 영향을 미칠 수 있는 데이터의 다른 요인은 무엇인가요?
- 고객의 질문에 답하는 데 필요하지 않을 가능성이 높은 열은 무엇인가요?
- 지금까지 제공된 내용을 바탕으로, 데이터가 계절별 팁 행동에 대한 어떤 증거를 제공하나요?

## 평가 기준

우수 | 적절 | 개선 필요
--- | --- | ---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.