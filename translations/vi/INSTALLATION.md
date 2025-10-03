<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:22:55+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Cài Đặt

Hướng dẫn này sẽ giúp bạn thiết lập môi trường để làm việc với giáo trình Khoa học Dữ liệu cho Người mới bắt đầu.

## Mục Lục

- [Yêu Cầu Trước](../..)
- [Các Tùy Chọn Bắt Đầu Nhanh](../..)
- [Cài Đặt Cục Bộ](../..)
- [Xác Minh Cài Đặt](../..)

## Yêu Cầu Trước

Trước khi bắt đầu, bạn cần:

- Có kiến thức cơ bản về dòng lệnh/terminal
- Tài khoản GitHub (miễn phí)
- Kết nối internet ổn định để thiết lập ban đầu

## Các Tùy Chọn Bắt Đầu Nhanh

### Tùy Chọn 1: GitHub Codespaces (Khuyến nghị cho Người mới bắt đầu)

Cách dễ nhất để bắt đầu là sử dụng GitHub Codespaces, cung cấp một môi trường phát triển hoàn chỉnh ngay trong trình duyệt của bạn.

1. Truy cập [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Nhấp vào menu thả xuống **Code**
3. Chọn tab **Codespaces**
4. Nhấp vào **Create codespace on main**
5. Chờ môi trường khởi tạo (2-3 phút)

Môi trường của bạn đã sẵn sàng với tất cả các phụ thuộc được cài đặt trước!

### Tùy Chọn 2: Phát Triển Cục Bộ

Để làm việc trên máy tính của bạn, hãy làm theo hướng dẫn chi tiết dưới đây.

## Cài Đặt Cục Bộ

### Bước 1: Cài Đặt Git

Git cần thiết để clone repository và theo dõi các thay đổi của bạn.

**Windows:**
- Tải xuống từ [git-scm.com](https://git-scm.com/download/win)
- Chạy trình cài đặt với các thiết lập mặc định

**macOS:**
- Cài đặt qua Homebrew: `brew install git`
- Hoặc tải xuống từ [git-scm.com](https://git-scm.com/download/mac)

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

### Bước 2: Clone Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Bước 3: Cài Đặt Python và Jupyter

Python 3.7 hoặc cao hơn là cần thiết cho các bài học khoa học dữ liệu.

**Windows:**
1. Tải Python từ [python.org](https://www.python.org/downloads/)
2. Trong quá trình cài đặt, chọn "Add Python to PATH"
3. Xác minh cài đặt:
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

### Bước 4: Thiết Lập Môi Trường Python

Khuyến nghị sử dụng môi trường ảo để giữ các phụ thuộc được cách ly.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Bước 5: Cài Đặt Các Gói Python

Cài đặt các thư viện khoa học dữ liệu cần thiết:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Bước 6: Cài Đặt Node.js và npm (Dành cho Ứng Dụng Quiz)

Ứng dụng quiz yêu cầu Node.js và npm.

**Windows/macOS:**
- Tải xuống từ [nodejs.org](https://nodejs.org/) (khuyến nghị phiên bản LTS)
- Chạy trình cài đặt

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

### Bước 7: Cài Đặt Các Phụ Thuộc Ứng Dụng Quiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Bước 8: Cài Đặt Docsify (Tùy Chọn)

Để truy cập tài liệu ngoại tuyến:

```bash
npm install -g docsify-cli
```

## Xác Minh Cài Đặt

### Kiểm Tra Python và Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Trình duyệt của bạn sẽ mở giao diện Jupyter. Bạn có thể điều hướng đến bất kỳ tệp `.ipynb` nào của bài học.

### Kiểm Tra Ứng Dụng Quiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Ứng dụng quiz sẽ có sẵn tại `http://localhost:8080` (hoặc một cổng khác nếu cổng 8080 đang bận).

### Kiểm Tra Máy Chủ Tài Liệu

```bash
# From the root directory of the repository
docsify serve
```

Tài liệu sẽ có sẵn tại `http://localhost:3000`.

## Sử Dụng VS Code Dev Containers

Nếu bạn đã cài đặt Docker, bạn có thể sử dụng VS Code Dev Containers:

1. Cài đặt [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Cài đặt [Visual Studio Code](https://code.visualstudio.com/)
3. Cài đặt [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Mở repository trong VS Code
5. Nhấn `F1` và chọn "Remote-Containers: Reopen in Container"
6. Chờ container được xây dựng (chỉ lần đầu tiên)

## Các Bước Tiếp Theo

- Khám phá [README.md](README.md) để có cái nhìn tổng quan về giáo trình
- Đọc [USAGE.md](USAGE.md) để biết các quy trình làm việc và ví dụ phổ biến
- Kiểm tra [TROUBLESHOOTING.md](TROUBLESHOOTING.md) nếu bạn gặp sự cố
- Xem [CONTRIBUTING.md](CONTRIBUTING.md) nếu bạn muốn đóng góp

## Nhận Trợ Giúp

Nếu bạn gặp sự cố:

1. Kiểm tra hướng dẫn [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Tìm kiếm các [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) hiện có
3. Tham gia cộng đồng [Discord của chúng tôi](https://aka.ms/ds4beginners/discord)
4. Tạo một issue mới với thông tin chi tiết về vấn đề của bạn

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.