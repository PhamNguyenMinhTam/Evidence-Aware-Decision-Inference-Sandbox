# EADIS Master Research & Development Checklist

Tài liệu tham chiếu được bổ sung từ danh sách P00–P12, C01–C05, O01–O05 và FINAL trong yêu cầu thiết lập, đối chiếu với [phương pháp](eadis/methodology.md), [RQ01–RQ08](eadis/research_questions.md) và [dataset pilot](../datasets/eadis/README.md). Theo dõi trạng thái và bằng chứng trong GitHub Issues.

WHY → WHAT → MATH → HOW → CODE → EXPERIMENT → REFLECTION. Chốt giả thuyết, assumptions, dữ liệu, baseline và phép đo trước khi mở nhãn tập cuối.

## MASTER — EADIS — Research & Development Roadmap

- [ ] Xác nhận P00–P12 với bằng chứng liên kết.
- [ ] Đối chiếu mục tiêu, kết quả, giới hạn và câu hỏi còn mở.
- [ ] Người thực hiện tự xác nhận readiness trong FINAL.

## P00 — Repository & Environment Foundation

- [ ] Xác minh dry-run, mock và live trên mỗi máy khả dụng. Ghi rõ bằng chứng còn thiếu.

## P00.1 — Repository Verification

- [ ] Kiểm tra remote, nhánh chính, giấy phép, CI và cấu trúc EADIS
- [ ] Đối chiếu E01–E12 và ghi phạm vi kế thừa
- [ ] Lưu SHA checkout và kết quả audit

## P00.2 — Python Environment

- [ ] Chọn phiên bản Python và môi trường ảo
- [ ] Cài editable cùng dev dependencies và lưu phiên bản
- [ ] Chạy test trong môi trường sạch

## P00.3 — Hardware Preparation

- [ ] Ghi CPU GPU RAM, hệ điều hành và mạng của từng laptop
- [ ] Kiểm soát nguồn, nhiệt và tải đồng thời
- [ ] Lưu inventory và điều kiện đo

## P00.4 — Ollama & Model Configuration

- [ ] Chọn tag và ghi version, digest, quantization từ từng máy
- [ ] Cấu hình seed, temperature, timeout, origin và worker ID riêng
- [ ] Kiểm chứng endpoint và model bằng cấu hình thực

## P00.5 — Experimental Framework

- [ ] Mô tả luồng input, extraction, validation, inference, evaluation
- [ ] Chạy dry-run, rule và mock để kiểm tra các nhánh
- [ ] Kiểm tra ghi kết quả, fingerprint và cách ly nhãn

## P00.6 — Environment Verification

- [ ] Chạy smoke test rule/mock, một worker và hai worker khi sẵn sàng
- [ ] Kiểm tra lỗi JSON, network và tiền tố bị gián đoạn
- [ ] Lưu lệnh, report và trạng thái từng cấu hình

## P00.7 — Completion Gate

- [ ] Tái chạy từ môi trường mới và đối chiếu manifest
- [ ] Xác minh model/worker độc lập và bằng chứng còn thiếu
- [ ] Tự xác nhận đủ điều kiện bắt đầu P01

## P01 — Scientific Research Foundation

- [ ] Mỗi RQ có giả thuyết, biến, đối chứng, thước đo và giới hạn.

## P01.1 — Scientific Research Concepts

- [ ] Phân biệt câu hỏi, giả thuyết, dự đoán và quan sát
- [ ] Viết ví dụ giả thuyết bác bỏ được và phân biệt mô tả với nhân quả
- [ ] Ghi một ví dụ áp dụng EADIS và phạm vi kết luận

## P01.2 — Experimental Design

- [ ] Xác định đơn vị phân tích, biến độc lập, phụ thuộc và kiểm soát
- [ ] Chọn đối chứng, chia tập theo họ, quy tắc loại mẫu và phép so ghép cặp
- [ ] Chốt protocol và cách xử lý thiếu hoặc lỗi

## P01.3 — Mathematical Foundation

- [ ] Giải tay bài tập tập hợp, logic, quan hệ, xác suất và đồ thị
- [ ] Tính precision, recall, F1 và coverage trên ví dụ biên
- [ ] Ghi giả định, chứng minh nhỏ và phản ví dụ

## P01.4 — Literature Reading Method

- [ ] Tạo truy vấn và tiêu chí chọn tài liệu gốc
- [ ] Tóm tắt câu hỏi, giả định, phương pháp, bằng chứng và giới hạn
- [ ] Ghi trích dẫn và câu hỏi tiếp theo trong literature notes

## P01.5 — Research Questions

- [ ] Rà soát RQ01–RQ08 và giả thuyết có thể bác bỏ
- [ ] Lập bảng RQ với baseline, biến, metric và threat
- [ ] Ghi quyết định trước khi xem nhãn tập cuối

## P01.6 — Completion Gate

- [ ] Tự giải thích thiết kế, thuật ngữ và phép đo
- [ ] Kiểm tra đủ protocol, ví dụ toán và nguồn tài liệu
- [ ] Ghi câu hỏi còn mở và xác nhận chuyển P02

## P02 — Data & Evidence Foundation

