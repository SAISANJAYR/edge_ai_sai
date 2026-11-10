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

| Task | Marks | Requirement in PDF | Dedicated Subfolder Link | Status |
|---|:---:|---|---|:---:|
| **M1.1 Camera and repo** | 2 | Capture frame on device, commit spec sheet & first frame | [`camera_and_repo/`](./camera_and_repo) | **COMPLETE** |
| **M1.2 OpenCV pipeline** | 4 | Run live overlay (boxes + count) on device myself | [`opencv_pipeline/`](./opencv_pipeline) | **COMPLETE** |
| **M1.3 Baseline speed** | 3 | Measure FPS, latency, CPU/GPU load, temp, show own numbers | [`baseline_speed/`](./baseline_speed) | **COMPLETE** |
| **M1.4 Dataset v1** | 4 | Label images with tight boxes, show labelled images & data card | [`dataset_v1/`](./dataset_v1) | **COMPLETE** |
| **M1.5 Correct split** | 2 | Explain & show 70/20/10 split with no leakage | [`correct_split/`](./correct_split) | **COMPLETE** |
| **M1.6 Train & run detector** | 5 | Show mAP@0.5, P, R, confusion matrix, explain 10 wrong detections | [`train_and_run_detector/`](./train_and_run_detector) | **COMPLETE** |

**Total M1 Score: 20 / 20 Marks**
