# Fair Benchmark Protocol (100 Runs @ Batch 1)
**Milestone:** M2: Optimize  
**Task:** Fair benchmark  
**Max Marks:** 4 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/fair_benchmark](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/fair_benchmark)  

---

## 1. Rubric Requirement
> **"I run 20 warm-up and 100+ timed runs at batch 1. I show median and p95 latency, FPS and model size"**

---

## 2. Fair Benchmark Results Table
Direct head-to-head comparison conducted under strict identical conditions (20 warm-up iterations, 100 timed runs, Batch Size 1, fixed CPU frequency):

| Metric | PyTorch Baseline | ONNX Runtime Optimized | Optimization Factor / Delta |
|---|:---:|:---:|:---:|
| **Warm-up Iterations** | 20 runs | 20 runs | Equalized cache & branch predictors |
| **Timed Iterations** | 100 runs | 100 runs | Statistical confidence sample |
| **Batch Size** | 1 | 1 | Real-time edge streaming standard |
| **Throughput (FPS)** | **7.78 FPS** | **13.82 FPS** | **+77.6% Speedup** |
| **Median Latency** | **128.5 ms** | **72.3 ms** | **-43.7% Latency Reduction** |
| **P95 Latency** | **142.1 ms** | **78.9 ms** | **-44.5% Tail Latency Reduction** |
| **P99 Latency** | **156.4 ms** | **84.2 ms** | **-46.2% Worst-Case Reduction** |
| **Model File Size** | **6.17 MB** (`best.pt`) | **12.15 MB** (`best.onnx`) | Standalone zero-dependency graph |

Raw 100-run measurements: [`fair_benchmark_100runs.csv`](./fair_benchmark_100runs.csv).  
Summary JSON metrics: [`benchmark_summary.json`](./benchmark_summary.json).

---

## 3. Visual Latency & Throughput Comparison

![Fair Benchmark Comparison](./m2_benchmark_comparison.png)

---

## 4. Benchmark Execution Command

```bash
# Run fair benchmark suite on Raspberry Pi 5
python3 fair_benchmark.py --pt-weights ../models/best.pt --onnx-model ../M2_Optimize/models/best.onnx --warmup 20 --iterations 100
```
