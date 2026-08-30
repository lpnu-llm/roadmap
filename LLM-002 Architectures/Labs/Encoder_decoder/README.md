---
library_name: pytorch
tags:
  - education
  - encoder-decoder
  - pytorch
---

# Encoder-decoder architecture lab

Implement `model.py` using plain PyTorch and the supplied anonymous checkpoint.
Do not use a pretrained-model implementation from another library.

## Dimensions

| Quantity | Value |
|---|---:|
| Stored / usable vocabulary | 40,000 / 32,128 |
| Hidden width | 512 |
| Heads / head width | 8 / 64 |
| Feed-forward width | 2,048 |
| Encoder / decoder units | 7 / 7 |
| Relative buckets / maximum distance | 32 / 128 |

```mermaid
flowchart LR
    S[Source IDs] --> E[Shared token table]
    E --> EN[7 encoder units]
    EN --> EF[Encoder RMSNorm]
    EF --> M[Encoder memory]
    T[Shifted target IDs] --> D[Shared token table]
    D --> DE[7 decoder units]
    M -->|K and V| DE
    DE --> DF[Decoder RMSNorm]
    DF --> SC[Scale by 512^-0.5]
    SC --> LM[Tied token-table projection]
    LM --> V[First 32,128 logits]
```

### Encoder unit

```mermaid
flowchart LR
    X[x] --> N1[RMSNorm] --> SA[Bidirectional self-attention<br/>relative-position bias] --> R1((+))
    X --> R1
    R1 --> N2[RMSNorm] --> FF[Linear 512→2048<br/>ReLU<br/>Linear 2048→512] --> R2((+))
    R1 --> R2
    R2 --> Z[output]
```

### Decoder unit

```mermaid
flowchart LR
    X[x] --> N1[RMSNorm] --> SA[Causal self-attention<br/>relative-position bias] --> R1((+))
    X --> R1
    R1 --> N2[RMSNorm] --> CA[Cross-attention<br/>Q from decoder; K,V from memory] --> R2((+))
    R1 --> R2
    R2 --> N3[RMSNorm] --> FF[Linear 512→2048<br/>ReLU<br/>Linear 2048→512] --> R3((+))
    R2 --> R3
    R3 --> Z[output]
```

## Required behavior

- Use separate bias-free query, key, value, and output projections.
- Do not scale attention scores by `1/sqrt(head_width)`.
- Bucket relative positions logarithmically and look up a bias per head.
- RMSNorm uses no mean subtraction and no additive bias.
- Mask encoder padding in encoder self-attention and decoder cross-attention.
- Apply a causal mask in decoder self-attention.
- Begin generation with `decoder_start_id` and stop at `eos_id` or the length
  limit.
- Return only the first `vocabulary_size` logits even though more token rows are
  stored.

Load `safetensor_encoder_decoder.safetensors`. Module names must match its
neutral hierarchy: `tokens`, `encoder_units`, `decoder_units`, `self_mix`,
`cross_mix`, `feed_in`, `feed_out`, and the final normalization modules.

## Completion criteria

- Implement every TODO in `model.py`.
- Verify padding, causal masking, and relative-position buckets.
- Return logits plus encoder and decoder hidden states.
- Encode the source once during greedy generation.
- Run `python inference.py . "translate English to German: The house is nice"`.
