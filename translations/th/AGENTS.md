<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:22:55+00:00",
  "source_file": "AGENTS.md",
  "language_code": "th"
}
-->
# AGENTS.md

## ภาพรวมของโครงการ

Data Science for Beginners เป็นหลักสูตรที่ครอบคลุมระยะเวลา 10 สัปดาห์ รวม 20 บทเรียน ซึ่งสร้างขึ้นโดย Microsoft Azure Cloud Advocates โดยที่เก็บนี้เป็นแหล่งเรียนรู้ที่สอนแนวคิดพื้นฐานของวิทยาศาสตร์ข้อมูลผ่านบทเรียนที่เน้นโครงการ รวมถึง Jupyter notebooks, แบบทดสอบเชิงโต้ตอบ และการมอบหมายงานที่ต้องลงมือปฏิบัติ

**เทคโนโลยีหลัก:**
- **Jupyter Notebooks**: สื่อการเรียนรู้หลักที่ใช้ Python 3
- **Python Libraries**: pandas, numpy, matplotlib สำหรับการวิเคราะห์และการแสดงผลข้อมูล
- **Vue.js 2**: แอปพลิเคชันแบบทดสอบ (โฟลเดอร์ quiz-app)
- **Docsify**: ตัวสร้างเว็บไซต์เอกสารสำหรับการเข้าถึงแบบออฟไลน์
- **Node.js/npm**: การจัดการแพ็กเกจสำหรับส่วนประกอบ JavaScript
- **Markdown**: เนื้อหาบทเรียนและเอกสารทั้งหมด

**สถาปัตยกรรม:**
- ที่เก็บการศึกษาหลายภาษา พร้อมการแปลที่ครอบคลุม
- โครงสร้างแบ่งเป็นโมดูลบทเรียน (1-Introduction ถึง 6-Data-Science-In-Wild)
- แต่ละบทเรียนประกอบด้วย README, notebooks, การมอบหมายงาน และแบบทดสอบ
- แอปพลิเคชันแบบทดสอบ Vue.js แบบสแตนด์อโลนสำหรับการประเมินก่อน/หลังบทเรียน
- รองรับ GitHub Codespaces และ VS Code dev containers

## คำสั่งการตั้งค่า

