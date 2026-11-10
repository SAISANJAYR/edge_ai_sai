# System Architecture: Edge AI Vision Pipeline

## 1. High-Level Architecture
The system architecture separates hardware sensor ingestion, vision preprocessing, neural network inference, and performance profiling into modular, decoupled Python components.

```mermaid
flowchart TD
    subgraph Ingestion Layer
        CAM[USB Webcam /dev/video0] -->|V4L2 Capture| CM[CameraManager]
        SYNTH[Synthetic Conveyor Generator] -.->|Fallback| CM
    end

    subgraph Pipeline Processing
        CM -->|BGR Frame 640x480| PRE[Letterbox & Normalization]
        PRE -->|Tensor 1x3x640x640| ENGINE{Inference Engine}
        ENGINE -->|Backend: PyTorch CPU| PT[YOLOv8 PyTorch Runtime]
        ENGINE -->|Backend: ONNX Runtime| ORT[ONNX Runtime NEON Engine]
        PT --> POST[NMS Post-Processing]
        ORT --> POST
        POST -->|Bounding Boxes & Conf| VIZ[Annotation & Visualization]
    end

    subgraph Telemetry & Monitoring
        MON[HardwareMonitor] -->|CPU %, RAM MB, Temp °C| LOG[Benchmark & Telemetry Logger]
        ENGINE -->|Latency & FPS| LOG
        LOG --> CSV[Raw CSV Records]
        LOG --> PLOT[Performance Graphs]
    end
```

---

## 2. Component Directory Mapping

| Architectural Component | File Path | Primary Responsibilities |
|---|---|---|
| **Camera Ingestion** | `src/camera/camera_manager.py` | V4L2 device polling, auto-fallback, resolution setting, clean release |
| **Snapshot Utility** | `src/camera/capture.py` | Single-frame acquisition and storage |
| **YOLOv8 Detector** | `src/detection/detector.py` | Live detection loop, visual overlays, FPS tracking |
| **Unified Inference** | `src/detection/inference.py` | Dual-backend inference interface (PyTorch vs ONNX Runtime) |
| **M1 Benchmarking** | `src/detection/benchmark.py` | Baseline 50-run CPU latency and hardware monitoring |
| **M2 Export** | `src/optimization/export_onnx.py` | Checkpoint to ONNX export, graph checking, parity verification |
| **M2 Comparison** | `src/optimization/benchmark_comparison.py` | 100-run comparative benchmark, latency distribution, graphs |
| **Hardware Monitor** | `src/monitoring/hardware_monitor.py` | Sysfs thermal reading, psutil CPU/RAM telemetry |
| **Training History** | `src/evaluation/extract_training_history.py` | Checkpoint historical metrics and loss curve extraction |

---

## 3. Memory & Computational Bounds on Raspberry Pi 5
- **RAM Budget**: Total available RAM is 4,096 MB. Operating system base consumes $\approx 1.5$ GB. PyTorch inference footprint is $\approx 450$ MB. ONNX Runtime footprint is $\approx 280$ MB. The system operates safely with $> 1.0$ GB free memory under continuous execution.
- **Thermal Management**: SoC temperature stabilizes between 74°C and 85°C under continuous inference with active cooling.
