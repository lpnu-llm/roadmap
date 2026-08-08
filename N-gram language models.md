## Subtopics

- The Markov assumption
- Unigram, bigram, and higher-order models
- Count estimation and maximum likelihood
- Start, end, and unknown-word symbols
- Sparse counts and out-of-vocabulary words
- Laplace, add-k, and interpolation smoothing
- Backoff and Kneser-Ney smoothing
- Perplexity and held-out evaluation
- Efficient storage and lookup

## Reading

- [Speech and Language Processing, Chapter 3: N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [A Bit of Progress in Language Modeling](https://www.microsoft.com/en-us/research/publication/a-bit-of-progress-in-language-modeling/)
- [KenLM: Faster and Smaller Language Model Queries](https://aclanthology.org/W11-2123/)

## Resources

- [KenLM repository](https://github.com/kpu/kenlm)

## Assignment

1. Implement unigram, bigram, and trigram language models. Add unknown-word handling and at least one smoothing method.
2. Evaluate each model with held-out perplexity and generated samples. Study the effects of n-gram order, training-set size, vocabulary size, and smoothing.
3. * Implement interpolated Kneser-Ney smoothing and compare it with add-k smoothing and a standard toolkit.

## Extra topics

- Cache and adaptive language models
- Class-based n-gram models
- Weighted finite-state representations of language models
