# Câu hỏi nghiên cứu EADIS

Các giả thuyết dưới đây là đề xuất kiểm định. Với tỷ lệ hoặc chênh lệch trong pilot, báo cáo số quan sát và hướng hiệu ứng. Khi mở rộng dữ liệu, chốt ngưỡng, cỡ mẫu và phương pháp phân tích trước khi mở nhãn tập đánh giá.

## RQ01 — LLM trích xuất quyết định và bằng chứng từ narrative chính xác đến mức nào?

- **Motivation**. Chuẩn hóa đơn vị phân tích để đo lỗi theo trường và theo mệnh đề.
- **Problem definition**. Trích xuất actor, tình huống, lựa chọn, hành động và claim theo từng batch.
- **Theoretical foundation**. So khớp chính xác theo trường và precision, recall, F1 theo tập.
- **Research hypothesis**. F1 claim của Ollama cao hơn luật trên các cặp paraphrase. Kiểm tra hiệu số ≤ 0.
- **Independent variables**. Phương pháp trích xuất, cách diễn đạt
- **Dependent variables**. F1 claim, action exact, actor/situation exact, F1 options
- **Controlled variables**. Cùng batch, từ điển định danh và nhãn
- **Baselines**. Regex, Ollama xuất JSON
- **Threats to validity**. Từ điển actor/situation/options được cung cấp, nên điểm các trường đó đo chuẩn hóa theo ngữ cảnh.
- **Expected learning outcomes**. Hiểu lỗi trích xuất cấu trúc và ranh giới giữa trích xuất và suy luận.
- **Relevance to ETVM-PI**. Schema và giao thức gán nhãn quyết định.
- **Evaluation metrics**. F1 claim, action exact, actor/situation exact, F1 options.

## RQ02 — Kết luận do LLM tạo ra có được bằng chứng đầu vào hỗ trợ không?

- **Motivation**. Một trích dẫn hợp lệ về vị trí vẫn có thể bị gán sai ý nghĩa.
- **Problem definition**. Đo định vị trích dẫn và đối chiếu mệnh đề với nhãn bằng chứng.
- **Theoretical foundation**. Provenance theo bộ (source, start, end) và so khớp mệnh đề có nguồn.
- **Research hypothesis**. Kiểm tra span làm giảm tỷ lệ claim ngoài văn bản được chấp nhận. Kiểm tra hiệu số ≤ 0.
- **Independent variables**. Bật/tắt kiểm tra span trong phân tích đối chứng
- **Dependent variables**. Tỷ lệ span hợp lệ, precision claim có nguồn, số claim bị loại
- **Controlled variables**. Cùng response thô và cùng nhãn
- **Baselines**. Claim thô, claim qua kiểm tra span
- **Threats to validity**. So khớp quote nguyên văn nhạy với cách xác định biên, còn kiểm tra span chỉ xác nhận vị trí.
- **Expected learning outcomes**. Phân biệt nhầm nguồn, quote bịa và quote có thật nhưng lập luận sai.
- **Relevance to ETVM-PI**. Giao thức truy vết bằng chứng.
- **Evaluation metrics**. Tỷ lệ span hợp lệ, precision claim có nguồn, số claim bị loại.

## RQ03 — Hệ thống biểu diễn và suy luận đúng quan hệ thời gian giữa các sự kiện không?

- **Motivation**. Thứ tự gián tiếp có thể cần kết hợp nhiều nguồn.
- **Problem definition**. Phục hồi quan hệ before và phát hiện chu trình.
- **Theoretical foundation**. Đồ thị có hướng, bao đóng bắc cầu, phản xạ suy ra từ chu trình.
- **Research hypothesis**. Bao đóng tăng recall trên chuỗi nhất quán có cạnh gián tiếp. Kiểm tra hiệu số ≤ 0.
- **Independent variables**. Cạnh trực tiếp hay bao đóng, dữ liệu theo chuỗi hoặc chu trình
- **Dependent variables**. Temporal precision/recall/F1, cờ chu trình
- **Controlled variables**. Cùng bộ cạnh trích xuất và từ điển sự kiện
- **Baselines**. Cạnh trực tiếp, bao đóng
- **Threats to validity**. ID sự kiện cho trước, fixture hiện chỉ đo before định tính.
- **Expected learning outcomes**. Hiểu lỗi cạnh đầu vào và sự lan truyền của lỗi.
- **Relevance to ETVM-PI**. Biểu diễn sự kiện thời gian tối giản.
- **Evaluation metrics**. Temporal precision/recall/F1, cờ chu trình.

## RQ04 — Khi bằng chứng bị thiếu, hệ thống có nhận ra giới hạn kết luận không?

- **Motivation**. Thiếu bằng chứng có thể cho phép nhiều quyết định.
- **Problem definition**. Xóa câu chọn phương án và đo số kết luận còn tương thích.
- **Theoretical foundation**. Thế giới mở, giao tập ràng buộc trên miền hữu hạn.
- **Research hypothesis**. Tập kết quả của fixture bị che chứa tập của fixture đầy đủ khi chỉ loại ràng buộc. Một vi phạm bác bỏ giả thuyết.
- **Independent variables**. Mức che bằng chứng, phương pháp
- **Dependent variables**. Set exact, coverage, kích thước tập
- **Controlled variables**. Cùng tình huống, actor và miền phương án
- **Baselines**. Đầu ra một hành động/abstain, tập tương thích
- **Threats to validity**. Bằng chứng thiếu tự nhiên có thể mang tín hiệu khác với phép xóa.
- **Expected learning outcomes**. Nhận diện khi nên duy trì nhiều khả năng.
- **Relevance to ETVM-PI**. Thiết kế thí nghiệm kiểm soát thiếu bằng chứng.
- **Evaluation metrics**. Set exact, coverage, kích thước tập.

