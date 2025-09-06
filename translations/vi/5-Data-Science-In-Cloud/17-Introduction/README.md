<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T23:31:31+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Khoa học Dữ liệu trên Đám mây

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Khoa học Dữ liệu trên Đám mây: Giới thiệu - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

Trong bài học này, bạn sẽ tìm hiểu các nguyên tắc cơ bản về Đám mây, sau đó bạn sẽ thấy tại sao việc sử dụng các dịch vụ Đám mây để thực hiện các dự án khoa học dữ liệu của mình lại thú vị và chúng ta sẽ xem một số ví dụ về các dự án khoa học dữ liệu được thực hiện trên Đám mây.

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Đám mây là gì?

Đám mây, hay Điện toán Đám mây, là việc cung cấp một loạt các dịch vụ điện toán trả phí theo nhu cầu được lưu trữ trên một cơ sở hạ tầng qua internet. Các dịch vụ bao gồm các giải pháp như lưu trữ, cơ sở dữ liệu, mạng, phần mềm, phân tích và các dịch vụ thông minh.

Chúng ta thường phân biệt Đám mây Công cộng, Đám mây Riêng tư và Đám mây Lai như sau:

* Đám mây công cộng: Đám mây công cộng được sở hữu và vận hành bởi một nhà cung cấp dịch vụ đám mây bên thứ ba, cung cấp tài nguyên điện toán của mình qua Internet cho công chúng.
* Đám mây riêng tư: Đề cập đến các tài nguyên điện toán đám mây được sử dụng độc quyền bởi một doanh nghiệp hoặc tổ chức duy nhất, với các dịch vụ và cơ sở hạ tầng được duy trì trên một mạng riêng.
* Đám mây lai: Đám mây lai là một hệ thống kết hợp giữa đám mây công cộng và đám mây riêng. Người dùng chọn một trung tâm dữ liệu tại chỗ, đồng thời cho phép dữ liệu và ứng dụng chạy trên một hoặc nhiều đám mây công cộng.

Hầu hết các dịch vụ điện toán đám mây thuộc ba loại chính: Cơ sở hạ tầng như một Dịch vụ (IaaS), Nền tảng như một Dịch vụ (PaaS) và Phần mềm như một Dịch vụ (SaaS).

* Cơ sở hạ tầng như một Dịch vụ (IaaS): Người dùng thuê cơ sở hạ tầng CNTT như máy chủ và máy ảo (VM), lưu trữ, mạng, hệ điều hành.
* Nền tảng như một Dịch vụ (PaaS): Người dùng thuê một môi trường để phát triển, kiểm thử, triển khai và quản lý các ứng dụng phần mềm. Người dùng không cần lo lắng về việc thiết lập hoặc quản lý cơ sở hạ tầng cơ bản của máy chủ, lưu trữ, mạng và cơ sở dữ liệu cần thiết cho việc phát triển.
* Phần mềm như một Dịch vụ (SaaS): Người dùng truy cập các ứng dụng phần mềm qua Internet, theo yêu cầu và thường theo hình thức đăng ký. Người dùng không cần lo lắng về việc lưu trữ và quản lý ứng dụng phần mềm, cơ sở hạ tầng cơ bản hoặc bảo trì, như nâng cấp phần mềm và vá lỗi bảo mật.

Một số nhà cung cấp Đám mây lớn nhất là Amazon Web Services, Google Cloud Platform và Microsoft Azure.

## Tại sao chọn Đám mây cho Khoa học Dữ liệu?

Các nhà phát triển và chuyên gia CNTT chọn làm việc với Đám mây vì nhiều lý do, bao gồm:

* Đổi mới: Bạn có thể tăng cường ứng dụng của mình bằng cách tích hợp các dịch vụ sáng tạo do các nhà cung cấp Đám mây tạo ra trực tiếp vào ứng dụng của bạn.
* Linh hoạt: Bạn chỉ trả tiền cho các dịch vụ mà bạn cần và có thể chọn từ một loạt các dịch vụ. Bạn thường trả theo nhu cầu và điều chỉnh các dịch vụ của mình theo nhu cầu thay đổi.
* Ngân sách: Bạn không cần đầu tư ban đầu để mua phần cứng và phần mềm, thiết lập và vận hành các trung tâm dữ liệu tại chỗ, và bạn chỉ cần trả tiền cho những gì bạn sử dụng.
* Khả năng mở rộng: Tài nguyên của bạn có thể mở rộng theo nhu cầu của dự án, nghĩa là ứng dụng của bạn có thể sử dụng nhiều hoặc ít sức mạnh tính toán, lưu trữ và băng thông hơn, bằng cách thích nghi với các yếu tố bên ngoài tại bất kỳ thời điểm nào.
* Năng suất: Bạn có thể tập trung vào công việc kinh doanh của mình thay vì dành thời gian cho các nhiệm vụ có thể được quản lý bởi người khác, chẳng hạn như quản lý trung tâm dữ liệu.
* Độ tin cậy: Điện toán Đám mây cung cấp nhiều cách để liên tục sao lưu dữ liệu của bạn và bạn có thể thiết lập các kế hoạch khôi phục thảm họa để duy trì hoạt động kinh doanh và dịch vụ của mình, ngay cả trong thời kỳ khủng hoảng.
* Bảo mật: Bạn có thể hưởng lợi từ các chính sách, công nghệ và kiểm soát giúp tăng cường bảo mật cho dự án của mình.

