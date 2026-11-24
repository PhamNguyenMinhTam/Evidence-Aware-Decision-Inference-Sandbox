# Evidence-Aware Decision Inference Sandbox — EADIS

**An Experimental Sandbox for Evidence Extraction, Temporal Reasoning, Uncertainty and Partial Identification.**

*Môi trường thực nghiệm suy luận quyết định dựa trên bằng chứng, quan hệ thời gian và thông tin không đầy đủ.*

EADIS là mini project tiền nghiên cứu chuẩn bị cho ETVM-PI, kế thừa hướng Autobiography-based Decision Twin. Repo GitHub giữ tên `LLM-AGENTS-EXPERIMENTS`. EADIS là phần mềm khoa học phục vụ học tập và thực nghiệm tái lập. Kết quả từ các fixture tổng hợp dùng để kiểm tra pipeline và thiết kế thí nghiệm tiếp theo.

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
