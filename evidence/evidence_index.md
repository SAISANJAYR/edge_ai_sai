# Individual Assessment Evidence Index & Traceability Matrix
## Scope: Milestone 1 (Detect) & Milestone 2 (Optimize) — Total: 40 Marks

This document tracks all 12 individual assessment requirements across M1 and M2 according to the project rubric.

Statuses:
- `NOT STARTED`: Task not yet initiated.
- `IN PROGRESS`: Implementation actively underway.
- `IMPLEMENTED`: Code written and committed.
- `TESTED`: Functional verification completed with empirical logs/data.
- `EVIDENCE CAPTURED`: Screenshots, photographs, benchmarks, and reports recorded.
- `BLOCKED`: Blocked on external dependency or physical hardware.

---

## Milestone 1: Detect (20 Marks)

| Item | Marks | Requirement Description | Implementation Target | Test Command / Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|---|
| **M1.1** | 2 | Camera & Repository Setup | `src/camera/camera_manager.py`, `src/camera/capture.py` | `python3 src/camera/capture.py` | Git initialized; USB camera absent, auto-fallback simulation active, snapshot saved | `evidence/photographs/camera_setup/initial_capture.jpg` | `data/test/initial_capture.jpg` | Pending commit | **EVIDENCE CAPTURED** |
| **M1.2** | 4 | OpenCV Pipeline & YOLOv8 Detection | `src/detection/detector.py` | `python3 src/detection/detector.py --headless --frames 25` | Real-time YOLOv8n detector with bounding box, conf %, FPS overlay, count | `evidence/screenshots/m1/m1_live_detection.jpg` | `src/detection/detector.py` | Pending commit | **EVIDENCE CAPTURED** |
| **M1.3** | 3 | Baseline Speed Benchmarking | `src/detection/benchmark.py`, `src/monitoring/hardware_monitor.py` | `python3 src/detection/benchmark.py --iterations 50 --warmup 10` | 50 iterations: Median latency 303.5 ms, 3.29 FPS, 82.9% CPU, 81.3°C avg | `evidence/graphs/m1_baseline_performance.png` | `results/m1/baseline_benchmark.csv` | Pending commit | **EVIDENCE CAPTURED** |
| **M1.4** | 4 | Roboflow Dataset v1 Audit & Card | `docs/DATASET_CARD.md`, `src/evaluation/` | Model checkpoint metadata extraction | Checkpoint metadata audited; single class `enclosure`; raw images not on disk | `evidence/graphs/m1_training_evaluation_curves.png` | `docs/DATASET_CARD.md` | Pending commit | **TESTED** |
| **M1.5** | 2 | Dataset Split Verification (70/20/10) | `docs/DATASET_CARD.md`, `docs/M1_REPORT.md` | Split ratio verification & leakage audit | Audit documented in Dataset Card & M1 Report | N/A | `docs/M1_REPORT.md` | Pending commit | **IN PROGRESS** |
| **M1.6** | 5 | Train and Run Detector Evaluation | `src/evaluation/extract_training_history.py` | `python3 src/evaluation/extract_training_history.py` | 52 epochs extracted: P=0.842, R=0.133, mAP50=0.142 at epoch 32 | `evidence/graphs/m1_training_evaluation_curves.png` | `results/m1/training_history.csv` | Pending commit | **EVIDENCE CAPTURED** |

---

## Milestone 2: Optimize (20 Marks)

| Item | Marks | Requirement Description | Implementation Target | Test Command / Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|---|
| **M2.1** | 3 | Export to ONNX | `src/optimization/export_onnx.py` | `python3 src/optimization/export_onnx.py` | Exported `best.onnx` (12.16 MB), opset 12, validated, max parity diff $2.29\times 10^{-4}$ | `evidence/screenshots/m2/m2_onnx_inference.jpg` | `results/m2/export_onnx.log` | Pending commit | **EVIDENCE CAPTURED** |
| **M2.2** | 4 | Convert & Run Live (NCNN/ONNX Runtime) | `src/optimization/convert_model.py`, `src/detection/inference.py` | `python3 src/detection/inference.py --backend onnx` | ONNX Runtime CPU selected & tested; NCNN/TFLite wheels evaluated | `evidence/screenshots/m2/m2_onnx_inference.jpg` | `results/m2/backend_investigation.json` | Pending commit | **TESTED** |
| **M2.3** | 4 | Accuracy Check (PyTorch vs ONNX) | `src/optimization/benchmark_comparison.py` | `python3 src/optimization/benchmark_comparison.py` | Exact numerical parity verified; bbox & conf parity confirmed ($\Delta < 10^{-3}$) | `evidence/graphs/m2_accuracy_comparison.png` | `results/m2/benchmark_summary.json` | Pending commit | **EVIDENCE CAPTURED** |
| **M2.4** | 4 | Fair Benchmark (Warm-up + Timed Runs) | `src/optimization/benchmark_comparison.py` | `python3 src/optimization/benchmark_comparison.py --iterations 50 --warmup 10` | 1.24x speedup: PyTorch 231.3ms (4.32 FPS) vs ONNX 185.9ms (5.38 FPS) | `evidence/graphs/m2_benchmark_comparison.png` | `results/m2/fair_benchmark.csv` | Pending commit | **EVIDENCE CAPTURED** |
| **M2.5** | 2 | CPU vs Accelerator + Architecture | `docs/SYSTEM_ARCHITECTURE.md`, `docs/M2_REPORT.md` | Hardware comparison table & stack diagram | Architecture diagram & CPU vs accelerator analysis documented | N/A | `docs/M2_REPORT.md` | Pending commit | **IMPLEMENTED** |
| **M2.6** | 3 | Target & Speedup Trade-off | `docs/PERFORMANCE_REPORT.md`, `docs/M2_REPORT.md` | Empirical speedup calculation vs accuracy delta | Pre-established target (15%) exceeded: 19.6% latency reduction achieved | `evidence/graphs/m2_benchmark_comparison.png` | `docs/PERFORMANCE_REPORT.md` | Pending commit | **EVIDENCE CAPTURED** |
