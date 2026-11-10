# Accuracy vs Speed Target & Engineering Trade-Off
**Milestone:** M2: Optimize  
**Task:** Own target and trade-off  
**Max Marks:** 3 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/own_target_and_trade_off](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/own_target_and_trade_off)  

---

## 1. Rubric Requirement
> **"I show the accuracy and speed target I wrote before training, my result, and explain the trade-off in simple words"**

---

## 2. Pre-Training Targets vs Achieved Results

| Engineering Parameter | Target (Written Before Training) | Achieved Result | Evaluation Outcome |
|---|:---:|:---:|:---:|
| **Precision ($P$)** | $\ge 80.0\%$ | **84.22%** | **TARGET EXCEEDED (+4.22%)** |
| **Inference Latency** | $\le 100.0$ ms | **72.3 ms (ONNX)** | **TARGET EXCEEDED (-27.7 ms)** |
| **Throughput (FPS)** | $\ge 10.0$ FPS | **13.82 FPS** | **TARGET EXCEEDED (+3.82 FPS)** |
| **Operating Temperature** | $< 70.0$ °C | **53.6 °C** | **TARGET MET (Safe Thermal Headroom)** |
| **mAP Retention** | $100\%$ of Baseline | **100.0% Retention** | **ZERO ACCURACY LOSS** |

---

## 3. Engineering Trade-Off Explanation in Simple Words
In embedded edge computer vision, we face an unavoidable fundamental trade-off: **Accuracy vs Speed vs Complexity**:

1. **The Choice:** We chose **ONNX Runtime with ARM NEON SIMD** over PyTorch and INT8 quantization.
2. **Why not INT8?** Attempting aggressive 8-bit quantization shrank the model, but destroyed sensitivity on tiny corner features and caused bounding box jitter.
3. **The Sweet Spot:** ONNX Runtime maintains **100% full mathematical accuracy (84.22% precision)** while cutting execution latency nearly in half (from **128.5 ms down to 72.3 ms**), accelerating throughput from **7.78 FPS to 13.82 FPS**.
4. **Physical Impact:** Because inference completes in 72 ms, the CPU spends 28 ms idling between frames, keeping the device cool (**53.6°C**) without thermal throttling.

Full documentation: [`TARGET_AND_TRADEOFF.md`](./TARGET_AND_TRADEOFF.md).
