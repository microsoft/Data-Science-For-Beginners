<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1441550a0d789796b2821e04f7f4cc94",
  "translation_date": "2025-08-26T22:40:18+00:00",
  "source_file": "3-Data-Visualization/README.md",
  "language_code": "th"
}
-->
# การสร้างภาพข้อมูล

![ผึ้งบนดอกลาเวนเดอร์](../../../translated_images/bee.0aa1d91132b12e3a8994b9ca12816d05ce1642010d9b8be37f8d37365ba845cf.th.jpg)
> ภาพถ่ายโดย <a href="https://unsplash.com/@jenna2980?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jenna Lee</a> บน <a href="https://unsplash.com/s/photos/bees-in-a-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

การสร้างภาพข้อมูลเป็นหนึ่งในงานที่สำคัญที่สุดของนักวิทยาศาสตร์ข้อมูล ภาพหนึ่งภาพมีค่ามากกว่าคำพูดนับพันคำ และการสร้างภาพข้อมูลสามารถช่วยให้คุณระบุส่วนที่น่าสนใจในข้อมูลของคุณ เช่น จุดพุ่งสูงสุด ค่าผิดปกติ การจัดกลุ่ม แนวโน้ม และอื่นๆ ซึ่งช่วยให้คุณเข้าใจเรื่องราวที่ข้อมูลของคุณพยายามจะบอก

ในบทเรียนทั้งห้านี้ คุณจะได้สำรวจข้อมูลที่มาจากธรรมชาติและสร้างภาพข้อมูลที่น่าสนใจและสวยงามโดยใช้เทคนิคต่างๆ

| หมายเลขหัวข้อ | หัวข้อ | บทเรียนที่เกี่ยวข้อง | ผู้เขียน |
| :-----------: | :--: | :-----------: | :----: |
| 1. | การสร้างภาพปริมาณ | <ul> <li> [Python](09-visualization-quantities/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/09-visualization-quantities) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 2. | การสร้างภาพการกระจายตัว | <ul> <li> [Python](10-visualization-distributions/README.md)</li>  <li>[R](../../../3-Data-Visualization/R/10-visualization-distributions) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 3. | การสร้างภาพสัดส่วน | <ul> <li> [Python](11-visualization-proportions/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 4. | การสร้างภาพความสัมพันธ์ | <ul> <li> [Python](12-visualization-relationships/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |
| 5. | การสร้างภาพที่มีความหมาย | <ul> <li> [Python](13-meaningful-visualizations/README.md)</li>  <li>[R](../../../3-Data-Visualization) </li> </ul>|<ul> <li> [Jen Looper](https://twitter.com/jenlooper)</li><li> [Vidushi Gupta](https://github.com/Vidushi-Gupta)</li> <li>[Jasleen Sondhi](https://github.com/jasleen101010)</li></ul> |

### เครดิต

บทเรียนการสร้างภาพข้อมูลเหล่านี้เขียนขึ้นด้วยความรัก 🌸 โดย [Jen Looper](https://twitter.com/jenlooper), [Jasleen Sondhi](https://github.com/jasleen101010) และ [Vidushi Gupta](https://github.com/Vidushi-Gupta)

🍯 ข้อมูลเกี่ยวกับการผลิตน้ำผึ้งในสหรัฐอเมริกามาจากโปรเจกต์ของ Jessica Li บน [Kaggle](https://www.kaggle.com/jessicali9530/honey-production) โดยข้อมูล [data](https://usda.library.cornell.edu/concern/publications/rn301137d) นี้ได้มาจาก [กระทรวงเกษตรของสหรัฐอเมริกา](https://www.nass.usda.gov/About_NASS/index.php)

🍄 ข้อมูลเกี่ยวกับเห็ดมาจาก [Kaggle](https://www.kaggle.com/hatterasdunton/mushroom-classification-updated-dataset) ที่ปรับปรุงโดย Hatteras Dunton ชุดข้อมูลนี้ประกอบด้วยคำอธิบายของตัวอย่างสมมติที่สอดคล้องกับเห็ด 23 สายพันธุ์ในตระกูล Agaricus และ Lepiota โดยข้อมูลเห็ดนี้นำมาจาก The Audubon Society Field Guide to North American Mushrooms (1981) และถูกบริจาคให้กับ UCI ML 27 ในปี 1987

🦆 ข้อมูลเกี่ยวกับนกในมินนิโซตามาจาก [Kaggle](https://www.kaggle.com/hannahcollins/minnesota-birds) ซึ่งดึงข้อมูลจาก [Wikipedia](https://en.wikipedia.org/wiki/List_of_birds_of_Minnesota) โดย Hannah Collins

ชุดข้อมูลทั้งหมดนี้ได้รับอนุญาตภายใต้ [CC0: Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/).

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้