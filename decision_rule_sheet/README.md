# Decision Rule Sheet
**Milestone:** M3: Decide and Act  
**Task:** Decision rule sheet  
**Max Marks:** 3 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/decision_rule_sheet](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/decision_rule_sheet)  

---

## 1. Rubric Requirement
> **"I write the input, threshold, action and safe state if the camera fails"**

---

## 2. Industrial Logic Specification Matrix

| State | Input Condition | Threshold Criteria | Actuator / Control Action | Failsafe State |
|---|---|---|---|---|
| **PASS** | Valid `enclosure` detected | Confidence $c \ge 0.50$, Overlap IoU $< 0.40$ | Green Status LED ON; Conveyor advances | Normal Operation |
| **DEFECT / FAIL** | Foreign object or malformed casing | Deviation $> 15\%$, Confidence $< 0.25$ | Pneumatic reject solenoid fires; Alert logged | Safe diverter engaged |
| **NO PART** | Clean conveyor surface | 0 bounding boxes detected | Idle state; Conveyor advances | Standby |
| **CAMERA FAILURE** | Frame drop, V4L2 disconnect, dark frame ($< 5$ avg brightness) | Timeout $> 500$ ms or 3 consecutive corrupt frames | Emergency conveyor halt; Amber strobe active; Failsafe relay OPEN | **FAILSAFE STOP (E-STOP)** |

---

## 3. Safe State Logic Implementation
```python
def evaluate_camera_safety(frame, last_frame_time, timeout_threshold=0.5):
    import time
    if frame is None or (time.time() - last_frame_time) > timeout_threshold:
        return 'TRIGGER_FAILSAFE_HALT'
    if frame.mean() < 5.0: # Blackout / camera disconnected
        return 'TRIGGER_FAILSAFE_HALT'
    return 'CAMERA_OK'
```