- [ ] Kiểm thử schema, kiểm tra rò rỉ và đối chiếu gán nhãn.

## P02.1 — Decision Modeling

- [ ] Định nghĩa actor, tình huống, lựa chọn, hành động và trạng thái chưa quyết định
- [ ] Phân biệt hành động quan sát với hành động suy ra
- [ ] Giải ví dụ nhiều lựa chọn và quyết định vắng mặt

## P02.2 — Evidence Modeling

- [ ] Định nghĩa claim, nguồn, quote, offset và danh tính sự kiện
- [ ] Mô hình hóa trạng thái thiếu, mơ hồ và mâu thuẫn
- [ ] Tách định vị quote khỏi hỗ trợ ngữ nghĩa

## P02.3 — Data Architecture

- [ ] Thiết kế inputs/labels riêng và version/hash
- [ ] Định nghĩa batch, prefix và provenance
- [ ] Kiểm thử nhãn không đến extractor hoặc engine

## P02.4 — Decision Case Schema

- [ ] Ghi trường, kiểu dữ liệu, ID và constraints cho case
- [ ] Xác minh miền phương án, nguồn và tham chiếu sự kiện
- [ ] Viết ca hợp lệ, lỗi và biên

## P02.5 — Evidence Schema

- [ ] Định nghĩa loại claim và khoảng ký tự đầu gồm/cuối loại
- [ ] Bảo toàn nguồn của claim trùng và mã hóa quan hệ before
- [ ] Kiểm tra quote sai nguồn, offset và entity không hợp lệ

## P02.6 — Ground Truth Design

- [ ] Gán nhãn theo batch và trạng thái tích lũy theo prefix
- [ ] Định nghĩa nhất quán tập nghiệm, fallback và closure
- [ ] Ghi đáp án nhập nhằng và chính sách bất đồng

## P02.7 — Annotation Protocol

- [ ] Viết hướng dẫn quote, claim và trường hợp biên
- [ ] Gán nhãn độc lập mẫu chồng lấp và đo đồng thuận
- [ ] Ghi quy tắc phân xử và lịch sử sửa nhãn

## P02.8 — Synthetic Dataset Development

- [ ] Viết mẫu nhiều domain có complete, missing, conflict, update và noise
- [ ] Thêm đối chứng/paraphrase bảo toàn nhãn
- [ ] Kiểm tra tính đa dạng, nguồn và giới hạn tổng hợp

## P02.9 — Dataset Splitting

- [ ] Chia theo họ narrative và condition trước thử nghiệm
- [ ] Kiểm tra trùng lặp gần đúng và rò rỉ từ prompt
- [ ] Khóa phiên bản, seed và checksum tập cuối

## P02.10 — Completion Gate

- [ ] Tái tạo manifest, chạy validate schema và kiểm tra split
- [ ] Đối chiếu nhãn với rubric trên mẫu độc lập
- [ ] Ghi lỗi còn mở và xác nhận điều kiện chạy M01

## P03 — Extraction Reliability

- [ ] Có so sánh regex/Ollama và báo mẫu số, lỗi API, hạn chế.

## M01.1 — Theory

- [ ] Phân biệt detection, extraction, normalization và inference
- [ ] Định nghĩa trường actor, tình huống, option, action và claim
- [ ] Giải tay ca thiếu và ca trích dẫn sai

## M01.2 — Mathematical Foundation

- [ ] Định nghĩa đơn vị ghép cặp và TP FP FN
- [ ] Tính micro/macro precision, recall, F1 và exact match
- [ ] Chốt quy ước tập rỗng và lỗi schema

## M01.3 — Experimental Design

- [ ] So regex, mock và Ollama structured output
- [ ] Khóa model, prompt, seed, dữ liệu và số lần lặp
- [ ] Chốt so sánh theo cặp điều kiện và cách báo lỗi

## M01.4 — Implementation

- [ ] Dùng schema có kiểm tra kiểu và parser JSON
- [ ] Tách input công khai khỏi gold labels
- [ ] Kiểm thử malformed output, trường thiếu và không tiết lộ batch sau

## M01.5 — Experiment Execution

- [ ] Chạy trên development rồi khóa cấu hình final
- [ ] Ghi run ID, SHA, worker, token và lỗi
- [ ] Lưu dự đoán thô và kết quả có cấu trúc

## M01.6 — Analysis

- [ ] Báo metric theo trường, condition và confidence interval nếu đủ cụm
- [ ] Phân loại lỗi bỏ sót, bịa, chuẩn hóa và JSON
- [ ] Diễn giải ảnh hưởng giới hạn vocabulary và dữ liệu

## M01.7 — Completion Gate

- [ ] Đối chiếu parser và đánh giá với fixture
- [ ] Xác minh đối chứng có cùng split và cấu hình lưu đủ
- [ ] Đính kèm run và ca lỗi trước khi chuyển M02

## P04 — Evidence Grounding

- [ ] Đo riêng tính hợp lệ quote và hỗ trợ ngữ nghĩa trên tập có nhãn.

## M02.1 — Theory