### การตั้งค่าที่เก็บ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### การตั้งค่าสภาพแวดล้อม Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### การตั้งค่าแอปพลิเคชันแบบทดสอบ
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### เซิร์ฟเวอร์เอกสาร Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### การตั้งค่าโครงการการแสดงผล
สำหรับโครงการการแสดงผล เช่น meaningful-visualizations (บทเรียนที่ 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## เวิร์กโฟลว์การพัฒนา

### การทำงานกับ Jupyter Notebooks
1. เริ่มต้น Jupyter ในโฟลเดอร์รากของที่เก็บ: `jupyter notebook`
2. ไปยังโฟลเดอร์บทเรียนที่ต้องการ
3. เปิดไฟล์ `.ipynb` เพื่อทำแบบฝึกหัด
4. Notebooks มีคำอธิบายและเซลล์โค้ดในตัว
5. ส่วนใหญ่ใช้ pandas, numpy และ matplotlib - ตรวจสอบให้แน่ใจว่าติดตั้งแล้ว

### โครงสร้างบทเรียน
แต่ละบทเรียนมักประกอบด้วย:
- `README.md` - เนื้อหาหลักของบทเรียนพร้อมทฤษฎีและตัวอย่าง
- `notebook.ipynb` - แบบฝึกหัด Jupyter notebook
- `assignment.ipynb` หรือ `assignment.md` - การมอบหมายงานเพื่อฝึกฝน
- โฟลเดอร์ `solution/` - โน้ตบุ๊กและโค้ดคำตอบ
- โฟลเดอร์ `images/` - วัสดุภาพประกอบ

### การพัฒนาแอปพลิเคชันแบบทดสอบ
- แอปพลิเคชัน Vue.js 2 พร้อม hot-reload ระหว่างการพัฒนา
- แบบทดสอบจัดเก็บใน `quiz-app/src/assets/translations/`
- แต่ละภาษามีโฟลเดอร์การแปลของตัวเอง (en, fr, es, ฯลฯ)
- หมายเลขแบบทดสอบเริ่มต้นที่ 0 และไปจนถึง 39 (รวม 40 แบบทดสอบ)

### การเพิ่มการแปลภาษา
- การแปลอยู่ในโฟลเดอร์ `translations/` ที่รากของที่เก็บ
- แต่ละภาษามีโครงสร้างบทเรียนที่สมบูรณ์เหมือนภาษาอังกฤษ
- การแปลอัตโนมัติผ่าน GitHub Actions (co-op-translator.yml)

## คำแนะนำการทดสอบ

### การทดสอบแอปพลิเคชันแบบทดสอบ
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### การทดสอบโน้ตบุ๊ก
- ไม่มีกรอบการทดสอบอัตโนมัติสำหรับโน้ตบุ๊ก
- การตรวจสอบด้วยตนเอง: รันเซลล์ทั้งหมดตามลำดับเพื่อให้แน่ใจว่าไม่มีข้อผิดพลาด
- ตรวจสอบว่าไฟล์ข้อมูลสามารถเข้าถึงได้และผลลัพธ์ถูกสร้างขึ้นอย่างถูกต้อง
- ตรวจสอบว่าการแสดงผลภาพทำงานได้อย่างเหมาะสม

### การทดสอบเอกสาร
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### การตรวจสอบคุณภาพโค้ด
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## แนวทางการเขียนโค้ด

### Python (Jupyter Notebooks)
- ปฏิบัติตามแนวทางสไตล์ PEP 8 สำหรับโค้ด Python
- ใช้ชื่อตัวแปรที่ชัดเจนซึ่งอธิบายข้อมูลที่กำลังวิเคราะห์
- รวมเซลล์ markdown พร้อมคำอธิบายก่อนเซลล์โค้ด
- ให้เซลล์โค้ดมุ่งเน้นไปที่แนวคิดหรือการดำเนินการเดียว
- ใช้ pandas สำหรับการจัดการข้อมูล, matplotlib สำหรับการแสดงผล
- รูปแบบการนำเข้าทั่วไป:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- ปฏิบัติตามแนวทางสไตล์ Vue.js 2 และแนวปฏิบัติที่ดีที่สุด
- การกำหนดค่า ESLint ใน `quiz-app/package.json`
- ใช้ส่วนประกอบ Vue แบบไฟล์เดียว (.vue files)
- รักษาสถาปัตยกรรมที่เน้นส่วนประกอบ
- รัน `npm run lint` ก่อนการ commit การเปลี่ยนแปลง

### เอกสาร Markdown
- ใช้ลำดับชั้นหัวข้อที่ชัดเจน (# ## ### ฯลฯ)
- รวมบล็อกโค้ดพร้อมตัวระบุภาษา
- เพิ่มข้อความ alt สำหรับภาพ
- ลิงก์ไปยังบทเรียนและแหล่งข้อมูลที่เกี่ยวข้อง
- รักษาความยาวบรรทัดให้อ่านง่าย

### การจัดระเบียบไฟล์
- เนื้อหาบทเรียนในโฟลเดอร์ที่มีหมายเลข (01-defining-data-science ฯลฯ)
- คำตอบในโฟลเดอร์ย่อย `solution/` โดยเฉพาะ
- การแปลโครงสร้างเหมือนภาษาอังกฤษในโฟลเดอร์ `translations/`
- เก็บไฟล์ข้อมูลใน `data/` หรือโฟลเดอร์เฉพาะบทเรียน

## การสร้างและการปรับใช้

### การปรับใช้แอปพลิเคชันแบบทดสอบ
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### การปรับใช้ Azure Static Web Apps
แอป quiz-app สามารถปรับใช้กับ Azure Static Web Apps:
1. สร้างทรัพยากร Azure Static Web App
2. เชื่อมต่อกับที่เก็บ GitHub
3. กำหนดค่าการตั้งค่าการสร้าง:
   - ตำแหน่งแอป: `quiz-app`
   - ตำแหน่งผลลัพธ์: `dist`
4. GitHub Actions workflow จะปรับใช้อัตโนมัติเมื่อมีการ push

### เว็บไซต์เอกสาร
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- ที่เก็บรวมการกำหนดค่า dev container
- Codespaces ตั้งค่าสภาพแวดล้อม Python และ Node.js โดยอัตโนมัติ
- เปิดที่เก็บใน Codespace ผ่าน UI ของ GitHub
- การติดตั้งการพึ่งพาทั้งหมดจะดำเนินการโดยอัตโนมัติ

## แนวทางการส่ง Pull Request

### ก่อนการส่ง
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### รูปแบบชื่อ PR
- ใช้ชื่อที่ชัดเจนและอธิบายได้
- รูปแบบ: `[Component] คำอธิบายสั้นๆ`
- ตัวอย่าง:
  - `[Lesson 7] แก้ไขข้อผิดพลาดการนำเข้า Python notebook`
  - `[Quiz App] เพิ่มการแปลภาษาเยอรมัน`
  - `[Docs] อัปเดต README พร้อมข้อกำหนดเบื้องต้นใหม่`

### การตรวจสอบที่จำเป็น
- ตรวจสอบให้แน่ใจว่าโค้ดทั้งหมดทำงานได้โดยไม่มีข้อผิดพลาด
- ยืนยันว่าโน้ตบุ๊กทำงานได้สมบูรณ์
- ยืนยันว่าแอป Vue.js สร้างสำเร็จ
- ตรวจสอบว่าเอกสารลิงก์ทำงานได้
- ทดสอบแอปพลิเคชันแบบทดสอบหากมีการแก้ไข
- ยืนยันว่าโครงสร้างการแปลยังคงสอดคล้องกัน

### แนวทางการมีส่วนร่วม
- ปฏิบัติตามสไตล์และรูปแบบโค้ดที่มีอยู่
- เพิ่มความคิดเห็นอธิบายสำหรับตรรกะที่ซับซ้อน
- อัปเดตเอกสารที่เกี่ยวข้อง
- ทดสอบการเปลี่ยนแปลงในโมดูลบทเรียนต่างๆ หากเกี่ยวข้อง
- อ่านไฟล์ CONTRIBUTING.md

## หมายเหตุเพิ่มเติม

### ไลบรารีที่ใช้บ่อย
- **pandas**: การจัดการและวิเคราะห์ข้อมูล
- **numpy**: การคำนวณเชิงตัวเลข
- **matplotlib**: การแสดงผลและการพล็อตข้อมูล
- **seaborn**: การแสดงผลข้อมูลเชิงสถิติ (บางบทเรียน)
- **scikit-learn**: การเรียนรู้ของเครื่อง (บทเรียนขั้นสูง)

### การทำงานกับไฟล์ข้อมูล
- ไฟล์ข้อมูลอยู่ในโฟลเดอร์ `data/` หรือไดเรกทอรีเฉพาะบทเรียน
- โน้ตบุ๊กส่วนใหญ่คาดหวังไฟล์ข้อมูลในเส้นทางสัมพัทธ์
- ไฟล์ CSV เป็นรูปแบบข้อมูลหลัก
- บางบทเรียนใช้ JSON สำหรับตัวอย่างข้อมูลที่ไม่ใช่เชิงสัมพันธ์

### การสนับสนุนหลายภาษา
- การแปลมากกว่า 40 ภาษา ผ่าน GitHub Actions อัตโนมัติ
- เวิร์กโฟลว์การแปลใน `.github/workflows/co-op-translator.yml`
- การแปลในโฟลเดอร์ `translations/` พร้อมรหัสภาษา
- การแปลแบบทดสอบใน `quiz-app/src/assets/translations/`

### ตัวเลือกสภาพแวดล้อมการพัฒนา
1. **การพัฒนาในเครื่อง**: ติดตั้ง Python, Jupyter, Node.js ในเครื่อง
2. **GitHub Codespaces**: สภาพแวดล้อมการพัฒนาแบบคลาวด์ทันที
3. **VS Code Dev Containers**: การพัฒนาบนคอนเทนเนอร์ในเครื่อง
4. **Binder**: เปิดโน้ตบุ๊กในคลาวด์ (หากกำหนดค่าไว้)

### แนวทางเนื้อหาบทเรียน
- แต่ละบทเรียนเป็นแบบสแตนด์อโลนแต่สร้างขึ้นจากแนวคิดก่อนหน้า
- แบบทดสอบก่อนบทเรียนทดสอบความรู้ก่อนหน้า
- แบบทดสอบหลังบทเรียนเสริมสร้างการเรียนรู้
- การมอบหมายงานให้โอกาสฝึกฝน
- Sketchnotes ให้สรุปภาพรวม

### การแก้ไขปัญหาทั่วไป

**ปัญหา Jupyter Kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**ข้อผิดพลาด npm Install:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**ข้อผิดพลาดการนำเข้าในโน้ตบุ๊ก:**
- ตรวจสอบให้แน่ใจว่าติดตั้งไลบรารีที่จำเป็นทั้งหมด
- ตรวจสอบความเข้ากันได้ของเวอร์ชัน Python (แนะนำ Python 3.7+)
- ตรวจสอบให้แน่ใจว่าสภาพแวดล้อมเสมือนถูกเปิดใช้งาน

**Docsify ไม่โหลด:**
- ตรวจสอบว่าคุณกำลังให้บริการจากโฟลเดอร์รากของที่เก็บ
- ตรวจสอบว่า `index.html` มีอยู่
- ตรวจสอบการเข้าถึงเครือข่ายที่เหมาะสม (พอร์ต 3000)

### ข้อควรพิจารณาด้านประสิทธิภาพ
- ชุดข้อมูลขนาดใหญ่อาจใช้เวลาโหลดในโน้ตบุ๊ก
- การแสดงผลภาพอาจช้าสำหรับพล็อตที่ซับซ้อน
- เซิร์ฟเวอร์ dev ของ Vue.js เปิดใช้งาน hot-reload สำหรับการทำซ้ำอย่างรวดเร็ว
- การสร้างสำหรับการใช้งานจริงได้รับการปรับให้เหมาะสมและย่อขนาด

### หมายเหตุด้านความปลอดภัย
- ห้าม commit ข้อมูลหรือข้อมูลประจำตัวที่ละเอียดอ่อน
- ใช้ตัวแปรสภาพแวดล้อมสำหรับคีย์ API ในบทเรียนคลาวด์
- บทเรียนที่เกี่ยวข้องกับ Azure อาจต้องใช้ข้อมูลประจำตัวบัญชี Azure
- อัปเดตการพึ่งพาเพื่อรับแพตช์ความปลอดภัย

## การมีส่วนร่วมในการแปล
- การแปลอัตโนมัติจัดการผ่าน GitHub Actions
- ยินดีต้อนรับการแก้ไขด้วยตนเองเพื่อความถูกต้องของการแปล
- ปฏิบัติตามโครงสร้างโฟลเดอร์การแปลที่มีอยู่
- อัปเดตลิงก์แบบทดสอบให้รวมพารามิเตอร์ภาษา: `?loc=fr`
- ทดสอบบทเรียนที่แปลเพื่อให้แน่ใจว่าการแสดงผลถูกต้อง

## แหล่งข้อมูลที่เกี่ยวข้อง
- หลักสูตรหลัก: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- ฟอรัมสนทนา: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- หลักสูตรอื่นๆ ของ Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## การดูแลรักษาโครงการ
- อัปเดตเป็นประจำเพื่อให้เนื้อหาทันสมัย
- ยินดีต้อนรับการมีส่วนร่วมจากชุมชน
- ติดตามปัญหาบน GitHub
- PRs ตรวจสอบโดยผู้ดูแลหลักสูตร
- การตรวจสอบและอัปเดตเนื้อหารายเดือน

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้