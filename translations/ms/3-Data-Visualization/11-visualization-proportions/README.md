<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc490897ee2d276870472bcb31602d03",
  "translation_date": "2025-09-04T20:48:19+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "ms"
}
-->
# Memvisualkan Peratusan

|![ Sketchnote oleh [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Memvisualkan Peratusan - _Sketchnote oleh [@nitya](https://twitter.com/nitya)_ |

Dalam pelajaran ini, anda akan menggunakan dataset yang berfokuskan alam semula jadi untuk memvisualkan peratusan, seperti berapa banyak jenis kulat yang terdapat dalam dataset tentang cendawan. Mari kita terokai kulat yang menarik ini menggunakan dataset yang diperoleh daripada Audubon yang menyenaraikan butiran tentang 23 spesies cendawan berinsang dalam keluarga Agaricus dan Lepiota. Anda akan bereksperimen dengan visualisasi yang menarik seperti:

- Carta pai 🥧
- Carta donat 🍩
- Carta waffle 🧇

> 💡 Satu projek yang sangat menarik dipanggil [Charticulator](https://charticulator.com) oleh Microsoft Research menawarkan antara muka seret dan lepas percuma untuk visualisasi data. Dalam salah satu tutorial mereka, mereka juga menggunakan dataset cendawan ini! Jadi anda boleh meneroka data dan belajar perpustakaan ini pada masa yang sama: [Tutorial Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Kuiz selepas kuliah](https://ff-quizzes.netlify.app/en/ds/)

## Kenali cendawan anda 🍄

Cendawan sangat menarik. Mari kita import dataset untuk mengkajinya:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Sebuah jadual dicetak dengan beberapa data yang hebat untuk analisis:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

Anda akan perasan bahawa semua data adalah berbentuk teks. Anda perlu menukar data ini supaya dapat digunakan dalam carta. Kebanyakan data, sebenarnya, diwakili sebagai objek:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Outputnya adalah:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Ambil data ini dan tukarkan kolum 'class' kepada kategori:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Sekarang, jika anda mencetak data cendawan, anda boleh lihat bahawa ia telah dikumpulkan ke dalam kategori mengikut kelas beracun/boleh dimakan:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

Jika anda mengikuti susunan yang ditunjukkan dalam jadual ini untuk mencipta label kategori kelas anda, anda boleh membina carta pai:

## Pai!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, sebuah carta pai yang menunjukkan peratusan data ini mengikut dua kelas cendawan. Sangat penting untuk mendapatkan susunan label dengan betul, terutamanya di sini, jadi pastikan anda mengesahkan susunan dengan cara array label dibina!

![carta pai](../../../../translated_images/pie1-wb.e201f2fcc335413143ce37650fb7f5f0bb21358e7823a327ed8644dfb84be9db.ms.png)

## Donat!

Carta pai yang lebih menarik secara visual adalah carta donat, iaitu carta pai dengan lubang di tengah. Mari kita lihat data kita menggunakan kaedah ini.

Lihat pelbagai habitat di mana cendawan tumbuh:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Di sini, anda mengelompokkan data anda mengikut habitat. Terdapat 7 habitat yang disenaraikan, jadi gunakan itu sebagai label untuk carta donat anda:

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

![carta donat](../../../../translated_images/donut-wb.be3c12a22712302b5d10c40014d5389d4a1ae4412fe1655b3cf4af57b64f799a.ms.png)

Kod ini melukis carta dan bulatan tengah, kemudian menambah bulatan tengah itu dalam carta. Edit lebar bulatan tengah dengan menukar `0.40` kepada nilai lain.

Carta donat boleh diubah suai dalam beberapa cara untuk menukar label. Label khususnya boleh diserlahkan untuk meningkatkan kebolehbacaan. Ketahui lebih lanjut dalam [dokumen](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Sekarang setelah anda tahu cara mengelompokkan data anda dan kemudian memaparkannya sebagai pai atau donat, anda boleh meneroka jenis carta lain. Cuba carta waffle, yang hanya cara berbeza untuk meneroka kuantiti.
## Waffle!

Carta jenis 'waffle' adalah cara berbeza untuk memvisualkan kuantiti sebagai array 2D kotak. Cuba visualkan kuantiti warna penutup cendawan yang berbeza dalam dataset ini. Untuk melakukan ini, anda perlu memasang perpustakaan pembantu yang dipanggil [PyWaffle](https://pypi.org/project/pywaffle/) dan gunakan Matplotlib:

```python
pip install pywaffle
```

Pilih segmen data anda untuk dikelompokkan:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Cipta carta waffle dengan mencipta label dan kemudian mengelompokkan data anda:

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

Menggunakan carta waffle, anda boleh melihat dengan jelas peratusan warna penutup dalam dataset cendawan ini. Menariknya, terdapat banyak cendawan dengan penutup hijau!

![carta waffle](../../../../translated_images/waffle.5455dbae4ccf17d53bb40ff0a657ecef7b8aa967e27a19cc96325bd81598f65e.ms.png)

✅ Pywaffle menyokong ikon dalam carta yang menggunakan mana-mana ikon yang tersedia dalam [Font Awesome](https://fontawesome.com/). Lakukan beberapa eksperimen untuk mencipta carta waffle yang lebih menarik menggunakan ikon dan bukannya kotak.

Dalam pelajaran ini, anda belajar tiga cara untuk memvisualkan peratusan. Pertama, anda perlu mengelompokkan data anda ke dalam kategori dan kemudian memutuskan cara terbaik untuk memaparkan data - pai, donat, atau waffle. Semua adalah menarik dan memberikan pengguna gambaran segera tentang dataset.

## 🚀 Cabaran

Cuba cipta semula carta yang menarik ini dalam [Charticulator](https://charticulator.com).
## [Kuiz selepas kuliah](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Ulasan & Kajian Kendiri

Kadang-kadang tidak jelas bila untuk menggunakan carta pai, donat, atau waffle. Berikut adalah beberapa artikel untuk dibaca mengenai topik ini:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Lakukan penyelidikan untuk mencari lebih banyak maklumat mengenai keputusan yang sukar ini.
## Tugasan

[Cuba di Excel](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.