- [ ] Định nghĩa provenance, span và semantic support
- [ ] Phân biệt quote có thật nhưng claim sai và quote bịa
- [ ] Giải tay ví dụ entailment và contradiction

## M02.2 — Data Preparation

- [ ] Gán nhãn claim có nguồn đúng, sai, bịa và nhập nhằng
- [ ] Giữ source ID, quote, offsets và quan hệ ngữ nghĩa
- [ ] Đo độ đồng thuận và tách theo họ

## M02.3 — Implementation

- [ ] Xác minh source ID, quote và entity
- [ ] Khử trùng lập có bảo toàn provenance
- [ ] Kiểm thử quote lặp, sai nguồn và claim sai kiểu

## M02.4 — Baselines

- [ ] Giữ claim thô làm mốc và bật tắt kiểm tra span
- [ ] Thử đối chứng xác minh ngữ nghĩa nếu có nhãn
- [ ] Giữ nguyên output và mẫu đánh giá giữa phương án

## M02.5 — Metrics

- [ ] Tính structural valid rate, precision/recall support và unsupported rate
- [ ] Tách lỗi từ chối giả và chấp nhận giả
- [ ] Ghi mẫu số, tập rỗng và span boundary

## M02.6 — Execution & Analysis

- [ ] Chạy các đối chứng trên cùng output M01
- [ ] Phân tích quote đúng nhưng diễn giải sai
- [ ] Lưu bảng lỗi và chênh lệch từng loại

## M02.7 — Completion Gate

- [ ] Xác minh truy hồi được source và khoảng ký tự
- [ ] Có so sánh raw/validated và bằng chứng semantic support
- [ ] Ghi giới hạn trước M03

## P05 — Temporal Consistency

- [ ] Tái lập kết quả trên chuỗi, thứ tự thiếu và chu trình đã gán nhãn.

## M03.1 — Theory

- [ ] Định nghĩa event, before, đồng thời, thứ tự mở và chu trình
- [ ] Phân biệt thứ tự văn bản, nhận nguồn và xảy ra
- [ ] Giải tay một ví dụ thời gian không đầy đủ

## M03.2 — Mathematical Foundation

- [ ] Định nghĩa đồ thị, đường đi, bao đóng và thứ tự bộ phận
- [ ] Chứng minh quy tắc bắc cầu, nêu ca phản xạ do cycle
- [ ] So sánh độ phức tạp closure theo kích thước

## M03.3 — Literature Review

- [ ] Đọc nguồn sơ cấp về biểu diễn thời gian và đồ thị
- [ ] Lập bảng assumptions, granularity và đánh giá
- [ ] Ghi phần áp dụng được cho EADIS

## M03.4 — Dataset Preparation

- [ ] Tạo chuỗi, nhánh rời, thứ tự bị đảo và cycle
- [ ] Gán cạnh trực tiếp và cạnh suy ra
- [ ] Giữ bằng chứng nguồn theo event ID

## M03.5 — Implementation

- [ ] Triển khai biểu diễn sự kiện và closure có kiểm chứng
- [ ] Phát hiện chu trình và lưu provenance của cạnh đầu vào
- [ ] Đối chiếu ví dụ tay và oracle

## M03.6 — Experimental Conditions

- [ ] So direct-only với closure dưới cạnh đầy đủ, thiếu và sai
- [ ] Kiểm soát số event và độ dài chuỗi
- [ ] Lưu cấu hình từng điều kiện

## M03.7 — Metrics & Analysis

- [ ] Đo PRF cạnh trực tiếp/suy ra và phát hiện cycle
- [ ] Phân tích lan lỗi cạnh, đồ thị rỗng và cạnh phản xạ
- [ ] Báo kết quả theo độ sâu đường đi

## M03.8 — Completion Gate

- [ ] Tái lập closure và phát hiện cycle trên tập khóa
- [ ] Giải thích tại sao có sai số và assumptions của before
- [ ] Ghi run và chuyển M04

## P06 — Missing Evidence

- [ ] Báo mức thiếu, coverage, set size và các vi phạm monotonicity.

## M04.1 — Theory

- [ ] Phân biệt thiếu, phủ định và chưa biết theo open world
- [ ] Mô tả masking có kiểm soát và giới hạn về cơ chế thiếu
- [ ] Giải ví dụ thiếu thông tin dẫn đến nhiều phương án

## M04.2 — Problem Formulation

- [ ] Định nghĩa miền Ω và evidence quan sát theo mức thiếu
- [ ] Chốt tính bao hàm khi chỉ loại ràng buộc
- [ ] Ghi phản ví dụ khi extractor đổi interpretation

## M04.3 — Dataset Transformations

- [ ] Tạo biến thể xóa claim ngẫu nhiên, xóa claim then chốt và không có bằng chứng
- [ ] Giữ family IDs và nhãn theo điều kiện
- [ ] Kiểm tra biến thể không thêm tín hiệu ngoài ý định

## M04.4 — Baselines

- [ ] So dự đoán điểm, abstain, toàn miền và tập ràng buộc
- [ ] Chốt cách ánh xạ điểm vào tập
- [ ] Giữ cùng input và budget

## M04.5 — Implementation

