<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T20:51:33+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "th"
}
-->
# การแสดงข้อมูลสนามบิน

คุณได้รับ [ฐานข้อมูล](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ที่สร้างขึ้นบน [SQLite](https://sqlite.org/index.html) ซึ่งมีข้อมูลเกี่ยวกับสนามบิน โครงสร้างของฐานข้อมูลแสดงอยู่ด้านล่าง คุณจะใช้ [ส่วนขยาย SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ใน [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) เพื่อแสดงข้อมูลเกี่ยวกับสนามบินในเมืองต่างๆ

## คำแนะนำ

เพื่อเริ่มต้นการทำงาน คุณจำเป็นต้องดำเนินการตามขั้นตอนบางอย่าง คุณจะต้องติดตั้งเครื่องมือและดาวน์โหลดฐานข้อมูลตัวอย่าง

### ตั้งค่าระบบของคุณ

คุณสามารถใช้ Visual Studio Code และส่วนขยาย SQLite เพื่อโต้ตอบกับฐานข้อมูล

1. ไปที่ [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) และทำตามคำแนะนำเพื่อติดตั้ง Visual Studio Code
1. ติดตั้ง [ส่วนขยาย SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ตามคำแนะนำในหน้าของ Marketplace

### ดาวน์โหลดและเปิดฐานข้อมูล

ต่อไปคุณจะดาวน์โหลดและเปิดฐานข้อมูล

1. ดาวน์โหลด [ไฟล์ฐานข้อมูลจาก GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) และบันทึกไว้ในไดเรกทอรี
1. เปิด Visual Studio Code
1. เปิดฐานข้อมูลในส่วนขยาย SQLite โดยเลือก **Ctl-Shift-P** (หรือ **Cmd-Shift-P** บน Mac) และพิมพ์ `SQLite: Open database`
1. เลือก **Choose database from file** และเปิดไฟล์ **airports.db** ที่คุณดาวน์โหลดมาก่อนหน้านี้
1. หลังจากเปิดฐานข้อมูล (คุณจะไม่เห็นการอัปเดตบนหน้าจอ) ให้สร้างหน้าต่างคำสั่งใหม่โดยเลือก **Ctl-Shift-P** (หรือ **Cmd-Shift-P** บน Mac) และพิมพ์ `SQLite: New query`

เมื่อเปิดหน้าต่างคำสั่งใหม่แล้ว คุณสามารถใช้มันเพื่อรันคำสั่ง SQL กับฐานข้อมูล คุณสามารถใช้คำสั่ง **Ctl-Shift-Q** (หรือ **Cmd-Shift-Q** บน Mac) เพื่อรันคำสั่งกับฐานข้อมูล

> [!NOTE] สำหรับข้อมูลเพิ่มเติมเกี่ยวกับส่วนขยาย SQLite คุณสามารถดู [เอกสารประกอบ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## โครงสร้างฐานข้อมูล

โครงสร้างฐานข้อมูลคือการออกแบบและโครงสร้างของตาราง ฐานข้อมูล **airports** มีสองตารางคือ `cities` ซึ่งมีรายการเมืองในสหราชอาณาจักรและไอร์แลนด์ และ `airports` ซึ่งมีรายการสนามบินทั้งหมด เนื่องจากบางเมืองอาจมีสนามบินหลายแห่ง จึงมีการสร้างสองตารางเพื่อจัดเก็บข้อมูล ในการฝึกนี้คุณจะใช้การเชื่อมโยงข้อมูลเพื่อแสดงข้อมูลสำหรับเมืองต่างๆ

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## งานที่ได้รับมอบหมาย

สร้างคำสั่งเพื่อดึงข้อมูลดังต่อไปนี้:

1. ชื่อเมืองทั้งหมดในตาราง `Cities`
1. เมืองทั้งหมดในไอร์แลนด์ในตาราง `Cities`
1. ชื่อสนามบินทั้งหมดพร้อมกับชื่อเมืองและประเทศ
1. สนามบินทั้งหมดในลอนดอน สหราชอาณาจักร

## เกณฑ์การประเมิน

| ดีเยี่ยม | เพียงพอ | ต้องปรับปรุง |

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้