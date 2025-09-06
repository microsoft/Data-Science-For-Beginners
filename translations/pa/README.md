<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-29T07:55:28+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# ਡਾਟਾ ਸਾਇੰਸ ਸ਼ੁਰੂਆਤੀ ਲਈ - ਇੱਕ ਪਾਠਕ੍ਰਮ

Azure Cloud Advocates at Microsoft ਨੇ 10 ਹਫ਼ਤਿਆਂ, 20 ਪਾਠਾਂ ਦਾ ਪਾਠਕ੍ਰਮ ਪੇਸ਼ ਕਰਨ ਵਿੱਚ ਖੁਸ਼ੀ ਮਹਿਸੂਸ ਕੀਤੀ ਹੈ ਜੋ ਡਾਟਾ ਸਾਇੰਸ ਬਾਰੇ ਹੈ। ਹਰ ਪਾਠ ਵਿੱਚ ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਪਾਠ ਤੋਂ ਬਾਅਦ ਦੇ ਪ੍ਰਸ਼ਨ, ਪਾਠ ਪੂਰਾ ਕਰਨ ਲਈ ਲਿਖਤ ਨਿਰਦੇਸ਼, ਇੱਕ ਹੱਲ ਅਤੇ ਇੱਕ ਅਸਾਈਨਮੈਂਟ ਸ਼ਾਮਲ ਹੈ। ਸਾਡੇ ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ ਪੈਡਾਗੌਜੀ ਤੁਹਾਨੂੰ ਸਿੱਖਣ ਦਿੰਦੀ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਬਣਾਉਂਦੇ ਹੋ, ਜੋ ਨਵੀਆਂ ਹੁਨਰਾਂ ਨੂੰ 'ਟਿਕਾਉਣ' ਦਾ ਸਾਬਤ ਤਰੀਕਾ ਹੈ।

**ਸਾਡੇ ਲੇਖਕਾਂ ਨੂੰ ਦਿਲੋਂ ਧੰਨਵਾਦ:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 ਵਿਸ਼ੇਸ਼ ਧੰਨਵਾਦ 🙏 ਸਾਡੇ [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) ਲੇਖਕਾਂ, ਸਮੀਖਾਕਾਰਾਂ ਅਤੇ ਸਮੱਗਰੀ ਯੋਗਦਾਨਕਰਤਿਆਂ ਨੂੰ,** ਖਾਸ ਤੌਰ 'ਤੇ Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.pa.png)|
|:---:|
| ਡਾਟਾ ਸਾਇੰਸ ਸ਼ੁਰੂਆਤੀ ਲਈ - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

### 🌐 ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ

#### GitHub Action ਰਾਹੀਂ ਸਹਾਇਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਹਮੇਸ਼ਾ ਅਪ-ਟੂ-ਡੇਟ)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md) | [Ukrainian](../uk/README.md) | [Burmese (Myanmar)](../my/README.md)

**ਜੇ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰਵਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਸਹਾਇਤ ਭਾਸ਼ਾਵਾਂ ਦੀ ਸੂਚੀ [ਇੱਥੇ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) ਦਿੱਤੀ ਗਈ ਹੈ।**

#### ਸਾਡੇ ਸਮੁਦਾਇ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# ਕੀ ਤੁਸੀਂ ਵਿਦਿਆਰਥੀ ਹੋ?

ਹੇਠਾਂ ਦਿੱਤੇ ਸਰੋਤਾਂ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ:

- [Student Hub page](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) ਇਸ ਪੇਜ 'ਤੇ, ਤੁਹਾਨੂੰ ਸ਼ੁਰੂਆਤੀ ਸਰੋਤ, ਵਿਦਿਆਰਥੀ ਪੈਕ ਅਤੇ ਮੁਫ਼ਤ ਸਰਟੀਫਿਕੇਟ ਵਾਊਚਰ ਪ੍ਰਾਪਤ ਕਰਨ ਦੇ ਤਰੀਕੇ ਮਿਲਣਗੇ। ਇਹ ਇੱਕ ਪੇਜ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਬੁੱਕਮਾਰਕ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਅਤੇ ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਚੈੱਕ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਕਿਉਂਕਿ ਅਸੀਂ ਘੱਟੋ-ਘੱਟ ਮਹੀਨਾਵਾਰ ਸਮੱਗਰੀ ਬਦਲਦੇ ਹਾਂ।
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) ਵਿਦਿਆਰਥੀ ਅੰਬੈਸਡਰਾਂ ਦੇ ਗਲੋਬਲ ਸਮੁਦਾਇ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ, ਇਹ Microsoft ਵਿੱਚ ਤੁਹਾਡਾ ਰਸਤਾ ਹੋ ਸਕਦਾ ਹੈ।

