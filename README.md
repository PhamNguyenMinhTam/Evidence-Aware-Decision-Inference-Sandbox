# Evidence-Aware Decision Inference Sandbox — EADIS

**An Experimental Sandbox for Evidence Extraction, Temporal Reasoning, Uncertainty and Partial Identification.**

*Môi trường thực nghiệm suy luận quyết định dựa trên bằng chứng, quan hệ thời gian và thông tin không đầy đủ.*

EADIS là mini project tiền nghiên cứu chuẩn bị cho ETVM-PI, kế thừa hướng Autobiography-based Decision Twin. EADIS là phần mềm khoa học phục vụ học tập và thực nghiệm tái lập. Kết quả từ các fixture tổng hợp dùng để kiểm tra pipeline và thiết kế thí nghiệm tiếp theo.

**UNDERSTANDING > MEMORIZATION**

**WHY → WHAT → MATH → HOW → CODE → EXPERIMENT → REFLECTION**

## Chạy benchmark

Tại thư mục gốc của repo, dùng Python 3.11 trở lên.

```sh
python -m pip install -e ".[dev]"
eadis --mode dry-run
eadis --mode rule --output results/eadis/rule.json
eadis --mode mock --output results/eadis/mock.json
python -m pytest
```

Có thể dùng `python -m eadis.cli` thay cho `eadis`. Dry-run đọc và kiểm tra bộ input. Mock thực hiện vòng JSON bằng bộ trích xuất luật. Rule và mock chạy cục bộ.

Với Ollama, sao chép [cấu hình mẫu](configs/eadis-worker.example.yaml) cho mỗi laptop. Điền endpoint mà máy điều khiển truy cập được, model tag, digest và quantization từ Ollama của từng máy. Dùng ID và endpoint riêng cho mỗi laptop. CLI kiểm tra model trước khi benchmark.

```sh
eadis --mode live --worker laptop-a.yaml --output results/eadis/laptop-a.json
eadis --mode live --worker laptop-a.yaml --worker laptop-b.yaml --output results/eadis/dual.json
```

Mỗi worker chạy độc lập trên cùng các batch. Controller chạy lần lượt các worker và dùng chung mã đánh giá. Các worker chỉ thấy bối cảnh bài toán và văn bản batch hiện hành. CLI mở tệp nhãn sau khi tạo dự đoán cho toàn bộ worker. Mỗi báo cáo lưu cấu hình, SHA-256 dữ liệu, kết quả theo bước, lỗi và thống kê theo điều kiện. Tên tệp báo cáo phải mới để bảo toàn kết quả lần trước.

## Tài liệu

- [Câu hỏi nghiên cứu RQ01–RQ08](docs/eadis/research_questions.md)
- [Kiến trúc, toán học, giao thức đánh giá và giới hạn](docs/eadis/methodology.md)
- [Dữ liệu tổng hợp và hợp đồng nhãn](datasets/eadis/README.md)
- [Nhật ký nghiên cứu và bản đồ chuyển giao ETVM-PI](docs/eadis/research_log.md)
- [Ma trận E01–E12](experiments/README.md) và [hướng dẫn runner trước EADIS](docs/archive/README_before_eadis.md)

## Research Progress & GitHub Issues

- [Master Tracking Issue](https://github.com/PhamNguyenMinhTam/Evidence-Aware-Decision-Inference-Sandbox/issues/2)
- [GitHub Issues](https://github.com/PhamNguyenMinhTam/Evidence-Aware-Decision-Inference-Sandbox/issues) · [Milestones](https://github.com/PhamNguyenMinhTam/Evidence-Aware-Decision-Inference-Sandbox/milestones) · [Issue Index](docs/issue_index.md)
- [Master Research & Development Checklist](docs/experiment_checklist.md) · [Learning Roadmap](docs/eadis/learning_roadmap.md) · [Research Log](docs/eadis/research_log.md) · [ETVM-PI Transfer Map](docs/eadis/research_log.md#bản-đồ-chuyển-giao)

1. Mở Master Tracking Issue hoặc Issue Index và chọn phase theo thứ tự completion gates. Dùng milestone để xem các phase liên quan và lọc labels theo `phase: P00`, `experiment: M01` hoặc `status: review`.
2. Mở Detailed Task Issue từ phase tương ứng. Đánh dấu checklist sau khi tự xác minh kiến thức hoặc kết quả. GitHub Issues giữ trạng thái chính, còn Markdown checklist trong repo cung cấp nội dung tham chiếu.
3. Ghi quan sát và diễn giải trong Research Log. Đính commit, run ID, phiên bản dữ liệu, research notes và kết quả xác minh trong Completion Evidence. Chuyển phase sau khi người thực hiện xác nhận completion gate. Duy trì Continuous Issues theo tuần và ưu tiên backlog tùy câu hỏi nghiên cứu.

Chạy `python scripts/setup_research_issues.py --dry-run` để kiểm tra manifest và checklist tại local. Với GitHub CLI đã đăng nhập bằng tài khoản có quyền ghi repo, dùng `--apply` để tạo đối tượng còn thiếu và `--verify` để đối chiếu dữ liệu thực tế. Nếu bị ngắt, chạy lại `--apply` sau khi xử lý thông báo lỗi. Script nhận diện issue bằng task ID trong HTML comment và báo xung đột khi phần liên kết đã bị sửa.
