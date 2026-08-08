## Subtopics

- Probability distributions over text sequences
- The chain rule and autoregressive factorization
- Next-token prediction
- Logits, softmax, and token probabilities
- Maximum-likelihood training
- Cross-entropy and negative log-likelihood
- Causal masking
- Teacher forcing
- Evaluation with loss and perplexity
- Limits of perplexity and data leakage

## Reading

- [Speech and Language Processing, Chapter 3: N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [Speech and Language Processing, Chapter 7: Large Language Models](https://web.stanford.edu/~jurafsky/slp3/7.pdf)
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)

## Assignment

1. Implement the next-token training objective for a small tokenized corpus. Verify shifted inputs and targets, causal masking, average cross-entropy, and perplexity with unit tests.
2. Compare token-level loss across frequent tokens, rare tokens, sentence beginnings, and sentence endings. Explain where perplexity is useful and where it can be misleading.
3. * Derive the gradient of softmax cross-entropy with respect to the logits and verify it numerically.

## Extra topics

- Bits per byte as a tokenizer-independent metric
- Calibration of next-token probabilities
- Language modeling for speech, music, and biological sequences
