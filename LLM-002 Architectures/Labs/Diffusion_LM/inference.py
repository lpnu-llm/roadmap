#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import torch
from huggingface_hub import snapshot_download
from tokenizers import Tokenizer

from diffusion import diffuse
# Prerequisite: first solve the Encoder lab, then copy its completed model.py
# into this directory. The diffusion lab intentionally does not provide or
# publish the encoder architecture solution.
from model import AnonymousEncoder


ENCODER_REPOSITORY = "ai-department-lpnu/encoder-lab"
MASK_ID = 50284
PAD_ID = 50283
FORBIDDEN_IDS = (MASK_ID, PAD_ID, 50281, 50282)


def encoder_directory(local_directory: Path | None) -> Path:
    if local_directory is not None:
        return local_directory
    return Path(
        snapshot_download(
            ENCODER_REPOSITORY,
            allow_patterns=[
                "model.json",
                "safetensor_encoder.safetensors",
                "tokenizer.json",
                "special_tokens_map.json",
            ],
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run absorbing-mask text diffusion")
    parser.add_argument("text", help='Text containing at least one "[MASK]" token')
    parser.add_argument("--model", type=Path, help="Local encoder-lab snapshot")
    parser.add_argument("--steps", type=int, default=12)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=64)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--device", default="cuda" if torch.cuda.is_available() else "cpu"
    )
    args = parser.parse_args()

    directory = encoder_directory(args.model)
    tokenizer = Tokenizer.from_file(str(directory / "tokenizer.json"))
    encoded = tokenizer.encode(args.text)
    input_ids = torch.tensor([encoded.ids], device=args.device)
    editable_mask = input_ids.eq(MASK_ID)
    if not editable_mask.any():
        raise ValueError('text must contain at least one literal "[MASK]" token')

    generator = torch.Generator(device=args.device).manual_seed(args.seed)
    model = AnonymousEncoder.from_directory(directory, device=args.device)
    output = diffuse(
        model,
        input_ids,
        editable_mask,
        steps=args.steps,
        mask_id=MASK_ID,
        pad_id=PAD_ID,
        temperature=args.temperature,
        top_k=args.top_k,
        forbidden_token_ids=FORBIDDEN_IDS,
        generator=generator,
    )
    for step, state in enumerate(output.history):
        print(f"{step:02d}: {tokenizer.decode(state[0].tolist())}")


if __name__ == "__main__":
    main()
