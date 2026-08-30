#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import torch
from tokenizers import Tokenizer

from model import AnonymousMoE


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the anonymous sparse MoE")
    parser.add_argument("model", type=Path)
    parser.add_argument("text")
    parser.add_argument("--max-new-tokens", type=int, default=32)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-k", type=int)
    parser.add_argument(
        "--device", default="cuda" if torch.cuda.is_available() else "cpu"
    )
    args = parser.parse_args()

    tokenizer = Tokenizer.from_file(str(args.model / "tokenizer.json"))
    ids = torch.tensor([tokenizer.encode(args.text).ids], device=args.device)
    model = AnonymousMoE.from_directory(args.model, device=args.device)
    generated = model.generate(
        ids,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
    )
    print(tokenizer.decode(generated[0].tolist()))


if __name__ == "__main__":
    main()
