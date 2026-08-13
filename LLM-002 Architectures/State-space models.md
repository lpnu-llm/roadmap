---
weeks: 2
---

## Subtopics

- Continuous/discrete state-space models
- Recurrent and convolutional views
- S4, Mamba, selective state spaces, and scans
- Linear-time training and constant-state decoding
- Linear attention and Transformer–SSM hybrids
- Long-sequence quality and efficiency

## Reading

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)
- [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060)
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887)

## Resources

- [Official Mamba implementation](https://github.com/state-spaces/mamba)
- [The Annotated S4](https://srush.github.io/annotated-s4/)

## Assignment

1. **Implement dual SSM forms.** Implement a small diagonal state-space layer in both recurrent and convolutional form. Check that both forms produce the same output, then compare their training and decoding costs as sequence length grows.
2. **Compare Mamba and Transformers.** Train a small Mamba-style model and a Transformer baseline on the same sequence task with similar parameter counts. Compare validation loss, training speed, peak memory, decoding speed, and performance by sequence length.
3. * **Implement a selective scan.** Implement a simplified selective scan without using an existing Mamba layer. Test its gradients and compare its output and speed with a clear sequential reference implementation.

## Extra topics

- Student presentation: state-space duality and the connection between Mamba-2 and attention
- Student presentation: hybrid Transformer–Mamba models such as Jamba
- Student presentation: when linear attention behaves like an RNN
- Student presentation: long-context retrieval failures in state-space models
