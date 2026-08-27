## Subtopics

- Autoregressive factorization and next-token prediction
- Logits, softmax, and token probabilities
- Maximum likelihood and cross-entropy
- Causal masking and teacher forcing
- Perplexity, leakage, and evaluation limits

## Reading

- [Speech and Language Processing, Chapter 3: N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [Speech and Language Processing, Chapter 7: Large Language Models](https://web.stanford.edu/~jurafsky/slp3/7.pdf)
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)

## Assignment

1. **Implement a contextual spellchecker.** You will be given a sentence with a spelling mistake in it and a set of candidate correction. Train a small n-gram model and user perplixity to select the correct candidate.
2. **Analyze token-level model loss.** Compare token-level loss across frequent tokens, rare tokens, sentence beginnings, and sentence endings. Explain where perplexity is useful and where it can be misleading.

## Extra topics

- Bits per byte as a tokenizer-independent metric
- Calibration of next-token probabilities
- Language modeling for speech, music, and biological sequences
