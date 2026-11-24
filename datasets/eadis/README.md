# Dữ liệu pilot EADIS

Hai tệp JSONL chứa chín tình huống tổng hợp trong hai domain và mười một bước. `inputs.jsonl` chứa từ điển phương án, actor, tình huống, sự kiện và các batch nguồn theo thứ tự nhận. ID nguồn là duy nhất trong một case. Các case transport-complete, transport-paraphrase và transport-noise dùng cùng nhãn logic.

`labels.jsonl` chứa một dòng cho mỗi ID case. Claim, action, actor, tình huống và options của mỗi bước mô tả batch hiện tại. Tập phương án, quan hệ before và cờ xung đột mô tả tích lũy đến hết bước đó. Tập fallback lấy lại toàn miền khi tập nghiêm ngặt rỗng. Bao đóng của đồ thị có chu trình chứa cạnh phản xạ, được báo cáo cùng cờ xung đột. Quote là chuỗi nguyên văn và offset dùng chỉ số ký tự Python, đầu bao gồm và cuối loại trừ.

Fixture được thiết kế thủ công để kiểm tra phần mềm, gồm thiếu bằng chứng, mâu thuẫn quyết định, chu trình, tăng dần, paraphrase, nhiễu và đổi domain. Bộ dữ liệu đánh giá ngoài cần có nhóm narrative độc lập, hướng dẫn gán nhãn, gán nhãn nhiều người và phân chia theo họ tình huống.
