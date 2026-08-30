#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import torch
from tokenizers import Tokenizer
from model import AnonymousEncoder


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the anonymous encoder")
    parser.add_argument("model", type=Path)
    parser.add_argument("text")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()
    tokenizer = Tokenizer.from_file(str(args.model / "tokenizer.json"))
    ids = torch.tensor([tokenizer.encode(args.text).ids], device=args.device)
    output = AnonymousEncoder.from_directory(args.model, device=args.device)(ids)
    pooled = output.hidden_states.mean(1)
    print(f"hidden_states: {tuple(output.hidden_states.shape)}")
    print(f"mean_pooled[:8]: {pooled[0, :8].tolist()}")


if __name__ == "__main__":
    main()
