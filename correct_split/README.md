# Dataset Split & Zero-Leakage Verification
**Milestone:** M1: Detect  
**Task:** Correct split  
**Max Marks:** 2 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/correct_split](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/correct_split)  

---

## 1. Rubric Requirement
> **"I explain and show the 70/20/10 split with no leakage"**

---

## 2. Partitioning Strategy (70 / 20 / 10)
The dataset of 100 images is divided into three disjoint subsets:

| Subset Partition | Target Percentage | Allocated Images | Operational Purpose |
|---|:---:|:---:|---|
| **Training Set (`train`)** | **70%** | **70 images** | Weight backpropagation and model feature learning |
| **Validation Set (`val`)** | **20%** | **20 images** | Checkpoint selection, learning rate decay, early stopping |
| **Test Set (`test`)** | **10%** | **10 images** | Final unbiased evaluation of generalization performance |
| **Total Dataset** | **100%** | **100 images** | Curated industrial enclosure inspection dataset |

---

## 3. Mathematical & Empirical Proof of Zero Data Leakage

### A. SHA-256 Cryptographic Hash Deduplication
Every image across `train`, `val`, and `test` splits was verified using SHA-256 hash hashing.
$$	ext{Train} \cap 	ext{Val} = \emptyset, \quad 	ext{Train} \cap 	ext{Test} = \emptyset, \quad 	ext{Val} \cap 	ext{Test} = \emptyset$$
- **Cross-Split Hash Overlap:** **0 images (0.00% leakage)**.

### B. Temporal Session Separation
- Training frames were captured across sessions A & B.
- Validation frames were captured across session C.
- Test frames were captured in session D under independent lighting and object placement conditions.

### C. Background Diversity Isolation
Workbench backgrounds and auxiliary distractors (tools, cables, metal plates) were stratified across partitions so that the model cannot memorize background artifacts.

---

## 4. Verification Command

```bash
# Execute automated zero-leakage hash verification
python3 verify_split.py
```

Full details are documented in [`SPLIT_REPORT.md`](./SPLIT_REPORT.md).
