---
library_name: pytorch
tags:
  - education
  - diffusion
  - masked-language-model
  - pytorch
---

# Masked language diffusion lab

Implement the absorbing-mask diffusion process in `diffusion.py`. This lab is
a continuation of the Encoder architecture lab. The included `model.py` is the
same unfinished scaffold: solve that lab first, then replace it with your
completed `Encoder/model.py`. The diffusion lab does not publish the encoder
implementation.

The model files are reused directly from
[`ai-department-lpnu/encoder-lab`](https://huggingface.co/ai-department-lpnu/encoder-lab):

- `model.json`;
- `safetensor_encoder.safetensors`;
- `tokenizer.json`;
- `special_tokens_map.json`.

`inference.py` downloads those files on first use. This repository intentionally
contains no copy of the model tensors.

The encoder repository is currently private. Students must be granted access
and authenticate once with `hf auth login` before running `inference.py`.

Your working directory should therefore contain:

```text
Diffusion_LM/
├── diffusion.py      # implement this lab
├── inference.py
├── model.py          # replace with your solved Encoder/model.py
└── requirements.txt
```

## Objective

Turn a frozen bidirectional masked-language encoder into an iterative text
denoiser. `[MASK]` is an absorbing noise state. The forward process gradually
replaces editable tokens by `[MASK]`; the reverse process predicts masked
tokens and reveals the most confident predictions over several steps.

This is an inference-only masked diffusion sampler. The backbone has not been
trained with timestep conditioning, so the exercise focuses on diffusion
mechanics, reconstruction, and infilling rather than state-of-the-art
unconditional generation.

## Forward process

```mermaid
flowchart LR
    X0[Clean sequence x₀] --> Q1[Mask a small subset]
    Q1 --> X1[x₁]
    X1 --> Q2[Increase mask probability]
    Q2 --> XT[xₜ]
    XT --> QT[Mask all editable positions]
    QT --> XM[All-mask state x_T]
```

Use a cosine schedule. `cosine_mask_ratio(step, total_steps)` describes the
fraction that remains masked during reverse sampling:

```text
r(step) = cos²(π · step / (2 · total_steps))
```

The corresponding forward corruption probability at timestep `t` is
`1 - r(t)`. Only positions selected by `editable_mask` may be corrupted.

## Reverse diffusion step

```mermaid
flowchart TD
    XT[Current sequence x_t] --> E[Frozen bidirectional encoder]
    E --> L[Vocabulary logits at every position]
    L --> S[Temperature / top-k sampling]
    S --> C[Probability of sampled token]
    C --> R[Rank currently masked positions]
    R --> H[Reveal highest-confidence subset]
    R --> M[Keep uncertain positions as MASK]
    H --> XP[Next state x_t-1]
    M --> XP
```

For each batch item, one call to `diffusion_step` must:

1. Run the encoder once over the complete current sequence.
2. Prevent `[MASK]`, padding, and boundary tokens from being sampled.
3. Select greedy candidates when `temperature <= 0`; otherwise sample from
   temperature-scaled, optionally top-k-filtered probabilities.
4. Record each candidate's probability as its confidence.
5. Compute the target number of remaining masks from the cosine schedule.
6. Reveal the highest-confidence currently masked positions.
7. Leave prompt, boundary, padding, and previously revealed positions intact.

The process is monotonic: a revealed token is not masked again.

## Tensor shapes

| Value | Shape |
|---|---|
| `input_ids` | `[batch, sequence]` |
| `editable_mask` | `[batch, sequence]`, boolean |
| Encoder logits | `[batch, sequence, 50,368]` |
| Sampled IDs | `[batch, sequence]` |
| Confidence | `[batch, sequence]` |
| Remaining masks | `[batch]` |

## Completion criteria

- Implement every `NotImplementedError` in `diffusion.py`.
- Schedule endpoints are exactly `r(0) = 1` and `r(T) = 0`.
- Forward corruption never changes protected positions.
- Reverse steps never change prompt or previously revealed positions.
- The number of `[MASK]` tokens decreases according to the schedule.
- No `[MASK]` tokens remain after the last step.
- Seeded sampling is reproducible.
- Batched sequences may have different numbers of editable positions.
- The encoder is evaluated under `torch.inference_mode()` and is not trained.

Example after completing `diffusion.py`:

```bash
python inference.py "Paris is the [MASK] of France." \
  --steps 8 --temperature 0
```
