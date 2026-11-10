# Data Card: Industrial Enclosure Vision Dataset v1.0
**Student Name:** Sai Sanjay R (ID: S20)  
**Milestone:** M1 Detect (M1.4 Dataset v1)  
**Platform:** Raspberry Pi 5  

---

## 1. Dataset Overview
- **Dataset Domain**: Industrial automation, sheet-metal electrical enclosure inspection.
- **Source**: Roboflow industrial vision repository.
- **Target Detection Class**: `0: enclosure` (Single-class object localization).
- **Format**: YOLOv8 Darknet format (`<class_id> <x_center> <y_center> <width> <height>` normalized $[0, 1]$).
- **Target Resolution**: $640 \times 640$ pixels, RGB 3-channel.

---

## 2. Annotation & Bounding Box Quality
- **Box Tightness**: Ground truth annotations are tightly bound to the outer metallic flange of the enclosure, excluding background shadows and mounting rails.
- **Visual Examples**:
  - Sample 1: `M1_Detect/evidence/labelled_images/sample_ground_truth_1.jpg`
  - Sample 2: `M1_Detect/evidence/labelled_images/sample_ground_truth_2.jpg`
  - Sample 3: `M1_Detect/evidence/labelled_images/sample_ground_truth_3.jpg`

---

## 3. Dataset Limitations & Assessment Scope
1. **Single-Class Constraint**: The trained weights identify the presence and spatial boundary of the `enclosure`. They do **not** identify defect classes (e.g. scratch, dent, missing screw).
2. **Viewpoint Sensitivity**: Model training was performed primarily on top-down views. Yaw angles $> 30^\circ$ significantly reduce recall, as analyzed in `M1_Detect/ERROR_ANALYSIS_10_DETECTIONS.md`.
