<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T21:34:36+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "th"
}
-->
# การแสดงภาพการกระจายตัวของข้อมูล

|![ภาพสเก็ตช์โดย [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| การแสดงภาพการกระจายตัวของข้อมูล - _ภาพสเก็ตช์โดย [@nitya](https://twitter.com/nitya)_ |

ในบทเรียนก่อนหน้านี้ คุณได้เรียนรู้ข้อเท็จจริงที่น่าสนใจเกี่ยวกับชุดข้อมูลเกี่ยวกับนกในรัฐมินนิโซตา คุณพบข้อมูลที่ผิดพลาดโดยการแสดงภาพจุดที่อยู่นอกกรอบ และได้ดูความแตกต่างระหว่างหมวดหมู่นกโดยพิจารณาจากความยาวสูงสุดของพวกมัน

## [แบบทดสอบก่อนเรียน](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## สำรวจชุดข้อมูลนก

อีกวิธีหนึ่งในการเจาะลึกข้อมูลคือการดูการกระจายตัวของข้อมูล หรือวิธีที่ข้อมูลถูกจัดเรียงตามแกนตัวอย่าง เช่น คุณอาจต้องการเรียนรู้เกี่ยวกับการกระจายตัวทั่วไปของความกว้างปีกสูงสุดหรือมวลร่างกายสูงสุดของนกในรัฐมินนิโซตาในชุดข้อมูลนี้

มาค้นพบข้อเท็จจริงบางอย่างเกี่ยวกับการกระจายตัวของข้อมูลในชุดข้อมูลนี้กัน ในไฟล์ _notebook.ipynb_ ที่อยู่ในโฟลเดอร์บทเรียนนี้ ให้ import Pandas, Matplotlib และข้อมูลของคุณ:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

โดยทั่วไป คุณสามารถดูการกระจายตัวของข้อมูลได้อย่างรวดเร็วโดยใช้ scatter plot เหมือนที่เราเคยทำในบทเรียนก่อนหน้านี้:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max length per order](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

นี่เป็นภาพรวมของการกระจายตัวทั่วไปของความยาวร่างกายต่อลำดับของนก แต่ไม่ใช่วิธีที่เหมาะสมที่สุดในการแสดงการกระจายตัวที่แท้จริง งานนี้มักจะทำโดยการสร้าง Histogram

## การทำงานกับ Histogram

Matplotlib มีวิธีที่ดีมากในการแสดงภาพการกระจายตัวของข้อมูลโดยใช้ Histogram ซึ่งเป็นกราฟที่คล้ายกับกราฟแท่งที่การกระจายตัวสามารถเห็นได้จากการเพิ่มขึ้นและลดลงของแท่ง เพื่อสร้าง Histogram คุณต้องมีข้อมูลเชิงตัวเลข ในการสร้าง Histogram คุณสามารถวาดกราฟโดยกำหนดชนิดเป็น 'hist' สำหรับ Histogram กราฟนี้แสดงการกระจายตัวของ MaxBodyMass สำหรับช่วงข้อมูลตัวเลขทั้งหมดในชุดข้อมูล โดยการแบ่งข้อมูลที่ได้รับออกเป็นกลุ่มย่อย (bins) จะสามารถแสดงการกระจายตัวของค่าข้อมูลได้:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

ดังที่คุณเห็น นกส่วนใหญ่ในชุดข้อมูลกว่า 400 ตัวนี้มีมวลร่างกายสูงสุดต่ำกว่า 2000 ลองเปลี่ยนพารามิเตอร์ `bins` เป็นค่าที่สูงขึ้น เช่น 30 เพื่อดูข้อมูลเพิ่มเติม:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset with larger bins param](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

กราฟนี้แสดงการกระจายตัวในลักษณะที่ละเอียดขึ้นเล็กน้อย คุณสามารถสร้างกราฟที่ไม่เอียงไปทางซ้ายมากนักโดยเลือกข้อมูลเฉพาะในช่วงที่กำหนด:

กรองข้อมูลของคุณเพื่อเลือกเฉพาะนกที่มีมวลร่างกายต่ำกว่า 60 และแสดง 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtered histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ ลองใช้ตัวกรองและจุดข้อมูลอื่น ๆ เพื่อดูการกระจายตัวของข้อมูลทั้งหมด ลบตัวกรอง `['MaxBodyMass']` เพื่อแสดงการกระจายตัวที่มีการติดป้ายกำกับ

Histogram ยังมีการปรับปรุงสีและการติดป้ายกำกับที่น่าสนใจให้ลองใช้:

สร้าง Histogram แบบ 2D เพื่อเปรียบเทียบความสัมพันธ์ระหว่างการกระจายตัวสองแบบ ลองเปรียบเทียบ `MaxBodyMass` กับ `MaxLength` Matplotlib มีวิธีในตัวเพื่อแสดงการบรรจบกันโดยใช้สีที่สว่างขึ้น:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
ดูเหมือนว่าจะมีความสัมพันธ์ที่คาดหวังระหว่างสององค์ประกอบนี้ตามแกนที่คาดไว้ โดยมีจุดบรรจบที่แข็งแกร่งจุดหนึ่ง:

![2D plot](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogram ทำงานได้ดีโดยค่าเริ่มต้นสำหรับข้อมูลเชิงตัวเลข แล้วถ้าคุณต้องการดูการกระจายตัวตามข้อมูลข้อความล่ะ?

## สำรวจชุดข้อมูลเพื่อดูการกระจายตัวโดยใช้ข้อมูลข้อความ

ชุดข้อมูลนี้ยังมีข้อมูลที่ดีเกี่ยวกับหมวดหมู่นก รวมถึงสกุล สปีชีส์ และวงศ์ รวมถึงสถานะการอนุรักษ์ ลองเจาะลึกข้อมูลการอนุรักษ์นี้ดู การกระจายตัวของนกตามสถานะการอนุรักษ์เป็นอย่างไร?

> ✅ ในชุดข้อมูลนี้ มีการใช้คำย่อหลายคำเพื่ออธิบายสถานะการอนุรักษ์ คำย่อเหล่านี้มาจาก [IUCN Red List Categories](https://www.iucnredlist.org/) ซึ่งเป็นองค์กรที่จัดทำรายการสถานะของสปีชีส์
> 
> - CR: ใกล้สูญพันธุ์อย่างยิ่ง
> - EN: ใกล้สูญพันธุ์
> - EX: สูญพันธุ์
> - LC: ไม่เป็นที่กังวล
> - NT: ใกล้ถูกคุกคาม
> - VU: มีความเสี่ยง

เนื่องจากค่าดังกล่าวเป็นข้อความ คุณจะต้องทำการแปลงเพื่อสร้าง Histogram โดยใช้ dataframe ที่กรองแล้ว แสดงสถานะการอนุรักษ์ควบคู่กับความกว้างปีกขั้นต่ำ คุณเห็นอะไรบ้าง?

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

![wingspan and conservation collation](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

ดูเหมือนว่าจะไม่มีความสัมพันธ์ที่ดีระหว่างความกว้างปีกขั้นต่ำและสถานะการอนุรักษ์ ลองทดสอบองค์ประกอบอื่น ๆ ในชุดข้อมูลโดยใช้วิธีนี้ คุณสามารถลองใช้ตัวกรองที่แตกต่างกันได้ คุณพบความสัมพันธ์หรือไม่?

## กราฟความหนาแน่น

คุณอาจสังเกตเห็นว่า Histogram ที่เราดูมาจนถึงตอนนี้มีลักษณะเป็น 'ขั้นบันได' และไม่ได้ไหลอย่างราบรื่นในลักษณะโค้ง เพื่อแสดงกราฟความหนาแน่นที่ราบรื่นขึ้น คุณสามารถลองใช้กราฟความหนาแน่น

ในการทำงานกับกราฟความหนาแน่น ลองทำความคุ้นเคยกับไลบรารีการวาดกราฟใหม่ [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)

โหลด Seaborn และลองสร้างกราฟความหนาแน่นพื้นฐาน:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Density plot](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

คุณสามารถเห็นได้ว่ากราฟนี้สะท้อนกราฟก่อนหน้านี้สำหรับข้อมูลความกว้างปีกขั้นต่ำ เพียงแต่ดูราบรื่นขึ้นเล็กน้อย ตามเอกสารของ Seaborn "เมื่อเทียบกับ Histogram, KDE สามารถสร้างกราฟที่ดูไม่รกและตีความได้ง่ายกว่า โดยเฉพาะเมื่อวาดการกระจายตัวหลายแบบ แต่มีโอกาสที่จะเกิดการบิดเบือนหากการกระจายตัวพื้นฐานมีขอบเขตหรือไม่ราบรื่น เช่นเดียวกับ Histogram คุณภาพของการแสดงผลยังขึ้นอยู่กับการเลือกพารามิเตอร์การปรับให้ราบรื่นที่ดี" [source](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) กล่าวคือ จุดที่อยู่นอกกรอบจะทำให้กราฟของคุณแสดงผลผิดปกติ

หากคุณต้องการกลับไปดูเส้น MaxBodyMass ที่เป็นขั้นบันไดในกราฟที่สองที่คุณสร้าง คุณสามารถทำให้มันราบรื่นได้ดีโดยสร้างใหม่ด้วยวิธีนี้:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

หากคุณต้องการเส้นที่ราบรื่น แต่ไม่ราบรื่นเกินไป ให้แก้ไขพารามิเตอร์ `bw_adjust`:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![less smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ อ่านเกี่ยวกับพารามิเตอร์ที่มีอยู่สำหรับกราฟประเภทนี้และทดลองใช้!

กราฟประเภทนี้ให้การแสดงภาพที่อธิบายได้อย่างสวยงาม ด้วยโค้ดเพียงไม่กี่บรรทัด ตัวอย่างเช่น คุณสามารถแสดงความหนาแน่นของมวลร่างกายสูงสุดต่อลำดับของนก:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![bodymass per order](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

คุณยังสามารถทำแผนที่ความหนาแน่นของตัวแปรหลายตัวในกราฟเดียว ลองเปรียบเทียบความยาวสูงสุดและความยาวขั้นต่ำของนกกับสถานะการอนุรักษ์ของพวกมัน:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![multiple densities, superimposed](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

บางทีอาจคุ้มค่าที่จะวิจัยว่ากลุ่มของนกที่ 'มีความเสี่ยง' ตามความยาวของพวกมันมีความหมายหรือไม่

## 🚀 ความท้าทาย

Histogram เป็นกราฟประเภทที่ซับซ้อนกว่ากราฟ scatterplot, bar chart หรือ line chart แบบพื้นฐาน ลองค้นหาตัวอย่างการใช้ Histogram ที่ดีบนอินเทอร์เน็ต พวกมันถูกใช้ในลักษณะใด แสดงอะไร และมักถูกใช้ในสาขาหรือพื้นที่การศึกษาประเภทใด?

## [แบบทดสอบหลังเรียน](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## ทบทวนและศึกษาด้วยตนเอง

ในบทเรียนนี้ คุณได้ใช้ Matplotlib และเริ่มทำงานกับ Seaborn เพื่อแสดงกราฟที่ซับซ้อนมากขึ้น ลองค้นคว้าเกี่ยวกับ `kdeplot` ใน Seaborn ซึ่งเป็น "กราฟความหนาแน่นความน่าจะเป็นต่อเนื่องในหนึ่งหรือหลายมิติ" อ่านเอกสาร [ที่นี่](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) เพื่อทำความเข้าใจวิธีการทำงาน

## งานที่ได้รับมอบหมาย

[ใช้ทักษะของคุณ](assignment.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้