- [ ] Thêm masking xác định theo seed và ghi biến đổi
- [ ] Tính tập khả dĩ có kiểm tra nghiệm rỗng
- [ ] Thêm fixture cho trường hợp không evidence

## M04.6 — Metrics

- [ ] Đo set exact, coverage, độ rộng và abstention
- [ ] Định nghĩa mẫu số khi gold rỗng
- [ ] Kiểm tra monotonicity và report rate theo mức thiếu

## M04.7 — Experiment Execution

- [ ] Chạy các mức thiếu trên cùng họ case
- [ ] Lưu seed, mask, run ID và output
- [ ] Xác minh thao tác che không đổi split

## M04.8 — Statistical Analysis

- [ ] Tính hiệu ứng ghép cặp theo họ và bất định khi đủ số họ
- [ ] Báo sai khác theo cấp độ thiếu
- [ ] Tách mô tả pilot khỏi suy luận tổng thể

## M04.9 — Completion Gate

- [ ] Đối chiếu coverage, kích thước và phản ví dụ
- [ ] Đính protocol, fixture, run và limitations
- [ ] Xác nhận trước khi chuyển M05

## P07 — Contradictory Evidence

- [ ] Kết quả phân biệt trạng thái và truy được nguồn gây xung đột.

## M05.1 — Theory

- [ ] Phân biệt mâu thuẫn logic, sai nguồn và cập nhật hợp lệ
- [ ] Giải thích tập vô nghiệm và fallback
- [ ] Nêu ca xung đột độc lập thời gian

## M05.2 — Conflict Taxonomy

- [ ] Phân nhóm chọn đối nghịch, chọn–loại, cycle và revision
- [ ] Ghi dấu hiệu, nguồn và hành động điều tra
- [ ] Thử taxonomy trên ca mới

## M05.3 — Dataset Preparation

- [ ] Tạo cặp nhất quán/mâu thuẫn có provenance
- [ ] Đảo thứ tự nguồn để thử order sensitivity
- [ ] Gán nhãn loại conflict và tập nghiêm ngặt

## M05.4 — Implementation

- [ ] Phát hiện vô nghiệm và cycle với cờ tách biệt
- [ ] Giữ nguồn gây xung đột và báo fallback có chính sách
- [ ] Kiểm thử duplicate, thêm cạnh và đổi thứ tự

## M05.5 — Baselines

- [ ] So chọn claim mới nhất, abstain và giao ràng buộc
- [ ] Ghi cách xử lý nguồn theo từng baseline
- [ ] Khóa evidence và chi phí đánh giá

## M05.6 — Evaluation

- [ ] Đo conflict precision/recall, set exact, fallback exact
- [ ] Đo độ ổn định theo thứ tự và khả năng truy nguồn
- [ ] Kiểm tra ca không conflict và false positive

## M05.7 — Experiment & Analysis

- [ ] Chạy theo loại và thứ tự source
- [ ] Lưu ca lỗi của từng baseline
- [ ] Diễn giải chính sách tin nguồn và giới hạn revision

## M05.8 — Completion Gate

- [ ] Xác minh mọi loại xung đột có đối chứng
- [ ] Đính bằng chứng run và minh họa witness
- [ ] Ghi quyết định chuyển M06

## P08 — Set-Valued Inference

- [ ] Giải tay và kiểm chứng máy, báo coverage cùng kích thước tập.

## M06.1 — Set-Valued Reasoning Theory

- [ ] Giải thích tập khả dĩ và dự đoán điểm
- [ ] Giải tay giao hợp, ràng buộc và bài toán vô nghiệm
- [ ] Phân biệt độ rộng tập với xác suất

## M06.2 — Partial Identification Foundation

- [ ] Định nghĩa đối tượng, giả định và identified set
- [ ] Giải thích point identification, set identification và bounds
- [ ] Ghi khi nào sandbox rời rạc không bảo đảm thống kê

## M06.3 — Formal Problem Definition

- [ ] Định nghĩa Ω, evidence E, tập thỏa và chính sách mâu thuẫn
- [ ] Nêu bất biến khi thêm ràng buộc và khi bỏ ràng buộc
- [ ] Viết ví dụ vi phạm khi giả định nguồn sai

## M06.4 — Manual Mathematical Exercises

- [ ] Tính bằng tay ca singleton, nhiều nghiệm, vô nghiệm và không evidence
- [ ] Chứng minh tính đơn điệu theo điều kiện đã nêu
- [ ] Đối chiếu với kết quả code

## M06.5 — Implementation

- [ ] Cài tập giao ràng buộc tất định và provenance
- [ ] Thêm oracle liệt kê phương án và test biên
- [ ] Tách tập fallback khỏi tập nghiêm ngặt

## M06.6 — Baselines

- [ ] Định nghĩa point, abstain, toàn miền và tập ràng buộc
- [ ] Dùng cùng miền và evidence
- [ ] Ghi giả định mỗi phương pháp

## M06.7 — Dataset Preparation

- [ ] Tạo fixture độ rộng khác nhau và nhãn nghiệm kiểm tay
- [ ] Kiểm soát miền phương án và số ràng buộc
- [ ] Xác minh nhãn không mâu thuẫn protocol

