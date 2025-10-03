<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:43:22+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Khắc Phục Sự Cố

Hướng dẫn này cung cấp các giải pháp cho những vấn đề thường gặp khi bạn làm việc với chương trình học "Data Science for Beginners".

## Mục Lục

- [Vấn Đề Python và Jupyter](../..)
- [Vấn Đề Gói và Phụ Thuộc](../..)
- [Vấn Đề Jupyter Notebook](../..)
- [Vấn Đề Ứng Dụng Quiz](../..)
- [Vấn Đề Git và GitHub](../..)
- [Vấn Đề Tài Liệu Docsify](../..)
- [Vấn Đề Dữ Liệu và Tệp](../..)
- [Vấn Đề Hiệu Suất](../..)
- [Nhận Hỗ Trợ Thêm](../..)

## Vấn Đề Python và Jupyter

### Python Không Tìm Thấy hoặc Sai Phiên Bản

**Vấn đề:** `python: command not found` hoặc sai phiên bản Python

**Giải pháp:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Giải pháp cho Windows:**
1. Cài đặt lại Python từ [python.org](https://www.python.org/)
2. Trong quá trình cài đặt, chọn "Add Python to PATH"
3. Khởi động lại terminal/command prompt

### Vấn Đề Kích Hoạt Môi Trường Ảo

**Vấn đề:** Môi trường ảo không kích hoạt được

**Giải pháp:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Xác minh kích hoạt:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Vấn Đề Kernel Jupyter

**Vấn đề:** "Kernel không tìm thấy" hoặc "Kernel liên tục bị lỗi"

**Giải pháp:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Vấn đề:** Sai phiên bản Python trong Jupyter

**Giải pháp:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Vấn Đề Gói và Phụ Thuộc

### Lỗi Import

**Vấn đề:** `ModuleNotFoundError: No module named 'pandas'` (hoặc các gói khác)

**Giải pháp:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Lỗi Cài Đặt Pip

**Vấn đề:** `pip install` gặp lỗi quyền

**Giải pháp:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Vấn đề:** `pip install` gặp lỗi chứng chỉ SSL

**Giải pháp:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Xung Đột Phiên Bản Gói

**Vấn đề:** Phiên bản gói không tương thích

**Giải pháp:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Vấn Đề Jupyter Notebook

### Jupyter Không Khởi Động

**Vấn đề:** Lệnh `jupyter notebook` không tìm thấy

**Giải pháp:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Không Tải hoặc Lưu Được

**Vấn đề:** "Notebook không tải được" hoặc lỗi lưu

**Giải pháp:**

1. Kiểm tra quyền tệp
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Kiểm tra tệp có bị hỏng không
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Xóa bộ nhớ cache của Jupyter
```bash
jupyter notebook --clear-cache
```

### Cell Không Thực Thi

**Vấn đề:** Cell bị kẹt ở "In [*]" hoặc chạy mãi không xong

**Giải pháp:**

1. **Ngắt kernel**: Nhấn nút "Interrupt" hoặc bấm `I, I`
2. **Khởi động lại kernel**: Menu Kernel → Restart
3. **Kiểm tra vòng lặp vô hạn** trong mã của bạn
4. **Xóa output**: Cell → All Output → Clear

### Biểu Đồ Không Hiển Thị

**Vấn đề:** Biểu đồ `matplotlib` không hiển thị trong notebook

**Giải pháp:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Cách thay thế cho biểu đồ tương tác:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Vấn Đề Ứng Dụng Quiz

### npm install Gặp Lỗi

**Vấn đề:** Lỗi khi chạy `npm install`

**Giải pháp:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Ứng Dụng Quiz Không Khởi Động

**Vấn đề:** `npm run serve` gặp lỗi

**Giải pháp:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Cổng Đã Được Sử Dụng

**Vấn đề:** "Port 8080 is already in use"

**Giải pháp:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Quiz Không Tải hoặc Trang Trống

**Vấn đề:** Ứng dụng quiz tải nhưng hiển thị trang trống

**Giải pháp:**

1. Kiểm tra lỗi trong console của trình duyệt (F12)
2. Xóa bộ nhớ cache và cookie của trình duyệt
3. Thử trình duyệt khác
4. Đảm bảo JavaScript được bật
5. Kiểm tra xem trình chặn quảng cáo có gây cản trở không

```bash
# Rebuild the app
npm run build
npm run serve
```

## Vấn Đề Git và GitHub

### Git Không Được Nhận Diện

**Vấn đề:** `git: command not found`

**Giải pháp:**

**Windows:**
- Cài đặt Git từ [git-scm.com](https://git-scm.com/)
- Khởi động lại terminal sau khi cài đặt

**macOS:**

> **Lưu ý:** Nếu bạn chưa cài đặt Homebrew, hãy làm theo hướng dẫn tại [https://brew.sh/](https://brew.sh/) để cài đặt trước.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Clone Gặp Lỗi

**Vấn đề:** `git clone` gặp lỗi xác thực

**Giải pháp:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Vấn đề:** Xác thực SSH key thất bại

**Giải pháp:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Vấn Đề Tài Liệu Docsify

### Lệnh Docsify Không Tìm Thấy

**Vấn đề:** `docsify: command not found`

**Giải pháp:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Tài Liệu Không Tải

**Vấn đề:** Docsify chạy nhưng nội dung không tải

**Giải pháp:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Hình Ảnh Không Hiển Thị

**Vấn đề:** Hình ảnh hiển thị biểu tượng liên kết bị hỏng

**Giải pháp:**

1. Kiểm tra đường dẫn hình ảnh có phải là tương đối không
2. Đảm bảo tệp hình ảnh tồn tại trong kho lưu trữ
3. Xóa bộ nhớ cache của trình duyệt
4. Xác minh phần mở rộng tệp khớp (phân biệt chữ hoa/thường trên một số hệ thống)

## Vấn Đề Dữ Liệu và Tệp

### Lỗi Không Tìm Thấy Tệp

**Vấn đề:** `FileNotFoundError` khi tải dữ liệu

**Giải pháp:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### Lỗi Đọc CSV

**Vấn đề:** Lỗi khi đọc tệp CSV

**Giải pháp:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Lỗi Bộ Nhớ Với Tập Dữ Liệu Lớn

**Vấn đề:** `MemoryError` khi tải tệp lớn

**Giải pháp:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Vấn Đề Hiệu Suất

### Hiệu Suất Notebook Chậm

**Vấn đề:** Notebook chạy rất chậm

**Giải pháp:**

1. **Khởi động lại kernel và xóa output**
   - Kernel → Restart & Clear Output

2. **Đóng các notebook không sử dụng**

3. **Tối ưu hóa mã:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Lấy mẫu tập dữ liệu lớn:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Trình Duyệt Bị Treo

**Vấn đề:** Trình duyệt bị treo hoặc không phản hồi

**Giải pháp:**

1. Đóng các tab không sử dụng
2. Xóa bộ nhớ cache của trình duyệt
3. Tăng bộ nhớ trình duyệt (Chrome: `chrome://settings/system`)
4. Sử dụng JupyterLab thay thế:
```bash
pip install jupyterlab
jupyter lab
```

## Nhận Hỗ Trợ Thêm

### Trước Khi Yêu Cầu Hỗ Trợ

1. Kiểm tra hướng dẫn khắc phục sự cố này
2. Tìm kiếm [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Xem lại [INSTALLATION.md](INSTALLATION.md) và [USAGE.md](USAGE.md)
4. Thử tìm kiếm thông báo lỗi trên mạng

### Cách Yêu Cầu Hỗ Trợ

Khi tạo một issue hoặc yêu cầu hỗ trợ, hãy bao gồm:

1. **Hệ Điều Hành**: Windows, macOS, hoặc Linux (phiên bản nào)
2. **Phiên Bản Python**: Chạy `python --version`
3. **Thông Báo Lỗi**: Sao chép toàn bộ thông báo lỗi
4. **Các Bước Tái Hiện**: Những gì bạn đã làm trước khi lỗi xảy ra
5. **Những Gì Bạn Đã Thử**: Các giải pháp bạn đã thử

**Ví dụ:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Tài Nguyên Cộng Đồng

- **GitHub Issues**: [Tạo một issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Tham gia cộng đồng của chúng tôi](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Diễn đàn Hỏi & Đáp](https://docs.microsoft.com/answers/)

### Tài Liệu Liên Quan

- [INSTALLATION.md](INSTALLATION.md) - Hướng dẫn cài đặt
- [USAGE.md](USAGE.md) - Cách sử dụng chương trình học
- [CONTRIBUTING.md](CONTRIBUTING.md) - Cách đóng góp
- [README.md](README.md) - Tổng quan về dự án

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.