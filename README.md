# 🚗 Context-Aware Automotive AI Assistant

This project simulates a real-world in-car voice assistant inspired by systems like Cerence AI.

It implements a complete NLP pipeline:
User Command → Intent Detection → Entity Extraction → Action Mapping

## 🚀 Features
- Transformer-based intent classification (zero-shot learning)
- Rule-based entity extraction
- Action mapping system
- Interactive Streamlit UI

## 🧠 Pipeline
1. User inputs a command  
2. Model predicts intent  
3. Entities are extracted using NLP rules  
4. System maps intent + entities to an action  

## 📌 Example

Input:
"Navigate to Starbucks"

Output:
- Intent: Navigation  
- Entities: { destination: Starbucks }  
- Action: Start navigation to Starbucks  

## 🛠 Tech Stack
- Python  
- HuggingFace Transformers (BART MNLI)  
- Streamlit  
- Regex (NLP rules)  

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app_ui.py
