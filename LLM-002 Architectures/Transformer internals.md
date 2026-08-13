---
weeks: 3
---

## Subtopics

- Embeddings, positions, and residual streams
- Causal scaled dot-product attention and QKV projections
- Self-, cross-, and multi-head attention
- MLPs, normalization, and residual flow
- Tied embeddings and next-token logits
- Tensor shapes, masks, and numerical stability

## Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Speech and Language Processing, Chapter 8: Transformers](https://web.stanford.edu/~jurafsky/slp3/8.pdf)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## Resources

- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
- [PyTorch scaled dot-product attention](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)

## Assignment

1. **Implement causal self-attention.** Implement scaled dot-product attention and multi-head causal self-attention in PyTorch. Add tests for tensor shapes, masking, and agreement with a slow reference implementation.
2. **Build a decoder-only Transformer.** Implement a minimal decoder-only Transformer with token embeddings, positional information, pre-norm blocks, an MLP, residual connections, and an output head. Train it on a small text corpus and report validation loss and sample outputs.
3. **Trace the residual stream.** Trace one batch through a trained model. Record the shape, mean, standard deviation, and gradient norm at every main block, then explain how the residual stream and normalization affect training.
4. * **Benchmark efficient attention kernels.** Implement a memory-efficient attention kernel or use PyTorch FlexAttention to express the same causal mask. Compare correctness, peak memory, and speed with the basic implementation.

## Extra topics

- Student presentation: induction heads and in-context pattern copying
- Student presentation: why Transformers use residual streams
- Student presentation: attention maps as explanations and their limits
- Student presentation: encoder-only, decoder-only, and encoder-decoder computation paths