Đây là một số lý do phổ biến nhất khiến mọi người chọn sử dụng các dịch vụ Đám mây. Bây giờ chúng ta đã hiểu rõ hơn về Đám mây là gì và những lợi ích chính của nó, hãy xem xét cụ thể hơn công việc của các nhà khoa học dữ liệu và nhà phát triển làm việc với dữ liệu, và cách Đám mây có thể giúp họ giải quyết một số thách thức mà họ có thể gặp phải:

* Lưu trữ lượng lớn dữ liệu: Thay vì mua, quản lý và bảo vệ các máy chủ lớn, bạn có thể lưu trữ dữ liệu của mình trực tiếp trên đám mây, với các giải pháp như Azure Cosmos DB, Azure SQL Database và Azure Data Lake Storage.
* Thực hiện tích hợp dữ liệu: Tích hợp dữ liệu là một phần thiết yếu của Khoa học Dữ liệu, cho phép bạn chuyển từ việc thu thập dữ liệu sang hành động. Với các dịch vụ tích hợp dữ liệu được cung cấp trên đám mây, bạn có thể thu thập, chuyển đổi và tích hợp dữ liệu từ nhiều nguồn khác nhau vào một kho dữ liệu duy nhất, với Data Factory.
* Xử lý dữ liệu: Xử lý lượng lớn dữ liệu đòi hỏi rất nhiều sức mạnh tính toán, và không phải ai cũng có quyền truy cập vào các máy đủ mạnh cho việc đó, đó là lý do tại sao nhiều người chọn tận dụng trực tiếp sức mạnh tính toán khổng lồ của đám mây để chạy và triển khai các giải pháp của họ.
* Sử dụng các dịch vụ phân tích dữ liệu: Các dịch vụ đám mây như Azure Synapse Analytics, Azure Stream Analytics và Azure Databricks giúp bạn biến dữ liệu của mình thành những thông tin có thể hành động.
* Sử dụng các dịch vụ học máy và trí tuệ dữ liệu: Thay vì bắt đầu từ đầu, bạn có thể sử dụng các thuật toán học máy được cung cấp bởi nhà cung cấp đám mây, với các dịch vụ như AzureML. Bạn cũng có thể sử dụng các dịch vụ nhận thức như chuyển giọng nói thành văn bản, chuyển văn bản thành giọng nói, thị giác máy tính và nhiều hơn nữa.

## Ví dụ về Khoa học Dữ liệu trên Đám mây

Hãy làm rõ hơn điều này bằng cách xem xét một vài kịch bản.

### Phân tích cảm xúc mạng xã hội theo thời gian thực
Chúng ta sẽ bắt đầu với một kịch bản thường được nghiên cứu bởi những người mới bắt đầu với học máy: phân tích cảm xúc mạng xã hội theo thời gian thực.

Giả sử bạn điều hành một trang web tin tức và muốn tận dụng dữ liệu trực tiếp để hiểu nội dung mà độc giả của bạn có thể quan tâm. Để biết thêm về điều đó, bạn có thể xây dựng một chương trình thực hiện phân tích cảm xúc theo thời gian thực từ các bài đăng trên Twitter, về các chủ đề liên quan đến độc giả của bạn.

Các chỉ số chính bạn sẽ xem xét là khối lượng tweet về các chủ đề cụ thể (hashtag) và cảm xúc, được xác định bằng các công cụ phân tích thực hiện phân tích cảm xúc xung quanh các chủ đề được chỉ định.

Các bước cần thiết để tạo dự án này bao gồm:

* Tạo một trung tâm sự kiện để thu thập dữ liệu đầu vào, sẽ thu thập dữ liệu từ Twitter.
* Cấu hình và khởi động một ứng dụng khách Twitter, sẽ gọi các API Streaming của Twitter.
* Tạo một công việc Stream Analytics.
* Chỉ định đầu vào và truy vấn công việc.
* Tạo một đầu ra và chỉ định đầu ra công việc.
* Khởi động công việc.

Để xem quy trình đầy đủ, hãy tham khảo [tài liệu](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Phân tích các bài báo khoa học
Hãy xem một ví dụ khác về một dự án được tạo bởi [Dmitry Soshnikov](http://soshnikov.com), một trong những tác giả của chương trình học này.

Dmitry đã tạo ra một công cụ phân tích các bài báo về COVID. Bằng cách xem xét dự án này, bạn sẽ thấy cách bạn có thể tạo ra một công cụ trích xuất kiến thức từ các bài báo khoa học, thu thập thông tin chi tiết và giúp các nhà nghiên cứu điều hướng qua các bộ sưu tập bài báo lớn một cách hiệu quả.

Hãy xem các bước khác nhau được sử dụng cho dự án này:

* Trích xuất và tiền xử lý thông tin với [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Sử dụng [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) để xử lý song song.
* Lưu trữ và truy vấn thông tin với [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Tạo một bảng điều khiển tương tác để khám phá và trực quan hóa dữ liệu bằng Power BI.

Để xem quy trình đầy đủ, hãy truy cập [blog của Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Như bạn có thể thấy, chúng ta có thể tận dụng các dịch vụ Đám mây theo nhiều cách để thực hiện Khoa học Dữ liệu.

## Ghi chú cuối

Nguồn:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Câu hỏi sau bài giảng

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Bài tập

[Nghiên cứu Thị trường](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.