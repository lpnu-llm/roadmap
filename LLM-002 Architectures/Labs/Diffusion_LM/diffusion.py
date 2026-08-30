"""Student scaffold for absorbing-mask diffusion sampling."""
from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor

# Prerequisite: copy the model.py that you completed in the Encoder lab into
# this directory. Its solution is intentionally not included in this lab.
from model import AnonymousEncoder


@dataclass
class DiffusionStepOutput:
    input_ids: Tensor
    sampled_ids: Tensor
    confidence: Tensor
    remaining_masks: Tensor


@dataclass
class DiffusionOutput:
    input_ids: Tensor
    history: tuple[Tensor, ...]


def cosine_mask_ratio(step: int, total_steps: int) -> float:
    """Fraction of editable positions that remain masked after this step."""
    raise NotImplementedError


def corrupt(
    clean_ids: Tensor,
    editable_mask: Tensor,
    *,
    step: int,
    total_steps: int,
    mask_id: int,
    generator: torch.Generator | None = None,
) -> Tensor:
    """Sample x_t from the absorbing-mask forward process q(x_t | x_0)."""
    raise NotImplementedError


def diffusion_step(
    model: AnonymousEncoder,
    input_ids: Tensor,
    editable_mask: Tensor,
    *,
    step: int,
    total_steps: int,
    mask_id: int,
    pad_id: int,
    temperature: float = 1.0,
    top_k: int | None = None,
    forbidden_token_ids: tuple[int, ...] = (),
    generator: torch.Generator | None = None,
) -> DiffusionStepOutput:
    """Perform one confidence-based reverse diffusion transition x_t -> x_(t-1)."""
    raise NotImplementedError


@torch.inference_mode()
def diffuse(
    model: AnonymousEncoder,
    input_ids: Tensor,
    editable_mask: Tensor,
    *,
    steps: int,
    mask_id: int,
    pad_id: int,
    temperature: float = 1.0,
    top_k: int | None = None,
    forbidden_token_ids: tuple[int, ...] = (),
    generator: torch.Generator | None = None,
) -> DiffusionOutput:
    """Run all reverse steps, returning the final sequence and its trajectory."""
    raise NotImplementedError
