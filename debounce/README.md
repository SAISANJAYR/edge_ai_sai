# Temporal Filter & Detection Debounce
**Milestone:** M3: Decide and Act  
**Task:** Debounce  
**Max Marks:** 4 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/debounce](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/debounce)  

---

## 1. Rubric Requirement
> **"I show one bad frame does not trigger and N frames in a row do"**

---

## 2. Temporal Debounce Specification ($N=3$)
To prevent sensor noise, transient lighting flickers, or conveyor vibrations from triggering false reject commands:
- **Single Bad Frame ($K=1$):** Rejection state remains **UNTRIGGERED** (suppressed by temporal window).
- **Consecutive Confirmations ($K \ge 3$):** Actuator trigger signal transitions to **HIGH**.

```python
class TemporalDebouncer:
    def __init__(self, n_frames=3):
        self.n_frames = n_frames
        self.counter = 0

    def update(self, condition_met: bool) -> bool:
        if condition_met:
            self.counter += 1
        else:
            self.counter = 0
        return self.counter >= self.n_frames
```
