# app/preprocessing.py

import re
import torch
import torchtext; torchtext.disable_torchtext_deprecation_warning()
from torchtext.data import get_tokenizer

class Preprocessor:
    def __init__(self, vocab_path: str, max_length: int = 235):
        self.special_chars_pattern = re.compile(r'([.,!?;:(){}\[\]@"#$%^&*\-_=+|\\<>~/^\'"])')
        self.multispace_pattern = re.compile(r"\s+")
        self.tokenizer = get_tokenizer(None, language="en")
        self.vocab = torch.load(vocab_path)
        self.max_length = max_length
        self.pad_index = self.vocab["<pad>"]
        
    def pad_sequence(self, tokens):
        if len(tokens) < self.max_length:
            return tokens + [self.pad_index] * (self.max_length - len(tokens))
        return tokens[:self.max_length]
    
    def preprocess(self, data: dict):
        splitter = ' ≠ '
        combine_header = (
            splitter + data["host"] +
            splitter + data["uri"] +
            splitter + data["auth"] +
            splitter + data["agent"] +
            splitter + data["cookie"] +
            splitter + data["referer"] +
            splitter + data["body"]
        )
       
        combine_header = combine_header.lower()
        combine_header = re.sub(self.special_chars_pattern, r' \1 ', combine_header)
        combine_header = re.sub(self.multispace_pattern, " ", combine_header).strip()
        
        tokens = self.tokenizer(combine_header)
        token_indices = self.vocab.lookup_indices(tokens)
        token_indices = self.pad_sequence(token_indices)
        return token_indices
