<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8dfe141a0f46f7d253e07f74913c7f44",
  "translation_date": "2025-08-27T17:37:11+00:00",
  "source_file": "5-Data-Science-In-Cloud/README.md",
  "language_code": "pa"
}
-->
# ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ

![cloud-picture](../../../translated_images/cloud-picture.f5526de3c6c6387b2d656ba94f019b3352e5e3854a78440e4fb00c93e2dea675.pa.jpg)

> ਫੋਟੋ [Jelleke Vanooteghem](https://unsplash.com/@ilumire) ਵੱਲੋਂ [Unsplash](https://unsplash.com/s/photos/cloud?orientation=landscape) ਤੋਂ

ਜਦੋਂ ਵੱਡੇ ਡਾਟਾ ਨਾਲ ਡਾਟਾ ਸਾਇੰਸ ਕਰਨ ਦੀ ਗੱਲ ਆਉਂਦੀ ਹੈ, ਤਾਂ ਕਲਾਉਡ ਇੱਕ ਬਹੁਤ ਵੱਡਾ ਬਦਲਾਅ ਲਿਆ ਸਕਦਾ ਹੈ। ਅਗਲੇ ਤਿੰਨ ਪਾਠਾਂ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਕਲਾਉਡ ਕੀ ਹੈ ਅਤੇ ਇਹ ਕਿਵੇਂ ਬਹੁਤ ਮਦਦਗਾਰ ਹੋ ਸਕਦਾ ਹੈ। ਅਸੀਂ ਇੱਕ ਹਾਰਟ ਫੇਲਿਅਰ ਡਾਟਾਸੈਟ ਦੀ ਵੀ ਜਾਂਚ ਕਰਾਂਗੇ ਅਤੇ ਇੱਕ ਮਾਡਲ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਾਂਗੇ ਜੋ ਕਿਸੇ ਵਿਅਕਤੀ ਦੇ ਹਾਰਟ ਫੇਲਿਅਰ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ ਦਾ ਅੰਕਲਨ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇ। ਅਸੀਂ ਕਲਾਉਡ ਦੀ ਤਾਕਤ ਦਾ ਇਸਤੇਮਾਲ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ, ਡਿਪਲੌਇ ਅਤੇ ਦੋ ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਨਾਲ ਕਨਜ਼ਿਊਮ ਕਰਾਂਗੇ। ਇੱਕ ਤਰੀਕਾ ਸਿਰਫ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ "ਲੋ ਕੋਡ/ਨੋ ਕੋਡ" ਢੰਗ ਵਿੱਚ, ਅਤੇ ਦੂਜਾ ਤਰੀਕਾ Azure Machine Learning Software Developer Kit (Azure ML SDK) ਦੀ ਵਰਤੋਂ ਕਰਕੇ।

![project-schema](../../../translated_images/project-schema.420e56d495624541eaecf2b737f138c86fb7d8162bb1c0bf8783c350872ffc4d.pa.png)

### ਵਿਸ਼ੇ

1. [ਡਾਟਾ ਸਾਇੰਸ ਲਈ ਕਲਾਉਡ ਕਿਉਂ ਵਰਤਿਆ ਜਾਵੇ?](17-Introduction/README.md)
2. [ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ: "ਲੋ ਕੋਡ/ਨੋ ਕੋਡ" ਤਰੀਕਾ](18-Low-Code/README.md)
3. [ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ: "Azure ML SDK" ਤਰੀਕਾ](19-Azure/README.md)

### ਸ਼੍ਰੇਯ

ਇਹ ਪਾਠ ☁️ ਅਤੇ 💕 ਨਾਲ [Maud Levy](https://twitter.com/maudstweets) ਅਤੇ [Tiffany Souterre](https://twitter.com/TiffanySouterre) ਵੱਲੋਂ ਲਿਖੇ ਗਏ ਹਨ।

ਹਾਰਟ ਫੇਲਿਅਰ ਪ੍ਰਡਿਕਸ਼ਨ ਪ੍ਰੋਜੈਕਟ ਲਈ ਡਾਟਾ [
Larxel](https://www.kaggle.com/andrewmvd) ਤੋਂ [Kaggle](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) 'ਤੇ ਲਿਆ ਗਿਆ ਹੈ। ਇਹ [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) ਅਧੀਨ ਲਾਇਸੰਸ ਕੀਤਾ ਗਿਆ ਹੈ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।