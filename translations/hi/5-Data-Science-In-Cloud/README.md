<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8dfe141a0f46f7d253e07f74913c7f44",
  "translation_date": "2025-08-24T21:53:03+00:00",
  "source_file": "5-Data-Science-In-Cloud/README.md",
  "language_code": "hi"
}
-->
# क्लाउड में डेटा साइंस

![cloud-picture](../../../translated_images/cloud-picture.f5526de3c6c6387b2d656ba94f019b3352e5e3854a78440e4fb00c93e2dea675.hi.jpg)

> फोटो [Jelleke Vanooteghem](https://unsplash.com/@ilumire) द्वारा [Unsplash](https://unsplash.com/s/photos/cloud?orientation=landscape) से

जब बड़े डेटा के साथ डेटा साइंस करने की बात आती है, तो क्लाउड एक गेम चेंजर साबित हो सकता है। अगले तीन पाठों में, हम देखेंगे कि क्लाउड क्या है और यह क्यों बहुत सहायक हो सकता है। हम एक हार्ट फेलियर डेटासेट का भी विश्लेषण करेंगे और एक मॉडल बनाएंगे जो किसी व्यक्ति के हार्ट फेलियर होने की संभावना का आकलन करने में मदद करेगा। हम क्लाउड की शक्ति का उपयोग करके दो अलग-अलग तरीकों से एक मॉडल को ट्रेन, डिप्लॉय और उपयोग करेंगे। एक तरीका केवल यूजर इंटरफेस का उपयोग करते हुए "लो कोड/नो कोड" तरीके से होगा, और दूसरा तरीका Azure Machine Learning Software Developer Kit (Azure ML SDK) का उपयोग करते हुए होगा।

![project-schema](../../../translated_images/project-schema.420e56d495624541eaecf2b737f138c86fb7d8162bb1c0bf8783c350872ffc4d.hi.png)

### विषय

1. [डेटा साइंस के लिए क्लाउड का उपयोग क्यों करें?](17-Introduction/README.md)  
2. [क्लाउड में डेटा साइंस: "लो कोड/नो कोड" तरीका](18-Low-Code/README.md)  
3. [क्लाउड में डेटा साइंस: "Azure ML SDK" तरीका](19-Azure/README.md)  

### क्रेडिट्स  
ये पाठ ☁️ और 💕 के साथ [Maud Levy](https://twitter.com/maudstweets) और [Tiffany Souterre](https://twitter.com/TiffanySouterre) द्वारा लिखे गए हैं।  

हार्ट फेलियर प्रेडिक्शन प्रोजेक्ट के लिए डेटा [Larxel](https://www.kaggle.com/andrewmvd) से [Kaggle](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) पर लिया गया है। यह [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) के तहत लाइसेंस प्राप्त है।  

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।