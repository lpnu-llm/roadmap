## Subtopics

- Multilingual pretraining and language sampling
- Cross-lingual transfer and alignment
- Tokenizer fertility and cost differences
- High-resource and low-resource performance gaps
- Multilingual instruction tuning
- Evaluation, benchmark coverage, and cultural context

## Reading

- [Unsupervised Cross-lingual Representation Learning at Scale](https://arxiv.org/abs/1911.02116)
- [Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model](https://arxiv.org/abs/2402.07827)
- [Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models](https://arxiv.org/abs/2305.13707)

## Resources

- [XTREME: A Massively Multilingual Multi-task Benchmark](https://arxiv.org/abs/2003.11080)
- [FLORES-200 evaluation benchmark](https://github.com/facebookresearch/flores)

## Assignment

1. Evaluate one open model on the same tasks in English, Ukrainian, and one lower-resource language. Measure task quality, tokenizer fertility, token cost, and failure types; explain whether translation-based evaluation changes the conclusion.
2. * Adapt a small model to a low-resource language using continued pretraining or parameter-efficient fine-tuning. Compare transfer quality, forgetting, token cost, and compute use against a translation-based baseline.

## Extra topics

- Research and present language-specific safety and bias evaluation.
- Research and present multilingual retrieval-augmented generation.
- Research and present language adaptation with continued pretraining or adapters.