# ਸ਼ੁਰੂਆਤ ਕਰਨਾ

> **ਅਧਿਆਪਕਾਂ**: ਅਸੀਂ [ਕੁਝ ਸੁਝਾਅ ਸ਼ਾਮਲ ਕੀਤੇ ਹਨ](for-teachers.md) ਕਿ ਇਸ ਪਾਠਕ੍ਰਮ ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।  ਅਸੀਂ ਤੁਹਾਡਾ ਫੀਡਬੈਕ [ਸਾਡੇ ਚਰਚਾ ਫੋਰਮ](https://github.com/microsoft/Data-Science-For-Beginners/discussions) ਵਿੱਚ ਚਾਹੁੰਦੇ ਹਾਂ!

> **[ਵਿਦਿਆਰਥੀ](https://aka.ms/student-page)**: ਇਸ ਪਾਠਕ੍ਰਮ ਨੂੰ ਆਪਣੇ ਆਪ ਵਰਤਣ ਲਈ, ਪੂਰੇ ਰਿਪੋ ਨੂੰ ਫੋਰਕ ਕਰੋ ਅਤੇ ਆਪਣੇ ਆਪ ਅਭਿਆਸ ਪੂਰੇ ਕਰੋ, ਪਾਠਕ੍ਰਮ ਦੇ ਪਹਿਲਾਂ ਪ੍ਰਸ਼ਨ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।  ਫਿਰ ਪਾਠ ਪੜ੍ਹੋ ਅਤੇ ਬਾਕੀ ਗਤੀਵਿਧੀਆਂ ਪੂਰੀਆਂ ਕਰੋ। ਪਾਠਾਂ ਨੂੰ ਸਮਝ ਕੇ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਨਾ ਕਿ ਹੱਲ ਕੋਡ ਨੂੰ ਕਾਪੀ ਕਰਨ ਦੀ; ਹਾਲਾਂਕਿ, ਉਹ ਕੋਡ /solutions ਫੋਲਡਰ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ ਪਾਠਾਂ ਵਿੱਚ ਉਪਲਬਧ ਹੈ। ਇੱਕ ਹੋਰ ਵਿਚਾਰ ਇਹ ਹੋ ਸਕਦਾ ਹੈ ਕਿ ਦੋਸਤਾਂ ਨਾਲ ਇੱਕ ਅਧਿਐਨ ਸਮੂਹ ਬਣਾਓ ਅਤੇ ਸਮੱਗਰੀ ਨੂੰ ਇਕੱਠੇ ਪੜ੍ਹੋ। ਹੋਰ ਅਧਿਐਨ ਲਈ, ਅਸੀਂ [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

## ਟੀਮ ਨਾਲ ਮਿਲੋ

[![Promo video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo video")

**Gif by** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 ਉਪਰੋਕਤ ਚਿੱਤਰ 'ਤੇ ਕਲਿਕ ਕਰੋ ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਉਹ ਲੋਕਾਂ ਬਾਰੇ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਜਿਨ੍ਹਾਂ ਨੇ ਇਸਨੂੰ ਬਣਾਇਆ!

## ਪੈਡਾਗੌਜੀ

ਅਸੀਂ ਇਸ ਪਾਠਕ੍ਰਮ ਨੂੰ ਬਣਾਉਂਦੇ ਸਮੇਂ ਦੋ ਪੈਡਾਗੌਜੀਕਲ ਸਿਧਾਂਤਾਂ ਨੂੰ ਚੁਣਿਆ ਹੈ: ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਕਿ ਇਹ ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ ਹੈ ਅਤੇ ਇਹ ਵਾਰੰ-ਵਾਰ ਪ੍ਰਸ਼ਨ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਇਸ ਸਿਰੀਜ਼ ਦੇ ਅੰਤ ਤੱਕ, ਵਿਦਿਆਰਥੀ ਡਾਟਾ ਸਾਇੰਸ ਦੇ ਮੁੱਢਲੇ ਸਿਧਾਂਤਾਂ ਸਿੱਖ ਚੁੱਕੇ ਹੋਣਗੇ, ਜਿਸ ਵਿੱਚ ਨੈਤਿਕ ਧਾਰਨਾਵਾਂ, ਡਾਟਾ ਤਿਆਰੀ, ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨ ਦੇ ਵੱਖ-ਵੱਖ ਤਰੀਕੇ, ਡਾਟਾ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ, ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ, ਡਾਟਾ ਸਾਇੰਸ ਦੇ ਅਸਲ-ਜਗਤ ਦੇ ਉਪਯੋਗ ਅਤੇ ਹੋਰ ਬਹੁਤ ਕੁਝ ਸ਼ਾਮਲ ਹੈ।

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਕਲਾਸ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਘੱਟ-ਦਬਾਅ ਵਾਲਾ ਪ੍ਰਸ਼ਨ ਵਿਦਿਆਰਥੀ ਨੂੰ ਇੱਕ ਵਿਸ਼ੇ ਨੂੰ ਸਿੱਖਣ ਵੱਲ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਨ ਲਈ ਸੈਟ ਕਰਦਾ ਹੈ, ਜਦੋਂ ਕਿ ਕਲਾਸ ਤੋਂ ਬਾਅਦ ਦੂਜਾ ਪ੍ਰਸ਼ਨ ਹੋਰ ਰਿਟੇਨਸ਼ਨ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਪਾਠਕ੍ਰਮ ਲਚਕੀਲਾ ਅਤੇ ਮਜ਼ੇਦਾਰ ਬਣਾਇਆ ਗਿਆ ਹੈ ਅਤੇ ਇਸਨੂੰ ਪੂਰੇ ਜਾਂ ਅੰਸ਼ਿਕ ਤੌਰ 'ਤੇ ਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ ਛੋਟੇ ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦੇ ਹਨ ਅਤੇ 10 ਹਫ਼ਤਿਆਂ ਦੇ ਚੱਕਰ ਦੇ ਅੰਤ ਤੱਕ ਵਧਦੇ ਹੀ ਜਟਿਲ ਹੋ ਜਾਂਦੇ ਹਨ।
> ਸਾਡਾ [Code of Conduct](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md), [Translation](TRANSLATIONS.md) ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਵੇਖੋ। ਅਸੀਂ ਤੁਹਾਡੀ ਰਚਨਾਤਮਕ ਪ੍ਰਤੀਕਿਰਿਆ ਦਾ ਸਵਾਗਤ ਕਰਦੇ ਹਾਂ!
## ਹਰ ਇਕ ਪਾਠ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:

- ਵਿਕਲਪਿਕ ਸਕੈਚਨੋਟ
- ਵਿਕਲਪਿਕ ਸਹਾਇਕ ਵੀਡੀਓ
- ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ ਵਾਰਮਅੱਪ ਕਵਿਜ਼
- ਲਿਖਤ ਪਾਠ
- ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਤ ਪਾਠਾਂ ਲਈ, ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ
- ਗਿਆਨ ਜਾਂਚ
- ਇੱਕ ਚੁਣੌਤੀ
- ਸਹਾਇਕ ਪੜ੍ਹਾਈ
- ਅਸਾਈਨਮੈਂਟ
- [ਪਾਠ ਤੋਂ ਬਾਅਦ ਕਵਿਜ਼](https://ff-quizzes.netlify.app/en/)

> **ਕਵਿਜ਼ਾਂ ਬਾਰੇ ਇੱਕ ਨੋਟ**: ਸਾਰੀਆਂ ਕਵਿਜ਼ਾਂ Quiz-App ਫੋਲਡਰ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ, ਜਿਹਨਾਂ ਵਿੱਚ ਕੁੱਲ 40 ਕਵਿਜ਼ ਹਨ, ਹਰ ਇੱਕ ਵਿੱਚ ਤਿੰਨ ਪ੍ਰਸ਼ਨ ਹਨ। ਇਹ ਪਾਠਾਂ ਵਿੱਚੋਂ ਲਿੰਕ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ, ਪਰ ਕਵਿਜ਼ ਐਪ ਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ Azure 'ਤੇ ਡਿਪਲੌਇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ; `quiz-app` ਫੋਲਡਰ ਵਿੱਚ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਇਹ ਹੌਲੀ-ਹੌਲੀ ਸਥਾਨਕ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦਿਤ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ।

## ਪਾਠ

|![ @sketchthedocs ਦੁਆਰਾ ਬਣਾਈ ਗਈ ਸਕੈਚਨੋਟ https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.pa.png)|
|:---:|
| ਸ਼ੁਰੂਆਤ ਲਈ ਡਾਟਾ ਸਾਇੰਸ: ਰੋਡਮੈਪ - _[@nitya](https://twitter.com/nitya) ਦੁਆਰਾ ਸਕੈਚਨੋਟ_ |

| ਪਾਠ ਨੰਬਰ | ਵਿਸ਼ਾ | ਪਾਠ ਸਮੂਹ | ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼ | ਲਿੰਕ ਕੀਤਾ ਪਾਠ | ਲੇਖਕ |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | ਡਾਟਾ ਸਾਇੰਸ ਦੀ ਪਰਿਭਾਸ਼ਾ | [ਪ੍ਰਸਤਾਵਨਾ](1-Introduction/README.md) | ਡਾਟਾ ਸਾਇੰਸ ਦੇ ਮੁੱਢਲੇ ਸੰਕਲਪਾਂ ਨੂੰ ਸਿੱਖੋ ਅਤੇ ਇਹ ਕਿਵੇਂ ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ, ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਬਿਗ ਡਾਟਾ ਨਾਲ ਸੰਬੰਧਿਤ ਹੈ। | [ਪਾਠ](1-Introduction/01-defining-data-science/README.md) [ਵੀਡੀਓ](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | ਡਾਟਾ ਸਾਇੰਸ ਨੈਤਿਕਤਾ | [ਪ੍ਰਸਤਾਵਨਾ](1-Introduction/README.md) | ਡਾਟਾ ਨੈਤਿਕਤਾ ਦੇ ਸੰਕਲਪ, ਚੁਣੌਤੀਆਂ ਅਤੇ ਢਾਂਚੇ। | [ਪਾਠ](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | ਡਾਟਾ ਦੀ ਪਰਿਭਾਸ਼ਾ | [ਪ੍ਰਸਤਾਵਨਾ](1-Introduction/README.md) | ਡਾਟਾ ਨੂੰ ਕਿਵੇਂ ਵਰਗੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਸ ਦੇ ਆਮ ਸਰੋਤ। | [ਪਾਠ](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | ਅੰਕੜੇ ਅਤੇ ਸੰਭਾਵਨਾ ਦਾ ਪਰਿਚਯ | [ਪ੍ਰਸਤਾਵਨਾ](1-Introduction/README.md) | ਡਾਟਾ ਨੂੰ ਸਮਝਣ ਲਈ ਸੰਭਾਵਨਾ ਅਤੇ ਅੰਕੜਿਆਂ ਦੀ ਗਣਿਤੀ ਤਕਨੀਕਾਂ। | [ਪਾਠ](1-Introduction/04-stats-and-probability/README.md) [ਵੀਡੀਓ](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | ਰਿਲੇਸ਼ਨਲ ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ | [ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ](2-Working-With-Data/README.md) | ਰਿਲੇਸ਼ਨਲ ਡਾਟਾ ਦਾ ਪਰਿਚਯ ਅਤੇ ਰਿਲੇਸ਼ਨਲ ਡਾਟਾ ਦੀ ਖੋਜ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਦੇ ਮੁੱਢਲੇ ਤਰੀਕੇ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਸਟ੍ਰਕਚਰਡ ਕਵੈਰੀ ਲੈਂਗਵੇਜ (SQL) ਕਿਹਾ ਜਾਂਦਾ ਹੈ। | [ਪਾਠ](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ | [ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ](2-Working-With-Data/README.md) | ਗੈਰ-ਰਿਲੇਸ਼ਨਲ ਡਾਟਾ ਦਾ ਪਰਿਚਯ, ਇਸ ਦੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਕਾਰ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਡਾਟਾਬੇਸ ਦੀ ਖੋਜ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਦੇ ਮੁੱਢਲੇ ਤਰੀਕੇ। | [ਪਾਠ](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | ਪਾਇਥਨ ਨਾਲ ਕੰਮ ਕਰਨਾ | [ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ](2-Working-With-Data/README.md) | Pandas ਵਰਗੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨਾਲ ਡਾਟਾ ਦੀ ਖੋਜ ਲਈ ਪਾਇਥਨ ਦੀ ਵਰਤੋਂ ਦੇ ਮੁੱਢਲੇ ਤਰੀਕੇ। ਪਾਇਥਨ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | [ਪਾਠ](2-Working-With-Data/07-python/README.md) [ਵੀਡੀਓ](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | ਡਾਟਾ ਤਿਆਰੀ | [ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਨਾ](2-Working-With-Data/README.md) | ਗੁੰਮ, ਗਲਤ ਜਾਂ ਅਧੂਰੇ ਡਾਟਾ ਦੀ ਸਮੱਸਿਆ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਡਾਟਾ ਸਾਫ਼ ਕਰਨ ਅਤੇ ਰੂਪਾਂਤਰਿਤ ਕਰਨ ਦੀਆਂ ਤਕਨੀਕਾਂ। | [ਪਾਠ](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | ਮਾਤਰਾ ਦੀ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ | [ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ](3-Data-Visualization/README.md) | ਸਿੱਖੋ ਕਿ ਕਿਵੇਂ Matplotlib ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੰਛੀਆਂ ਦੇ ਡਾਟਾ ਨੂੰ ਵਿਜੁਅਲਾਈਜ਼ ਕੀਤਾ ਜਾਵੇ 🦆 | [ਪਾਠ](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | ਡਾਟਾ ਦੇ ਵੰਡ ਦੀ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ | [ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ](3-Data-Visualization/README.md) | ਇੱਕ ਅੰਤਰਾਲ ਦੇ ਅੰਦਰ ਦੇ ਅਵਲੋਕਨ ਅਤੇ ਰੁਝਾਨਾਂ ਨੂੰ ਵਿਜੁਅਲਾਈਜ਼ ਕਰਨਾ। | [ਪਾਠ](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | ਅਨੁਪਾਤ ਦੀ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ | [ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ](3-Data-Visualization/README.md) | ਵਿਸ਼ੇਸ਼ ਅਤੇ ਸਮੂਹੀਕ੍ਰਿਤ ਪ੍ਰਤੀਸ਼ਤਾਂ ਨੂੰ ਵਿਜੁਅਲਾਈਜ਼ ਕਰਨਾ। | [ਪਾਠ](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | ਸੰਬੰਧਾਂ ਦੀ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ | [ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ](3-Data-Visualization/README.md) | ਡਾਟਾ ਦੇ ਸੈੱਟਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਵੈਰੀਏਬਲਾਂ ਦੇ ਵਿਚਕਾਰ ਦੇ ਸੰਬੰਧਾਂ ਅਤੇ ਸਹਸੰਬੰਧਾਂ ਨੂੰ ਵਿਜੁਅਲਾਈਜ਼ ਕਰਨਾ। | [ਪਾਠ](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | ਅਰਥਪੂਰਨ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ | [ਡਾਟਾ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ](3-Data-Visualization/README.md) | ਤੁਹਾਡੇ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਅਤੇ ਅੰਦਰੂਨੀ ਜਾਣਕਾਰੀ ਲਈ ਕੀਮਤੀ ਬਣਾਉਣ ਲਈ ਤਕਨੀਕਾਂ ਅਤੇ ਮਾਰਗਦਰਸ਼ਨ। | [ਪਾਠ](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | ਡਾਟਾ ਸਾਇੰਸ ਲਾਈਫਸਾਈਕਲ ਦਾ ਪਰਿਚਯ | [ਲਾਈਫਸਾਈਕਲ](4-Data-Science-Lifecycle/README.md) | ਡਾਟਾ ਸਾਇੰਸ ਲਾਈਫਸਾਈਕਲ ਦਾ ਪਰਿਚਯ ਅਤੇ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਕੱਢਣ ਦੇ ਪਹਿਲੇ ਕਦਮ। | [ਪਾਠ](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | ਵਿਸ਼ਲੇਸ਼ਣ | [ਲਾਈਫਸਾਈਕਲ](4-Data-Science-Lifecycle/README.md) | ਡਾਟਾ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ ਤਕਨੀਕਾਂ 'ਤੇ ਕੇਂਦ੍ਰਿਤ। | [ਪਾਠ](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | ਸੰਚਾਰ | [ਲਾਈਫਸਾਈਕਲ](4-Data-Science-Lifecycle/README.md) | ਡਾਟਾ ਤੋਂ ਪ੍ਰਾਪਤ ਅੰਦਰੂਨੀ ਜਾਣਕਾਰੀ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਪੇਸ਼ ਕਰਨ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਜੋ ਫੈਸਲੇ ਲੈਣ ਵਾਲਿਆਂ ਲਈ ਸਮਝਣਾ ਆਸਾਨ ਬਣਾਏ। | [ਪਾਠ](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ | [ਕਲਾਉਡ ਡਾਟਾ](5-Data-Science-In-Cloud/README.md) | ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ ਅਤੇ ਇਸ ਦੇ ਫਾਇਦਿਆਂ ਦਾ ਪਰਿਚਯ। | [ਪਾਠ](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) ਅਤੇ [Maud](https://twitter.com/maudstweets) |
| 18 | ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ | [ਕਲਾਉਡ ਡਾਟਾ](5-Data-Science-In-Cloud/README.md) | Low Code ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲਾਂ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨਾ। |[ਪਾਠ](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) ਅਤੇ [Maud](https://twitter.com/maudstweets) |
| 19 | ਕਲਾਉਡ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ | [ਕਲਾਉਡ ਡਾਟਾ](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio ਨਾਲ ਮਾਡਲਾਂ ਨੂੰ ਡਿਪਲੌਇ ਕਰਨਾ। | [ਪਾਠ](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) ਅਤੇ [Maud](https://twitter.com/maudstweets) |
| 20 | ਜੰਗਲੀ ਪ੍ਰਸਥਿਤੀਆਂ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ | [ਜੰਗਲੀ ਪ੍ਰਸਥਿਤੀਆਂ](6-Data-Science-In-Wild/README.md) | ਅਸਲ ਦੁਨੀਆ ਵਿੱਚ ਡਾਟਾ ਸਾਇੰਸ ਚਲਿਤ ਪ੍ਰੋਜੈਕਟ। | [ਪਾਠ](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub ਕੋਡਸਪੇਸ

ਇਸ ਨਮੂਨੇ ਨੂੰ ਇੱਕ ਕੋਡਸਪੇਸ ਵਿੱਚ ਖੋਲ੍ਹਣ ਲਈ ਇਹ ਕਦਮ ਅਨੁਸਰਣ ਕਰੋ:
1. ਕੋਡ ਡ੍ਰੌਪ-ਡਾਊਨ ਮੀਨੂ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ "Open with Codespaces" ਵਿਕਲਪ ਚੁਣੋ।
2. ਪੈਨ ਦੇ ਹੇਠਾਂ + ਨਵਾਂ ਕੋਡਸਪੇਸ ਚੁਣੋ।
ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, [GitHub ਦਸਤਾਵੇਜ਼](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) ਵੇਖੋ।

## VSCode ਰਿਮੋਟ - ਕੰਟੇਨਰ
ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਆਪਣੇ ਸਥਾਨਕ ਮਸ਼ੀਨ ਅਤੇ VSCode 'ਤੇ VS Code ਰਿਮੋਟ - ਕੰਟੇਨਰ ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਕੰਟੇਨਰ ਵਿੱਚ ਖੋਲ੍ਹਣ ਲਈ ਇਹ ਕਦਮ ਅਨੁਸਰਣ ਕਰੋ:

1. ਜੇ ਇਹ ਪਹਿਲੀ ਵਾਰ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਡਿਵੈਲਪਮੈਂਟ ਕੰਟੇਨਰ ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੀ ਸਿਸਟਮ [ਸ਼ੁਰੂਆਤ ਦਸਤਾਵੇਜ਼](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) ਵਿੱਚ ਦਿੱਤੀਆਂ ਪੂਰਕ ਸ਼ਰਤਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦੀ ਹੈ (ਜਿਵੇਂ ਕਿ Docker ਇੰਸਟਾਲ ਹੋਣਾ)।

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ, ਤੁਸੀਂ ਇਸਨੂੰ ਇੱਕ ਅਲੱਗ Docker ਵਾਲਿਊਮ ਵਿੱਚ ਖੋਲ੍ਹ ਸਕਦੇ ਹੋ:

**ਨੋਟ**: ਇਸ ਦੇ ਪਿੱਛੇ, ਇਹ ਰਿਮੋਟ-ਕੰਟੇਨਰ: **Clone Repository in Container Volume...** ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰੇਗਾ ਜੋ ਸਥਾਨਕ ਫਾਈਲ ਸਿਸਟਮ ਦੀ ਬਜਾਏ Docker ਵਾਲਿਊਮ ਵਿੱਚ ਸਰੋਤ ਕੋਡ ਨੂੰ ਕਲੋਨ ਕਰੇਗਾ। [ਵਾਲਿਊਮ](https://docs.docker.com/storage/volumes/) ਕੰਟੇਨਰ ਡਾਟਾ ਨੂੰ ਸਥਾਈ ਬਣਾਉਣ ਲਈ ਪਸੰਦੀਦਾ ਤਰੀਕਾ ਹਨ।

ਜਾਂ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕੀਤੀ ਜਾਂ ਡਾਊਨਲੋਡ ਕੀਤੀ ਗਈ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਖੋਲ੍ਹੋ:

- ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਆਪਣੇ ਸਥਾਨਕ ਫਾਈਲ ਸਿਸਟਮ 'ਤੇ ਕਲੋਨ ਕਰੋ।
- F1 ਦਬਾਓ ਅਤੇ **Remote-Containers: Open Folder in Container...** ਕਮਾਂਡ ਚੁਣੋ।
- ਇਸ ਫੋਲਡਰ ਦੀ ਕਲੋਨ ਕੀਤੀ ਕਾਪੀ ਚੁਣੋ, ਕੰਟੇਨਰ ਦੇ ਸ਼ੁਰੂ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰੋ, ਅਤੇ ਚੀਜ਼ਾਂ ਨੂੰ ਅਜ਼ਮਾਓ।

## ਆਫਲਾਈਨ ਪਹੁੰਚ

ਤੁਸੀਂ ਇਸ ਦਸਤਾਵੇਜ਼ ਨੂੰ [Docsify](https://docsify.js.org/#/) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਫਲਾਈਨ ਚਲਾ ਸਕਦੇ ਹੋ। ਇਸ ਰਿਪੋ ਨੂੰ ਫੋਰਕ ਕਰੋ, ਆਪਣੇ ਸਥਾਨਕ ਮਸ਼ੀਨ 'ਤੇ [Docsify ਇੰਸਟਾਲ ਕਰੋ](https://docsify.js.org/#/quickstart), ਫਿਰ ਇਸ ਰਿਪੋ ਦੇ ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ, `docsify serve` ਟਾਈਪ ਕਰੋ। ਵੈਬਸਾਈਟ ਤੁਹਾਡੇ ਲੋਕਲਹੋਸਟ `localhost:3000` 'ਤੇ ਪੋਰਟ 3000 'ਤੇ ਸਰਵ ਕੀਤੀ ਜਾਵੇਗੀ।

> ਨੋਟ, ਨੋਟਬੁੱਕ Docsify ਰਾਹੀਂ ਰੈਂਡਰ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾਣਗੀਆਂ, ਇਸ ਲਈ ਜਦੋਂ ਤੁਹਾਨੂੰ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਦੀ ਲੋੜ ਹੋਵੇ, ਤਾਂ ਇਸਨੂੰ ਵੱਖਰੇ ਤੌਰ 'ਤੇ VS Code ਵਿੱਚ ਪਾਇਥਨ ਕਰਨਲ ਚਲਾਉਂਦੇ ਹੋਏ ਚਲਾਓ।

## ਹੋਰ ਪਾਠਕ੍ਰਮ

ਸਾਡੀ ਟੀਮ ਹੋਰ ਪਾਠਕ੍ਰਮ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਵੇਖੋ:

- [ਸ਼ੁਰੂਆਤ ਲਈ ਜਨਰੇਟਿਵ AI](https://aka.ms/genai-beginners)
- [ਸ਼ੁਰੂਆਤ ਲਈ ਜਨਰੇਟਿਵ AI .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਨਾਲ ਜਨਰੇਟਿਵ AI](https://github.com/microsoft/generative-ai-with-javascript)
- [ਜਾਵਾ ਨਾਲ ਜਨਰੇਟਿਵ AI](https://aka.ms/genaijava)
- [ਸ਼ੁਰੂਆਤ ਲਈ AI](https://aka.ms/ai-beginners)
- [ਸ਼ੁਰੂਆਤ ਲਈ ਡਾਟਾ ਸਾਇੰਸ](https://aka.ms/datascience-beginners)
- [ਸ਼ੁਰੂਆਤ ਲਈ ਮਸ਼ੀਨ ਲਰਨਿੰਗ](https://aka.ms/ml-beginners)
- [ਸ਼ੁਰੂਆਤ ਲਈ ਸਾਈਬਰਸੁਰੱਖ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।  