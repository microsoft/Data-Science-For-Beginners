<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "abc3309ab41bc5a7846f70ee1a055838",
  "translation_date": "2025-08-27T16:41:13+00:00",
  "source_file": "2-Working-With-Data/README.md",
  "language_code": "pa"
}
-->
# ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ

![ਡਾਟਾ ਪਿਆਰ](../../../translated_images/data-love.a22ef29e6742c852505ada062920956d3d7604870b281a8ca7c7ac6f37381d5a.pa.jpg)
> ਫੋਟੋ <a href="https://unsplash.com/@swimstaralex?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alexander Sinn</a> ਦੁਆਰਾ <a href="https://unsplash.com/s/photos/data?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> 'ਤੇ
  
ਇਨ੍ਹਾਂ ਪਾਠਾਂ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਡਾਟਾ ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਬੰਧਿਤ, ਹੇਰਫੇਰ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ ਰਿਲੇਸ਼ਨਲ ਅਤੇ ਨਾਨ-ਰਿਲੇਸ਼ਨਲ ਡਾਟਾਬੇਸਾਂ ਬਾਰੇ ਸਿੱਖੋਗੇ ਅਤੇ ਇਹ ਵੀ ਕਿ ਡਾਟਾ ਨੂੰ ਇਨ੍ਹਾਂ ਵਿੱਚ ਕਿਵੇਂ ਸਟੋਰ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ ਡਾਟਾ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਲਈ Python ਨਾਲ ਕੰਮ ਕਰਨ ਦੇ ਮੁੱਢਲੇ ਸਿਧਾਂਤ ਸਿੱਖੋਗੇ ਅਤੇ ਇਹ ਵੀ ਪਤਾ ਲਗਾਓਗੇ ਕਿ Python ਨਾਲ ਡਾਟਾ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਅਤੇ ਖੋਜਣ ਦੇ ਕਈ ਤਰੀਕੇ ਕੀ ਹਨ। 

### ਵਿਸ਼ੇ

1. [ਰਿਲੇਸ਼ਨਲ ਡਾਟਾਬੇਸ](05-relational-databases/README.md)
2. [ਨਾਨ-ਰਿਲੇਸ਼ਨਲ ਡਾਟਾਬੇਸ](06-non-relational/README.md)
3. [Python ਨਾਲ ਕੰਮ ਕਰਨਾ](07-python/README.md)
4. [ਡਾਟਾ ਤਿਆਰ ਕਰਨਾ](08-data-preparation/README.md)

### ਸ਼੍ਰੇਯ

ਇਨ੍ਹਾਂ ਪਾਠਾਂ ਨੂੰ ❤️ ਨਾਲ [Christopher Harrison](https://twitter.com/geektrainer), [Dmitry Soshnikov](https://twitter.com/shwars) ਅਤੇ [Jasmine Greenaway](https://twitter.com/paladique) ਦੁਆਰਾ ਲਿਖਿਆ ਗਿਆ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।