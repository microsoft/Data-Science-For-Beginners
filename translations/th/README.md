<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-29T09:59:07+00:00",
  "source_file": "README.md",
  "language_code": "th"
}
-->
# วิทยาศาสตร์ข้อมูลสำหรับผู้เริ่มต้น - หลักสูตร

Azure Cloud Advocates ที่ Microsoft มีความยินดีที่จะนำเสนอหลักสูตร 10 สัปดาห์ 20 บทเรียนเกี่ยวกับวิทยาศาสตร์ข้อมูล แต่ละบทเรียนประกอบด้วยแบบทดสอบก่อนและหลังบทเรียน คำแนะนำที่เขียนไว้สำหรับการทำบทเรียน โซลูชัน และงานมอบหมาย หลักสูตรที่เน้นการสร้างโปรเจกต์ช่วยให้คุณเรียนรู้ผ่านการลงมือทำ ซึ่งเป็นวิธีที่พิสูจน์แล้วว่าทำให้ทักษะใหม่ๆ ติดตัวได้อย่างมีประสิทธิภาพ

**ขอขอบคุณผู้เขียนของเรา:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 ขอขอบคุณเป็นพิเศษ 🙏 แก่ [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) ผู้เขียน ผู้ตรวจสอบ และผู้มีส่วนร่วมในเนื้อหา,** โดยเฉพาะ Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![ภาพสเก็ตช์โดย @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.th.png)|
|:---:|
| วิทยาศาสตร์ข้อมูลสำหรับผู้เริ่มต้น - _ภาพสเก็ตช์โดย [@nitya](https://twitter.com/nitya)_ |

### 🌐 การสนับสนุนหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติและอัปเดตเสมอ)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](./README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md) | [Ukrainian](../uk/README.md) | [Burmese (Myanmar)](../my/README.md)

**หากคุณต้องการให้มีการสนับสนุนภาษาเพิ่มเติม รายการภาษาที่รองรับสามารถดูได้ [ที่นี่](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### เข้าร่วมชุมชนของเรา 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# คุณเป็นนักเรียนหรือไม่?

เริ่มต้นด้วยแหล่งข้อมูลต่อไปนี้:

- [หน้าศูนย์กลางนักเรียน](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) ในหน้านี้ คุณจะพบแหล่งข้อมูลสำหรับผู้เริ่มต้น ชุดเครื่องมือสำหรับนักเรียน และแม้กระทั่งวิธีการรับบัตรกำนัลสอบฟรี นี่คือหน้าที่คุณควรบุ๊กมาร์กและตรวจสอบเป็นระยะๆ เนื่องจากเรามีการเปลี่ยนแปลงเนื้อหาอย่างน้อยทุกเดือน
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) เข้าร่วมชุมชนระดับโลกของนักเรียนแอมบาสเดอร์ นี่อาจเป็นทางเข้าสู่ Microsoft ของคุณ

# เริ่มต้นใช้งาน

> **ครูผู้สอน**: เราได้ [รวมคำแนะนำบางส่วน](for-teachers.md) เกี่ยวกับวิธีการใช้หลักสูตรนี้ เราต้องการรับฟังความคิดเห็นของคุณ [ในฟอรัมการสนทนาของเรา](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[นักเรียน](https://aka.ms/student-page)**: หากต้องการใช้หลักสูตรนี้ด้วยตัวเอง ให้ fork repo ทั้งหมดและทำแบบฝึกหัดด้วยตัวเอง โดยเริ่มจากแบบทดสอบก่อนบทเรียน จากนั้นอ่านบทเรียนและทำกิจกรรมที่เหลือ พยายามสร้างโปรเจกต์โดยการทำความเข้าใจบทเรียนแทนที่จะคัดลอกรหัสโซลูชัน อย่างไรก็ตาม รหัสโซลูชันนั้นมีอยู่ในโฟลเดอร์ /solutions ในแต่ละบทเรียนที่เน้นโปรเจกต์ อีกแนวคิดหนึ่งคือการสร้างกลุ่มการเรียนรู้กับเพื่อนๆ และเรียนรู้เนื้อหาด้วยกัน สำหรับการศึกษาเพิ่มเติม เราขอแนะนำ [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)

## พบกับทีมงาน

[![วิดีโอโปรโมต](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "วิดีโอโปรโมต")

**Gif โดย** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 คลิกที่ภาพด้านบนเพื่อดูวิดีโอเกี่ยวกับโปรเจกต์และผู้ที่สร้างมันขึ้นมา!

## วิธีการสอน

เราได้เลือกใช้หลักการสอนสองข้อในขณะที่สร้างหลักสูตรนี้: การทำให้เป็นโปรเจกต์และการมีแบบทดสอบบ่อยครั้ง ภายในสิ้นสุดซีรีส์นี้ นักเรียนจะได้เรียนรู้หลักการพื้นฐานของวิทยาศาสตร์ข้อมูล รวมถึงแนวคิดด้านจริยธรรม การเตรียมข้อมูล วิธีการทำงานกับข้อมูลในรูปแบบต่างๆ การสร้างภาพข้อมูล การวิเคราะห์ข้อมูล กรณีการใช้งานจริงของวิทยาศาสตร์ข้อมูล และอื่นๆ

นอกจากนี้ แบบทดสอบที่มีความเสี่ยงต่ำก่อนชั้นเรียนจะช่วยตั้งเป้าหมายให้นักเรียนมุ่งเน้นไปที่การเรียนรู้หัวข้อหนึ่งๆ ในขณะที่แบบทดสอบหลังชั้นเรียนช่วยเสริมสร้างความจำ หลักสูตรนี้ถูกออกแบบให้ยืดหยุ่นและสนุกสนาน และสามารถเรียนได้ทั้งแบบเต็มหลักสูตรหรือบางส่วน โปรเจกต์เริ่มต้นจากขนาดเล็กและมีความซับซ้อนเพิ่มขึ้นเรื่อยๆ จนถึงสิ้นสุดรอบ 10 สัปดาห์
> ค้นหา [หลักปฏิบัติของเรา](CODE_OF_CONDUCT.md), [การมีส่วนร่วม](CONTRIBUTING.md), [แนวทางการแปล](TRANSLATIONS.md) เรายินดีรับฟังความคิดเห็นที่สร้างสรรค์ของคุณ!
## แต่ละบทเรียนประกอบด้วย:

- สเก็ตโน้ต (ถ้ามี)
- วิดีโอเสริม (ถ้ามี)
- แบบทดสอบอุ่นเครื่องก่อนเริ่มบทเรียน
- บทเรียนที่เขียนไว้
- สำหรับบทเรียนที่เน้นโครงการ มีคำแนะนำทีละขั้นตอนเกี่ยวกับวิธีสร้างโครงการ
- การตรวจสอบความรู้
- ความท้าทาย
- การอ่านเพิ่มเติม
- การบ้าน
- [แบบทดสอบหลังบทเรียน](https://ff-quizzes.netlify.app/en/)

> **หมายเหตุเกี่ยวกับแบบทดสอบ**: แบบทดสอบทั้งหมดอยู่ในโฟลเดอร์ Quiz-App ซึ่งมีทั้งหมด 40 แบบทดสอบ แต่ละแบบทดสอบมี 3 คำถาม แบบทดสอบเหล่านี้เชื่อมโยงจากในบทเรียน แต่แอปแบบทดสอบสามารถรันได้ในเครื่องหรือดีพลอยไปยัง Azure โดยทำตามคำแนะนำในโฟลเดอร์ `quiz-app` ขณะนี้กำลังอยู่ในกระบวนการแปลเป็นภาษาท้องถิ่น

## บทเรียน

|![ สเก็ตโน้ตโดย @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.th.png)|
|:---:|
| วิทยาศาสตร์ข้อมูลสำหรับผู้เริ่มต้น: แผนที่เส้นทาง - _สเก็ตโน้ตโดย [@nitya](https://twitter.com/nitya)_ |

| หมายเลขบทเรียน | หัวข้อ | กลุ่มบทเรียน | วัตถุประสงค์การเรียนรู้ | บทเรียนที่เชื่อมโยง | ผู้เขียน |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | การนิยามวิทยาศาสตร์ข้อมูล | [บทนำ](1-Introduction/README.md) | เรียนรู้แนวคิดพื้นฐานของวิทยาศาสตร์ข้อมูลและความสัมพันธ์กับปัญญาประดิษฐ์ การเรียนรู้ของเครื่อง และข้อมูลขนาดใหญ่ | [บทเรียน](1-Introduction/01-defining-data-science/README.md) [วิดีโอ](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | จริยธรรมในวิทยาศาสตร์ข้อมูล | [บทนำ](1-Introduction/README.md) | แนวคิดเกี่ยวกับจริยธรรมในข้อมูล ความท้าทาย และกรอบการทำงาน | [บทเรียน](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | การนิยามข้อมูล | [บทนำ](1-Introduction/README.md) | วิธีการจำแนกข้อมูลและแหล่งข้อมูลที่พบบ่อย | [บทเรียน](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | บทนำสถิติและความน่าจะเป็น | [บทนำ](1-Introduction/README.md) | เทคนิคทางคณิตศาสตร์ของความน่าจะเป็นและสถิติในการทำความเข้าใจข้อมูล | [บทเรียน](1-Introduction/04-stats-and-probability/README.md) [วิดีโอ](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | การทำงานกับข้อมูลเชิงสัมพันธ์ | [การทำงานกับข้อมูล](2-Working-With-Data/README.md) | บทนำเกี่ยวกับข้อมูลเชิงสัมพันธ์และพื้นฐานของการสำรวจและวิเคราะห์ข้อมูลเชิงสัมพันธ์ด้วย Structured Query Language หรือ SQL (อ่านว่า "ซีเควล") | [บทเรียน](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | การทำงานกับข้อมูล NoSQL | [การทำงานกับข้อมูล](2-Working-With-Data/README.md) | บทนำเกี่ยวกับข้อมูลที่ไม่ใช่เชิงสัมพันธ์ ประเภทต่างๆ และพื้นฐานของการสำรวจและวิเคราะห์ฐานข้อมูลเอกสาร | [บทเรียน](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | การทำงานกับ Python | [การทำงานกับข้อมูล](2-Working-With-Data/README.md) | พื้นฐานการใช้ Python ในการสำรวจข้อมูลด้วยไลบรารี เช่น Pandas แนะนำให้มีความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Python | [บทเรียน](2-Working-With-Data/07-python/README.md) [วิดีโอ](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | การเตรียมข้อมูล | [การทำงานกับข้อมูล](2-Working-With-Data/README.md) | หัวข้อเกี่ยวกับเทคนิคการทำความสะอาดและแปลงข้อมูลเพื่อจัดการกับปัญหาข้อมูลที่ขาดหาย ไม่ถูกต้อง หรือไม่สมบูรณ์ | [บทเรียน](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | การสร้างภาพข้อมูลเชิงปริมาณ | [การสร้างภาพข้อมูล](3-Data-Visualization/README.md) | เรียนรู้วิธีใช้ Matplotlib ในการสร้างภาพข้อมูลนก 🦆 | [บทเรียน](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | การสร้างภาพการกระจายของข้อมูล | [การสร้างภาพข้อมูล](3-Data-Visualization/README.md) | การสร้างภาพการสังเกตและแนวโน้มภายในช่วงข้อมูล | [บทเรียน](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | การสร้างภาพสัดส่วน | [การสร้างภาพข้อมูล](3-Data-Visualization/README.md) | การสร้างภาพเปอร์เซ็นต์แบบแยกและแบบกลุ่ม | [บทเรียน](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | การสร้างภาพความสัมพันธ์ | [การสร้างภาพข้อมูล](3-Data-Visualization/README.md) | การสร้างภาพการเชื่อมโยงและความสัมพันธ์ระหว่างชุดข้อมูลและตัวแปร | [บทเรียน](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | การสร้างภาพที่มีความหมาย | [การสร้างภาพข้อมูล](3-Data-Visualization/README.md) | เทคนิคและคำแนะนำในการทำให้การสร้างภาพของคุณมีคุณค่าเพื่อการแก้ปัญหาและการให้ข้อมูลเชิงลึกที่มีประสิทธิภาพ | [บทเรียน](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | บทนำวงจรชีวิตวิทยาศาสตร์ข้อมูล | [วงจรชีวิต](4-Data-Science-Lifecycle/README.md) | บทนำเกี่ยวกับวงจรชีวิตวิทยาศาสตร์ข้อมูลและขั้นตอนแรกของการรวบรวมและดึงข้อมูล | [บทเรียน](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | การวิเคราะห์ | [วงจรชีวิต](4-Data-Science-Lifecycle/README.md) | ขั้นตอนนี้ในวงจรชีวิตวิทยาศาสตร์ข้อมูลมุ่งเน้นไปที่เทคนิคการวิเคราะห์ข้อมูล | [บทเรียน](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | การสื่อสาร | [วงจรชีวิต](4-Data-Science-Lifecycle/README.md) | ขั้นตอนนี้ในวงจรชีวิตวิทยาศาสตร์ข้อมูลมุ่งเน้นไปที่การนำเสนอข้อมูลเชิงลึกจากข้อมูลในรูปแบบที่ช่วยให้ผู้ตัดสินใจเข้าใจได้ง่ายขึ้น | [บทเรียน](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | วิทยาศาสตร์ข้อมูลบนคลาวด์ | [ข้อมูลบนคลาวด์](5-Data-Science-In-Cloud/README.md) | ชุดบทเรียนนี้แนะนำวิทยาศาสตร์ข้อมูลบนคลาวด์และประโยชน์ของมัน | [บทเรียน](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) และ [Maud](https://twitter.com/maudstweets) |
| 18 | วิทยาศาสตร์ข้อมูลบนคลาวด์ | [ข้อมูลบนคลาวด์](5-Data-Science-In-Cloud/README.md) | การฝึกอบรมโมเดลโดยใช้เครื่องมือ Low Code |[บทเรียน](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) และ [Maud](https://twitter.com/maudstweets) |
| 19 | วิทยาศาสตร์ข้อมูลบนคลาวด์ | [ข้อมูลบนคลาวด์](5-Data-Science-In-Cloud/README.md) | การดีพลอยโมเดลด้วย Azure Machine Learning Studio | [บทเรียน](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) และ [Maud](https://twitter.com/maudstweets) |
| 20 | วิทยาศาสตร์ข้อมูลในโลกจริง | [ในโลกจริง](6-Data-Science-In-Wild/README.md) | โครงการที่ขับเคลื่อนด้วยวิทยาศาสตร์ข้อมูลในโลกจริง | [บทเรียน](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

ทำตามขั้นตอนเหล่านี้เพื่อเปิดตัวอย่างนี้ใน Codespace:
1. คลิกเมนูแบบเลื่อนลง Code และเลือกตัวเลือก Open with Codespaces
2. เลือก + New codespace ที่ด้านล่างของแผง
สำหรับข้อมูลเพิ่มเติม โปรดดู [เอกสาร GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace)

## VSCode Remote - Containers
ทำตามขั้นตอนเหล่านี้เพื่อเปิด repo นี้ใน container โดยใช้เครื่องในพื้นที่ของคุณและ VSCode ด้วยส่วนขยาย VS Code Remote - Containers:

1. หากนี่เป็นครั้งแรกที่คุณใช้ development container โปรดตรวจสอบให้แน่ใจว่าระบบของคุณตรงตามข้อกำหนดเบื้องต้น (เช่น ติดตั้ง Docker) ใน [เอกสารเริ่มต้นใช้งาน](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)

ในการใช้ repository นี้ คุณสามารถเปิด repository ใน Docker volume ที่แยกออกมา:

**หมายเหตุ**: ภายใต้ฮูด คำสั่งนี้จะใช้ Remote-Containers: **Clone Repository in Container Volume...** เพื่อโคลนซอร์สโค้ดใน Docker volume แทนที่จะเป็นระบบไฟล์ในเครื่อง [Volumes](https://docs.docker.com/storage/volumes/) เป็นกลไกที่แนะนำสำหรับการเก็บข้อมูล container

หรือเปิดเวอร์ชันที่โคลนหรือดาวน์โหลดในเครื่องของ repository:

- โคลน repository นี้ไปยังระบบไฟล์ในเครื่องของคุณ
- กด F1 และเลือกคำสั่ง **Remote-Containers: Open Folder in Container...**
- เลือกสำเนาที่โคลนของโฟลเดอร์นี้ รอให้ container เริ่มต้น และลองใช้งาน

## การเข้าถึงแบบออฟไลน์

คุณสามารถรันเอกสารนี้แบบออฟไลน์ได้โดยใช้ [Docsify](https://docsify.js.org/#/). Fork repo นี้, [ติดตั้ง Docsify](https://docsify.js.org/#/quickstart) บนเครื่องในพื้นที่ของคุณ จากนั้นในโฟลเดอร์ root ของ repo นี้ ให้พิมพ์ `docsify serve` เว็บไซต์จะถูกให้บริการบนพอร์ต 3000 บน localhost ของคุณ: `localhost:3000`

> หมายเหตุ โน้ตบุ๊กจะไม่ถูกเรนเดอร์ผ่าน Docsify ดังนั้นเมื่อคุณต้องการรันโน้ตบุ๊ก ให้ทำสิ่งนั้นแยกต่างหากใน VS Code โดยใช้ Python kernel

## หลักสูตรอื่นๆ

ทีมของเราผลิตหลักสูตรอื่นๆ! ลองดู:

- [Generative AI for Beginners](https://aka.ms/genai-beginners)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI with JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative AI with Java](https://aka.ms/genaijava)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101) 
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners)
- [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้