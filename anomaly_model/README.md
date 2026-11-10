# Vibration Anomaly Detection Model
**Milestone:** M4: Monitor and Connect  
**Task:** Anomaly model  
**Max Marks:** 4 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/anomaly_model](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/anomaly_model)  

---

## 1. Rubric Requirement
> **"I train on normal data only and show the live alert when I inject the fault"**

---

## 2. Model Methodology
Unsupervised Isolation Forest / Autoencoder trained strictly on 100% normal motor baseline telemetry. When an unbalance or bearing fault is injected, reconstruction error spikes above threshold, generating a real-time MQTT alert.
