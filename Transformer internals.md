---
weeks: 3
---

## Subtopics

- Token embeddings, positional information, and the residual stream
- Scaled dot-product attention and causal masking
- Self-attention, cross-attention, and multi-head attention
- Query, key, value, and output projections
- MLP blocks and activation functions
- Layer normalization, pre-norm, and post-norm blocks
- Residual connections and information flow through a Transformer
- Vocabulary projection, tied embeddings, and next-token logits
- Training-time tensor shapes and the autoregressive decoding path
- Attention masks, padding masks, and numerical stability

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

1. Implement scaled dot-product attention and multi-head causal self-attention in PyTorch. Add tests for tensor shapes, masking, and agreement with a slow reference implementation.
2. Implement a minimal decoder-only Transformer with token embeddings, positional information, pre-norm blocks, an MLP, residual connections, and an output head. Train it on a small text corpus and report validation loss and sample outputs.
3. Trace one batch through a trained model. Record the shape, mean, standard deviation, and gradient norm at every main block, then explain how the residual stream and normalization affect training.
4. * Implement a memory-efficient attention kernel or use PyTorch FlexAttention to express the same causal mask. Compare correctness, peak memory, and speed with the basic implementation.

## Extra topics

- Student presentation: induction heads and in-context pattern copying
- Student presentation: why Transformers use residual streams
- Student presentation: attention maps as explanations and their limits
- Student presentation: encoder-only, decoder-only, and encoder-decoder computation paths
