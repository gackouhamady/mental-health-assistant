# Mental Health Assistant - Based on Language Models

[![Transformers](https://img.shields.io/badge/Transformers-4.41.1%2B-orange.svg)](https://huggingface.co/transformers/)
[![Datasets](https://img.shields.io/badge/Datasets-2.19.1%2B-lightblue.svg)](https://huggingface.co/docs/datasets/)
[![Torch](https://img.shields.io/badge/Torch-2.3.0%2B-red.svg)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.30.0%2B-success.svg)](https://www.gradio.app/)
[![Accelerate](https://img.shields.io/badge/Accelerate-compatible-yellow.svg)](https://huggingface.co/docs/accelerate/)
[![License: Open](https://img.shields.io/badge/license-Open-lightgrey.svg)](#ethical-note)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![GitHub Repo](https://img.shields.io/badge/source-GitHub-black.svg)](https://github.com/yourusername/mental-health-assistant)

- [Mental Health Assistant - Based on Language Models](#mental-health-assistant---based-on-language-models)
    - [Project Goal](#-project-goal)
    - [Project Steps](#-project-steps)
      - [1. Model Exploration](#1-model-exploration)
      - [2. Data Preparation](#2-data-preparation)
      - [3. Fine-tuning on CPU](#3-fine-tuning-on-cpu)
      - [4. CPU Optimization](#4-cpu-optimization)
      - [5. Deployment](#5-deployment)
      - [6. Validation](#6-validation)
    - [Technologies Used](#-technologies-used)
    - [Next Steps](#-next-steps)
    - [Ethical Note](#️-ethical-note)

##  Project Goal

This project aims to develop a virtual assistant capable of engaging empathetically and helpfully with users seeking support in mental health. The assistant leverages Transformer-based language models (like GPT-2, BERT, T5) and is fine-tuned specifically on data related to emotional well-being, stress management, and active listening.

##  Project Steps

### 1. Model Exploration

* Compare models: GPT-2, DistilGPT-2, BERT, T5
* Analyze their performance for tasks like conversation, classification, and emotion detection

### 2. Data Preparation

* Collect dialogues related to mental health (e.g., EmpatheticDialogues)
* Clean, tokenize, and format the data

### 3. Fine-tuning on CPU

* Choose a lightweight model (DistilGPT-2)
* Train using `transformers.Trainer`
* Adjust hyperparameters to fit CPU constraints (8 GB RAM)

### 4. CPU Optimization

* Reduced batch size (e.g., 2)
* Gradient accumulation to simulate larger batches
* Split training into multiple sessions if needed

### 5. Deployment

* User interface with **Gradio**
* Interactive chatbot generating empathetic responses

### 6. Validation

* Test response quality (empathy, usefulness, non-judgment)
* Gather user feedback for continuous improvement

##  Technologies Used

* Python
* Hugging Face Transformers & Datasets
* Gradio for the web interface
* CPU with 8 GB RAM (training optimized accordingly)

##  Next Steps

* Finalize data collection and cleaning
* Start fine-tuning the base model
* Prototype the Gradio interface

##  Ethical Note

This project aims for supportive, non-medical use. The assistant does not replace a mental health professional. In cases of acute distress, please contact a helpline or a qualified professional.



## Start  VsCode   on  Cloud   GCP

```bash
 bash ~/start_vscode_cloud.sh
```
