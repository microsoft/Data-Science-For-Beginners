<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-06T08:15:44+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "pa"
}
-->
# ਵੰਡਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਮਾਨ ਕਰਨਾ

|![ [(@sketchthedocs)] ਦੁਆਰਾ ਸਕੈਚਨੋਟ](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| ਵੰਡਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਮਾਨ ਕਰਨਾ - _[@nitya](https://twitter.com/nitya) ਦੁਆਰਾ ਸਕੈਚਨੋਟ_ |

ਪਿਛਲੇ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਮਿਨੇਸੋਟਾ ਦੇ ਪੰਛੀਆਂ ਦੇ ਡਾਟਾਸੈਟ ਬਾਰੇ ਕੁਝ ਦਿਲਚਸਪ ਤੱਥ ਸਿੱਖੇ। ਤੁਸੀਂ ਆਉਟਲਾਇਰਜ਼ ਨੂੰ ਦ੍ਰਿਸ਼ਮਾਨ ਕਰਕੇ ਕੁਝ ਗਲਤ ਡਾਟਾ ਲੱਭਿਆ ਅਤੇ ਪੰਛੀ ਸ਼੍ਰੇਣੀਆਂ ਦੇ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਦੇ ਅੰਤਰਾਂ ਨੂੰ ਦੇਖਿਆ।

## [ਪ੍ਰੀ-ਲੈਕਚਰ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## ਪੰਛੀਆਂ ਦੇ ਡਾਟਾਸੈਟ ਦੀ ਖੋਜ ਕਰੋ

ਡਾਟਾ ਵਿੱਚ ਖੋਜ ਕਰਨ ਦਾ ਇੱਕ ਹੋਰ ਤਰੀਕਾ ਇਸ ਦੀ ਵੰਡ ਦੇਖਣਾ ਹੈ, ਜਾਂ ਡਾਟਾ ਕਿਸੇ ਧੁਰੇ 'ਤੇ ਕਿਵੇਂ ਸੰਗਠਿਤ ਹੈ। ਉਦਾਹਰਣ ਲਈ, ਸ਼ਾਇਦ ਤੁਸੀਂ ਮਿਨੇਸੋਟਾ ਦੇ ਪੰਛੀਆਂ ਲਈ ਵੱਧ ਤੋਂ ਵੱਧ ਪੰਖਾਂ ਦੇ ਫੈਲਾਅ ਜਾਂ ਵੱਧ ਤੋਂ ਵੱਧ ਸਰੀਰਕ ਭਾਰ ਦੀ ਆਮ ਵੰਡ ਬਾਰੇ ਜਾਣਨਾ ਚਾਹੁੰਦੇ ਹੋ। 

ਆਓ ਇਸ ਡਾਟਾਸੈਟ ਵਿੱਚ ਡਾਟਾ ਦੀਆਂ ਵੰਡਾਂ ਬਾਰੇ ਕੁਝ ਤੱਥ ਖੋਜੀਏ। ਇਸ ਪਾਠ ਫੋਲਡਰ ਦੇ ਰੂਟ ਵਿੱਚ _notebook.ipynb_ ਫਾਈਲ ਵਿੱਚ Pandas, Matplotlib, ਅਤੇ ਆਪਣਾ ਡਾਟਾ ਇੰਪੋਰਟ ਕਰੋ:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | ਨਾਮ                          | ਵਿਗਿਆਨਕ ਨਾਮ           | ਸ਼੍ਰੇਣੀ               | ਕ੍ਰਮ         | ਪਰਿਵਾਰ   | ਜਨਸ        | ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ      | ਘੱਟੋ-ਘੱਟ ਲੰਬਾਈ | ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ | ਘੱਟੋ-ਘੱਟ ਸਰੀਰਕ ਭਾਰ | ਵੱਧ ਤੋਂ ਵੱਧ ਸਰੀਰਕ ਭਾਰ | ਘੱਟੋ-ਘੱਟ ਪੰਖਾਂ ਦਾ ਫੈਲਾਅ | ਵੱਧ ਤੋਂ ਵੱਧ ਪੰਖਾਂ ਦਾ ਫੈਲਾਅ |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | ਬਲੈਕ-ਬੈਲੀਡ ਵਿਸਲਿੰਗ-ਡੱਕ     | Dendrocygna autumnalis | ਬਤਖਾਂ/ਹੰਸ/ਜਲ ਪੰਛੀ    | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | ਫੁਲਵਸ ਵਿਸਲਿੰਗ-ਡੱਕ           | Dendrocygna bicolor    | ਬਤਖਾਂ/ਹੰਸ/ਜਲ ਪੰਛੀ    | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | ਸਨੋ ਗੂਸ                     | Anser caerulescens     | ਬਤਖਾਂ/ਹੰਸ/ਜਲ ਪੰਛੀ    | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | ਰੌਸ ਦਾ ਗੂਸ                  | Anser rossii           | ਬਤਖਾਂ/ਹੰਸ/ਜਲ ਪੰਛੀ    | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | ਵੱਡਾ ਵ੍ਹਾਈਟ-ਫਰੰਟਡ ਗੂਸ      | Anser albifrons        | ਬਤਖਾਂ/ਹੰਸ/ਜਲ ਪੰਛੀ    | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |


ਆਮ ਤੌਰ 'ਤੇ, ਤੁਸੀਂ ਡਾਟਾ ਦੀ ਵੰਡ ਨੂੰ ਛੇਤੀ ਨਾਲ ਸਕੈਟਰ ਪਲਾਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਦੇਖ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਪਿਛਲੇ ਪਾਠ ਵਿੱਚ ਕੀਤਾ ਸੀ:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![ਕ੍ਰਮ ਪ੍ਰਤੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

ਇਹ ਪੰਛੀ ਦੇ ਕ੍ਰਮ ਪ੍ਰਤੀ ਸਰੀਰਕ ਲੰਬਾਈ ਦੀ ਆਮ ਵੰਡ ਦਾ ਝਲਕ ਦਿੰਦਾ ਹੈ, ਪਰ ਇਹ ਸੱਚੀ ਵੰਡਾਂ ਨੂੰ ਦਿਖਾਉਣ ਦਾ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕਾ ਨਹੀਂ ਹੈ। ਇਹ ਕੰਮ ਆਮ ਤੌਰ 'ਤੇ ਹਿਸਟੋਗ੍ਰਾਮ ਬਣਾਉਣ ਦੁਆਰਾ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
## ਹਿਸਟੋਗ੍ਰਾਮ ਨਾਲ ਕੰਮ ਕਰਨਾ

Matplotlib ਹਿਸਟੋਗ੍ਰਾਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾ ਵੰਡ ਨੂੰ ਦ੍ਰਿਸ਼ਮਾਨ ਕਰਨ ਦੇ ਬਹੁਤ ਵਧੀਆ ਤਰੀਕੇ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਇਸ ਕਿਸਮ ਦਾ ਚਾਰਟ ਇੱਕ ਬਾਰ ਚਾਰਟ ਵਾਂਗ ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ ਵੰਡ ਬਾਰਾਂ ਦੇ ਉਤਾਰ-ਚੜ੍ਹਾਵ ਦੁਆਰਾ ਵੇਖੀ ਜਾ ਸਕਦੀ ਹੈ। ਹਿਸਟੋਗ੍ਰਾਮ ਬਣਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਸੰਖਿਆਤਮਕ ਡਾਟਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਹਿਸਟੋਗ੍ਰਾਮ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਚਾਰਟ ਨੂੰ 'hist' ਕਿਸਮ ਦੇ ਰੂਪ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ ਪਲਾਟ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਚਾਰਟ ਪੂਰੇ ਡਾਟਾਸੈਟ ਦੇ ਸੰਖਿਆਤਮਕ ਡਾਟਾ ਦੀ ਵੰਡ ਦਿਖਾਉਂਦਾ ਹੈ। ਡਾਟਾ ਦੇ ਐਰੇ ਨੂੰ ਛੋਟੇ ਬਿਨਾਂ ਵਿੱਚ ਵੰਡ ਕੇ, ਇਹ ਡਾਟਾ ਦੇ ਮੁੱਲਾਂ ਦੀ ਵੰਡ ਦਿਖਾ ਸਕਦਾ ਹੈ:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![ਪੂਰੇ ਡਾਟਾਸੈਟ 'ਤੇ ਵੰਡ](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

ਜਿਵੇਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ, ਇਸ ਡਾਟਾਸੈਟ ਵਿੱਚ ਮੌਜੂਦ 400+ ਪੰਛੀਆਂ ਵਿੱਚੋਂ ਜ਼ਿਆਦਾਤਰ ਦਾ ਵੱਧ ਤੋਂ ਵੱਧ ਸਰੀਰਕ ਭਾਰ 2000 ਤੋਂ ਘੱਟ ਹੈ। `bins` ਪੈਰਾਮੀਟਰ ਨੂੰ ਵਧੇਰੇ ਸੰਖਿਆ ਵਿੱਚ ਬਦਲ ਕੇ ਡਾਟਾ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ, ਜਿਵੇਂ ਕਿ 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![ਵੱਡੇ ਬਿਨ ਪੈਰਾਮੀਟਰ ਨਾਲ ਪੂਰੇ ਡਾਟਾਸੈਟ 'ਤੇ ਵੰਡ](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

ਇਹ ਚਾਰਟ ਵੰਡ ਨੂੰ ਥੋੜ੍ਹਾ ਹੋਰ ਵਿਸਤ੍ਰਿਤ ਢੰਗ ਨਾਲ ਦਿਖਾਉਂਦਾ ਹੈ। ਇੱਕ ਚਾਰਟ ਜੋ ਖੱਬੇ ਵੱਲ ਘੱਟ ਝੁਕਿਆ ਹੋਵੇ, ਉਸ ਨੂੰ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਜੇਕਰ ਤੁਸੀਂ ਸਿਰਫ਼ ਦਿੱਤੇ ਗਏ ਰੇਂਜ ਦੇ ਅੰਦਰ ਡਾਟਾ ਚੁਣੋ:

ਆਪਣੇ ਡਾਟਾ ਨੂੰ ਫਿਲਟਰ ਕਰੋ ਤਾਂ ਜੋ ਸਿਰਫ਼ ਉਹ ਪੰਛੀ ਮਿਲਣ ਜਿਨ੍ਹਾਂ ਦਾ ਸਰੀਰਕ ਭਾਰ 60 ਤੋਂ ਘੱਟ ਹੈ, ਅਤੇ 40 `bins` ਦਿਖਾਓ:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![ਫਿਲਟਰ ਕੀਤਾ ਹਿਸਟੋਗ੍ਰਾਮ](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ ਕੁਝ ਹੋਰ ਫਿਲਟਰ ਅਤੇ ਡਾਟਾ ਪੌਇੰਟ ਅਜ਼ਮਾਓ। ਡਾਟਾ ਦੀ ਪੂਰੀ ਵੰਡ ਦੇਖਣ ਲਈ, `['MaxBodyMass']` ਫਿਲਟਰ ਨੂੰ ਹਟਾਓ ਤਾਂ ਜੋ ਲੇਬਲ ਕੀਤੀਆਂ ਵੰਡਾਂ ਦਿਖਾਈ ਜਾ ਸਕਣ।

ਹਿਸਟੋਗ੍ਰਾਮ ਵਿੱਚ ਕੁਝ ਸੁੰਦਰ ਰੰਗ ਅਤੇ ਲੇਬਲਿੰਗ ਸੁਧਾਰ ਵੀ ਹਨ ਜੋ ਅਜ਼ਮਾਏ ਜਾ ਸਕਦੇ ਹਨ:

ਦੋ ਵੰਡਾਂ ਦੇ ਰਿਸ਼ਤੇ ਦੀ ਤੁਲਨਾ ਕਰਨ ਲਈ ਇੱਕ 2D ਹਿਸਟੋਗ੍ਰਾਮ ਬਣਾਓ। ਆਓ `MaxBodyMass` ਅਤੇ `MaxLength` ਦੀ ਤੁਲਨਾ ਕਰੀਏ। Matplotlib ਇੱਕ ਚਮਕਦਾਰ ਰੰਗਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਮਿਲਨ ਦਿਖਾਉਣ ਦਾ ਇੱਕ ਅੰਦਰੂਨੀ ਤਰੀਕਾ ਪੇਸ਼ ਕਰਦਾ ਹੈ:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
ਇਹ ਦੋ ਤੱਤਾਂ ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਉਮੀਦਵਾਰ ਧੁਰੇ ਦੇ ਨਾਲ ਸੰਭਾਵਿਤ ਰਿਸ਼ਤਾ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇੱਕ ਖਾਸ ਤਾਕਤਵਰ ਸੰਮਿਲਨ ਬਿੰਦੂ ਹੈ:

![2D ਪਲਾਟ](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

ਹਿਸਟੋਗ੍ਰਾਮ ਸੰਖਿਆਤਮਕ ਡਾਟਾ ਲਈ ਮੂਲ ਰੂਪ ਵਿੱਚ ਚੰਗਾ ਕੰਮ ਕਰਦੇ ਹਨ। ਜੇਕਰ ਤੁਹਾਨੂੰ ਟੈਕਸਟ ਡਾਟਾ ਦੇ ਅਨੁਸਾਰ ਵੰਡਾਂ ਦੇਖਣ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ ਕੀ ਹੋਵੇਗਾ? 
## ਟੈਕਸਟ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾਸੈਟ ਲਈ ਵੰਡਾਂ ਦੀ ਖੋਜ ਕਰੋ 

ਇਸ ਡਾਟਾਸੈਟ ਵਿੱਚ ਪੰਛੀ ਦੀ ਸ਼੍ਰੇਣੀ ਅਤੇ ਇਸ ਦੇ ਜਨਸ, ਪ੍ਰਜਾਤੀ, ਅਤੇ ਪਰਿਵਾਰ ਦੇ ਨਾਲ-साथ ਇਸ ਦੀ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਬਾਰੇ ਚੰਗੀ ਜਾਣਕਾਰੀ ਸ਼ਾਮਲ ਹੈ। ਆਓ ਇਸ ਸੰਰਕਸ਼ਣ ਜਾਣਕਾਰੀ ਵਿੱਚ ਖੋਜ ਕਰੀਏ। ਪੰਛੀਆਂ ਦੀ ਵੰਡ ਉਨ੍ਹਾਂ ਦੀ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਦੇ ਅਨੁਸਾਰ ਕੀ ਹੈ?

> ✅ ਡਾਟਾਸੈਟ ਵਿੱਚ, ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਨੂੰ ਵੇਰਵਾ ਦੇਣ ਲਈ ਕਈ ਸੰਖੇਪ ਸ਼ਬਦ ਵਰਤੇ ਗਏ ਹਨ। ਇਹ ਸੰਖੇਪ ਸ਼ਬਦ [IUCN Red List Categories](https://www.iucnredlist.org/) ਤੋਂ ਆਉਂਦੇ ਹਨ, ਇੱਕ ਸੰਗਠਨ ਜੋ ਪ੍ਰਜਾਤੀਆਂ ਦੀ ਸਥਿਤੀ ਨੂੰ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ।
> 
> - CR: ਗੰਭੀਰ ਖਤਰੇ ਵਿੱਚ
> - EN: ਖਤਰੇ ਵਿੱਚ
> - EX: ਲੁਪਤ
> - LC: ਘੱਟ ਚਿੰਤਾ
> - NT: ਨਜ਼ਦੀਕੀ ਖਤਰੇ ਵਿੱਚ
> - VU: ਸੰਵਿਦਨਸ਼ੀਲ

ਇਹ ਟੈਕਸਟ-ਅਧਾਰਿਤ ਮੁੱਲ ਹਨ ਇਸ ਲਈ ਤੁਹਾਨੂੰ ਹਿਸਟੋਗ੍ਰਾਮ ਬਣਾਉਣ ਲਈ ਇੱਕ ਰੂਪਾਂਤਰ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ। ਫਿਲਟਰ ਕੀਤਾ ਡਾਟਾਫਰੇਮ ਵਰਤ ਕੇ, ਇਸ ਦੀ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਨੂੰ ਘੱਟੋ-ਘੱਟ ਪੰਖਾਂ ਦੇ ਫੈਲਾਅ ਦੇ ਨਾਲ ਦਿਖਾਓ। ਤੁਸੀਂ ਕੀ ਦੇਖਦੇ ਹੋ? 

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![ਪੰਖਾਂ ਦਾ ਫੈਲਾਅ ਅਤੇ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

ਘੱਟੋ-ਘੱਟ ਪੰਖਾਂ ਦੇ ਫੈਲਾਅ ਅਤੇ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਦੇ ਵਿਚਕਾਰ ਕੋਈ ਵਧੀਆ ਸੰਬੰਧ ਨਹੀਂ ਦਿਖਾਈ ਦਿੰਦਾ। ਇਸ ਤਰੀਕੇ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾਸੈਟ ਦੇ ਹੋਰ ਤੱਤਾਂ ਦੀ ਜਾਂਚ ਕਰੋ। ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਫਿਲਟਰਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ। ਕੀ ਤੁਹਾਨੂੰ ਕੋਈ ਸੰਬੰਧ ਮਿਲਦਾ ਹੈ?

## ਡੈਂਸਿਟੀ ਪਲਾਟ

ਤੁਹਾਨੂੰ ਸ਼ਾਇਦ ਧਿਆਨ ਦਿੱਤਾ ਹੋਵੇਗਾ ਕਿ ਅਸੀਂ ਹੁਣ ਤੱਕ ਦੇਖੇ ਹਿਸਟੋਗ੍ਰਾਮ 'ਕਦਮਦਾਰ' ਹਨ ਅਤੇ ਇੱਕ ਆਰਕ ਵਿੱਚ ਸੁਚਾਰੂ ਤੌਰ 'ਤੇ ਨਹੀਂ ਵਹਿੰਦੇ। ਇੱਕ ਹੋਰ ਸੁਚਾਰੂ ਡੈਂਸਿਟੀ ਚਾਰਟ ਦਿਖਾਉਣ ਲਈ, ਤੁਸੀਂ ਡੈਂਸਿਟੀ ਪਲਾਟ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ।

ਡੈਂਸਿਟੀ ਪਲਾਟ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ, ਇੱਕ ਨਵੀਂ ਪਲਾਟਿੰਗ ਲਾਇਬ੍ਰੇਰੀ, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ਨਾਲ ਜਾਣੂ ਹੋਵੋ। 

Seaborn ਨੂੰ ਲੋਡ ਕਰਕੇ, ਇੱਕ ਬੁਨਿਆਦੀ ਡੈਂਸਿਟੀ ਪਲਾਟ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![ਡੈਂਸਿਟੀ ਪਲਾਟ](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਪਲਾਟ ਘੱਟੋ-ਘੱਟ ਪੰਖਾਂ ਦੇ ਫੈਲਾਅ ਡਾਟਾ ਲਈ ਪਿਛਲੇ ਪਲਾਟ ਨੂੰ ਗੂੰਜਦਾ ਹੈ; ਇਹ ਸਿਰਫ਼ ਥੋੜ੍ਹਾ ਹੋਰ ਸੁਚਾਰੂ ਹੈ। Seaborn ਦੀ ਦਸਤਾਵੇਜ਼ੀ ਦੇ ਅਨੁਸਾਰ, "ਹਿਸਟੋਗ੍ਰਾਮ ਦੇ ਮੁਕਾਬਲੇ, KDE ਇੱਕ ਪਲਾਟ ਪੈਦਾ ਕਰ ਸਕਦਾ ਹੈ ਜੋ ਘੱਟ ਭਰੇ ਹੋਏ ਅਤੇ ਹੋਰ ਵਿਆਖਿਆਯੋਗ ਹੁੰਦਾ ਹੈ, ਖਾਸ ਕਰਕੇ ਜਦੋਂ ਕਈ ਵੰਡਾਂ ਖਿੱਚੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਪਰ ਇਹ ਸੰਭਾਵਿਤ ਤੌਰ 'ਤੇ ਵਿਗੜਨ ਪੈਦਾ ਕਰ ਸਕਦਾ ਹੈ ਜੇਕਰ ਅਧਾਰਭੂਤ ਵੰਡ ਬਾਊਂਡ ਕੀਤੀ ਜਾਂ ਸੁਚਾਰੂ ਨਾ ਹੋਵੇ। ਇੱਕ ਹਿਸਟੋਗ੍ਰਾਮ ਵਾਂਗ, ਪ੍ਰਸਤੁਤੀ ਦੀ ਗੁਣਵੱਤਾ ਵੀ ਚੰਗੇ ਸੁਚਾਰੂ ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਚੋਣ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।" [source](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ਦੂਜੇ ਸ਼ਬਦਾਂ ਵਿੱਚ, ਆਉਟਲਾਇਰਜ਼ ਹਮੇਸ਼ਾ ਤੁਹਾਡੇ ਚਾਰਟਾਂ ਨੂੰ ਖਰਾਬ ਕਰਦੇ ਹਨ।

ਜੇਕਰ ਤੁਸੀਂ ਦੂਜੇ ਚਾਰਟ ਵਿੱਚ ਉਸ ਜੱਗਡ MaxBodyMass ਲਾਈਨ ਨੂੰ ਦੁਬਾਰਾ ਵੇਖਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਤਰੀਕੇ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਬਹੁਤ ਚੰਗੀ ਤਰ੍ਹਾਂ ਸੁਚਾਰੂ ਕਰ ਸਕਦੇ ਹੋ:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![ਸੁਚਾਰੂ ਸਰੀਰਕ ਭਾਰ ਲਾਈਨ](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

ਜੇਕਰ ਤੁਸੀਂ ਇੱਕ ਸੁਚਾਰੂ, ਪਰ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸੁਚਾਰੂ ਲਾਈਨ ਨਹੀਂ ਚਾਹੁੰਦੇ, ਤਾਂ `bw_adjust` ਪੈਰਾਮੀਟਰ ਨੂੰ ਸੋਧੋ: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![ਘੱਟ ਸੁਚਾਰੂ ਸਰੀਰਕ ਭਾਰ ਲਾਈਨ](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ ਇਸ ਕਿਸਮ ਦੇ ਪਲਾਟ ਲਈ ਉਪਲਬਧ ਪੈਰਾਮੀਟਰਾਂ ਬਾਰੇ ਪੜ੍ਹੋ ਅਤੇ ਪ੍ਰਯੋਗ ਕਰੋ!

ਇਸ ਕਿਸਮ ਦਾ ਚਾਰਟ ਸੁੰਦਰ ਤਰੀਕੇ ਨਾਲ ਵਿਆਖਿਆਯੋਗ ਦ੍ਰਿਸ਼ਮਾਨਤਾ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਣ ਲਈ, ਕੁਝ ਕੋਡ ਦੀਆਂ ਲਾਈਨਾਂ ਨਾਲ, ਤੁਸੀਂ ਪੰਛੀ ਦੇ ਕ੍ਰਮ ਪ੍ਰਤੀ ਵੱਧ ਤੋਂ ਵੱਧ ਸਰੀਰਕ ਭਾਰ ਦੀ ਡੈਂਸਿਟੀ ਦਿਖਾ ਸਕਦੇ ਹੋ:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![ਕ੍ਰਮ ਪ੍ਰਤੀ ਸਰੀਰਕ ਭਾਰ](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

ਤੁਸੀਂ ਇੱਕ ਚਾਰਟ ਵਿੱਚ ਕਈ ਵੈਰੀਏਬਲਾਂ ਦੀ ਡੈਂਸਿਟੀ ਨੂੰ ਮੈਪ ਕਰ ਸਕਦੇ ਹੋ। ਪੰਛੀ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਅਤੇ ਘੱਟੋ-ਘੱਟ ਲੰਬਾਈ ਦੀ ਸੰਰਕਸ਼ਣ ਸਥਿਤੀ ਦੇ ਮੁਕਾਬਲੇ ਜਾਂਚ ਕਰੋ:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![ਕਈ ਡੈਂਸਿਟੀਆਂ, ਸਪਰਿੰਪੋਜ਼ਡ](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

ਸ਼ਾਇਦ ਇਹ ਖੋਜ ਕਰਨ ਯੋਗ ਹੈ ਕਿ 'ਸੰਵਿਦਨਸ਼ੀਲ' ਪੰਛੀਆਂ ਦੀ ਲੰਬਾਈ ਦੇ ਅਨੁਸਾਰ ਕਲਸਟਰ ਮਹੱਤਵਪੂਰਨ ਹੈ ਜਾਂ ਨਹੀਂ।

## 🚀 ਚੁਣੌਤੀ

ਹਿਸਟੋਗ੍ਰਾਮ ਬੁਨਿਆਦੀ ਸਕੈਟਰਪਲਾਟ, ਬਾਰ ਚਾਰਟ, ਜਾਂ ਲਾਈਨ ਚਾਰਟ ਦੇ ਮੁਕਾਬਲੇ ਇੱਕ ਹੋਰ ਸੁਧਾਰਤ ਕਿਸਮ ਦਾ ਚਾਰਟ ਹੈ। ਇੰਟਰਨੈਟ 'ਤੇ ਜਾਓ ਅਤੇ ਹਿਸਟੋਗ੍ਰਾਮ ਦੀ ਵਰਤੋਂ ਦੇ ਚੰਗੇ ਉਦਾਹਰਣ ਲੱਭੋ। ਇਹ ਕਿਵੇਂ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਇਹ ਕੀ ਦਿਖਾਉਂਦੇ ਹਨ, ਅਤੇ ਇਹ ਕਿਹੜੇ ਖੇਤਰਾਂ ਜਾਂ ਖੋਜ ਦੇ ਖੇਤਰਾਂ ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਹਨ?

## [ਪੋਸਟ-ਲੈਕਚਰ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## ਸਮੀਖਿਆ ਅਤੇ ਸਵੈ ਅਧਿਐਨ

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ Matplotlib ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਅਤੇ ਹੋਰ ਸੁਧਾਰਤ ਚਾਰਟ ਦਿਖਾਉਣ ਲਈ Seaborn ਨਾਲ ਕੰਮ ਕਰਨਾ ਸ਼ੁਰੂ ਕੀਤਾ। Seaborn ਵਿੱਚ `kdeplot`, ਇੱਕ "ਇੱਕ ਜਾਂ ਕਈ ਮਾਪਾਂ ਵਿੱਚ ਲਗਾਤਾਰ ਸੰਭਾਵਨਾ ਡੈਂਸਿਟੀ ਵਕਰ" 'ਤੇ ਕੁਝ ਖੋਜ ਕਰੋ। [ਦ

---

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।