## RQ05 — Hệ thống xử lý bằng chứng mâu thuẫn như thế nào?

- **Motivation**. Chọn quyết định tùy ý làm mất dấu xung đột.
- **Problem definition**. Kiểm tra hai lựa chọn loại trừ nhau và chu trình thời gian.
- **Theoretical foundation**. Tính thỏa được của giao ràng buộc và chu trình trong đồ thị.
- **Research hypothesis**. Cờ xung đột phân biệt đúng các fixture mâu thuẫn và nhất quán. Một lỗi cờ bác bỏ giả thuyết.
- **Independent variables**. Loại xung đột và thứ tự nguồn
- **Dependent variables**. Conflict exact, tập nghiệm nghiêm ngặt, fallback set exact
- **Controlled variables**. Cùng miền lựa chọn và chính sách tin nguồn
- **Baselines**. Hành động từ batch mới nhất, suy luận giao ràng buộc
- **Threats to validity**. Hai nguồn được gán vai trò ràng buộc như nhau, các diễn giải sửa sai nguồn chưa được mô phỏng.
- **Expected learning outcomes**. Phân biệt vô nghiệm và thiếu dữ liệu.
- **Relevance to ETVM-PI**. Mã hóa xung đột có nguồn.
- **Evaluation metrics**. Conflict exact, tập nghiệm nghiêm ngặt, fallback set exact.

## RQ06 — Set-valued inference biểu diễn các kết luận còn tương thích bằng cách nào?

- **Motivation**. Một dự đoán điểm làm mất các lựa chọn tương thích còn lại.
- **Problem definition**. So sánh tập khả dĩ với nhãn dưới miền quyết định hữu hạn.
- **Theoretical foundation**. Tập nhận dạng xác định theo ràng buộc đã giả định.
- **Research hypothesis**. Khi có từ hai nghiệm trở lên, tập ràng buộc đạt exact-set cao hơn hành động điểm được đổi thành singleton hoặc tập rỗng. Kiểm tra hiệu số ≤ 0.
- **Independent variables**. Phương pháp và số ràng buộc
- **Dependent variables**. Set exact, coverage và kích thước tập
- **Controlled variables**. Miền hữu hạn và cùng batch
- **Baselines**. Dự đoán điểm, tập toàn miền, tập ràng buộc
- **Threats to validity**. Phương án ngoài miền ảnh hưởng coverage và giới hạn khả năng khái quát.
- **Expected learning outcomes**. Hiểu độ rộng tập dưới giả định đo lường rõ ràng.
- **Relevance to ETVM-PI**. Bài tập nền tảng partial identification rời rạc.
- **Evaluation metrics**. Set exact, coverage và kích thước tập.

## RQ07 — Khi nào cập nhật gia tăng khớp kết quả tính lại với chi phí thấp hơn?

- **Motivation**. Thêm bằng chứng thường xuyên có thể làm tính lại toàn bộ tốn kém.
- **Problem definition**. Đối chiếu các bước trên cùng tiền tố nguồn và cùng claim.
- **Theoretical foundation**. Bất biến giao tập và bao đóng đồ thị sau khi thêm cạnh.
- **Research hypothesis**. Kết quả phải trùng tại mọi tiền tố. Với benchmark đã warm-up lặp lại, kiểm tra median thời gian gia tăng thấp hơn ở prefix dài.
- **Independent variables**. Thuật toán, độ dài tiền tố, kích thước batch
- **Dependent variables**. Agreement, thời gian engine tính bằng ns, phân phối chênh lệch ghép cặp
- **Controlled variables**. Cùng thứ tự claim, máy, Python và đầu ra
- **Baselines**. Tính lại từ toàn bộ tiền tố, cập nhật trạng thái
- **Threats to validity**. Chi phí timer, tải máy, fixture quá nhỏ và thuật toán tính lại đơn giản ảnh hưởng điểm hòa vốn.
- **Expected learning outcomes**. Hiểu bất biến thuật toán và cách đo chi phí.
- **Relevance to ETVM-PI**. Baseline cập nhật khi có nguồn mới.
- **Evaluation metrics**. Agreement, thời gian engine tính bằng ns, phân phối chênh lệch ghép cặp.

## RQ08 — Hiệu quả thay đổi ra sao theo paraphrase, domain và nhiễu?

- **Motivation**. Kết quả trên câu mẫu có thể phản ánh cú pháp fixture.
- **Problem definition**. Đo thay đổi trên các biến thể ghép cặp cùng ý nghĩa và thăm dò domain mới.
- **Theoretical foundation**. Độ bền dưới biến đổi bảo toàn nhãn và dịch chuyển phân phối.
- **Research hypothesis**. F1 claim giảm dưới paraphrase đối với regex. Hiệu số giảm ≤ 0 bác bỏ giả thuyết.
- **Independent variables**. Điều kiện văn bản, phương pháp, domain
- **Dependent variables**. Chênh lệch F1 và set exact ghép cặp, tỷ lệ lỗi theo điều kiện
- **Controlled variables**. Cùng nhãn logic cho mỗi cặp, cùng model và tùy chọn
- **Baselines**. Bản gốc đối chiếu với paraphrase và nhiễu
- **Threats to validity**. Domain housing cũng thay đổi số phương án, nên chỉ dùng kết quả để thăm dò.
- **Expected learning outcomes**. Phân biệt độ nhạy câu chữ và giới hạn domain.
- **Relevance to ETVM-PI**. Mẫu thiết kế robustness cho dữ liệu ETVM-PI.
- **Evaluation metrics**. Chênh lệch F1 và set exact ghép cặp, tỷ lệ lỗi theo điều kiện.
