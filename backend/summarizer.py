from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Use BART instead of T5 (no sentencepiece needed)
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_articles(articles):
    summaries = []
    for text in articles:
        try:
            inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
            outputs = model.generate(**inputs, max_length=150, num_beams=4, early_stopping=True)
            summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
            summaries.append(summary)
        except Exception as e:
            summaries.append("Error summarizing article.")
            print(f"Error: {e}")
    return summaries
