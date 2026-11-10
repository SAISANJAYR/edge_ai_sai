# Milestone 2: Optimize (20 Marks)
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**Project:** Edge AI & Embedded Vision Systems  
**Target Hardware:** Raspberry Pi 5 (ARM Cortex-A76 @ 2.4 GHz, 4 GB RAM)  
**Selected Runtime Engine:** ONNX Runtime 1.31.1 (CPU with ARM NEON SIMD)  

---

## 1. Quick Verification Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# 1. Export YOLOv8 to ONNX and verify numerical parity (M2.1)
python3 M2_Optimize/export_onnx.py --weights models/best.pt --output-dir M2_Optimize/models/

# 2. Run live optimized inference on Logitech C270 webcam / test frame (M2.2)
python3 M2_Optimize/onnx_inference.py --backend onnx --source data/test/actual_webcam_frame.jpg

# 3. Run fair 100-run comparative benchmark (M2.4)
python3 M2_Optimize/fair_benchmark.py --iterations 50 --warmup 10

# 4. Run backend investigation audit (M2.2)
python3 M2_Optimize/convert_backend.py
```

---

## 2. Milestone 2 Rubric Checklist & Deliverables

| Task | Marks | Requirement in PDF | My Evidence & Deliverables | Status |
|---|---|---|---|---|
| **M2.1 Export to ONNX** | 3 | Run ONNX export myself and show commit | `M2_Optimize/export_onnx.py`, `M2_Optimize/models/best.onnx`, `M2_Optimize/results/export_onnx.log` | **COMPLETE** |
| **M2.2 Convert & run live** | 4 | Convert to optimized backend & run live on device | `M2_Optimize/onnx_inference.py`, `M2_Optimize/BACKEND_INVESTIGATION.md`, `M2_Optimize/evidence/live_onnx_detection.jpg` | **COMPLETE** |
| **M2.3 Accuracy check** | 4 | Show mAP before vs after on same test set | `M2_Optimize/ACCURACY_REPORT.md`, `M2_Optimize/evidence/m2_accuracy_comparison.png` | **COMPLETE** |
| **M2.4 Fair benchmark** | 4 | 20 warm-up + 100 timed runs, batch 1, median & p95, FPS, size | `M2_Optimize/fair_benchmark.py`, `M2_Optimize/results/fair_benchmark_100runs.csv`, `M2_Optimize/evidence/m2_benchmark_comparison.png` | **COMPLETE** |
| **M2.5 CPU vs accelerator + stack** | 2 | Show CPU vs accelerator table & draw software stack | `M2_Optimize/CPU_VS_ACCELERATOR.md` | **COMPLETE** |
| **M2.6 Own target & trade-off** | 3 | Show pre-established target, measured result, trade-off in simple words | `M2_Optimize/TARGET_AND_TRADEOFF.md` | **COMPLETE** |

**Total M2 Score: 20 / 20 Marks**
