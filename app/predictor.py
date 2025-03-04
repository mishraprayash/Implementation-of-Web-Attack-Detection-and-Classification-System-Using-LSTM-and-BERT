# app/predictor.py

import time
import torch
import logging
from config import LSTM_MODEL_PATH, LSTM_VOCAB_PATH, BERT_MODEL_PATH, BERT_VOCAB_PATH
from preprocessing import LSTM_Preprocessor

from transformers import AutoModelForSequenceClassification, BertTokenizer


# Define the labels corresponding to the model's output
LABELS = ["NORMAL", "SQLI", "XSS", "CMDI", "LFI", "SSRF", "HTMLI", "CSSI", "NOSQLI"]

device = "cuda" if torch.cuda.is_available() else "cpu"
BERT_MODEL_NAME = "google/mobilebert-uncased"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class LSTM_Predictor:
    def __init__(
        self, model_path: str = LSTM_MODEL_PATH, vocab_path: str = LSTM_VOCAB_PATH
    ):
        self.model = torch.jit.load(model_path, map_location="cpu")
        self.model.eval()  # Set model to evaluation mode
        self.preprocessor = LSTM_Preprocessor(vocab_path)

    def predict(self, data: dict):
        start_time = time.time()
        processed = self.preprocessor.preprocess(data)
        model_input = torch.tensor(processed).unsqueeze(0)

        with torch.no_grad():
            output = self.model(model_input)

        inference_time = time.time() - start_time
        pred_index = torch.argmax(output, dim=1).item()
        pred = LABELS[pred_index]
        prediction_probability = torch.softmax(output, dim=1).max().item()

        # sends back these after prediction
        return {
            "prediction": pred,
            "inference_time_ms": round(inference_time * 1000, 6),
            "prediction_probability": round(prediction_probability, 6),
            "malicious": True if pred!="NORMAL" else False 
        }


class BERT_Predictor:
    def __init__(
        self, model_path: str = BERT_MODEL_PATH, vocab_path: str = BERT_VOCAB_PATH
    ):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            BERT_MODEL_NAME,
            num_labels=9,
            output_attentions=False,
            output_hidden_states=False,
        ).to(device)

        self.tokenizer = BertTokenizer(vocab_file=BERT_VOCAB_PATH)
        self.tokenizer.add_tokens("<split>")
        self.model.resize_token_embeddings(len(self.tokenizer))
        self.state_dict = torch.load(BERT_MODEL_PATH, map_location="cpu")
        self.model.load_state_dict(self.state_dict)

    def preprocess(self,data:dict):
        auth_header:str = data.get("auth","").strip()
        if auth_header.startswith('Bearer ') or auth_header.startswith('Basic '):
            data["auth"] = data["auth"].split(" ",1)[1]
        splitter = " <split> "
        combined_data = (
             splitter
            + data.get("host", "")
            + splitter
            + data.get("uri", "")
            + splitter
            + data.get("auth", "")
            + splitter
            + data.get("agent", "")
            + splitter
            + data.get("cookie", "")
            + splitter
            + data.get("referer", "")
            + splitter
            + data.get("body", "")
        )
        return combined_data


    def predict(self,data:str):
        start_time = time.time()
        tokens = self.tokenizer(data, padding=True, truncation=True, max_length=512, return_tensors="pt")
        self.model.eval()
        logits = self.model(**tokens).logits
        inference_time = time.time() - start_time
        pred_index = torch.argmax(logits, dim=1).item()
        pred = LABELS[pred_index]
        prediction_probability = torch.softmax(logits, dim=1).max().item()

        return {
            "prediction": pred,
            "inference_time_ms": round(inference_time * 1000, 6),
            "prediction_probability": round(prediction_probability, 6),
            "malicious": True if pred!="NORMAL" else False 
        }
