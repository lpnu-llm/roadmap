---
weeks: 2
---

## Subtopics

- Limits of recurrent sequence models
- Token and position embeddings
- Queries, keys, values, and scaled dot-product attention
- Self-attention and cross-attention
- Causal and padding masks
- Multi-head attention
- Feed-forward blocks
- Residual connections and layer normalization
- Encoder, decoder, and encoder-decoder Transformers
- Autoregressive output heads
- Training and inference paths
- Computational and memory complexity

## Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Speech and Language Processing, Chapter 8: Transformers](https://web.stanford.edu/~jurafsky/slp3/8.pdf)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Let's Build GPT from Scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## Resources

- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)

## Assignment

1. Implement scaled dot-product attention and multi-head self-attention in PyTorch. Test tensor shapes, padding masks, causal masks, and attention probabilities.
2. Build and train a minimal decoder-only Transformer on a small corpus. Report parameter count, loss, perplexity, sample outputs, and an estimate of attention memory use as sequence length changes.
3. * Implement an encoder-decoder Transformer and compare it with the recurrent sequence-to-sequence model on the same task.

## Extra topics

- What attention maps do and do not explain
- Relative position representations
- Sparse and linear attention
- In-context learning in small Transformers
