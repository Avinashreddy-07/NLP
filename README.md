# CS5760 Natural Language Processing — Homework 1

**Name:**  Avinash K
**Student ID:**  700771195
**Course:** CS5760 Natural Language Processing (Fall 2025)  
**University:** University of Central Missouri  

---

## 📘 Overview
This homework covers four key NLP concepts:

1. **Regular Expressions** — advanced pattern matching
2. **Tokenization** — splitting text into tokens
3. **Byte Pair Encoding (BPE)** — subword tokenization
4. **Edit Distance** — measuring similarity between strings


---

### **Q1: Regular Expressions — `q1_regex.py`**
- **Patterns Implemented:**
  - **ZIP Codes:** `\b\d{5}(?:[-\s]\d{4})?\b`
  - **Non-Capital Words:** `\b(?![A-Z])[A-Za-z]+(?:[’'-][A-Za-z]+)*\b`
  - **Rich Numbers:** `[+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?`
  - **Email Variants:** `(?i)\be[-\s–]?mail\b`
  - **Go Interjections:** `\bgo+(?:[!.,?])?(?=\s|$)`
  - **Question Lines:** `.*\?[\"”’\')\]\s]*$`
- **Behavior:** Tests regex patterns on an inline sample text.
- **Run:**  
  ```bash
  python q1_regex.py

---

### **Q2: Tokenization — `q2_tokenization.py`**
- **Naïve Tokenization:** Space-based splitting  
- **Manual Tokenization:** Handles punctuation and clitics (`isn't → is + n't`)  
- **Tool Comparison:** Uses spaCy (preferred) or NLTK (fallback)  
- **Multiword Expressions (MWEs):**
  - New York City  
  - kick the bucket  
  - high school  
- **Reflection:** Discusses difficulties, comparison with other languages, and tool alignment  
- **Run:**  
  ```bash
  python q2_tokenization.py


  ---

### **Q3: Byte Pair Encoding — `q3_bpe.py`**
- **Manual BPE (in docstring):** First three merges shown step-by-step  
- **Mini BPE Learner:**
  - Learns merges from a toy corpus (`low`, `newer`, `wider`)  
  - Prints top pairs and evolving vocabulary  
- **Word Segmentation Tests:**
  - `new → [new, _]`  
  - `newer → [new, er, _]`  
  - `lowest → [low, est, _]`  
  - `widest → [wide, est, _]`  
  - `newestest → [new, est, est, _]`  
- **Reflection:** BPE reduces OOV issues and aligns with morphemes but sometimes splits awkwardly  
- **Run:**  
  ```bash
  python q3_bpe.py

---

### **Q4: Edit Distance — `q4_edit_distance.py`**
- **Task:** Compute edit distance `Sunday → Saturday`  
- **Models:**
  - Model A: Sub=1, Ins=1, Del=1  
  - Model B: Sub=2, Ins=1, Del=1  
- **Implementation:** Dynamic programming with DP matrix and backtracking for one valid edit path  
- **Reflection:**  
  - Model A favors substitutions (spell checking)  
  - Model B favors insertions/deletions (DNA alignment)  
- **Run:**  
  ```bash
  python q4_edit_distance.py

### **Installation**
```bash
  pip install -r requirements.txt
  python -m spacy download en_core_web_sm
