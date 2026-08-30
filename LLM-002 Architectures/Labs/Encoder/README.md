---
library_name: pytorch
tags:
  - education
  - encoder
  - pytorch
---

# Encoder architecture lab

Your task is to implement `model.py` and run the supplied anonymous checkpoint
without using a pretrained-model implementation from another library. You may
use PyTorch, `safetensors`, and `tokenizers`.

## Required model

The model is an encoder-only Transformer. It accepts `input_ids` and an optional
padding mask and returns contextual hidden states and vocabulary logits.

The exact dimensions are in `model.json`. For this artifact they are:

| Quantity | Value |
|---|---:|
| Stored vocabulary rows | 65,536 |
| Returned vocabulary logits | 50,368 |
| Hidden width | 1,024 |
| Attention heads | 16 |
| Width per head | 64 |
| Expanded MLP width | 2,624 |
| Transformer units | 29 |
| Maximum sequence length | 7,999 |
| Local radius | 64 tokens per side |
| Global-attention interval | Every third unit |

```mermaid
flowchart TD
    A[Token IDs<br/>batch × sequence] --> B[Token table<br/>65,536 × 1,024]
    B --> C[Input LayerNorm]
    C --> D[29 encoder units]
    D --> E[Final LayerNorm]
    E --> F[Contextual states<br/>batch × sequence × 1,024]
    F --> G[Dense 1,024 → 1,024]
    G --> H[GELU]
    H --> I[Head LayerNorm]
    I --> J[Tied token-table projection + bias]
    J --> K[Keep first 50,368 logits]
```

Each encoder unit has two pre-normalized residual branches:

```mermaid
flowchart LR
    X[Input x] --> N1[Pre-attention LayerNorm]
    X --> R1((+))
    N1 --> A[Fused QKV projection<br/>bidirectional attention<br/>global or local]
    A --> O[Output projection]
    O --> R1
    R1 --> Y[Intermediate y]
    Y --> N2[Pre-MLP LayerNorm]
    Y --> R2((+))
    N2 --> W1[Linear 1,024 → 5,248]
    W1 --> S[Split into two 2,624-wide tensors]
    S --> M[GELU first half × second half]
    M --> W2[Linear 2,624 → 1,024]
    W2 --> R2
    R2 --> Z[Unit output]
```

Unit 0 applies attention directly to the embedding output; units after it use
the pre-attention LayerNorm. Every unit uses the pre-MLP LayerNorm.

Units whose zero-based index is divisible by three use full bidirectional
attention. Other units use bidirectional local attention: a token may attend up
to 64 positions left and 64 positions right. Padding keys must never be
attended to.

Apply rotary position information to queries and keys after splitting into 16
heads. Read the rotary bases from `model.json`; do not hard-code them.

## Checkpoint contract

Load `safetensor_encoder.safetensors`. Your module names must match its neutral
tensor names, including `tokens`, `units`, `mix`, `expand`, and `contract`.
The token table has more stored rows than the tokenizer uses. Return only the
first `vocabulary_size` logits.

## Completion criteria

- All TODOs in `model.py` are implemented.
- Padding and local-attention masks work for batches with different lengths.
- `forward` returns hidden states and logits with the documented shapes.
- `python inference.py . "A short example"` runs successfully.
- The implementation uses the supplied weights rather than another model
  library.
