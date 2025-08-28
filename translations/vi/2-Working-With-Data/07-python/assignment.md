<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-28T18:11:39+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "vi"
}
-->
# Bài tập xử lý dữ liệu trong Python

Trong bài tập này, chúng tôi yêu cầu bạn phát triển thêm mã mà chúng tôi đã bắt đầu xây dựng trong các thử thách trước. Bài tập gồm hai phần:

## Mô hình hóa sự lây lan của COVID-19

 - [ ] Vẽ đồ thị *R* cho 5-6 quốc gia khác nhau trên một biểu đồ để so sánh, hoặc sử dụng nhiều biểu đồ đặt cạnh nhau.
 - [ ] Xem cách số ca tử vong và số ca hồi phục tương quan với số ca nhiễm bệnh.
 - [ ] Tìm hiểu thời gian trung bình của một bệnh bằng cách trực quan hóa tỷ lệ nhiễm bệnh và tỷ lệ tử vong, đồng thời tìm kiếm một số điểm bất thường. Bạn có thể cần xem xét các quốc gia khác nhau để tìm ra điều này.
 - [ ] Tính tỷ lệ tử vong và cách nó thay đổi theo thời gian. *Bạn có thể muốn tính đến thời gian kéo dài của bệnh (tính theo ngày) để dịch chuyển một chuỗi thời gian trước khi thực hiện các phép tính.*

## Phân tích các bài báo về COVID-19

- [ ] Xây dựng ma trận đồng xuất hiện của các loại thuốc khác nhau và xem loại thuốc nào thường xuất hiện cùng nhau (tức là được đề cập trong một bản tóm tắt). Bạn có thể chỉnh sửa mã để xây dựng ma trận đồng xuất hiện cho các loại thuốc và chẩn đoán.
- [ ] Trực quan hóa ma trận này bằng cách sử dụng heatmap.
- [ ] Mục tiêu mở rộng: trực quan hóa sự đồng xuất hiện của các loại thuốc bằng [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Thư viện này](https://pypi.org/project/chord/) có thể giúp bạn vẽ chord diagram.
- [ ] Mục tiêu mở rộng khác: trích xuất liều lượng của các loại thuốc khác nhau (chẳng hạn như **400mg** trong *uống 400mg chloroquine mỗi ngày*) bằng cách sử dụng biểu thức chính quy, và xây dựng dataframe hiển thị các liều lượng khác nhau cho từng loại thuốc. **Lưu ý**: xem xét các giá trị số nằm gần tên thuốc trong văn bản.

## Tiêu chí đánh giá

Xuất sắc | Đạt yêu cầu | Cần cải thiện
--- | --- | -- |
Hoàn thành tất cả các nhiệm vụ, minh họa bằng đồ họa và giải thích rõ ràng, bao gồm ít nhất một trong hai mục tiêu mở rộng | Hoàn thành hơn 5 nhiệm vụ, không thực hiện mục tiêu mở rộng, hoặc kết quả không rõ ràng | Hoàn thành dưới 5 (nhưng hơn 3) nhiệm vụ, các hình ảnh trực quan không giúp làm rõ vấn đề

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.