## Subtopics

- Causal versus masked language modeling
- Bidirectional context
- Mask selection and the pretraining-finetuning mismatch
- BERT architecture and pretraining objectives
- Special tokens and input segments
- Fine-tuning for sequence classification
- Token classification and part-of-speech tagging
- Named-entity recognition
- RoBERTa and improved training recipes
- Modern encoder models such as ModernBERT and Ettin
- Encoder-only models versus decoder-only models

## Reading

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- [Speech and Language Processing, Chapter 10: Masked Language Models](https://web.stanford.edu/~jurafsky/slp3/10.pdf)
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)
- [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](https://arxiv.org/abs/2412.13663)

## Resources

- [Hugging Face masked language modeling guide](https://huggingface.co/docs/transformers/tasks/masked_language_modeling)
- [Hugging Face token classification guide](https://huggingface.co/docs/transformers/tasks/token_classification)

## Assignment

1. Fine-tune a small masked language model for token classification or part-of-speech tagging. Report token-level metrics and analyze errors by token type and sequence length.
2. Probe a pretrained masked model by comparing predictions under different masks and contexts. Document examples of syntax, semantics, factual recall, and failure cases.
3. * Continue masked-language-model pretraining on a small domain corpus, then measure whether it improves the downstream task.

## Extra topics

- Span masking and replaced-token detection
- Multilingual masked language models
- Efficient long-context encoders
- Using encoder models as bi-encoders and cross-encoders
