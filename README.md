[![Transformers](https://img.shields.io/badge/Transformers-4.46.0-orange.svg)](https://huggingface.co/transformers/)
[![Datasets](https://img.shields.io/badge/Datasets-2.19.1-lightblue.svg)](https://huggingface.co/docs/datasets/)
[![PyTorch](https://img.shields.io/badge/Torch-2.3.0-red.svg)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.30.0-success.svg)](https://www.gradio.app/)
[![Evaluate](https://img.shields.io/badge/BERTScore-evaluate-yellow.svg)](https://huggingface.co/docs/evaluate/)
[![Hugging%20Face%20Spaces](https://img.shields.io/badge/Hugging%20Face-Spaces-blue.svg)](https://huggingface.co/spaces)
[![License: Open](https://img.shields.io/badge/license-Open-lightgrey.svg)](#ethical-note)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![GitHub](https://img.shields.io/badge/source-GitHub-black.svg)](https://github.com/gackouhamady/mental-health-assistant)


#  Empathetic Assistant — Well-being and Dialogue  
*(Mental Health Assistant — Based on Language Models)*  

This emotional assistant is powered by **DistilGPT-2** fine-tuned for generating empathetic responses,  
and **DistilBERT** for emotion detection in user conversations.

---

##  Project Objective

To develop an **empathetic conversational assistant** capable of interacting in a natural and comforting way with users, while detecting expressed emotions.  
The model relies on **Transformer architectures** (GPT-2, BERT) and the **EmpatheticDialogues** dataset.

---

##  Context

Modern language models can produce coherent and context-aware responses.  
However, adapting them to **emotionally sensitive conversations** requires specialized fine-tuning.  
This project explores how to fine-tune a lightweight model (DistilGPT-2) on **CPU hardware** to generate emotionally supportive and context-aware replies.

---

##  Main Project Phases

### **Phase 1 – Data Exploration and Preparation**
- Load the `facebook/empathetic_dialogues` dataset from Hugging Face.  
- Clean the text: remove duplicates, normalize content, and strip special characters.  
- Perform exploratory analysis: average dialogue length, emotion distribution.

### **Phase 2 – Tokenization**
- Apply tokenization and formatting for DistilGPT-2.  
- Handle missing tokens by adding a `pad_token` where necessary.  

### **Phase 3 – Baseline Prototype**
- Build a **Hugging Face pipeline** for text generation.  
- Run test generations with the un-finetuned DistilGPT-2 on simple examples.

### **Phase 4 – Fine-Tuning on CPU**
- Train the model using `Trainer` from Hugging Face Transformers.  
- Adjust training parameters: *small batch size, gradient accumulation, max_length = 128*.  
- Execution performed on **CPU (8 GB RAM)**.  
- Save the fine-tuned model under `distilgpt2-empathetic-finetuned`.

### **Phase 5 – Hyperparameter Tuning & Re-Training**
- Adjust hyperparameters (learning rate, epochs, batch size).  
- Perform qualitative evaluation: empathy, coherence, fluency.  
- Perform quantitative evaluation using **BERTScore** on 30 samples.  

| Metric | Average Score | Evaluation Model |
|---------|----------------|------------------|
| Precision | 0.41 | `bert-base-uncased` |
| Recall | 0.40 | `bert-base-uncased` |
| F1 (BERTScore) | **0.40** | `bert-base-uncased` |

> ⚠️ Results correspond to CPU-only execution (no GPU acceleration).  
> The main goal was to **master the full fine-tuning pipeline**, not raw performance.

### **Phase 6 – User Interface (Gradio)**
- Interface built with **Gradio Blocks**:  
  - Textbox for user input.  
  - Sliders to adjust response temperature and length.  
  - Display panel for generated response with detected emotion.  
- Bilingual interface (English/French), deployable locally or via **Hugging Face Spaces**.  

**Preview:**
![Gradio Interface](ae_gradio.png)

---

##  Technologies Used

| Category | Tools |
|-----------|--------|
| NLP Framework |  Transformers (4.46.0), Datasets (2.19.1) |
| Training | PyTorch 2.3+, Trainer API |
| Evaluation | BERTScore (evaluate) |
| Interface | Gradio 4.30+ |
| Deployment | Hugging Face Spaces |
| Hardware | CPU – 8 vCPUs / 30 GB RAM (GCP VM) |

---

## Summary of Results

| Phase | Key Outcome |
|-------|--------------|
| Data Cleaning | Cleaned and balanced dataset |
| CPU Fine-Tuning | Successful fine-tuning of DistilGPT-2 |
| Evaluation | BERTScore average ≈ 0.40 (CPU baseline) |
| Gradio Interface | Fully functional and interactive |
| Deployment | Compatible with Hugging Face Spaces |

---

##  Cloud Execution (GCP)
```bash
# Launch Visual Studio Code on your GCP virtual machine
bash ~/start_vscode_cloud.sh
