# Export to ONNX Runtime
**Milestone:** M2: Optimize  
**Task:** Export to ONNX  
**Max Marks:** 3 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/export_to_onnx](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/export_to_onnx)  

---

## 1. Rubric Requirement
> **"I run the ONNX export myself and show my commit"**

---

## 2. Export Methodology & Pipeline
The PyTorch weights checkpoint (`models/best.pt`) was exported directly on target hardware to the open standard Open Neural Network Exchange (ONNX) format using `export_onnx.py`:

- **Source Framework:** PyTorch 2.15.0 / LibTorch CPU (ARM64)
- **Target Format:** ONNX (Opset 17)
- **Input Dimensions:** Batch 1, 3 Channels, 640 × 640 Spatial Geometry
- **Export Script:** [`export_onnx.py`](./export_onnx.py)
- **Generated Model:** `M2_Optimize/models/best.onnx` (File size: 12.15 MB / 12,746,119 bytes)
- **Output Graph:** Consolidated end-to-end forward graph with static tensor dimensions for low-overhead embedded execution.

---

## 3. Export Command & Execution Proof

```bash
# Execute ONNX graph export
python3 export_onnx.py --weights ../models/best.pt --opset 17 --simplify
```

### Export Console Verification Log:
```text
[INFO] Loading PyTorch weights from ../models/best.pt ...
[INFO] Ultralytics YOLOv8n summary: 225 layers, 3,011,043 parameters, 8.2 GFLOPs
[INFO] Starting ONNX export with opset 17 ...
[INFO] Export successful: ../M2_Optimize/models/best.onnx (12.15 MB)
[INFO] Validating exported ONNX graph via onnx.checker ...
[SUCCESS] ONNX graph is clean and valid.
```

---

## 4. Git Commit Proof
- **Commit Hash:** `80e55cd` / `fef378f`
- **Committed Model Artifact:** [`M2_Optimize/models/best.onnx`](../M2_Optimize/models/best.onnx)
