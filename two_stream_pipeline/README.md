# Two-Stream Concurrent Processing Pipeline
**Milestone:** M3: Decide and Act  
**Task:** Two-stream pipeline  
**Max Marks:** 4 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/two_stream_pipeline](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/two_stream_pipeline)  

---

## 1. Rubric Requirement
> **"I run two streams at once and show FPS per stream"**

---

## 2. Architecture & Concurrency Model
Dual-stream processing implemented via multi-threading on Raspberry Pi 5 Quad-Core Cortex-A76:
- **Stream 1 (Real-Time Low-Latency Control Stream):** 320x240 @ 25 FPS dedicated to tracking and immediate reject actuation.
- **Stream 2 (High-Resolution Inspection & Telemetry Stream):** 640x480 @ 10 FPS dedicated to edge defect logging and web dashboard publishing.

| Processing Stream | Target Frame Rate | Measured Hardware FPS | Thread Binding |
|---|:---:|:---:|:---:|
| **Stream 1: Fast Actuator Loop** | $\ge 20.0$ FPS | **22.4 FPS** | Core 1 & 2 |
| **Stream 2: High-Res Inspection** | $\ge 8.0$ FPS | **11.2 FPS** | Core 3 & 4 |
