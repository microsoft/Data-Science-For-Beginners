<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:21:00+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "th"
}
-->
# คู่มือการติดตั้ง

คู่มือนี้จะช่วยคุณตั้งค่าสภาพแวดล้อมเพื่อใช้งานหลักสูตร Data Science for Beginners

## สารบัญ

- [ข้อกำหนดเบื้องต้น](../..)
- [ตัวเลือกเริ่มต้นอย่างรวดเร็ว](../..)
- [การติดตั้งในเครื่อง](../..)
- [ตรวจสอบการติดตั้ง](../..)

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น คุณควรมี:

- ความคุ้นเคยพื้นฐานกับคำสั่งใน command line/terminal
- บัญชี GitHub (ฟรี)
- การเชื่อมต่ออินเทอร์เน็ตที่เสถียรสำหรับการตั้งค่าเริ่มต้น

## ตัวเลือกเริ่มต้นอย่างรวดเร็ว

### ตัวเลือกที่ 1: GitHub Codespaces (แนะนำสำหรับผู้เริ่มต้น)

วิธีที่ง่ายที่สุดในการเริ่มต้นคือใช้ GitHub Codespaces ซึ่งให้สภาพแวดล้อมการพัฒนาแบบครบวงจรในเบราว์เซอร์ของคุณ

1. ไปที่ [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. คลิกเมนู **Code** แบบดรอปดาวน์
3. เลือกแท็บ **Codespaces**
4. คลิก **Create codespace on main**
5. รอให้สภาพแวดล้อมเริ่มต้น (ประมาณ 2-3 นาที)

ตอนนี้สภาพแวดล้อมของคุณพร้อมใช้งานแล้ว พร้อมด้วย dependencies ที่ติดตั้งไว้ล่วงหน้า!

### ตัวเลือกที่ 2: การพัฒนาในเครื่อง

สำหรับการทำงานบนคอมพิวเตอร์ของคุณเอง ให้ทำตามคำแนะนำโดยละเอียดด้านล่าง

## การติดตั้งในเครื่อง

### ขั้นตอนที่ 1: ติดตั้ง Git

Git จำเป็นสำหรับการโคลน repository และติดตามการเปลี่ยนแปลงของคุณ

**Windows:**
- ดาวน์โหลดจาก [git-scm.com](https://git-scm.com/download/win)
- รันตัวติดตั้งด้วยการตั้งค่าเริ่มต้น

**macOS:**
- ติดตั้งผ่าน Homebrew: `brew install git`
- หรือดาวน์โหลดจาก [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### ขั้นตอนที่ 2: โคลน Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### ขั้นตอนที่ 3: ติดตั้ง Python และ Jupyter

Python 3.7 หรือสูงกว่าจำเป็นสำหรับบทเรียนด้านวิทยาศาสตร์ข้อมูล

**Windows:**
1. ดาวน์โหลด Python จาก [python.org](https://www.python.org/downloads/)
2. ในระหว่างการติดตั้ง ให้เลือก "Add Python to PATH"
3. ตรวจสอบการติดตั้ง:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### ขั้นตอนที่ 4: ตั้งค่าสภาพแวดล้อม Python

แนะนำให้ใช้ virtual environment เพื่อแยก dependencies ออกจากกัน

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### ขั้นตอนที่ 5: ติดตั้ง Python Packages

ติดตั้งไลบรารีที่จำเป็นสำหรับวิทยาศาสตร์ข้อมูล:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ขั้นตอนที่ 6: ติดตั้ง Node.js และ npm (สำหรับแอป Quiz)

แอป Quiz ต้องการ Node.js และ npm

**Windows/macOS:**
- ดาวน์โหลดจาก [nodejs.org](https://nodejs.org/) (แนะนำเวอร์ชัน LTS)
- รันตัวติดตั้ง

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### ขั้นตอนที่ 7: ติดตั้ง Dependencies ของแอป Quiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### ขั้นตอนที่ 8: ติดตั้ง Docsify (ไม่บังคับ)

สำหรับการเข้าถึงเอกสารแบบออฟไลน์:

```bash
npm install -g docsify-cli
```

## ตรวจสอบการติดตั้ง

### ทดสอบ Python และ Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

เบราว์เซอร์ของคุณควรเปิดด้วยอินเทอร์เฟซ Jupyter คุณสามารถไปยังไฟล์ `.ipynb` ของบทเรียนใดก็ได้

### ทดสอบแอป Quiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

แอป Quiz ควรพร้อมใช้งานที่ `http://localhost:8080` (หรือพอร์ตอื่นหากพอร์ต 8080 ถูกใช้งาน)

### ทดสอบเซิร์ฟเวอร์เอกสาร

```bash
# From the root directory of the repository
docsify serve
```

เอกสารควรพร้อมใช้งานที่ `http://localhost:3000`

## การใช้ VS Code Dev Containers

หากคุณติดตั้ง Docker แล้ว คุณสามารถใช้ VS Code Dev Containers:

1. ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. ติดตั้ง [Visual Studio Code](https://code.visualstudio.com/)
3. ติดตั้ง [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. เปิด repository ใน VS Code
5. กด `F1` และเลือก "Remote-Containers: Reopen in Container"
6. รอให้ container สร้างขึ้น (ครั้งแรกเท่านั้น)

## ขั้นตอนถัดไป

- สำรวจ [README.md](README.md) เพื่อดูภาพรวมของหลักสูตร
- อ่าน [USAGE.md](USAGE.md) สำหรับเวิร์กโฟลว์และตัวอย่างทั่วไป
- ตรวจสอบ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) หากคุณพบปัญหา
- ทบทวน [CONTRIBUTING.md](CONTRIBUTING.md) หากคุณต้องการมีส่วนร่วม

## การขอความช่วยเหลือ

หากคุณพบปัญหา:

1. ตรวจสอบคู่มือ [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. ค้นหาปัญหาที่มีอยู่ใน [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. เข้าร่วมชุมชน [Discord](https://aka.ms/ds4beginners/discord)
4. สร้าง issue ใหม่พร้อมข้อมูลรายละเอียดเกี่ยวกับปัญหาของคุณ

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้