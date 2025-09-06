<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-06T08:01:47+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "pa"
}
-->
# ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ: "Azure ML SDK" ਦਾ ਤਰੀਕਾ

|![ [(@sketchthedocs)](https://sketchthedocs.dev) ਦੁਆਰਾ ਬਣਾਈ ਗਈ ਸਕੈਚਨੋਟ ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ: Azure ML SDK - _[@nitya](https://twitter.com/nitya) ਦੁਆਰਾ ਬਣਾਈ ਗਈ ਸਕੈਚਨੋਟ_ |

ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ:

- [ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ: "Azure ML SDK" ਦਾ ਤਰੀਕਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [ਪ੍ਰੀ-ਲੈਕਚਰ ਕਵਿਜ਼](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. ਪਰਿਚਯ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Azure ML SDK ਕੀ ਹੈ?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 ਹਾਰਟ ਫੇਲਿਅਰ ਪ੍ਰਡਿਕਸ਼ਨ ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਡਾਟਾਸੈਟ ਦਾ ਪਰਿਚਯ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Azure ML SDK ਨਾਲ ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Azure ML ਵਰਕਸਪੇਸ ਬਣਾਉਣਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 ਡਾਟਾਸੈਟ ਲੋਡ ਕਰਨਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 ਨੋਟਬੁੱਕ ਬਣਾਉਣਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 ਵਰਕਸਪੇਸ, ਐਕਸਪੇਰੀਮੈਂਟ, ਕੰਪਿਊਟ ਕਲਸਟਰ ਅਤੇ ਡਾਟਾਸੈਟ ਸੈਟਅਪ](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 AutoML ਕਨਫਿਗਰੇਸ਼ਨ ਅਤੇ ਟ੍ਰੇਨਿੰਗ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Azure ML SDK ਨਾਲ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਅਤੇ ਐਂਡਪੌਇੰਟ ਖਪਤ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਸੇਵ ਕਰਨਾ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 ਐਂਡਪੌਇੰਟ ਖਪਤ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 ਚੁਣੌਤੀ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [ਪੋਸਟ-ਲੈਕਚਰ ਕਵਿਜ਼](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [ਸਮੀਖਿਆ ਅਤੇ ਸਵੈ-ਅਧਿਐਨ](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [ਅਸਾਈਨਮੈਂਟ](../../../../5-Data-Science-In-Cloud/19-Azure)

## [ਪ੍ਰੀ-ਲੈਕਚਰ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. ਪਰਿਚਯ

### 1.1 Azure ML SDK ਕੀ ਹੈ?

ਡਾਟਾ ਸਾਇੰਟਿਸਟ ਅਤੇ AI ਡਿਵੈਲਪਰ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ Azure Machine Learning ਸੇਵਾ ਨਾਲ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਵਰਕਫਲੋ ਬਣਾਉਣ ਅਤੇ ਚਲਾਉਣ ਲਈ। ਤੁਸੀਂ ਇਸ ਸੇਵਾ ਨਾਲ ਕਿਸੇ ਵੀ Python ਐਨਵਾਇਰਮੈਂਟ ਵਿੱਚ ਇੰਟਰਐਕਟ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ Jupyter Notebooks, Visual Studio Code, ਜਾਂ ਤੁਹਾਡਾ ਮਨਪਸੰਦ Python IDE।

SDK ਦੇ ਮੁੱਖ ਖੇਤਰ ਸ਼ਾਮਲ ਹਨ:

- ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਐਕਸਪੇਰੀਮੈਂਟਾਂ ਵਿੱਚ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਡਾਟਾਸੈਟਾਂ ਦੇ ਜੀਵਨ ਚੱਕਰ ਦੀ ਖੋਜ, ਤਿਆਰੀ ਅਤੇ ਪ੍ਰਬੰਧਨ।
- ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਐਕਸਪੇਰੀਮੈਂਟਾਂ ਦੀ ਨਿਗਰਾਨੀ, ਲੌਗਿੰਗ ਅਤੇ ਆਯੋਜਨ ਲਈ ਕਲਾਉਡ ਸਰੋਤਾਂ ਦਾ ਪ੍ਰਬੰਧਨ।
- ਮਾਡਲਾਂ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਜਾਂ ਕਲਾਉਡ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰੇਨ ਕਰੋ, ਜਿਸ ਵਿੱਚ GPU-ਤੇਜ਼ ਮਾਡਲ ਟ੍ਰੇਨਿੰਗ ਸ਼ਾਮਲ ਹੈ।
- ਆਟੋਮੈਟਿਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰੋ, ਜੋ ਕਨਫਿਗਰੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਡਾਟਾ ਨੂੰ ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ। ਇਹ ਆਲਗੋਰਿਥਮ ਅਤੇ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਸੈਟਿੰਗਾਂ ਦੇ ਦੁਆਰਾ ਆਪਣੇ ਆਪ ਦੁਹਰਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਪ੍ਰਡਿਕਸ਼ਨ ਚਲਾਉਣ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਲੱਭ ਸਕੇ।
- ਵੈੱਬ ਸੇਵਾਵਾਂ ਨੂੰ ਡਿਪਲੌਇ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਟ੍ਰੇਨ ਕੀਤੇ ਮਾਡਲਾਂ ਨੂੰ RESTful ਸੇਵਾਵਾਂ ਵਿੱਚ ਬਦਲਿਆ ਜਾ ਸਕੇ ਜੋ ਕਿਸੇ ਵੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਖਪਤ ਕੀਤੀ ਜਾ ਸਕੇ।

[Azure Machine Learning SDK ਬਾਰੇ ਹੋਰ ਜਾਣੋ](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

[ਪਿਛਲੇ ਪਾਠ](../18-Low-Code/README.md) ਵਿੱਚ, ਅਸੀਂ ਦੇਖਿਆ ਕਿ ਕਿਵੇਂ ਇੱਕ ਮਾਡਲ ਨੂੰ Low code/No code ਤਰੀਕੇ ਨਾਲ ਟ੍ਰੇਨ, ਡਿਪਲੌਇ ਅਤੇ ਖਪਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਅਸੀਂ Heart Failure ਡਾਟਾਸੈਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Heart Failure ਪ੍ਰਡਿਕਸ਼ਨ ਮਾਡਲ ਬਣਾਇਆ। ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਬਿਲਕੁਲ ਉਹੀ ਕੰਮ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ ਪਰ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ।

![ਪ੍ਰੋਜੈਕਟ-ਸਕੀਮਾ](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 ਹਾਰਟ ਫੇਲਿਅਰ ਪ੍ਰਡਿਕਸ਼ਨ ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਡਾਟਾਸੈਟ ਦਾ ਪਰਿਚਯ

[ਇਥੇ](../18-Low-Code/README.md) ਹਾਰਟ ਫੇਲਿਅਰ ਪ੍ਰਡਿਕਸ਼ਨ ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਡਾਟਾਸੈਟ ਦਾ ਪਰਿਚਯ ਦੇਖੋ।

## 2. Azure ML SDK ਨਾਲ ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨਾ

### 2.1 Azure ML ਵਰਕਸਪੇਸ ਬਣਾਉਣਾ

ਸਰਲਤਾ ਲਈ, ਅਸੀਂ ਇੱਕ Jupyter Notebook 'ਤੇ ਕੰਮ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਵਰਕਸਪੇਸ ਅਤੇ ਇੱਕ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਵਰਕਸਪੇਸ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਸਿੱਧੇ ਸੈਕਸ਼ਨ 2.3 ਨੋਟਬੁੱਕ ਬਣਾਉਣ 'ਤੇ ਜਾ ਸਕਦੇ ਹੋ।

ਜੇ ਨਹੀਂ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [ਪਿਛਲੇ ਪਾਠ](../18-Low-Code/README.md) ਵਿੱਚ ਸੈਕਸ਼ਨ **2.1 Azure ML ਵਰਕਸਪੇਸ ਬਣਾਉਣਾ** ਵਿੱਚ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

### 2.2 ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ

[Azure ML ਵਰਕਸਪੇਸ](https://ml.azure.com/) ਵਿੱਚ ਜੋ ਅਸੀਂ ਪਹਿਲਾਂ ਬਣਾਇਆ ਸੀ, ਕੰਪਿਊਟ ਮੀਨੂ 'ਤੇ ਜਾਓ ਅਤੇ ਤੁਹਾਨੂੰ ਉਪਲਬਧ ਵੱਖ-ਵੱਖ ਕੰਪਿਊਟ ਸਰੋਤਾਂ ਦੇਖਣ ਨੂੰ ਮਿਲਣਗੇ।

![ਕੰਪਿਊਟ-ਇੰਸਟੈਂਸ-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

ਆਓ ਇੱਕ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਬਣਾਈਏ ਤਾਂ ਜੋ Jupyter Notebook ਪ੍ਰੋਵਿਜ਼ਨ ਕੀਤਾ ਜਾ ਸਕੇ।
1. + New ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ।
2. ਆਪਣੇ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਨੂੰ ਇੱਕ ਨਾਮ ਦਿਓ।
3. ਆਪਣੇ ਵਿਕਲਪ ਚੁਣੋ: CPU ਜਾਂ GPU, VM ਸਾਈਜ਼ ਅਤੇ ਕੋਰ ਨੰਬਰ।
4. Create ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ।

ਵਧਾਈਆਂ, ਤੁਸੀਂ ਸਿਰਫ ਇੱਕ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਬਣਾਇਆ ਹੈ! ਅਸੀਂ ਇਸ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ ਵਰਤੋਂ [ਨੋਟਬੁੱਕ ਬਣਾਉਣ ਦੇ ਸੈਕਸ਼ਨ](../../../../5-Data-Science-In-Cloud/19-Azure) ਵਿੱਚ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ।

### 2.3 ਡਾਟਾਸੈਟ ਲੋਡ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ ਹਾਲੇ ਤੱਕ ਡਾਟਾਸੈਟ ਅੱਪਲੋਡ ਨਹੀਂ ਕੀਤਾ ਹੈ, ਤਾਂ [ਪਿਛਲੇ ਪਾਠ](../18-Low-Code/README.md) ਵਿੱਚ ਸੈਕਸ਼ਨ **2.3 ਡਾਟਾਸੈਟ ਲੋਡ ਕਰਨਾ** ਨੂੰ ਵੇਖੋ।

### 2.4 ਨੋਟਬੁੱਕ ਬਣਾਉਣਾ

> **_ਨੋਟ:_** ਅਗਲੇ ਕਦਮ ਲਈ ਤੁਸੀਂ ਜਾਂ ਤਾਂ ਨਵਾਂ ਨੋਟਬੁੱਕ ਸ਼ੁਰੂ ਤੋਂ ਬਣਾਉਣ ਦਾ ਚੋਣ ਕਰ ਸਕਦੇ ਹੋ, ਜਾਂ [ਅਸੀਂ ਬਣਾਇਆ ਨੋਟਬੁੱਕ](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) ਨੂੰ ਆਪਣੇ Azure ML Studio ਵਿੱਚ ਅੱਪਲੋਡ ਕਰ ਸਕਦੇ ਹੋ। ਇਸਨੂੰ ਅੱਪਲੋਡ ਕਰਨ ਲਈ, ਸਿਰਫ "Notebook" ਮੀਨੂ 'ਤੇ ਕਲਿਕ ਕਰੋ ਅਤੇ ਨੋਟਬੁੱਕ ਅੱਪਲੋਡ ਕਰੋ।

ਨੋਟਬੁੱਕ ਡਾਟਾ ਸਾਇੰਸ ਪ੍ਰਕਿਰਿਆ ਦਾ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਹਿੱਸਾ ਹਨ। ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ Exploratory Data Analysis (EDA) ਕਰਨ ਲਈ, ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨ ਲਈ ਕਲਸਟਰ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ, ਜਾਂ ਐਂਡਪੌਇੰਟ ਡਿਪਲੌਇ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

ਨੋਟਬੁੱਕ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਇੱਕ ਕੰਪਿਊਟ ਨੋਡ ਦੀ ਲੋੜ ਹੈ ਜੋ Jupyter Notebook ਇੰਸਟੈਂਸ ਨੂੰ ਸਰਵ ਕਰ ਰਿਹਾ ਹੈ। ਵਾਪਸ [Azure ML ਵਰਕਸਪੇਸ](https://ml.azure.com/) 'ਤੇ ਜਾਓ ਅਤੇ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ 'ਤੇ ਕਲਿਕ ਕਰੋ। ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ ਸੂਚੀ ਵਿੱਚ ਤੁਹਾਨੂੰ [ਅਸੀਂ ਪਹਿਲਾਂ ਬਣਾਇਆ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ](../../../../5-Data-Science-In-Cloud/19-Azure) ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ।

1. Applications ਸੈਕਸ਼ਨ ਵਿੱਚ, Jupyter ਵਿਕਲਪ 'ਤੇ ਕਲਿਕ ਕਰੋ।
2. "Yes, I understand" ਬਾਕਸ 'ਤੇ ਟਿਕ ਕਰੋ ਅਤੇ Continue ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ।
![ਨੋਟਬੁੱਕ-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. ਇਹ ਤੁਹਾਡੇ Jupyter Notebook ਇੰਸਟੈਂਸ ਨਾਲ ਇੱਕ ਨਵਾਂ ਬ੍ਰਾਊਜ਼ਰ ਟੈਬ ਖੋਲ੍ਹੇਗਾ। "New" ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰਕੇ ਨੋਟਬੁੱਕ ਬਣਾਓ।

![ਨੋਟਬੁੱਕ-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

ਹੁਣ ਜਦੋਂ ਸਾਡੇ ਕੋਲ ਨੋਟਬੁੱਕ ਹੈ, ਅਸੀਂ Azure ML SDK ਨਾਲ ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਾਂ।

### 2.5 ਮਾਡਲ ਟ੍ਰੇਨ ਕਰਨਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਜੇ ਤੁਹਾਨੂੰ ਕਦੇ ਵੀ ਕੋਈ ਸ਼ੱਕ ਹੋਵੇ, ਤਾਂ [Azure ML SDK ਡੌਕੂਮੈਂਟੇਸ਼ਨ](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ਨੂੰ ਵੇਖੋ। ਇਸ ਵਿੱਚ ਉਹ ਸਾਰੀਆਂ ਜਾਣਕਾਰੀਆਂ ਹਨ ਜੋ ਅਸੀਂ ਇਸ ਪਾਠ ਵਿੱਚ ਦੇਖਣ ਜਾ ਰਹੇ ਮੌਡੀਊਲਾਂ ਨੂੰ ਸਮਝਣ ਲਈ ਲੋੜੀਂਦੀਆਂ ਹਨ।

#### 2.5.1 ਵਰਕਸਪੇਸ, ਐਕਸਪੇਰੀਮੈਂਟ, ਕੰਪਿਊਟ ਕਲਸਟਰ ਅਤੇ ਡਾਟਾਸੈਟ ਸੈਟਅਪ

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ `workspace` ਨੂੰ ਕਨਫਿਗਰੇਸ਼ਨ ਫਾਈਲ ਤੋਂ ਲੋਡ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

ਇਹ `Workspace` ਕਿਸਮ ਦਾ ਇੱਕ ਆਬਜੈਕਟ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਵਰਕਸਪੇਸ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਫਿਰ ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ `experiment` ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੈ:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```

ਵਰਕਸਪੇਸ ਤੋਂ ਇੱਕ ਐਕਸਪੇਰੀਮੈਂਟ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਜਾਂ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਐਕਸਪੇਰੀਮੈਂਟ ਦਾ ਨਾਮ ਦੀ ਬੇਨਤੀ ਕਰਦੇ ਹੋ। ਐਕਸਪੇਰੀਮੈਂਟ ਦਾ ਨਾਮ 3-36 ਅੱਖਰਾਂ ਦਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਇੱਕ ਅੱਖਰ ਜਾਂ ਨੰਬਰ ਨਾਲ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਅਤੇ ਸਿਰਫ ਅੱਖਰਾਂ, ਨੰਬਰਾਂ, ਅੰਡਰਸਕੋਰ ਅਤੇ ਡੈਸ਼ ਸ਼ਾਮਲ ਕਰ ਸਕਦਾ ਹੈ। ਜੇ ਵਰਕਸਪੇਸ ਵਿੱਚ ਐਕਸਪੇਰੀਮੈਂਟ ਨਹੀਂ ਮਿਲਦਾ, ਤਾਂ ਇੱਕ ਨਵਾਂ ਐਕਸਪੇਰੀਮੈਂਟ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ।

ਹੁਣ ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰੇਨਿੰਗ ਲਈ ਇੱਕ ਕੰਪਿਊਟ ਕਲਸਟਰ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ ਕਦਮ ਕੁਝ ਮਿੰਟ ਲੈ ਸਕਦਾ ਹੈ।

```python
from azureml.core.compute import AmlCompute

aml_name = "heart-f-cluster"
try:
    aml_compute = AmlCompute(ws, aml_name)
    print('Found existing AML compute context.')
except:
    print('Creating new AML compute context.')
    aml_config = AmlCompute.provisioning_configuration(vm_size = "Standard_D2_v2", min_nodes=1, max_nodes=3)
    aml_compute = AmlCompute.create(ws, name = aml_name, provisioning_configuration = aml_config)
    aml_compute.wait_for_completion(show_output = True)

cts = ws.compute_targets
compute_target = cts[aml_name]
```

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਵਰਕਸਪੇਸ ਤੋਂ ਡਾਟਾਸੈਟ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```

#### 2.5.2 AutoML ਕਨਫਿਗਰੇਸ਼ਨ ਅਤੇ ਟ੍ਰੇਨਿੰਗ

AutoML ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟ ਕਰਨ ਲਈ, [AutoMLConfig ਕਲਾਸ](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ਦੀ ਵਰਤੋਂ ਕਰੋ।

ਜਿਵੇਂ ਕਿ ਡੌਕ ਵਿੱਚ ਵਰਣਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਇਸ ਵਿੱਚ ਬਹੁਤ ਸਾਰੇ ਪੈਰਾਮੀਟਰ ਹਨ ਜਿਨ੍ਹਾਂ ਨਾਲ ਤੁਸੀਂ ਖੇਡ ਸਕਦੇ ਹੋ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ, ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ:

- `experiment_timeout_minutes`: ਅਧਿਕਤਮ ਸਮਾਂ (ਮਿੰਟਾਂ ਵਿੱਚ) ਜੋ ਐਕਸਪੇਰੀਮੈਂਟ ਨੂੰ ਚਲਾਉਣ ਦੀ ਆਗਿਆ ਹੈ।
- `max_concurrent_iterations`: ਐਕਸਪੇਰੀਮੈਂਟ ਲਈ ਅਧਿਕਤਮ ਸੰਖਿਆ ਜੋ ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਚਲ ਸਕਦੀ ਹੈ।
- `primary_metric`: ਐਕਸਪੇਰੀਮੈਂਟ ਦੀ ਸਥਿਤੀ ਨੂੰ ਨਿਰਧਾਰਤ ਕਰਨ ਲਈ ਮੁੱਖ ਮਾਪ।
- `compute_target`: Automated Machine Learning ਐਕਸਪੇਰੀਮੈਂਟ ਚਲਾਉਣ ਲਈ Azure Machine Learning ਕੰਪਿਊਟ ਟਾਰਗਟ।
- `task`: ਚਲਾਉਣ ਲਈ ਟਾਸਕ ਦੀ ਕਿਸਮ। ਮੁੱਲ 'classification', 'regression', ਜਾਂ 'forecasting' ਹੋ ਸਕਦੇ ਹਨ।
- `training_data`: ਐਕਸਪੇਰੀਮੈਂਟ ਵਿੱਚ ਵਰਤਣ ਲਈ ਟ੍ਰੇਨਿੰਗ ਡਾਟਾ।
- `label_column_name`: ਲੇਬਲ ਕਾਲਮ ਦਾ ਨਾਮ।
- `path`: Azure Machine Learning ਪ੍ਰੋਜੈਕਟ ਫੋਲਡਰ ਦਾ ਪੂਰਾ ਪਾਥ।
- `enable_early_stopping`: ਜੇ ਸਕੋਰ ਛੋਟੇ ਸਮੇਂ ਵਿੱਚ ਸੁਧਾਰ ਨਹੀਂ ਕਰ ਰਿਹਾ, ਤਾਂ ਸ਼ੁਰੂਆਤੀ ਰੋਕਥਾਮ ਨੂੰ ਯੋਗ ਕਰੋ।
- `featurization`: ਕੀ ਫੀਚਰਾਈਜ਼ੇਸ਼ਨ ਕਦਮ ਆਪਣੇ ਆਪ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।
- `debug_log`: ਡਿਬੱਗ ਜਾਣਕਾਰੀ ਲਿਖਣ ਲਈ ਲੌਗ ਫਾਈਲ।

```python
from azureml.train.automl import AutoMLConfig

project_folder = './aml-project'

automl_settings = {
    "experiment_timeout_minutes": 20,
    "max_concurrent_iterations": 3,
    "primary_metric" : 'AUC_weighted'
}

automl_config = AutoMLConfig(compute_target=compute_target,
                             task = "classification",
                             training_data=dataset,
                             label_column_name="DEATH_EVENT",
                             path = project_folder,  
                             enable_early_stopping= True,
                             featurization= 'auto',
                             debug_log = "automl_errors.log",
                             **automl_settings
                            )
```

ਹੁਣ ਜਦੋਂ ਤੁਹਾਡੀ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟ ਹੈ, ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਟ੍ਰੇਨ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਕਦਮ ਤੁਹਾਡੇ ਕਲਸਟਰ ਸਾਈਜ਼ ਦੇ ਅਨੁਸਾਰ ਇੱਕ ਘੰਟੇ ਤੱਕ ਲੈ ਸਕਦਾ ਹੈ।

```python
remote_run = experiment.submit(automl_config)
```

ਤੁਸੀਂ RunDetails ਵਿਜਟ ਚਲਾ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਵੱਖ-ਵੱਖ ਐਕਸਪੇਰੀਮੈਂਟਾਂ ਨੂੰ ਦਿਖਾਇਆ ਜਾ ਸਕੇ।

```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```

## 3. Azure ML SDK ਨਾਲ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਅਤੇ ਐਂਡਪੌਇੰਟ ਖਪਤ

### 3.1 ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਸੇਵ ਕਰਨਾ

`remote_run` [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ਕਿਸਮ ਦਾ ਇੱਕ ਆਬਜੈਕਟ ਹੈ। ਇਸ ਆਬਜੈਕਟ ਵਿੱਚ `get
```python
response = aci_service.run(input_data=test_sample)
response
```  
ਇਸ ਦਾ ਨਤੀਜਾ `'{"result": [false]}'` ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਜੋ ਮਰੀਜ਼ ਦੀ ਜਾਣਕਾਰੀ ਅਸੀਂ ਐਂਡਪੌਇੰਟ ਨੂੰ ਭੇਜੀ ਸੀ, ਉਸ ਨੇ `false` ਦੀ ਪੇਸ਼ਗੋਈ ਕੀਤੀ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਸ ਵਿਅਕਤੀ ਨੂੰ ਦਿਲ ਦਾ ਦੌਰਾ ਪੈਣ ਦੀ ਸੰਭਾਵਨਾ ਨਹੀਂ ਹੈ।  

ਮੁਬਾਰਕਾਂ! ਤੁਸੀਂ Azure ML SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure ML 'ਤੇ ਮਾਡਲ ਤਿਆਰ ਕੀਤਾ, ਡਿਪਲੌਇ ਕੀਤਾ ਅਤੇ ਕਨਜ਼ਿਊਮ ਕੀਤਾ!  

> **_NOTE:_** ਜਦੋਂ ਤੁਸੀਂ ਪ੍ਰੋਜੈਕਟ ਪੂਰਾ ਕਰ ਲਓ, ਤਾਂ ਸਾਰੇ ਸਰੋਤਾਂ ਨੂੰ ਮਿਟਾਉਣਾ ਨਾ ਭੁੱਲੋ।  

## 🚀 ਚੁਣੌਤੀ  

SDK ਰਾਹੀਂ ਹੋਰ ਬਹੁਤ ਕੁਝ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਪਰ ਅਫਸੋਸ, ਅਸੀਂ ਇਸ ਪਾਠ ਵਿੱਚ ਸਾਰਾ ਕੁਝ ਨਹੀਂ ਦੇਖ ਸਕਦੇ। ਪਰ ਚੰਗੀ ਖਬਰ ਇਹ ਹੈ ਕਿ SDK ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਨੂੰ ਸਮਝਣ ਦੀ ਯੋਗਤਾ ਤੁਹਾਨੂੰ ਆਪਣੇ ਆਪ ਬਹੁਤ ਅੱਗੇ ਲੈ ਜਾ ਸਕਦੀ ਹੈ। Azure ML SDK ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਨੂੰ ਦੇਖੋ ਅਤੇ `Pipeline` ਕਲਾਸ ਨੂੰ ਲੱਭੋ ਜੋ ਤੁਹਾਨੂੰ ਪਾਈਪਲਾਈਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਪਾਈਪਲਾਈਨ ਕਦਮਾਂ ਦਾ ਇਕ ਸੰਗ੍ਰਹਿ ਹੈ ਜੋ ਵਰਕਫਲੋ ਵਜੋਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।  

**ਸੁਝਾਅ:** [SDK ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 'ਤੇ ਜਾਓ ਅਤੇ ਖੋਜ ਬਾਰ ਵਿੱਚ "Pipeline" ਵਰਗੇ ਕੀਵਰਡ ਟਾਈਪ ਕਰੋ। ਤੁਹਾਨੂੰ ਖੋਜ ਦੇ ਨਤੀਜਿਆਂ ਵਿੱਚ `azureml.pipeline.core.Pipeline` ਕਲਾਸ ਮਿਲਣੀ ਚਾਹੀਦੀ ਹੈ।  

## [ਪਾਠ-ਪ੍ਰਚਾਰ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/37)  

## ਸਮੀਖਿਆ ਅਤੇ ਸਵੈ ਅਧਿਐਨ  

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖਿਆ ਕਿ ਕਿਵੇਂ Azure ML SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਲਾਉਡ ਵਿੱਚ ਦਿਲ ਦੇ ਦੌਰੇ ਦੇ ਖਤਰੇ ਦੀ ਪੇਸ਼ਗੋਈ ਕਰਨ ਲਈ ਮਾਡਲ ਨੂੰ ਤਿਆਰ, ਡਿਪਲੌਇ ਅਤੇ ਕਨਜ਼ਿਊਮ ਕਰਨਾ ਹੈ। ਇਸ [ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ਨੂੰ ਚੈੱਕ ਕਰੋ ਜੇ ਤੁਸੀਂ Azure ML SDK ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲੈਣਾ ਚਾਹੁੰਦੇ ਹੋ। Azure ML SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣਾ ਮਾਡਲ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।  

## ਅਸਾਈਨਮੈਂਟ  

[Azure ML SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾ ਸਾਇੰਸ ਪ੍ਰੋਜੈਕਟ](assignment.md)  

---

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।