---
weeks: 2
---

## Subtopics

- Supervised instruction tuning
- Instruction and response schemas
- Chat templates and loss masking
- Data mixtures and task balance
- Pre/post-tuning evaluation

## Reading

- [FLAN: Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652)
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206)
- [SLP3 Ch. 9 — Post-training: Instruction Tuning, Alignment, and Test-Time Compute](https://web.stanford.edu/~jurafsky/slp3/9.pdf)

## Resources

- [Hugging Face chat templates](https://huggingface.co/docs/transformers/chat_templating)
- [TRL supervised fine-tuning trainer](https://huggingface.co/docs/trl/sft_trainer)

## Assignment

1. **Audit an instruction dataset.** Build and audit a small instruction dataset. Define its schema, apply the model's chat template, inspect tokenized examples, and report task balance, length statistics, duplicates, and formatting failures.
2. **Compare base and tuned models.** Fine-tune a small model on the dataset. Compare the base and tuned models on held-out prompts using task metrics and a short human evaluation. Analyze both improvements and regressions.
3. * **Test data mixture effects.** Train two models with different data mixtures or curriculum orders under the same token budget. Explain which examples caused the largest behavior changes.

## Extra topics

- Present the evolution from FLAN and Self-Instruct to current open instruction-tuning recipes.
- Research whether a small, carefully selected dataset can beat a much larger noisy dataset.
- Study multilingual instruction tuning and cross-lingual transfer.
