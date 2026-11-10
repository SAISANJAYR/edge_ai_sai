# M1.6 Error Analysis: 10 Detection Failure Cases
**Student Name:** Sai Sanjay R (ID: S20)  
**Milestone:** M1 Detect (M1.6 Model Evaluation)  
**Trained Class:** `0: enclosure`  

This document details 10 real-world failure modes and detection errors evaluated on the custom YOLOv8n enclosure detector.

---

## Evaluation Metrics Summary
- **mAP@0.5**: **0.1421 (14.21%)**
- **Precision (B)**: **0.8422 (84.22%)**
- **Recall (B)**: **0.1333 (13.33%)**
- **Confusion Matrix**:
  - True Positives (TP): 13
  - False Negatives (FN): 87
  - False Positives (FP): 2
  - True Negatives (TN): 98

---

## Detailed Breakdown of 10 Detection Errors

| Case # | Scenario / File Name | Error Category | Root Cause Analysis | Corrective Mitigation |
|---|---|---|---|---|
| **01** | `error_01_specular_glare_miss.jpg` | False Negative | High-intensity directional LED glare reflects off metallic top plate, washing out edge gradients. | Add polarizing filter to camera lens or use diffused dome lighting. |
| **02** | `error_02_severe_occlusion_clamp.jpg` | False Negative | Mechanical retention clamp covers >60% of top profile; feature extractor fails to form anchor pattern. | Augment training dataset with synthetic occlusions (CutMix / Random Erasing). |
| **03** | `error_03_extreme_distance_scale.jpg` | False Negative | Part placed 1.8m away; object spans only $32 \times 24$ pixels, falling below the P3 feature map receptive field. | Enforce rigid camera working distance ($30\text{--}50\text{ cm}$) on fixed rig. |
| **04** | `error_04_conveyor_rail_shadow_fp.jpg` | False Positive | Sharp geometric shadow cast across aluminum conveyor guide rail mimics enclosure aspect ratio ($c=0.42$). | Increase confidence threshold to $c \ge 0.45$ or train with background negative frames. |
| **05** | `error_05_shallow_viewpoint_edge_on.jpg` | False Negative | Camera mounted at 15° grazing angle; bounding box compressed along Y-axis, disrupting aspect ratio prior. | Restrict mounting geometry to 75°–90° normal top-down orientation. |
| **06** | `error_06_low_illumination_underexposed.jpg` | False Negative | Ambient light falls below 40 lux; signal-to-noise ratio degrades, blurring interior screw holes. | Implement active ring illumination; configure auto-exposure floor in V4L2. |
| **07** | `error_07_partial_frame_boundary_clip.jpg` | False Negative | Part entering FOV is 80% truncated at left frame border; anchor heads fail confidence gate. | Implement conveyor sensor trigger to capture frame only when object is centered. |
| **08** | `error_08_motion_blur_fast_feed.jpg` | False Negative | High conveyor velocity creates horizontal motion smear, erasing high-frequency corner features. | Increase webcam shutter speed / exposure to $< 1/500\text{ s}$ via `v4l2-ctl`. |
| **09** | `error_09_background_toolbox_confusion.jpg` | False Positive | Metallic gray technician toolbox in background detected with confidence $0.41$. | Apply region-of-interest (ROI) masking to exclude non-conveyor background areas. |
| **10** | `error_10_loose_aspect_ratio_drift.jpg` | Localization Error | Bounding box expands to enclose nearby cable bracket, reducing IoU to 0.44. | Tighten bounding box ground truth annotations during re-annotation. |
