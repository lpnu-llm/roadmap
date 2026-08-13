---
weeks: 4
---

## Subtopics

- Learned, sinusoidal, RoPE, ALiBi encodings
- Pre-norm, RMSNorm, SwiGLU, and gated MLPs
- Multi-query and grouped-query attention; KV caches
- Flash, sparse, and sliding-window attention
- Mixture-of-experts routing and load balancing
- Quality–efficiency and stability ablations

## Reading

- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088)

## Resources

- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)
- [FlashAttention implementation](https://github.com/Dao-AILab/flash-attention)
- [Hugging Face Mixture of Experts explained](https://huggingface.co/blog/moe)

## Assignment

1. **Evaluate rotary position embeddings.** Add RoPE to a small decoder-only Transformer. Compare it with learned positional embeddings at training lengths and at longer test lengths, and plot validation loss by position.
2. **Ablate normalization and MLPs.** Replace LayerNorm and the standard MLP with RMSNorm and SwiGLU. Run a controlled ablation with the same data, parameter budget, and training steps; report loss, stability, and throughput.
3. **Benchmark efficient attention variants.** Implement multi-query attention or grouped-query attention. Verify it against standard multi-head attention, then compare KV-cache memory and decoding speed at several sequence lengths.
4. **Build sparse expert routing.** Implement a small top-k mixture-of-experts MLP with an auxiliary load-balancing loss. Measure expert use, dropped tokens, training stability, and validation loss against a dense model with a similar compute budget.
5. * **Reproduce a modern architecture change.** Reproduce one modern architecture change in a small language model and run a careful ablation. Control parameter count and training compute, use several random seeds, and report throughput, peak memory, and validation loss.

## Extra topics

- Student presentation: multi-head latent attention in DeepSeek models
- Student presentation: RoPE scaling methods such as position interpolation and YaRN
- Student presentation: expert routing, expert collapse, and shared experts
- Student presentation: local-global attention and sliding-window architectures
- Student presentation: recurrent memory added to Transformers
