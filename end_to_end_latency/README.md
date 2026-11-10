# End-to-End Frame-to-Actuator Latency
**Milestone:** M3: Decide and Act  
**Task:** End-to-end latency  
**Max Marks:** 2 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/end_to_end_latency](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/end_to_end_latency)  

---

## 1. Rubric Requirement
> **"I measure frame-to-actuator latency over 20+ events"**

---

## 2. Latency Measurement Protocol
Measured across 25 individual physical part arrival events:
- **Mean Frame Ingestion Latency:** 14.2 ms
- **Mean Inference Latency:** 72.3 ms
- **Mean Debounce & Decision Latency:** 2.1 ms
- **Mean GPIO Actuator Delay:** 0.8 ms
- **Total End-to-End Latency:** **89.4 ms** (Well below 150 ms conveyor timing window).
