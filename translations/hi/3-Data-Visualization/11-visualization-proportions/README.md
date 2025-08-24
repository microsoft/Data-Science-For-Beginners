<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "af6a12015c6e250e500b570a9fa42593",
  "translation_date": "2025-08-24T01:33:23+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "hi"
}
-->
# अनुपातों का विज़ुअलाइज़ेशन

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|अनुपातों का विज़ुअलाइज़ेशन - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

इस पाठ में, आप प्रकृति-केंद्रित एक अलग डेटा सेट का उपयोग करके अनुपातों को विज़ुअलाइज़ करेंगे, जैसे कि मशरूम के बारे में दिए गए डेटा सेट में कितने प्रकार के फंगी मौजूद हैं। आइए इस दिलचस्प फंगी को एक डेटा सेट के माध्यम से खोजें, जो ऑडुबॉन से लिया गया है और इसमें Agaricus और Lepiota परिवारों के 23 प्रजातियों के गिल्ड मशरूम के विवरण शामिल हैं। आप स्वादिष्ट विज़ुअलाइज़ेशन के साथ प्रयोग करेंगे, जैसे:

- पाई चार्ट 🥧
- डोनट चार्ट 🍩
- वाफल चार्ट 🧇

> 💡 माइक्रोसॉफ्ट रिसर्च द्वारा एक बहुत ही दिलचस्प प्रोजेक्ट [Charticulator](https://charticulator.com) एक मुफ्त ड्रैग और ड्रॉप इंटरफ़ेस प्रदान करता है डेटा विज़ुअलाइज़ेशन के लिए। उनके एक ट्यूटोरियल में वे भी इस मशरूम डेटा सेट का उपयोग करते हैं! तो आप डेटा को एक्सप्लोर कर सकते हैं और लाइब्रेरी को एक साथ सीख सकते हैं: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html)।

## [प्री-लेक्चर क्विज़](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## अपने मशरूम को जानें 🍄

मशरूम बहुत दिलचस्प होते हैं। आइए एक डेटा सेट आयात करें और उनका अध्ययन करें:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
एक टेबल प्रिंट होती है जिसमें विश्लेषण के लिए शानदार डेटा होता है:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

जैसे ही आप डेटा देखते हैं, आपको पता चलता है कि सारा डेटा टेक्स्ट के रूप में है। आपको इस डेटा को चार्ट में उपयोग करने के लिए बदलना होगा। वास्तव में, अधिकांश डेटा एक ऑब्जेक्ट के रूप में प्रस्तुत किया गया है:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

आउटपुट है:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
इस डेटा को लें और 'class' कॉलम को एक श्रेणी में बदलें:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

अब, यदि आप मशरूम डेटा प्रिंट करते हैं, तो आप देख सकते हैं कि इसे जहरीले/खाने योग्य वर्ग के अनुसार श्रेणियों में समूहित किया गया है:

|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

यदि आप इस टेबल में प्रस्तुत क्रम का पालन करते हुए अपने वर्ग श्रेणी लेबल बनाते हैं, तो आप एक पाई चार्ट बना सकते हैं:

## पाई!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
देखिए, एक पाई चार्ट जो मशरूम के इन दो वर्गों के अनुसार डेटा के अनुपात को दिखाता है। लेबल्स के क्रम को सही रखना बहुत महत्वपूर्ण है, खासकर यहां, इसलिए सुनिश्चित करें कि लेबल एरे के निर्माण के क्रम को सत्यापित करें!

![pie chart](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## डोनट्स!

पाई चार्ट का एक अधिक दृश्य रूप से दिलचस्प संस्करण डोनट चार्ट है, जो एक पाई चार्ट है जिसमें बीच में एक छेद होता है। आइए इस विधि का उपयोग करके अपने डेटा को देखें।

मशरूम के विभिन्न आवासों पर एक नज़र डालें:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
यहां, आप अपने डेटा को आवास के अनुसार समूहित कर रहे हैं। 7 सूचीबद्ध हैं, इसलिए अपने डोनट चार्ट के लिए उन्हें लेबल के रूप में उपयोग करें:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```

![donut chart](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

यह कोड एक चार्ट और एक केंद्र सर्कल बनाता है, फिर उस केंद्र सर्कल को चार्ट में जोड़ता है। केंद्र सर्कल की चौड़ाई को बदलने के लिए `0.40` को किसी अन्य मान में बदलें।

डोनट चार्ट को कई तरीकों से ट्वीक किया जा सकता है ताकि लेबल्स को बदला जा सके। विशेष रूप से लेबल्स को पढ़ने में आसानी के लिए हाइलाइट किया जा सकता है। अधिक जानकारी के लिए [डॉक्स](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) पढ़ें।

अब जब आप जानते हैं कि अपने डेटा को कैसे समूहित करें और फिर इसे पाई या डोनट के रूप में प्रदर्शित करें, तो आप अन्य प्रकार के चार्ट का पता लगा सकते हैं। वाफल चार्ट आज़माएं, जो मात्रा का पता लगाने का एक अलग तरीका है।

## वाफल्स!

'वाफल' प्रकार का चार्ट मात्रा को 2D वर्गों के रूप में विज़ुअलाइज़ करने का एक अलग तरीका है। इस डेटा सेट में मशरूम कैप रंगों की विभिन्न मात्राओं को विज़ुअलाइज़ करने का प्रयास करें। ऐसा करने के लिए, आपको [PyWaffle](https://pypi.org/project/pywaffle/) नामक एक सहायक लाइब्रेरी स्थापित करनी होगी और Matplotlib का उपयोग करना होगा:

```python
pip install pywaffle
```

अपने डेटा का एक खंड चुनें और उसे समूहित करें:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

लेबल्स बनाकर और फिर अपने डेटा को समूहित करके एक वाफल चार्ट बनाएं:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```

वाफल चार्ट का उपयोग करके, आप मशरूम डेटा सेट के कैप रंगों के अनुपात को स्पष्ट रूप से देख सकते हैं। दिलचस्प बात यह है कि कई हरे रंग के कैप वाले मशरूम हैं!

![waffle chart](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle चार्ट में आइकन का समर्थन करता है जो [Font Awesome](https://fontawesome.com/) में उपलब्ध किसी भी आइकन का उपयोग करता है। आइकन के बजाय वर्गों का उपयोग करके एक और अधिक दिलचस्प वाफल चार्ट बनाने के लिए कुछ प्रयोग करें।

इस पाठ में, आपने अनुपातों को विज़ुअलाइज़ करने के तीन तरीके सीखे। सबसे पहले, आपको अपने डेटा को श्रेणियों में समूहित करना होगा और फिर यह तय करना होगा कि डेटा को प्रदर्शित करने का सबसे अच्छा तरीका कौन सा है - पाई, डोनट, या वाफल। सभी स्वादिष्ट हैं और उपयोगकर्ता को डेटा सेट का त्वरित स्नैपशॉट प्रदान करते हैं।

## 🚀 चुनौती

इन स्वादिष्ट चार्ट को [Charticulator](https://charticulator.com) में फिर से बनाने का प्रयास करें।
## [पोस्ट-लेक्चर क्विज़](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## समीक्षा और स्व-अध्ययन

कभी-कभी यह स्पष्ट नहीं होता कि पाई, डोनट, या वाफल चार्ट का उपयोग कब करना है। इस विषय पर पढ़ने के लिए यहां कुछ लेख दिए गए हैं:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

इस निर्णय पर अधिक जानकारी प्राप्त करने के लिए कुछ शोध करें।

## असाइनमेंट

[Excel में आज़माएं](assignment.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।