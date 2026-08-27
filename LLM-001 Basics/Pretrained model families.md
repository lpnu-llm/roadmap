## Subtopics

- Pretraining, transfer learning, and downstream adaptation
- Encoder-only, decoder-only, and encoder-decoder Transformers
- Masked, causal, and span-corruption objectives
- Contextual token and sequence representations
- Sequence classification, token classification, embedding, and generation tasks
- Choosing a model family for a task

## Reading

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)
- [Speech and Language Processing, Chapter 10: Masked Language Models](https://web.stanford.edu/~jurafsky/slp3/10.pdf)

## Resources

- [Hugging Face Transformers task guides](https://huggingface.co/docs/transformers/tasks)
- [Hugging Face model summaries](https://huggingface.co/docs/transformers/model_summary)

## Assignment

1. **Compare pretrained model families.** Use small pretrained encoder-only, decoder-only, and encoder-decoder models on representative classification, scoring, and generation examples. Compare their inputs, outputs, parameter counts, latency, and suitability for each task.
2. **Fine-tune an encoder model.** Fine-tune a small encoder-only model for sequence or token classification. Report the task metric, compare it with a linear baseline, and analyze errors by input length and label.
3. * **Probe contextual token representations.** Compare representations of the same word in several contexts across multiple layers of an encoder model. Measure similarity and relate the results to word sense and syntax.

## Extra topics

- Sentence-level embedding models
- Domain-specific and multilingual pretrained models
- Model licenses and deployment constraints
