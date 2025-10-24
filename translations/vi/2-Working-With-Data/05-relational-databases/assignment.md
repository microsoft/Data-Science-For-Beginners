<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:56:51+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "vi"
}
-->
# Hiển thị dữ liệu sân bay

Bạn đã được cung cấp một [cơ sở dữ liệu](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) được xây dựng trên [SQLite](https://sqlite.org/index.html) chứa thông tin về các sân bay. Lược đồ được hiển thị bên dưới. Bạn sẽ sử dụng [phần mở rộng SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) trong [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) để hiển thị thông tin về các sân bay của các thành phố khác nhau.

## Hướng dẫn

Để bắt đầu bài tập, bạn cần thực hiện một vài bước. Bạn sẽ cần cài đặt một số công cụ và tải xuống cơ sở dữ liệu mẫu.

### Cài đặt hệ thống của bạn

Bạn có thể sử dụng Visual Studio Code và phần mở rộng SQLite để tương tác với cơ sở dữ liệu.

1. Truy cập [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) và làm theo hướng dẫn để cài đặt Visual Studio Code
1. Cài đặt phần mở rộng [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) như được hướng dẫn trên trang Marketplace

### Tải xuống và mở cơ sở dữ liệu

Tiếp theo, bạn sẽ tải xuống và mở cơ sở dữ liệu.

1. Tải xuống [tệp cơ sở dữ liệu từ GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) và lưu vào một thư mục
1. Mở Visual Studio Code
1. Mở cơ sở dữ liệu trong phần mở rộng SQLite bằng cách chọn **Ctl-Shift-P** (hoặc **Cmd-Shift-P** trên Mac) và nhập `SQLite: Open database`
1. Chọn **Choose database from file** và mở tệp **airports.db** mà bạn đã tải xuống trước đó
1. Sau khi mở cơ sở dữ liệu (bạn sẽ không thấy cập nhật trên màn hình), tạo một cửa sổ truy vấn mới bằng cách chọn **Ctl-Shift-P** (hoặc **Cmd-Shift-P** trên Mac) và nhập `SQLite: New query`

Khi đã mở, cửa sổ truy vấn mới có thể được sử dụng để chạy các câu lệnh SQL trên cơ sở dữ liệu. Bạn có thể sử dụng lệnh **Ctl-Shift-Q** (hoặc **Cmd-Shift-Q** trên Mac) để chạy các truy vấn trên cơ sở dữ liệu.

> [!NOTE] 
> Để biết thêm thông tin về phần mở rộng SQLite, bạn có thể tham khảo [tài liệu](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Lược đồ cơ sở dữ liệu

Lược đồ của cơ sở dữ liệu là thiết kế và cấu trúc bảng của nó. Cơ sở dữ liệu **airports** có hai bảng, `cities`, chứa danh sách các thành phố ở Vương quốc Anh và Ireland, và `airports`, chứa danh sách tất cả các sân bay. Vì một số thành phố có thể có nhiều sân bay, hai bảng đã được tạo để lưu trữ thông tin. Trong bài tập này, bạn sẽ sử dụng các phép nối để hiển thị thông tin cho các thành phố khác nhau.

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

## Bài tập

Tạo các truy vấn để trả về thông tin sau:

1. tất cả tên thành phố trong bảng `Cities`
1. tất cả các thành phố ở Ireland trong bảng `Cities`
1. tất cả tên sân bay cùng với thành phố và quốc gia của chúng
1. tất cả các sân bay ở London, Vương quốc Anh

## Tiêu chí đánh giá

| Xuất sắc | Đạt yêu cầu | Cần cải thiện |
| --------- | ----------- | ------------- |

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.