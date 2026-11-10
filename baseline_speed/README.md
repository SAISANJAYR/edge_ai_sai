# Baseline Speed & Telemetry Benchmark
**Milestone:** M1: Detect  
**Task:** Baseline speed  
**Max Marks:** 3 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/baseline_speed](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/baseline_speed)  

---

## 1. Rubric Requirement
> **"I measure FPS, latency, CPU/GPU load, temperature and show my own numbers"**

---

## 2. Experimental Benchmark Results
Measurements collected on Raspberry Pi 5 (Debian 13 ARM64) over 50 continuous timed inference iterations at batch size 1 ($640 	imes 640$ input resolution):

| Performance Metric | Laboratory Measurement | Rubric / Engineering Standard | Status |
|---|:---:|:---:|:---:|
| **Mean Throughput (FPS)** | **7.78 FPS** | $\ge 5.0$ FPS | **PASSED** |
| **Median Latency** | **128.5 ms** | $\le 150.0$ ms | **PASSED** |
| **95th Percentile (P95) Latency** | **142.1 ms** | $\le 200.0$ ms | **PASSED** |
| **Min Latency** | **121.3 ms** | - | **PASSED** |
| **Max Latency** | **156.4 ms** | - | **PASSED** |
| **Average CPU Load** | **58.4%** | $< 80\%$ (Quad-Core Cortex-A76) | **PASSED** |
| **GPU / VPU Load** | **12.1%** | Handled by VideoCore VII | **PASSED** |
| **Core Operating Temperature** | **53.6 °C** | $< 75.0$ °C (Active Cooler) | **PASSED** |
| **Thermal Throttling Events** | **0 events** | Zero frequency capping | **PASSED** |

Raw iteration telemetry is documented in [`baseline_speed_measurements.csv`](./baseline_speed_measurements.csv).

---

## 3. Graphical Performance Analysis
Telemetry visualizations generated directly from recorded device logs:

![Baseline Speed Performance Visualization](./m1_baseline_performance.png)

The visualization demonstrates:
1. **Latency Distribution:** Tight clustering around 128 ms with negligible tail latency outliers.
2. **Throughput Stability:** Constant 7.6 – 8.0 FPS sustained across the 50 runs.
3. **Thermal Stability:** Stable 53.6°C operating temperature under full inference load, confirming active cooling sufficiency.

---

## 4. Benchmark Script & Replication

```bash
# Run baseline speed benchmark on device
python3 benchmark.py --weights ../models/best.pt --iterations 50 --warmup 10 --output baseline_speed_measurements.csv
```

Full engineering analysis is documented in [`BASELINE_REPORT.md`](./BASELINE_REPORT.md).
