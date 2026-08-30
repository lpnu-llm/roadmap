#!/usr/bin/env python3
import argparse
from pathlib import Path
import torch
from tokenizers import Tokenizer
from model import AnonymousEncoderDecoder

def main():
    p=argparse.ArgumentParser(); p.add_argument('model',type=Path); p.add_argument('text'); p.add_argument('--max-new-tokens',type=int,default=32); p.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); a=p.parse_args()
    tokenizer=Tokenizer.from_file(str(a.model/'tokenizer.json')); ids=torch.tensor([tokenizer.encode(a.text).ids],device=a.device)
    model=AnonymousEncoderDecoder.from_directory(a.model,device=a.device); generated=model.generate(ids,max_new_tokens=a.max_new_tokens)
    print(tokenizer.decode(generated[0].tolist()))

if __name__=='__main__': main()
