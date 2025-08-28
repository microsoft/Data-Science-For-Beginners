<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-28T19:00:53+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Đạo đức Dữ liệu

|![ Sketchnote bởi [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Đạo đức Khoa học Dữ liệu - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

---

Chúng ta đều là công dân dữ liệu sống trong một thế giới được số hóa bởi dữ liệu.

Xu hướng thị trường cho thấy rằng đến năm 2022, cứ 3 tổ chức lớn thì sẽ có 1 tổ chức mua và bán dữ liệu của họ thông qua các [Thị trường và Sàn giao dịch](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Là **Nhà phát triển ứng dụng**, chúng ta sẽ thấy việc tích hợp các thông tin chi tiết dựa trên dữ liệu và tự động hóa dựa trên thuật toán vào trải nghiệm người dùng hàng ngày trở nên dễ dàng và rẻ hơn. Nhưng khi AI trở nên phổ biến, chúng ta cũng cần hiểu những tác hại tiềm ẩn do [việc vũ khí hóa](https://www.youtube.com/watch?v=TQHs8SA1qpk) các thuật toán này ở quy mô lớn.

Xu hướng cũng chỉ ra rằng chúng ta sẽ tạo ra và tiêu thụ hơn [180 zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) dữ liệu vào năm 2025. Là **Nhà khoa học dữ liệu**, điều này mang lại cho chúng ta mức độ truy cập chưa từng có vào dữ liệu cá nhân. Điều này có nghĩa là chúng ta có thể xây dựng hồ sơ hành vi của người dùng và ảnh hưởng đến việc ra quyết định theo cách tạo ra một [ảo tưởng về sự lựa chọn tự do](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) trong khi có thể hướng người dùng đến các kết quả mà chúng ta mong muốn. Nó cũng đặt ra các câu hỏi rộng hơn về quyền riêng tư dữ liệu và bảo vệ người dùng.

Đạo đức dữ liệu giờ đây là _hàng rào cần thiết_ cho khoa học và kỹ thuật dữ liệu, giúp chúng ta giảm thiểu các tác hại tiềm ẩn và hậu quả không mong muốn từ các hành động dựa trên dữ liệu của mình. [Chu kỳ Hype của Gartner về AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) xác định các xu hướng liên quan đến đạo đức kỹ thuật số, AI có trách nhiệm và quản trị AI là các yếu tố thúc đẩy các xu hướng lớn hơn xung quanh _dân chủ hóa_ và _công nghiệp hóa_ AI.

![Chu kỳ Hype của Gartner về AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Trong bài học này, chúng ta sẽ khám phá lĩnh vực thú vị về đạo đức dữ liệu - từ các khái niệm và thách thức cốt lõi, đến các nghiên cứu điển hình và các khái niệm AI ứng dụng như quản trị - giúp thiết lập văn hóa đạo đức trong các nhóm và tổ chức làm việc với dữ liệu và AI.

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Định nghĩa cơ bản

Hãy bắt đầu bằng cách hiểu các thuật ngữ cơ bản.

Từ "đạo đức" xuất phát từ [từ tiếng Hy Lạp "ethikos"](https://en.wikipedia.org/wiki/Ethics) (và gốc của nó "ethos") có nghĩa là _tính cách hoặc bản chất đạo đức_.

**Đạo đức** là về các giá trị chung và nguyên tắc đạo đức chi phối hành vi của chúng ta trong xã hội. Đạo đức không dựa trên luật pháp mà dựa trên các chuẩn mực được chấp nhận rộng rãi về điều gì là "đúng và sai". Tuy nhiên, các cân nhắc đạo đức có thể ảnh hưởng đến các sáng kiến quản trị doanh nghiệp và quy định của chính phủ, tạo ra nhiều động lực hơn cho việc tuân thủ.

**Đạo đức dữ liệu** là một [nhánh mới của đạo đức](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) nghiên cứu và đánh giá các vấn đề đạo đức liên quan đến _dữ liệu, thuật toán và các thực hành tương ứng_. Ở đây, **"dữ liệu"** tập trung vào các hành động liên quan đến việc tạo ra, ghi lại, quản lý, xử lý, phổ biến, chia sẻ và sử dụng; **"thuật toán"** tập trung vào AI, tác nhân, học máy và robot; và **"thực hành"** tập trung vào các chủ đề như đổi mới có trách nhiệm, lập trình, hack và các quy tắc đạo đức.

**Đạo đức ứng dụng** là [việc áp dụng thực tế các cân nhắc đạo đức](https://en.wikipedia.org/wiki/Applied_ethics). Đây là quá trình điều tra tích cực các vấn đề đạo đức trong bối cảnh _hành động, sản phẩm và quy trình thực tế_, và thực hiện các biện pháp khắc phục để đảm bảo rằng chúng vẫn phù hợp với các giá trị đạo đức đã xác định.

**Văn hóa đạo đức** là về [_hiện thực hóa_ đạo đức ứng dụng](https://hbr.org/2019/05/how-to-design-an-ethical-organization) để đảm bảo rằng các nguyên tắc và thực hành đạo đức của chúng ta được áp dụng một cách nhất quán và có thể mở rộng trên toàn tổ chức. Các văn hóa đạo đức thành công xác định các nguyên tắc đạo đức trên toàn tổ chức, cung cấp các động lực có ý nghĩa cho việc tuân thủ, và củng cố các chuẩn mực đạo đức bằng cách khuyến khích và khuếch đại các hành vi mong muốn ở mọi cấp độ của tổ chức.

## Các khái niệm về đạo đức

Trong phần này, chúng ta sẽ thảo luận về các khái niệm như **giá trị chung** (nguyên tắc) và **thách thức đạo đức** (vấn đề) đối với đạo đức dữ liệu - và khám phá **các nghiên cứu điển hình** giúp bạn hiểu các khái niệm này trong bối cảnh thực tế.

### 1. Nguyên tắc đạo đức

Mọi chiến lược đạo đức dữ liệu đều bắt đầu bằng việc xác định _các nguyên tắc đạo đức_ - "giá trị chung" mô tả các hành vi chấp nhận được và hướng dẫn các hành động tuân thủ trong các dự án dữ liệu & AI của chúng ta. Bạn có thể xác định chúng ở cấp độ cá nhân hoặc nhóm. Tuy nhiên, hầu hết các tổ chức lớn đều phác thảo chúng trong một tuyên bố sứ mệnh hoặc khung đạo đức AI được xác định ở cấp độ doanh nghiệp và được thực thi nhất quán trên tất cả các nhóm.

**Ví dụ:** Tuyên bố sứ mệnh [AI có trách nhiệm](https://www.microsoft.com/en-us/ai/responsible-ai) của Microsoft nêu rõ: _"Chúng tôi cam kết thúc đẩy AI dựa trên các nguyên tắc đạo đức đặt con người lên hàng đầu"_ - xác định 6 nguyên tắc đạo đức trong khung dưới đây:

![AI có trách nhiệm tại Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Hãy cùng khám phá ngắn gọn các nguyên tắc này. _Minh bạch_ và _trách nhiệm_ là các giá trị nền tảng mà các nguyên tắc khác được xây dựng dựa trên - vì vậy hãy bắt đầu từ đó:

* [**Trách nhiệm**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) khiến các nhà thực hành _chịu trách nhiệm_ về các hoạt động dữ liệu & AI của họ, và tuân thủ các nguyên tắc đạo đức này.
* [**Minh bạch**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) đảm bảo rằng các hành động dữ liệu và AI _có thể hiểu được_ (có thể diễn giải) đối với người dùng, giải thích điều gì và tại sao đằng sau các quyết định.
* [**Công bằng**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - tập trung vào việc đảm bảo AI đối xử _công bằng với tất cả mọi người_, giải quyết bất kỳ thiên vị xã hội-kỹ thuật nào trong dữ liệu và hệ thống.
* [**Độ tin cậy & An toàn**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - đảm bảo rằng AI hoạt động _nhất quán_ với các giá trị đã xác định, giảm thiểu các tác hại tiềm ẩn hoặc hậu quả không mong muốn.
* [**Quyền riêng tư & Bảo mật**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - là về việc hiểu nguồn gốc dữ liệu và cung cấp _quyền riêng tư dữ liệu và các bảo vệ liên quan_ cho người dùng.
* [**Tính bao gồm**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - là về việc thiết kế các giải pháp AI với ý định, điều chỉnh chúng để đáp ứng _một loạt các nhu cầu và khả năng của con người_.

> 🚨 Hãy nghĩ về tuyên bố sứ mệnh đạo đức dữ liệu của bạn có thể là gì. Khám phá các khung đạo đức AI từ các tổ chức khác - đây là các ví dụ từ [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), và [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Các giá trị chung của họ có điểm gì tương đồng? Các nguyên tắc này liên quan như thế nào đến sản phẩm AI hoặc ngành mà họ hoạt động?

### 2. Thách thức đạo đức

Khi chúng ta đã xác định các nguyên tắc đạo đức, bước tiếp theo là đánh giá các hành động dữ liệu và AI của chúng ta để xem liệu chúng có phù hợp với các giá trị chung đó hay không. Hãy nghĩ về các hành động của bạn trong hai danh mục: _thu thập dữ liệu_ và _thiết kế thuật toán_.

Với việc thu thập dữ liệu, các hành động có thể liên quan đến **dữ liệu cá nhân** hoặc thông tin nhận dạng cá nhân (PII) cho các cá nhân có thể nhận dạng. Điều này bao gồm [các mục dữ liệu không cá nhân đa dạng](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) mà _tập hợp lại_ có thể nhận dạng một cá nhân. Các thách thức đạo đức có thể liên quan đến _quyền riêng tư dữ liệu_, _quyền sở hữu dữ liệu_, và các chủ đề liên quan như _sự đồng ý được thông báo_ và _quyền sở hữu trí tuệ_ của người dùng.

Với thiết kế thuật toán, các hành động sẽ liên quan đến việc thu thập & quản lý **bộ dữ liệu**, sau đó sử dụng chúng để huấn luyện & triển khai **mô hình dữ liệu** dự đoán kết quả hoặc tự động hóa quyết định trong các bối cảnh thực tế. Các thách thức đạo đức có thể phát sinh từ _thiên vị bộ dữ liệu_, _vấn đề chất lượng dữ liệu_, _sự không công bằng_, và _sự sai lệch_ trong thuật toán - bao gồm một số vấn đề mang tính hệ thống.

Trong cả hai trường hợp, các thách thức đạo đức làm nổi bật các lĩnh vực mà hành động của chúng ta có thể gặp xung đột với các giá trị chung. Để phát hiện, giảm thiểu, giảm bớt hoặc loại bỏ các mối quan ngại này - chúng ta cần đặt ra các câu hỏi đạo đức "có/không" liên quan đến hành động của mình, sau đó thực hiện các hành động khắc phục khi cần thiết. Hãy cùng xem xét một số thách thức đạo đức và các câu hỏi đạo đức mà chúng đặt ra:

#### 2.1 Quyền sở hữu dữ liệu

Việc thu thập dữ liệu thường liên quan đến dữ liệu cá nhân có thể nhận dạng các đối tượng dữ liệu. [Quyền sở hữu dữ liệu](https://permission.io/blog/data-ownership) là về _kiểm soát_ và [_quyền của người dùng_](https://permission.io/blog/data-ownership) liên quan đến việc tạo ra, xử lý và phổ biến dữ liệu.

Các câu hỏi đạo đức cần đặt ra là:
* Ai sở hữu dữ liệu? (người dùng hay tổ chức)
* Các quyền mà đối tượng dữ liệu có là gì? (ví dụ: truy cập, xóa, di chuyển)
* Các quyền mà tổ chức có là gì? (ví dụ: chỉnh sửa đánh giá người dùng độc hại)

#### 2.2 Sự đồng ý được thông báo

[Sự đồng ý được thông báo](https://legaldictionary.net/informed-consent/) định nghĩa hành động người dùng đồng ý với một hành động (như thu thập dữ liệu) với _sự hiểu biết đầy đủ_ về các sự kiện liên quan bao gồm mục đích, rủi ro tiềm ẩn, và các lựa chọn thay thế.

Các câu hỏi cần khám phá ở đây là:
* Người dùng (đối tượng dữ liệu) có cho phép thu thập và sử dụng dữ liệu không?
* Người dùng có hiểu mục đích mà dữ liệu đó được thu thập không?
* Người dùng có hiểu các rủi ro tiềm ẩn từ sự tham gia của họ không?

#### 2.3 Quyền sở hữu trí tuệ

[Quyền sở hữu trí tuệ](https://en.wikipedia.org/wiki/Intellectual_property) đề cập đến các sáng tạo vô hình xuất phát từ sáng kiến của con người, có thể _có giá trị kinh tế_ đối với cá nhân hoặc doanh nghiệp.

Các câu hỏi cần khám phá ở đây là:
* Dữ liệu được thu thập có giá trị kinh tế đối với người dùng hoặc doanh nghiệp không?
* Người dùng có quyền sở hữu trí tuệ ở đây không?
* Tổ chức có quyền sở hữu trí tuệ ở đây không?
* Nếu các quyền này tồn tại, chúng ta đang bảo vệ chúng như thế nào?

#### 2.4 Quyền riêng tư dữ liệu

[Quyền riêng tư dữ liệu](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) hoặc quyền riêng tư thông tin đề cập đến việc bảo vệ quyền riêng tư của người dùng và bảo vệ danh tính của họ liên quan đến thông tin nhận dạng cá nhân.

Các câu hỏi cần khám phá ở đây là:
* Dữ liệu (cá nhân) của người dùng có được bảo mật chống lại các cuộc tấn công và rò rỉ không?
* Dữ liệu của người dùng có chỉ được truy cập bởi các người dùng và bối cảnh được ủy quyền không?
* Tính ẩn danh của người dùng có được bảo tồn khi dữ liệu được chia sẻ hoặc phổ biến không?
* Người dùng có thể được không nhận dạng từ các bộ dữ liệu đã được ẩn danh không?

#### 2.5 Quyền được lãng quên

[Quyền được lãng quên](https://en.wikipedia.org/wiki/Right_to_be_forgotten) hoặc [Quyền xóa bỏ](https://www.gdpreu.org/right-to-be-forgotten/) cung cấp thêm sự bảo vệ dữ liệu cá nhân cho người dùng. Cụ thể, nó cho phép người dùng yêu cầu xóa hoặc loại bỏ dữ liệu cá nhân khỏi các tìm kiếm trên Internet và các địa điểm khác, _trong các trường hợp cụ thể_ - cho phép họ có một khởi đầu mới trực tuyến mà không bị các hành động trong quá khứ chống lại họ.

Các câu hỏi cần khám phá ở đây là:
* Hệ thống có cho phép đối tượng dữ liệu yêu cầu xóa bỏ không?
* Việc rút lại sự đồng ý của người dùng có nên kích hoạt việc xóa bỏ tự động không?
* Dữ liệu có được thu thập mà không có sự đồng ý hoặc bằng các phương tiện bất hợp pháp không?
* Chúng ta có tuân thủ các quy định của chính phủ về quyền riêng tư dữ liệu không?

#### 2.6 Thiên vị bộ dữ liệu

Thiên vị bộ dữ liệu hoặc [Thiên vị thu thập](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) là về việc chọn một tập hợp con _không đại diện_ của dữ liệu để phát triển thuật toán, tạo ra sự không công bằng tiềm ẩn trong kết quả cho các nhóm đa dạng. Các loại thiên bias bao gồm thiên bias chọn lọc hoặc lấy mẫu, thiên bias tình nguyện, và thiên bias công cụ.

Các câu hỏi cần khám phá ở đây là:
* Chúng ta có tuyển chọn một tập hợp đại diện của các đối tượng dữ liệu không?
* Chúng ta có kiểm tra bộ dữ liệu đã thu thập hoặc quản lý để phát hiện các thiên bias khác nhau không?
* Chúng ta có thể giảm thiểu hoặc loại bỏ các thiên bias đã phát hiện không?

#### 2.7 Chất lượng dữ liệu

[Chất lượng dữ liệu](https://lakefs.io/data-quality-testing/) xem xét tính hợp lệ của bộ dữ liệu được quản lý để phát triển thuật toán của chúng ta, kiểm tra xem các đặc điểm và bản ghi có đáp ứng yêu cầu về mức độ chính xác và nhất quán cần thiết cho mục đích AI của chúng ta hay không.

Các câu hỏi cần khám phá ở đây là:
* Chúng ta có thu thập các _đặc điểm hợp lệ_ cho trường hợp sử dụng của mình không?
* Dữ liệu có được thu thập _
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) kiểm tra xem thiết kế thuật toán có phân biệt đối xử một cách hệ thống với các nhóm đối tượng dữ liệu cụ thể hay không, dẫn đến [những tổn hại tiềm tàng](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) trong _phân bổ_ (nơi tài nguyên bị từ chối hoặc không được cung cấp cho nhóm đó) và _chất lượng dịch vụ_ (nơi AI không chính xác đối với một số nhóm như đối với các nhóm khác).

Các câu hỏi cần khám phá ở đây là:
 * Chúng ta đã đánh giá độ chính xác của mô hình đối với các nhóm và điều kiện đa dạng chưa?
 * Chúng ta đã xem xét hệ thống để tìm các tổn hại tiềm tàng (ví dụ: định kiến) chưa?
 * Chúng ta có thể sửa đổi dữ liệu hoặc huấn luyện lại mô hình để giảm thiểu các tổn hại đã xác định không?

Khám phá các tài nguyên như [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) để tìm hiểu thêm.

#### 2.9 Sai lệch thông tin

[Sai lệch thông tin dữ liệu](https://www.sciencedirect.com/topics/computer-science/misrepresentation) liên quan đến việc đặt câu hỏi liệu chúng ta có đang truyền đạt những thông tin từ dữ liệu được báo cáo một cách trung thực nhưng lại gây hiểu lầm để hỗ trợ một câu chuyện mong muốn hay không.

Các câu hỏi cần khám phá ở đây là:
 * Chúng ta có đang báo cáo dữ liệu không đầy đủ hoặc không chính xác không?
 * Chúng ta có đang trực quan hóa dữ liệu theo cách dẫn đến kết luận sai lệch không?
 * Chúng ta có đang sử dụng các kỹ thuật thống kê chọn lọc để thao túng kết quả không?
 * Có những giải thích thay thế nào có thể đưa ra kết luận khác không?

#### 2.10 Quyền tự do lựa chọn
[Ảo tưởng về quyền tự do lựa chọn](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) xảy ra khi "kiến trúc lựa chọn" của hệ thống sử dụng các thuật toán ra quyết định để thúc đẩy mọi người chọn một kết quả ưu tiên trong khi vẫn tạo cảm giác rằng họ có quyền lựa chọn và kiểm soát. Những [mô hình tối](https://www.darkpatterns.org/) này có thể gây hại về mặt xã hội và kinh tế cho người dùng. Vì các quyết định của người dùng ảnh hưởng đến hồ sơ hành vi, những hành động này có thể thúc đẩy các lựa chọn trong tương lai, làm khuếch đại hoặc kéo dài tác động của những tổn hại này.

Các câu hỏi cần khám phá ở đây là:
 * Người dùng có hiểu rõ các tác động của việc đưa ra lựa chọn đó không?
 * Người dùng có nhận thức được các lựa chọn (thay thế) và ưu nhược điểm của từng lựa chọn không?
 * Người dùng có thể đảo ngược một lựa chọn tự động hoặc bị ảnh hưởng sau này không?

### 3. Nghiên cứu tình huống

Để đặt những thách thức đạo đức này vào bối cảnh thực tế, việc xem xét các nghiên cứu tình huống giúp làm nổi bật những tổn hại và hậu quả tiềm tàng đối với cá nhân và xã hội khi các vi phạm đạo đức như vậy bị bỏ qua.

Dưới đây là một vài ví dụ:

| Thách thức đạo đức | Nghiên cứu tình huống | 
|--- |--- |
| **Sự đồng ý được thông báo** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Những người đàn ông Mỹ gốc Phi tham gia nghiên cứu được hứa hẹn chăm sóc y tế miễn phí _nhưng bị lừa dối_ bởi các nhà nghiên cứu không thông báo cho họ về chẩn đoán hoặc sự sẵn có của phương pháp điều trị. Nhiều người đã chết và đối tác hoặc con cái của họ bị ảnh hưởng; nghiên cứu kéo dài 40 năm. | 
| **Quyền riêng tư dữ liệu** | 2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) cung cấp cho các nhà nghiên cứu _10 triệu xếp hạng phim ẩn danh từ 50 nghìn khách hàng_ để cải thiện thuật toán gợi ý. Tuy nhiên, các nhà nghiên cứu đã có thể liên kết dữ liệu ẩn danh với dữ liệu nhận dạng cá nhân trong _các tập dữ liệu bên ngoài_ (ví dụ: bình luận IMDb) - thực tế "giải ẩn danh" một số người dùng Netflix.|
| **Thiên vị trong thu thập dữ liệu** | 2013 - Thành phố Boston [phát triển Street Bump](https://www.boston.gov/transportation/street-bump), một ứng dụng cho phép công dân báo cáo ổ gà, cung cấp cho thành phố dữ liệu đường xá tốt hơn để tìm và sửa chữa các vấn đề. Tuy nhiên, [những người thuộc nhóm thu nhập thấp ít có quyền truy cập vào ô tô và điện thoại hơn](https://hbr.org/2013/04/the-hidden-biases-in-big-data), khiến các vấn đề đường xá của họ trở nên vô hình trong ứng dụng này. Các nhà phát triển đã làm việc với các học giả để giải quyết _vấn đề tiếp cận công bằng và chia rẽ kỹ thuật số_ nhằm đảm bảo tính công bằng. |
| **Công bằng thuật toán** | 2018 - [Gender Shades Study](http://gendershades.org/overview.html) của MIT đánh giá độ chính xác của các sản phẩm AI phân loại giới tính, phơi bày những khoảng cách về độ chính xác đối với phụ nữ và người da màu. Một [Apple Card năm 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) dường như cung cấp ít tín dụng hơn cho phụ nữ so với nam giới. Cả hai đều minh họa các vấn đề về thiên vị thuật toán dẫn đến tổn hại kinh tế xã hội.|
| **Sai lệch thông tin dữ liệu** | 2020 - [Sở Y tế Georgia công bố biểu đồ COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) dường như gây hiểu lầm cho công dân về xu hướng các ca bệnh được xác nhận với thứ tự không theo thời gian trên trục x. Điều này minh họa sự sai lệch thông tin thông qua các thủ thuật trực quan hóa. |
| **Ảo tưởng về quyền tự do lựa chọn** | 2020 - Ứng dụng học tập [ABCmouse trả 10 triệu USD để giải quyết khiếu nại của FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) nơi phụ huynh bị mắc kẹt trong việc trả tiền cho các gói đăng ký mà họ không thể hủy bỏ. Điều này minh họa các mô hình tối trong kiến trúc lựa chọn, nơi người dùng bị thúc đẩy đến các lựa chọn có thể gây hại. |
| **Quyền riêng tư dữ liệu & Quyền người dùng** | 2021 - [Facebook Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) làm lộ dữ liệu của 530 triệu người dùng, dẫn đến khoản bồi thường 5 tỷ USD cho FTC. Tuy nhiên, Facebook từ chối thông báo cho người dùng về vi phạm, vi phạm quyền của người dùng liên quan đến tính minh bạch và quyền truy cập dữ liệu. |

Muốn khám phá thêm các nghiên cứu tình huống? Hãy xem các tài nguyên sau:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - các tình huống đạo đức trong nhiều ngành công nghiệp.
* [Khóa học Đạo đức Khoa học Dữ liệu](https://www.coursera.org/learn/data-science-ethics#syllabus) - nghiên cứu các tình huống nổi bật.
* [Những nơi đã xảy ra sai sót](https://deon.drivendata.org/examples/) - danh sách kiểm tra Deon với các ví dụ.

> 🚨 Hãy nghĩ về các nghiên cứu tình huống bạn đã thấy - bạn đã từng trải qua hoặc bị ảnh hưởng bởi một thách thức đạo đức tương tự trong cuộc sống chưa? Bạn có thể nghĩ ra ít nhất một nghiên cứu tình huống khác minh họa một trong những thách thức đạo đức mà chúng ta đã thảo luận trong phần này không?

## Đạo đức ứng dụng

Chúng ta đã nói về các khái niệm đạo đức, thách thức và nghiên cứu tình huống trong bối cảnh thực tế. Nhưng làm thế nào để chúng ta bắt đầu _áp dụng_ các nguyên tắc và thực hành đạo đức vào các dự án của mình? Và làm thế nào để chúng ta _hiện thực hóa_ những thực hành này để cải thiện quản trị? Hãy khám phá một số giải pháp thực tế:

### 1. Bộ quy tắc nghề nghiệp

Bộ quy tắc nghề nghiệp cung cấp một lựa chọn cho các tổ chức để "khuyến khích" các thành viên hỗ trợ các nguyên tắc đạo đức và tuyên bố sứ mệnh của họ. Các bộ quy tắc là _hướng dẫn đạo đức_ cho hành vi nghề nghiệp, giúp nhân viên hoặc thành viên đưa ra quyết định phù hợp với các nguyên tắc của tổ chức. Chúng chỉ hiệu quả khi có sự tuân thủ tự nguyện từ các thành viên; tuy nhiên, nhiều tổ chức cung cấp thêm phần thưởng và hình phạt để thúc đẩy sự tuân thủ từ các thành viên.

Các ví dụ bao gồm:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Bộ quy tắc đạo đức
 * [Hiệp hội Khoa học Dữ liệu](http://datascienceassn.org/code-of-conduct.html) Bộ quy tắc ứng xử (được tạo năm 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (từ năm 1993)

> 🚨 Bạn có thuộc một tổ chức kỹ thuật hoặc khoa học dữ liệu chuyên nghiệp không? Hãy khám phá trang web của họ để xem liệu họ có định nghĩa một bộ quy tắc đạo đức nghề nghiệp không. Điều này nói gì về các nguyên tắc đạo đức của họ? Họ đang "khuyến khích" các thành viên tuân theo bộ quy tắc như thế nào?

### 2. Danh sách kiểm tra đạo đức

Trong khi các bộ quy tắc nghề nghiệp định nghĩa hành vi _đạo đức cần thiết_ từ các nhà thực hành, chúng [có những hạn chế đã biết](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) trong việc thực thi, đặc biệt trong các dự án quy mô lớn. Thay vào đó, nhiều chuyên gia khoa học dữ liệu [ủng hộ danh sách kiểm tra](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), có thể **kết nối các nguyên tắc với thực hành** theo cách xác định và có thể hành động hơn.

Danh sách kiểm tra chuyển đổi các câu hỏi thành các nhiệm vụ "có/không" có thể hiện thực hóa, cho phép chúng được theo dõi như một phần của quy trình phát hành sản phẩm tiêu chuẩn.

Các ví dụ bao gồm:
 * [Deon](https://deon.drivendata.org/) - danh sách kiểm tra đạo đức dữ liệu đa mục đích được tạo từ [khuyến nghị ngành](https://deon.drivendata.org/#checklist-citations) với công cụ dòng lệnh để tích hợp dễ dàng.
 * [Danh sách kiểm tra kiểm toán quyền riêng tư](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - cung cấp hướng dẫn chung về thực hành xử lý thông tin từ góc độ pháp lý và xã hội.
 * [Danh sách kiểm tra công bằng AI](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - được tạo bởi các nhà thực hành AI để hỗ trợ việc áp dụng và tích hợp các kiểm tra công bằng vào chu kỳ phát triển AI.
 * [22 câu hỏi về đạo đức trong dữ liệu và AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - khung mở hơn, được cấu trúc để khám phá ban đầu các vấn đề đạo đức trong thiết kế, triển khai và bối cảnh tổ chức.

### 3. Quy định đạo đức

Đạo đức là về việc định nghĩa các giá trị chung và làm điều đúng _một cách tự nguyện_. **Tuân thủ** là về _tuân theo luật pháp_ nếu và nơi được định nghĩa. **Quản trị** bao quát tất cả các cách mà các tổ chức hoạt động để thực thi các nguyên tắc đạo đức và tuân thủ các luật đã được thiết lập.

Ngày nay, quản trị có hai hình thức trong các tổ chức. Đầu tiên, đó là việc định nghĩa các nguyên tắc **AI đạo đức** và thiết lập các thực hành để hiện thực hóa việc áp dụng trên tất cả các dự án liên quan đến AI trong tổ chức. Thứ hai, đó là việc tuân thủ tất cả các quy định **bảo vệ dữ liệu** do chính phủ quy định cho các khu vực mà tổ chức hoạt động.

Các ví dụ về quy định bảo vệ dữ liệu và quyền riêng tư:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - quy định việc thu thập, sử dụng và tiết lộ thông tin cá nhân của _chính phủ liên bang_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - bảo vệ dữ liệu sức khỏe cá nhân.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - bảo vệ quyền riêng tư dữ liệu của trẻ em dưới 13 tuổi.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - cung cấp quyền người dùng, bảo vệ dữ liệu và quyền riêng tư.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) cung cấp cho người tiêu dùng nhiều _quyền_ hơn đối với dữ liệu (cá nhân) của họ.
 * `2021`, [Luật Bảo vệ Thông tin Cá nhân của Trung Quốc](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) vừa được thông qua, tạo ra một trong những quy định bảo vệ quyền riêng tư dữ liệu trực tuyến mạnh nhất trên toàn thế giới.

> 🚨 Liên minh châu Âu đã định nghĩa GDPR (Quy định Bảo vệ Dữ liệu Chung) vẫn là một trong những quy định bảo vệ quyền riêng tư dữ liệu có ảnh hưởng nhất hiện nay. Bạn có biết rằng nó cũng định nghĩa [8 quyền người dùng](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) để bảo vệ quyền riêng tư kỹ thuật số và dữ liệu cá nhân của công dân không? Tìm hiểu về những quyền này và tại sao chúng lại quan trọng.

### 4. Văn hóa đạo đức

Lưu ý rằng vẫn còn một khoảng cách vô hình giữa _tuân thủ_ (làm đủ để đáp ứng "tinh thần của luật pháp") và giải quyết [các vấn đề hệ thống](https://www.coursera.org/learn/data-science-ethics/home/week/4) (như sự cứng nhắc, bất đối xứng thông tin và sự không công bằng trong phân phối) có thể đẩy nhanh việc vũ khí hóa AI.

Điều này đòi hỏi [các cách tiếp cận hợp tác để định nghĩa văn hóa đạo đức](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) nhằm xây dựng kết nối cảm xúc và các giá trị chung nhất quán _trong các tổ chức_ trong ngành. Điều này kêu gọi [văn hóa đạo đức dữ liệu được chính thức hóa](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) trong các tổ chức - cho phép _bất kỳ ai_ [kéo dây Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (để nêu lên các mối quan ngại về đạo đức sớm trong quy trình) và làm cho _đánh giá đạo đức_ (ví dụ: trong tuyển dụng) trở thành tiêu chí cốt lõi trong việc hình thành nhóm cho các dự án AI.

---
## [Câu hỏi kiểm tra sau bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## Ôn tập & Tự học 

Các khóa học và sách giúp hiểu các khái niệm đạo đức cốt lõi và thách thức, trong khi các nghiên cứu tình huống và công cụ giúp thực hành đạo đức trong bối cảnh thực tế. Dưới đây là một vài tài nguyên để bắt đầu.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - bài học về Công bằng, từ Microsoft.
* [Nguyên tắc AI có trách nhiệm](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - lộ trình học miễn phí từ Microsoft Learn.  
* [Đạo đức và Khoa học Dữ liệu](https://resources.oreilly.com/examples/0636920203964) - Sách điện tử O'Reilly (M. Loukides, H. Mason và các tác giả khác).  
* [Đạo đức trong Khoa học Dữ liệu](https://www.coursera.org/learn/data-science-ethics#syllabus) - khóa học trực tuyến từ Đại học Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - các nghiên cứu tình huống từ Đại học Texas.  

# Bài tập  

[Viết một nghiên cứu tình huống về đạo đức dữ liệu](assignment.md)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.