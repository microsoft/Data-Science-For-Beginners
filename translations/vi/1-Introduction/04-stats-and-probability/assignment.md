<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-28T18:53:56+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "vi"
}
-->
# Nghiên cứu nhỏ về bệnh tiểu đường

Trong bài tập này, chúng ta sẽ làm việc với một tập dữ liệu nhỏ về bệnh nhân tiểu đường được lấy từ [đây](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | TUỔI | GIỚI TÍNH | BMI | HUYẾT ÁP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|-----------|-----|----------|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Hướng dẫn

* Mở [notebook bài tập](assignment.ipynb) trong môi trường jupyter notebook
* Hoàn thành tất cả các nhiệm vụ được liệt kê trong notebook, cụ thể:
   * [ ] Tính giá trị trung bình và phương sai cho tất cả các giá trị
   * [ ] Vẽ biểu đồ hộp cho BMI, huyết áp và Y dựa trên giới tính
   * [ ] Phân phối của các biến Tuổi, Giới tính, BMI và Y là gì?
   * [ ] Kiểm tra mối tương quan giữa các biến khác nhau và sự tiến triển của bệnh (Y)
   * [ ] Kiểm tra giả thuyết rằng mức độ tiến triển của bệnh tiểu đường khác nhau giữa nam và nữ
   
## Tiêu chí đánh giá

Xuất sắc | Đạt yêu cầu | Cần cải thiện
--- | --- | -- |
Hoàn thành tất cả các nhiệm vụ yêu cầu, minh họa bằng đồ thị và giải thích rõ ràng | Hoàn thành hầu hết các nhiệm vụ, thiếu giải thích hoặc kết luận từ đồ thị và/hoặc giá trị thu được | Chỉ hoàn thành các nhiệm vụ cơ bản như tính toán giá trị trung bình/phương sai và vẽ đồ thị cơ bản, không đưa ra kết luận từ dữ liệu

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.