# Nhật ký nghiên cứu và chuyển giao ETVM-PI

## Pilot EADIS

Câu hỏi ban đầu là liệu có thể tách lỗi extraction, provenance, logic thời gian và tập quyết định trong một lần chạy được tái lập. Dữ liệu gồm case kiểm chứng xác định, trong đó câu paraphrase tạo đối chứng cho regex. Các kết quả offline kiểm tra tính nhất quán phần mềm. Kết luận về chất lượng LLM và chi phí trên laptop cần kết quả chạy live và thiết kế mở rộng.

| Failure case | Dấu hiệu trong báo cáo | Kiểm tra |
|---|---|---|
| JSON hoặc API lỗi | error và lỗi tiền tố | Kiểm tra adapter, model và response format |
| Quote hoặc nguồn sai | rejected_claims tăng | Đối chiếu khoảng ký tự theo source ID |
| Quote đúng, claim sai | F1 evidence giảm | Xem ngữ nghĩa cùng nhãn |
| Thiếu claim | Recall giảm, tập có thể rộng ra | Xem paraphrase và các câu bị che |
| Hai quyết định loại trừ nhau | decision_conflict và tập nghiêm ngặt rỗng | Đọc các claim cùng provenance |
| Chu trình thời gian | temporal_conflict và cặp phản xạ | Truy vết cạnh before |
| Sai cập nhật | incremental_agreement bằng false | Tái hiện tiền tố đầu tiên bị lệch |

## Bản đồ chuyển giao

| Thành phần EADIS | Sản phẩm chuẩn bị cho ETVM-PI | Điều kiện cần nghiên cứu |
|---|---|---|
| Fixture và nhãn tách biệt | Hợp đồng dataset trích xuất | Narrative thực, quy trình đồng thuận người gán nhãn |
| Source ID, quote, offset | Schema provenance | Phiên bản nguồn, tham chiếu và đánh giá entailment |
| Sự kiện và before | Biểu diễn thời gian ban đầu | Mốc bất định, khoảng và các quan hệ khác |
| Regex và Ollama | Baseline trích xuất | So sánh trên tập độc lập, mô hình và ngôn ngữ khác |
| Tập nghiệm và cờ xung đột | Baseline suy luận tập hữu hạn | Định nghĩa estimand và giả định partial identification |
| Engine gia tăng và tính lại | Oracle kiểm tra từng tiền tố | Sửa nguồn, quy mô lớn và đo hiệu năng có kiểm soát |
| Runner và taxonomy | Giao thức đánh giá, nhật ký lỗi | Thống kê có độ bất định và phân tích độ nhạy |