## M06.8 — Metrics

- [ ] Đo exact-set, coverage, cardinality và tỷ lệ conflict
- [ ] Định nghĩa điều kiện gold rỗng
- [ ] Báo chất lượng và độ rộng cùng lúc

## M06.9 — Experimental Execution

- [ ] Khóa bảng ca, baseline và seed
- [ ] Chạy và lưu kết quả từng case
- [ ] Tái chạy từ command đã ghi

## M06.10 — Analysis

- [ ] Đối chiếu ưu nhược coverage–size và lỗi ràng buộc
- [ ] Tách mismatch extractor và solver
- [ ] Ghi trường hợp chỉ đủ kết luận từng phần

## M06.11 — Statistical Partial Identification Toy Example

- [ ] Xây ví dụ tỷ lệ nhị phân với outcome thiếu
- [ ] Giải cận xấu nhất và thêm giả định có giải thích
- [ ] Phân biệt sampling uncertainty và identification region

## M06.12 — Completion Gate

- [ ] Đối chiếu chứng minh, bài giải tay và oracle
- [ ] Lưu kết quả coverage cùng độ rộng và ca vô nghiệm
- [ ] Tự giải thích điều kiện partial identification trước M07

## P09 — Incremental Inference

- [ ] So khớp oracle từng prefix trước khi so hiệu năng.

## M07.1 — Algorithmic Foundation

- [ ] Ôn cập nhật trạng thái, cache, dependency graph và bất biến
- [ ] So compute từ đầu với tái sử dụng tiền tố
- [ ] Giải tay sequence có invalidate

## M07.2 — Literature Review

- [ ] Đọc nguồn sơ cấp về incremental computation và truth maintenance
- [ ] So assumptions về append, delete, revise
- [ ] Ghi phạm vi dùng lại và nguồn

## M07.3 — Formal Problem

- [ ] Định nghĩa prefix, state, output và phép update
- [ ] Chọn đặc tả equivalence theo từng bước với full oracle
- [ ] Nêu điều kiện cho deterministic behavior

## M07.4 — Evidence Update Operations

- [ ] Đặc tả append, duplicate, remove và replace
- [ ] Ghi semantics ID, provenance cùng invalidation
- [ ] Kiểm thử thứ tự, ca không đổi và ca xung đột

## M07.5 — Full Recomputation Baseline

- [ ] Tính lại từ evidence hiện hành và oracle độc lập
- [ ] Đảm bảo cùng semantics qua cập nhật
- [ ] Xác minh bằng ví dụ tay và test

## M07.6 — Cached Recomputation Baseline

- [ ] Cache phần tái dùng đã xác định và ghi cache key
- [ ] Kiểm thử invalidation trên thay đổi provenance và state
- [ ] Đo hit rate và chi phí riêng

## M07.7 — Dependency-Aware Incremental Baseline

- [ ] Xác định phụ thuộc từ claim tới trạng thái và closure
- [ ] Cập nhật phần bị tác động và invalidation hoàn chỉnh
- [ ] Kiểm tra output kèm nguồn so oracle

## M07.8 — Correctness Verification

- [ ] So từng prefix và loại update với full recompute
- [ ] Dùng chuỗi nhỏ bao quát và test ngẫu nhiên tái tạo được
- [ ] Lưu counterexample đầu tiên và tránh benchmark sai

## M07.9 — Complexity Analysis

- [ ] Suy ra chi phí theo số claim, option, event và vùng tác động
- [ ] Phân biệt worst-case, amortized và kích thước cache
- [ ] Nêu closure dày và chi phí invalidation

## M07.10 — Dataset & Update Sequences

- [ ] Sinh chuỗi theo seed có append, duplicate, remove và revise
- [ ] Thay prefix length và batch size có đối chứng
- [ ] Khóa nhãn và manifest thử nghiệm

## M07.11 — Performance Evaluation

- [ ] Warm-up, lặp cặp đo và đảo thứ tự
- [ ] Tách extraction IO khỏi thời gian engine, đo memory nếu có
- [ ] Báo median và phân tán trên cùng máy

## M07.12 — Result Analysis

- [ ] Tính sai khác theo prefix, vùng tác động và loại update
- [ ] Xác định điểm hòa vốn và outlier
- [ ] Ghi hardware và sai số timing

## M07.13 — Theoretical Reasoning

- [ ] Chứng minh bất biến append và nêu điều kiện invalidation đủ
- [ ] Đưa phản ví dụ cho xóa nguồn khi chỉ có giao tích lũy
- [ ] Tách điều kiện chứng minh và quan sát thực nghiệm

## M07.14 — Completion Gate

- [ ] Xác minh agreement từng prefix thuộc phạm vi
- [ ] Đính oracle, run, độ phức tạp và giới hạn
- [ ] Chỉ xác nhận tốc độ sau khi đã kiểm tra correctness

## P10 — Robustness & Generalization

- [ ] Kiểm tra nhãn trước khi chạy và báo riêng từng điều kiện.

## M08.1 — Theory

- [ ] Phân biệt robustness, generalization và distribution shift
- [ ] Xác định đơn vị ghép cặp và điều kiện bảo toàn nhãn
- [ ] Nêu domain confound và giới hạn suy rộng

