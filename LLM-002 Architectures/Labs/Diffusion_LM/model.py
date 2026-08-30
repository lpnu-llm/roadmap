"""Encoder scaffold reused from the prerequisite Encoder architecture lab.

If you already solved that lab, replace this file with your completed
Encoder/model.py implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch
from torch import Tensor, nn


@dataclass(frozen=True)
class ModelConfig:
    vocabulary_size: int
    width: int
    expanded_width: int
    heads: int
    layers: int
    maximum_length: int
    local_window: int
    global_every: int
    global_rope_base: float
    local_rope_base: float
    norm_epsilon: float = 1e-5
    pad_id: int | None = None
    eos_id: int | None = None
    head_activation: str = "gelu"
    storage_vocabulary_size: int | None = None

    @property
    def head_width(self) -> int:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "ModelConfig":
        raise NotImplementedError


@dataclass
class ModelOutput:
    logits: Tensor
    hidden_states: Tensor


def _rotate_half(value: Tensor) -> Tensor:
    raise NotImplementedError


def _rotary_factors(
    positions: Tensor, head_width: int, base: float, dtype: torch.dtype
) -> tuple[Tensor, Tensor]:
    raise NotImplementedError


def _apply_rotary(
    query: Tensor, key: Tensor, cosine: Tensor, sine: Tensor
) -> tuple[Tensor, Tensor]:
    raise NotImplementedError


def _attention_mask(
    valid_tokens: Tensor,
    *,
    causal: bool,
    window: int | None,
    dtype: torch.dtype,
) -> Tensor:
    raise NotImplementedError


class Mixer(nn.Module):
    def __init__(self, config: ModelConfig, layer_index: int):
        super().__init__()
        raise NotImplementedError

    def forward(
        self, hidden: Tensor, positions: Tensor, valid_tokens: Tensor
    ) -> Tensor:
        raise NotImplementedError


class Unit(nn.Module):
    def __init__(self, config: ModelConfig, layer_index: int):
        super().__init__()
        raise NotImplementedError

    def forward(
        self, hidden: Tensor, positions: Tensor, valid_tokens: Tensor
    ) -> Tensor:
        raise NotImplementedError


class AnonymousEncoder(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        raise NotImplementedError

    def forward(
        self, input_ids: Tensor, attention_mask: Tensor | None = None
    ) -> ModelOutput:
        raise NotImplementedError

    @classmethod
    def from_directory(
        cls,
        directory: str | Path,
        *,
        device: str | torch.device = "cpu",
        dtype: torch.dtype | None = None,
    ) -> "AnonymousEncoder":
        """Load model.json and safetensor_encoder.safetensors."""
        raise NotImplementedError
