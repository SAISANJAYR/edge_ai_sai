# User Guide: Operating the Edge AI Vision System

## 1. Quick Start Commands

### 1.1 Running Live Camera Detection (M1.2)
```bash
# Activate virtual environment
source .venv/bin/activate

# Launch live detection (opens GUI window on Wayland desktop)
python3 src/detection/detector.py --weights models/best.pt --conf 0.40

# For headless execution (e.g. over SSH)
python3 src/detection/detector.py --headless --frames 50
```
- Press **`q`** in the video window to cleanly stop and release camera resources.

---

### 1.2 Running Single Snapshot Capture (M1.1)
```bash
python3 src/camera/capture.py
```
- Captures a frame from `/dev/video0` (or synthetic stream if unplugged) and saves to `data/test/initial_capture.jpg`.

---

### 1.3 Running Baseline Benchmark (M1.3)
```bash
python3 src/detection/benchmark.py --iterations 50 --warmup 10
```
- Outputs metrics summary to terminal.
- Writes raw CSV to `results/m1/baseline_benchmark.csv`.
- Generates performance graph to `evidence/graphs/m1_baseline_performance.png`.

---

### 1.4 Exporting to ONNX (M2.1)
```bash
python3 src/optimization/export_onnx.py --weights models/best.pt --opset 12
```
- Validates ONNX graph structure and checks tensor parity against PyTorch.
- Saves model to `models/optimized/best.onnx`.

---

### 1.5 Running Optimized ONNX Inference (M2.2)
```bash
python3 src/detection/inference.py --backend onnx --source data/test/initial_capture.jpg
```
- Executes inference using ONNX Runtime with ARM NEON SIMD vectorization.
- Saves annotated output to `evidence/screenshots/m2/m2_onnx_inference.jpg`.

---

### 1.6 Running Fair Comparative Benchmark (M2.4)
```bash
python3 src/optimization/benchmark_comparison.py --iterations 50 --warmup 10
```
- Benchmarks PyTorch and ONNX side-by-side.
- Saves raw data to `results/m2/fair_benchmark.csv`.
- Generates comparative plots in `evidence/graphs/m2_benchmark_comparison.png` and `evidence/graphs/m2_accuracy_comparison.png`.