## M08.2 — Dataset Conditions

- [ ] Tạo paraphrase, noise, thay domain và biến thể khó
- [ ] Giữ family IDs, phiên bản và độ nhiễu
- [ ] Tách held-out theo họ và domain

## M08.3 — Transformation Validation

- [ ] Kiểm tra độc lập label invariance và điều kiện ngoại lệ
- [ ] Lưu provenance biến thể và quy tắc loại
- [ ] Đo đồng thuận trên subset

## M08.4 — Pipeline Evaluation

- [ ] Chạy cùng pipeline, prompt và ngân sách trên từng điều kiện
- [ ] Giữ kết quả thô và lỗi, ghi version
- [ ] Đánh giá lỗi truyền giữa extraction, validation và inference

## M08.5 — Metrics & Analysis

- [ ] Tính chênh lệch ghép cặp F1, set exact và failure rate
- [ ] Báo bất định theo họ có đủ dữ liệu
- [ ] Phân tích lỗi theo điều kiện và giới hạn external validity

## M08.6 — Optional Model Comparison

- [ ] Nếu cần, chọn model theo câu hỏi đã chốt
- [ ] Kiểm soát prompt, quantization, split và hardware
- [ ] Ghi cấu hình và phân tích tương tác model/condition

## M08.7 — Completion Gate

- [ ] Xác minh biến thể có nhãn đã kiểm chứng
- [ ] Đính kết quả theo condition và kết luận có phạm vi
- [ ] Xác nhận đủ dữ liệu chuyển P11

## P11 — Statistical Analysis & Scientific Validation

- [ ] Kết luận truy được về run/commit/data và nêu bất định.

## P11.1 — Data Integrity

- [ ] Đối chiếu checksum, split, đơn vị phân tích và schema
- [ ] Kiểm tra missing runs, outlier và sai merge
- [ ] Ghi loại trừ kèm lý do và manifest gốc

## P11.2 — Statistical Methodology

- [ ] Chọn thống kê mô tả, effect size, paired bootstrap theo family nếu đủ
- [ ] Ghi cách xử lý nhiều phép so, bất định và missingness
- [ ] Kiểm chứng phép tính với ví dụ tay

## P11.3 — Visualization

- [ ] Vẽ kết quả theo condition với số mẫu và bất định
- [ ] Thể hiện phân bố timing, độ rộng tập và lỗi
- [ ] Lưu dữ liệu nguồn, code và chú thích rõ đơn vị

## P11.4 — Ablation Studies

- [ ] Chốt các thành phần span check, closure, constraints và cache
- [ ] Giữ dữ liệu/setting nhất quán giữa đối chứng
- [ ] Báo tác động và tương tác quan sát được

## P11.5 — Failure Taxonomy

- [ ] Lấy mẫu lỗi stratified theo condition
- [ ] Mã hóa lỗi extraction, grounding, temporal, inference và runner
- [ ] Kiểm tra đồng thuận và lưu ca đại diện

## P11.6 — Threats to Validity

- [ ] Rà construct, internal, external và conclusion validity
- [ ] Ghi confound, bias chọn mẫu và độ nhạy metric
- [ ] Liên kết mỗi kết luận với phạm vi bằng chứng

## P11.7 — Reproducibility Verification

- [ ] Tái chạy độc lập từ commit, manifest, môi trường và seed
- [ ] Đối chiếu output dự đoán và dung sai cho timing
- [ ] Lưu run so sánh và chênh lệch

## P11.8 — Completion Gate

- [ ] Kiểm tra kết quả, chỉ số, biểu đồ và tái lập
- [ ] Ghi bất định, giới hạn và claims có thể bảo vệ
- [ ] Đính bằng chứng và xác nhận chuyển P12

## P12 — Research Transfer to ETVM-PI

- [ ] Người thực hiện xác nhận bằng chứng và điều kiện nghiên cứu.

## P12.1 — Research Knowledge Integration

- [ ] Tóm tắt kết quả theo RQ và phần chưa bác bỏ
- [ ] Nối quan sát với lý thuyết và giả định
- [ ] Ghi bài học, ca biên và điều kiện chuyển giao

## P12.2 — Computer Science Transfer

- [ ] Lập bản đồ schema, provenance, temporal graph và thuật toán
- [ ] Ghi API, invariants và trade-off đo được
- [ ] Phân biệt phần có thể tái dùng và phần cần đặc tả mới

## P12.3 — Data Science Transfer

- [ ] Lập bản đồ dataset, nhãn, metrics, split và protocol
- [ ] Ghi split theo họ, uncertainty và giám sát rò rỉ
- [ ] Ưu tiên bằng chứng cần thu thập tiếp

## P12.4 — Literature & Research Gap Review

- [ ] Tổng hợp nghiên cứu gốc và đối chiếu giả định
- [ ] Cập nhật bảng vị trí EADIS/ETVM-PI và ngày tìm kiếm
- [ ] Ghi giới hạn độ bao phủ của truy vấn

## P12.5 — Potential Research Gap Identification

