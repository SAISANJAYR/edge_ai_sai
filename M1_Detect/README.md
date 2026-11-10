# Milestone 1: Detect (20 Marks)
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**Project:** Edge AI & Embedded Vision Systems  
**Target Hardware:** Raspberry Pi 5 (4 GB RAM, Broadcom BCM2712 Cortex-A76 @ 2.4 GHz)  
**Camera:** Logitech C270 HD Webcam (`/dev/video0`)  

---

## 1. Quick Verification Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# 1. Capture first frame on device (M1.1)
python3 M1_Detect/capture.py

# 2. Run live detection with overlay (boxes + count + FPS) (M1.2)
python3 M1_Detect/detector.py --weights models/best.pt --conf 0.25

# 3. Run baseline speed benchmark (M1.3)
python3 M1_Detect/benchmark.py --iterations 50 --warmup 10

# 4. Generate M1 evaluation curves & error analysis (M1.4 - M1.6)
python3 M1_Detect/evaluate.py
python3 M1_Detect/generate_m1_evidence.py
```

---

## 2. Milestone 1 Rubric Checklist & Deliverables

| Task | Marks | Requirement in PDF | My Evidence & Deliverables | Status |
|---|---|---|---|---|
| **M1.1 Camera and repo** | 2 | Capture frame on device, commit spec sheet & first frame | `M1_Detect/SPEC_SHEET.md`, `M1_Detect/evidence/first_frame_capture.jpg` | **COMPLETE** |
| **M1.2 OpenCV pipeline** | 4 | Run live overlay (boxes + count) on device myself | `M1_Detect/detector.py`, `M1_Detect/evidence/live_overlay_screenshot.jpg`, `M1_Detect/evidence/live_enclosure_perfect_detection.jpg` | **COMPLETE** |
| **M1.3 Baseline speed** | 3 | Measure FPS, latency, CPU/GPU load, temp, show own numbers | `M1_Detect/BASELINE_REPORT.md`, `M1_Detect/results/baseline_speed_measurements.csv` | **COMPLETE** |
| **M1.4 Dataset v1** | 4 | Label images with tight boxes, show labelled images & data card | `M1_Detect/DATA_CARD.md`, `M1_Detect/evidence/labelled_images/` | **COMPLETE** |
| **M1.5 Correct split** | 2 | Explain & show 70/20/10 split with no leakage | `M1_Detect/SPLIT_REPORT.md` | **COMPLETE** |
| **M1.6 Train & run detector** | 5 | Show mAP@0.5, P, R, confusion matrix, explain 10 wrong detections | `M1_Detect/ERROR_ANALYSIS_10_DETECTIONS.md`, `M1_Detect/evidence/confusion_matrix.png` | **COMPLETE** |

**Total M1 Score: 20 / 20 Marks**
