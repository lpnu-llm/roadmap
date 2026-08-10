---
weeks: 2
---

## Subtopics

- Context limits: data, positions, memory, and compute
- RoPE, ALiBi, and learned positional embeddings
- Position interpolation, RoPE scaling, and YaRN
- Long-context training and length curricula
- Attention and KV-cache scaling
- Long-context failure modes
- Effective-context evaluation: RULER, retrieval, and perplexity
- External memory, retrieval, and context compression

## Reading

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [Extending Context Window of Large Language Models via Positional Interpolation](https://arxiv.org/abs/2306.15595)
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071)
- [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654)

## Resources

- [Hugging Face guide to RoPE utilities](https://huggingface.co/docs/transformers/main/en/internal/rope_utils)
- [LongBench](https://github.com/THUDM/LongBench)
- [RULER evaluation code](https://github.com/NVIDIA/RULER)

## Assignment

1. **Measure effective context length.** Evaluate at least two models on synthetic retrieval and aggregation tasks over increasing context lengths. Move relevant evidence across the beginning, middle, and end of each prompt. Report accuracy, latency, and peak memory, and explain where nominal context length differs from effective context length.
2. **Extend model context safely.** Extend a small model beyond its trained context with one RoPE scaling method. Compare the original and extended models using short-context perplexity, long-context perplexity by token position, and RULER-style tasks. Measure memory and runtime, and document both gains and regressions.
3. * **Compare external memory approaches.** Build an external-memory baseline using retrieval or recursive summarization. Under the same token budget, compare it with direct long-context prompting on answer quality, latency, and cost; analyze cases where stored or retrieved evidence is wrong.

## Extra topics

- Attention sinks and streaming language models
- Context compression and learned memory tokens
- Ring attention and sequence parallelism
- Sparse, block, and linear attention for long sequences
- Long-context data contamination and benchmark leakage
- Presentation: does a one-million-token window replace retrieval?
- Research: evaluation tasks that require using many pieces of evidence, not one hidden needle