- [ ] Phát biểu khoảng trống ứng viên như câu hỏi có thể kiểm định
- [ ] So với phương pháp gần nhất và nêu bằng chứng bác bỏ
- [ ] Ghi điều kiện cần xác minh trước khi khẳng định đóng góp

## P12.6 — ETVM-PI Research Readiness

- [ ] Tự đánh giá năng lực CS, DS, toán và protocol
- [ ] Đối chiếu bằng chứng với tiêu chí FINAL
- [ ] Ghi điều kiện mở và rủi ro chuyển giao

## P12.7 — Final Technical Report

- [ ] Viết báo cáo theo câu hỏi, phương pháp, kết quả và limitations
- [ ] Gắn run ID, code/data hash và nguồn tài liệu
- [ ] Rà các nhận định và tái chạy ví dụ

## P12.8 — Final Repository Verification

- [ ] Xác minh README, liên kết, tests, issue mappings và artifacts
- [ ] Kiểm tra truy xuất các bằng chứng đã dẫn
- [ ] Người thực hiện xác nhận readiness và các phần hoãn

## CONTINUOUS — Research Quality & Progress Management

- [ ] Duy trì chu kỳ đọc, kiểm tra code, xác minh run và reflection.
- [ ] Giữ trách nhiệm mở và ghi bằng chứng theo tuần.

## OPTIONAL — Advanced Research Extensions

- [ ] Chốt câu hỏi, giá trị và protocol trước khi kích hoạt extension.
- [ ] Ghi lý do thực hiện hoặc hoãn. Completion gates EADIS có thể đạt khi backlog còn mở.

## C01 — Literature Reading & Research Notes

- [ ] Mỗi tuần đọc nguồn gốc và ghi câu hỏi, giả định, kết quả
- [ ] Đối chiếu evidence với diễn giải cá nhân
- [ ] Liên kết note, RQ và việc đọc tiếp

## C02 — Git Workflow & Code Quality

- [ ] Kiểm tra diff, tests và commit theo thay đổi nhỏ
- [ ] Ghi phiên bản, giữ cấu hình sạch và review code
- [ ] Lặp lại khi có thay đổi mới

## C03 — Experiment Run Verification

- [ ] Mỗi run kiểm tra input hash, split, seed, config và tình trạng worker
- [ ] So output với oracle/smoke và lưu raw artifacts
- [ ] Ghi lỗi, rerun và lý do tách riêng

## C04 — Weekly Research Reflection

- [ ] Mỗi tuần ghi điều học được, lỗi, giả định và câu hỏi
- [ ] Tách quan sát khỏi suy đoán
- [ ] Liên kết run, commit và bước tiếp

## C05 — Responsible Use of AI Coding Assistants

- [ ] Tự giải thích thuật toán, test và kiểm tra nguồn AI hỗ trợ
- [ ] Bảo vệ dữ liệu nhạy cảm và kiểm chứng trích dẫn
- [ ] Ghi phần đã review và quyết định do người thực hiện

## O01 — Advanced Uncertainty

- [ ] Đề xuất mô hình uncertainty và tiêu chí hiệu chỉnh
- [ ] So với baseline tập khả dĩ dưới giả định rõ
- [ ] Chốt chi phí và bằng chứng trước khi đưa vào core

## O02 — Advanced Temporal Modeling

- [ ] Thử khoảng, thời điểm không chắc chắn và quan hệ mở rộng
- [ ] Xây fixture và kiểm tính nhất quán
- [ ] So với đồ thị before theo protocol

## O03 — Advanced Inference Algorithms

- [ ] Đề xuất solver hoặc logic mềm cho nguồn xung đột
- [ ] So correctness, giải thích và độ phức tạp với oracle
- [ ] Ghi điều kiện áp dụng và giới hạn

## O04 — External Validation

- [ ] Chọn dữ liệu có giấy phép và điều kiện riêng tư phù hợp
- [ ] Thiết kế annotation và đánh giá độc lập
- [ ] Báo dịch chuyển domain và giới hạn ngoại suy

## O05 — Advanced Infrastructure

- [ ] Đo bottleneck trước khi thiết kế hạ tầng
- [ ] Ưu tiên trace, run recovery và khả năng tái lập
- [ ] So chi phí vận hành với runner hiện có

## FINAL — EADIS Research Readiness Assessment for ETVM-PI

- [ ] Kiến thức · Tự giải thích extraction, grounding, thời gian, uncertainty, partial identification và incremental reasoning bằng ví dụ và phản ví dụ.
- [ ] Implementation · Chạy tests, xác minh provenance, cách ly nhãn và đối chiếu oracle theo prefix.
- [ ] Thực nghiệm · Đối chiếu M01–M08 với protocol, chỉ số, đối chứng, run và hạn chế.
- [ ] Sản phẩm · Nộp ghi chú toán, dữ liệu, manifest, taxonomy, báo cáo và transfer map.
- [ ] Giới hạn · Ghi kết luận có thể bảo vệ, giả định chưa kiểm chứng và bằng chứng còn thiếu.
- [ ] CS · Giải thích invariants, chi phí và ca lỗi của schema, solver, closure và cập nhật.
- [ ] DS · Giải thích annotation, split, mẫu số, thống kê, khái quát và tái lập.
- [ ] ETVM-PI · Liệt kê phần tái dùng, điều kiện chuyển giao và giả thuyết kế tiếp.
- [ ] Trả lời: run nào hỗ trợ mỗi kết luận, kết quả nào bác bỏ và bước kiểm chứng tiếp theo là gì?
- [ ] Người thực hiện xác nhận các gate P00–P12 trước khi đóng.

