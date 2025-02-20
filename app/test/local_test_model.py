import torch 
import torchtext; torchtext.disable_torchtext_deprecation_warning()
from torchtext.data import get_tokenizer
import re
from requestgenerator import generate_request_malicious, generate_request_normal
import time


model=torch.jit.load("./model.pt",map_location="cpu")
label=['normal', 'sql', 'xss', 'cmd', 'lfi', 'ssrf', 'html', 'css', 'nosql']

class preprocess:
    def __init__(self):
        self.special_chars_pattern = re.compile(r'([.,!?;:(){}\[\]@"#$%^&*\-_=+|\\<>~/^\'"])')
        self.multispace_pattern = re.compile(r"\s+")
        self.tokenizer=get_tokenizer(None,language="en")
        self.vocab=torch.load("./vocab.pth")
        self.max_length=235
        self.pad_index=self.vocab["<pad>"]
        
    def pad_sequence(self, tokens):
        if len(tokens) < self.max_length:
            return tokens + [self.pad_index] * (self.max_length - len(tokens))
        return tokens[:self.max_length]
    
    def preprocess(self,test_dict):
        splitter=' ≠ '
        combineHeader=splitter + test_dict["host"] + splitter + test_dict["uri"] + splitter + test_dict["auth"] +  splitter + test_dict["agent"] + splitter + test_dict["cookie"] + splitter + test_dict["referer"] + splitter + test_dict["body"]
       
        combineHeader=combineHeader.lower()
        combineHeader=re.sub(self.special_chars_pattern , r' \1 ',combineHeader)
        
        combineHeader = re.sub(self.multispace_pattern, " ", combineHeader).strip()
        
        converted=self.tokenizer(combineHeader)
        
        converted=self.vocab.lookup_indices(converted)
        
        converted=self.pad_sequence(converted)
        return converted


preprocessor = preprocess()


def testFunction(test_dict):
    start = time.time()
    model_input=torch.tensor(preprocessor.preprocess(test_dict=test_dict)).unsqueeze(0)
    model.eval()
    inference_time = time.time()-start
    pred = label[torch.argmax(model(model_input),dim=1).item()]
    print(f"{pred}, {round(inference_time*1000,5)}ms")



TEST_REQUEST_COUNT = 20

print("----Malicious Test ----")

for i in range(TEST_REQUEST_COUNT):
    normal_req = generate_request_normal()
    testFunction(normal_req)