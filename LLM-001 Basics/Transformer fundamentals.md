## Subtopics

- Token and position embeddings
- Scaled dot-product self-attention
- Multi-head and cross-attention
- Causal and padding masks
- Feed-forward blocks, residuals, and normalization
- Encoder, decoder, and computational complexity

## Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Speech and Language Processing, Chapter 8: Transformers](https://web.stanford.edu/~jurafsky/slp3/8.pdf)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Let's Build GPT from Scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## Resources

- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)

## Assignment

1. **Implement multi-head self-attention.** Implement scaled dot-product attention and multi-head self-attention in PyTorch. Test tensor shapes, padding masks, causal masks, and attention probabilities.
2. **Train a decoder-only Transformer.** Build and train a minimal decoder-only Transformer on a small corpus. Report parameter count, loss, perplexity, sample outputs, and an estimate of attention memory use as sequence length changes.
3. * **Build an encoder-decoder Transformer.** Implement an encoder-decoder Transformer and compare it with the recurrent sequence-to-sequence model on the same task.

## Extra topics

- What attention maps do and do not explain
- Relative position representations
- Sparse and linear attention
- In-context learning in small Transformers