<!-- eadis-checklist-end -->

## Lịch sử E01–E12

## Checklist tổng tiến độ

`[x]` chỉ cho việc đã kiểm chứng tại local; không đại diện hoàn thành benchmark hoặc triển khai từ xa.

### 1. Repository Setup

- [x] Tạo framework và cấu trúc E01–E12 trên local.
- [x] Tạo 12 branch thí nghiệm có commit điều kiện riêng.
- [x] Gắn origin đúng repository được chỉ định.
- [x] Push main và 12 branch; xác minh remote.
- [x] Xác minh GitHub Actions trên main.
- [ ] Rà soát tài liệu sau từng đợt cập nhật.

### 2. Linux & Ollama Setup

- [ ] Cài Ubuntu/Python trên hai laptop.
- [ ] Cài Ollama và tải tag model.
- [ ] Kiểm kê chip, GPU, RAM/VRAM, nguồn và thermal throttling.
- [ ] Kiểm tra API/digest/quantization từng endpoint.
- [ ] Xác nhận hai chip cùng loại không bị coi là hiệu năng giống tuyệt đối.

### 3. Agent Runtime

- [x] Chuẩn hóa response Ollama và kiểm thử parser.
- [x] Kiểm thử timeout/lỗi API bằng mock.
- [x] Không truyền expected_output hoặc lịch sử agent khác vào request.
- [ ] Xác minh agent A/B trên Ollama thật.

### 4. Experiment Controller

- [x] Đọc và validate YAML/dataset.
- [x] Hỗ trợ repetition, dry-run và mock test.
- [x] Ghi manifest, JSONL và CSV qua kiểm thử.
- [ ] Xác minh toàn bộ luồng trên hai laptop.

### 5. Dataset Preparation

- [x] Tạo smoke tasks có ghi rõ giới hạn sử dụng.
- [ ] Chọn dataset nghiên cứu có nguồn/license.
- [ ] Khử trùng lặp và chuẩn hóa domain/độ khó.
- [ ] Tách experience/development khỏi final evaluation.
- [ ] Khóa checksum, rubric và cỡ mẫu.

### 6. E01–E06: Model & Hardware

- [ ] E01: đo độ ổn định và biến động.
- [ ] E02: so model cùng điều kiện.
- [ ] E03: kiểm soát nguồn/nhiệt và đo tài nguyên.
- [ ] E04: so kích thước và ghi OOM.
- [ ] E05: so quantization từ cùng trọng số.
- [ ] E06: đo đủ tổ hợp chip–model hoặc ghi không khả thi.

### 7. E07–E10: Domain & Behavior

- [ ] E07: đánh giá chuyên môn hóa trong và ngoài domain.
- [ ] E08: xác nhận độ khó trước chạy.
- [ ] E09: khóa prompt và ví dụ few-shot ngoài final.
- [ ] E10: triển khai tool loop/trace rồi đo can thiệp.

### 8. E11–E12: Adaptation

- [ ] Triển khai memory store tách agent/session và retrieval trace.
- [ ] E11: đánh giá chuyển giao, lỗi lặp và memory cũ.
- [ ] Thiết kế feedback đúng/sai, binary/detailed và correction trace.
- [ ] E12: đánh giá sửa lỗi và chống feedback sai.
- [ ] Đóng băng adaptation trước final; không kết luận thay đổi trọng số.

### 9. Evaluation & Analysis

- [x] Kiểm thử exact-match, latency và consistency.
- [ ] Thu thập resource/energy/TTFT bằng công cụ phù hợp.
- [ ] Chấm rubric mù và giải quyết bất đồng.
- [ ] Bootstrap theo task, báo CI, phân tích lỗi và vẽ biểu đồ.
- [ ] Kiểm tra tính tái lập từ manifest.

### 10. Research Reporting

- [ ] Tổng hợp kết quả và hạn chế.
- [ ] Tách giả thuyết, dự đoán và quan sát thực tế.
- [ ] Cập nhật research log.
- [ ] Viết báo cáo khoa học có nguồn dữ liệu và code/config version.

### Trạng thái từng thí nghiệm

#### [E01_baseline](../experiments/E01_baseline/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E02_model_type](../experiments/E02_model_type/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E03_hardware](../experiments/E03_hardware/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E04_model_size](../experiments/E04_model_size/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E05_quantization](../experiments/E05_quantization/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E06_hardware_model](../experiments/E06_hardware_model/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E07_domain](../experiments/E07_domain/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E08_difficulty](../experiments/E08_difficulty/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E09_prompt](../experiments/E09_prompt/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E10_tools](../experiments/E10_tools/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E11_memory](../experiments/E11_memory/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

#### [E12_feedback](../experiments/E12_feedback/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành
