# Assessment Evidence Index & Traceability Matrix

This document tracks all requirements across Milestones M1 through M5 according to the assessment rubric.

Statuses:
- `NOT STARTED`: Task not yet initiated.
- `IN PROGRESS`: Implementation actively underway.
- `IMPLEMENTED`: Code written and committed.
- `TESTED`: Functional verification completed with logs/data.
- `EVIDENCE CAPTURED`: Screenshots, photographs, benchmarks, and reports recorded.
- `BLOCKED`: Blocked on external dependency or physical hardware.

---

## Milestone 1: Detect (20 Marks)

| Item | Requirement Description | Implementation Target | Test Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|
| M1.1 | Camera & Repository Setup | `src/camera/camera_manager.py`, Git repo | Initialize git, detect webcam, save first frame | Git repo initialized; USB camera absent, auto-fallback simulation active | `evidence/photographs/hardware/` | `results/logs/m1_init.log` | Pending commit | IN PROGRESS |
| M1.2 | OpenCV Pipeline & YOLO Detection | `src/detection/detector.py`, `detect.py` | Run live inference with bounding box, conf, FPS, count | Verified YOLOv8n loads `models/best.pt`, class 'enclosure' | `evidence/screenshots/m1/` | `results/benchmarks/m1_detector.csv` | Pending commit | IMPLEMENTED |
| M1.3 | Baseline Performance Benchmarking | `src/detection/benchmark.py` | 100 runs measuring FPS, latency, CPU, RAM, Temp | Initial cold run successful; comprehensive benchmark pending | `evidence/screenshots/m1/` | `results/benchmarks/m1_baseline.csv` | Pending commit | IN PROGRESS |
| M1.4 | Dataset v1 Audit & Card | `docs/DATASET_CARD.md`, `data/` | Inspect model metadata, training arguments, classes | Dataset trained on Colab (`/content/edge_ai-1`), 1 class (`enclosure`) | `evidence/screenshots/m1/` | `results/evaluation/dataset_audit.json` | Pending commit | IN PROGRESS |
| M1.5 | Dataset Split Verification (70/20/10) | `docs/DATASET_CARD.md` | Audit split ratios and leakage prevention | Split verification documented in Dataset Card | N/A | `results/evaluation/split_summary.md` | Pending commit | NOT STARTED |
| M1.6 | Detector Evaluation & Metrics | `src/detection/inference.py`, `docs/TESTING_REPORT.md` | Evaluate mAP@0.5, Precision, Recall, Confusion Matrix | Historical training metrics: P=0.8422, R=0.1333, mAP50=0.142 | `evidence/screenshots/m1/` | `results/confusion_matrices/m1_eval.csv` | Pending commit | IN PROGRESS |

---

## Milestone 2: Optimize (20 Marks)

| Item | Requirement Description | Implementation Target | Test Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|
| M2.1 | ONNX Export & Validation | `optimization/export_onnx.py` | Export `best.pt` to ONNX and validate with onnxruntime | Dependencies installed (`onnx==1.23.2`, `onnxruntime==1.31.1`) | `evidence/screenshots/m2/` | `results/logs/m2_onnx_export.log` | Pending commit | NOT STARTED |
| M2.2 | Optimized Runtime Deployment | `optimization/convert_model.py` | Investigate NCNN / TFLite / ONNX Runtime CPU | ONNX Runtime CPU engine ready | `evidence/screenshots/m2/` | `results/benchmarks/m2_optimized.csv` | Pending commit | NOT STARTED |
| M2.3 | Accuracy Comparison | `optimization/benchmark.py` | Compare PyTorch vs ONNX on identical test frames | Planned | `evidence/screenshots/m2/` | `results/benchmarks/m2_accuracy_comparison.csv` | Pending commit | NOT STARTED |
| M2.4 | Fair Latency Benchmark | `optimization/benchmark.py` | 20 warm-up + 100 runs, batch 1, median, P95, FPS | Planned | `evidence/screenshots/m2/` | `results/benchmarks/m2_fair_benchmark.csv` | Pending commit | NOT STARTED |
| M2.5 | CPU vs Accelerator & Architecture | `docs/SYSTEM_ARCHITECTURE.md` | Document Cortex-A76 vs accelerator trade-offs | Documented in Technical Specification | N/A | `docs/SYSTEM_ARCHITECTURE.md` | Pending commit | NOT STARTED |
| M2.6 | Accuracy-Speed Trade-off Report | `docs/PERFORMANCE_REPORT.md` | Quantify speedup vs mAP delta | Planned | `evidence/screenshots/m2/` | `docs/PERFORMANCE_REPORT.md` | Pending commit | NOT STARTED |

---

## Milestone 3: Decide and Act (20 Marks)

| Item | Requirement Description | Implementation Target | Test Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|
| M3.1 | Decision Rule Sheet | `configs/rules.yaml`, `src/decision/` | Document input, threshold, action, safe state | Initial rules sheet written in `configs/rules.yaml` | N/A | `configs/rules.yaml` | Pending commit | IMPLEMENTED |
| M3.2 | Two-Stream Pipeline | `src/camera/camera_manager.py` | Run 2 simultaneous streams, measure FPS independently | Planned | `evidence/screenshots/m3/` | `results/benchmarks/m3_two_stream.csv` | Pending commit | NOT STARTED |
| M3.3 | Debounce Confirmation Logic | `src/decision/debounce.py` | N-frame consecutive confirmation test | Planned | `evidence/screenshots/m3/` | `results/logs/m3_debounce_test.log` | Pending commit | NOT STARTED |
| M3.4 | Actuator Controller (Safe States) | `src/actuators/actuator_controller.py` | GPIO activation with safe startup/shutdown states | Planned | `evidence/photographs/actuator/` | `results/logs/m3_actuator.log` | Pending commit | NOT STARTED |
| M3.5 | Docker Containerization | `Dockerfile`, `docker-compose.yml` | Container build, cold start deployment, test run | Planned | `evidence/screenshots/m3/` | `results/logs/m3_docker_build.log` | Pending commit | NOT STARTED |
| M3.6 | End-to-End Latency Measurement | `tests/test_decision.py` | 20+ frame-to-actuator latency measurements | Planned | `evidence/screenshots/m3/` | `results/benchmarks/m3_e2e_latency.csv` | Pending commit | NOT STARTED |

---

## Milestone 4: Monitor and Connect (20 Marks)

| Item | Requirement Description | Implementation Target | Test Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|
| M4.1 | MPU6050 IMU Integration | `src/sensors/mpu6050.py` | 3 normal + 3 fault runs saved to CSV | Planned | `evidence/photographs/sensors/` | `results/logs/m4_sensor_runs.csv` | Pending commit | NOT STARTED |
| M4.2 | Anomaly Detection Model | `src/anomaly/train.py`, `monitor.py` | Train on normal data only, inject fault | Planned | `evidence/screenshots/m4/` | `results/benchmarks/m4_anomaly.csv` | Pending commit | NOT STARTED |
| M4.3 | False Alarm Analysis | `src/anomaly/monitor.py` | 5 normal runs, false positive count, threshold tuning | Planned | `evidence/screenshots/m4/` | `results/evaluation/m4_false_alarms.csv` | Pending commit | NOT STARTED |
| M4.4 | Secure MQTT (TLS & Auth) | `src/communication/mqtt_client.py` | Reject unauthenticated, allow authenticated | Planned | `evidence/screenshots/m4/` | `results/logs/m4_mqtt_auth.log` | Pending commit | NOT STARTED |
| M4.5 | Industrial MQTT Topics | `src/communication/mqtt_client.py` | Publish detections and anomaly scores to topics | Planned | `evidence/screenshots/m4/` | `results/logs/m4_mqtt_sub.log` | Pending commit | NOT STARTED |
| M4.6 | PLC Link / Modbus Integration | `src/communication/plc_interface.py` | Modbus holding register / tag update on detection | Planned | `evidence/screenshots/m4/` | `results/logs/m4_plc_tag.log` | Pending commit | NOT STARTED |
| M4.7 | Industrial Threat Model | `docs/SECURITY_REPORT.md` | STRIDE analysis per level + 2 implemented mitigations | Planned | N/A | `docs/SECURITY_REPORT.md` | Pending commit | NOT STARTED |
| M4.8 | System Reliability & OTA Update | `scripts/update_ota.sh`, `src/utils/` | Drift report, OTA v1->v2, rollback, auto-restart | Planned | `evidence/screenshots/m4/` | `results/logs/m4_ota_rollback.log` | Pending commit | NOT STARTED |

---

## Milestone 5: Complete System & Dashboard (20 Marks)

| Item | Requirement Description | Implementation Target | Test Procedure | Actual Result | Screenshot / Photo Path | Log / CSV / Data Path | Git Commit | Status |
|---|---|---|---|---|---|---|---|---|
| M5.1 | Fixed Inspection Rig | `docs/HARDWARE_DOCUMENTATION.md` | Camera distance, lighting, angle, defect coverage | Hardware setup documentation planned | `evidence/photographs/inspection_rig/` | `docs/HARDWARE_DOCUMENTATION.md` | Pending commit | NOT STARTED |
| M5.2 | Pass/Fail Decision Station | `src/decision/decision_engine.py` | 10 good + 10 defective part evaluation | Clarification flagged: single-class vs 2-object goal | `evidence/screenshots/m5/` | `results/confusion_matrices/m5_pass_fail.csv` | Pending commit | NOT STARTED |
| M5.3 | Full-Chain 10-Minute Integration | `main.py` | Run integrated pipeline 10 min continuous | Planned | `evidence/screenshots/m5/` | `results/logs/m5_10min_run.log` | Pending commit | NOT STARTED |
| M5.4 | Professional Live Dashboard | `dashboard/app.py` | Live video, bounding boxes, KPIs, anomaly, health | Flask dashboard architecture designed | `evidence/screenshots/m5/` | `dashboard/app.py` | Pending commit | NOT STARTED |
| M5.5 | Product Readiness | `scripts/systemd_service.sh` | Power-cycle recovery, offline operation, logging | Planned | `evidence/screenshots/m5/` | `results/logs/m5_product_readiness.log` | Pending commit | NOT STARTED |
| M5.6 | Headline Real-Time Metric | `src/utils/system_monitor.py` | Live display of primary inspection metric | Planned | `evidence/screenshots/m5/` | `results/benchmarks/m5_headline_metric.csv` | Pending commit | NOT STARTED |
| M5.7 | Engineering Documentation Pack | `docs/` | Datasheets, architecture, user manual, reports | In progress | N/A | `docs/` | Pending commit | IN PROGRESS |
| M5.8 | Live Demonstration Protocol | `docs/FINAL_DEMONSTRATION.md` | Scripted normal and fault runs + Q&A prep | Planned | `evidence/videos/` | `docs/FINAL_DEMONSTRATION.md` | Pending commit | NOT STARTED |
