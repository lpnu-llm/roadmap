## Subtopics

- Unicode, bytes, words, and subwords
- BPE, WordPiece, and unigram tokenization
- Byte-level tokenization and special tokens
- Training, encoding, and decoding
- Multilingual fertility and failure modes

## Reading

- [Speech and Language Processing, Chapter 2: Regular Expressions, Text Normalization, and Edit Distance](https://web.stanford.edu/~jurafsky/slp3/2.pdf)
- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909)
- [SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing](https://aclanthology.org/D18-2012/)
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)

## Resources

- [Hugging Face Tokenizers documentation](https://huggingface.co/docs/tokenizers/)
- [Let's Build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)

## Assignment

1. **Implement a BPE tokenizer.** Implement a BPE tokenizer from scratch, including training, encoding, decoding, and tests for round-trip correctness.
2. **Compare multilingual tokenizer fertility.** Compare the fertility of at least three existing tokenizers on English, Ukrainian, Georgian, and Thai. Explain the main differences and show difficult examples.
3. * **Add byte-level tokenization.** Extend the tokenizer to use byte-level input and measure how this changes unknown-token handling and sequence length.

## Extra topics

- Morphology-aware tokenization
- Dynamic vocabularies
- Tokenization-free byte and character models
- Security issues caused by Unicode and invisible characters