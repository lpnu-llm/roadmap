## Subtopics

- Pretraining, continued pretraining, and supervised fine-tuning
- Task tuning and instruction tuning
- Full fine-tuning, adapters, LoRA, and QLoRA
- Training examples, chat templates, and loss masking
- Overfitting, catastrophic forgetting, and evaluation
- Choosing between prompting, RAG, and fine-tuning

## Reading

- [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)

## Resources

- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/)
- [TRL supervised fine-tuning trainer](https://huggingface.co/docs/trl/sft_trainer)

## Assignment

1. **Choose an adaptation strategy.** For several application scenarios, decide between prompting, RAG, continued pretraining, and supervised fine-tuning. Justify each decision using data availability, knowledge freshness, latency, cost, and evaluation requirements.
2. **Fine-tune with a LoRA adapter.** Prepare a small instruction dataset and fine-tune an open model with LoRA or QLoRA. Compare it with the untuned model on held-out prompts and report trainable parameters, memory use, quality changes, and regressions.
3. * **Test adaptation data quality.** Train two adapters with clean and deliberately noisy versions of the same dataset under an equal token budget. Analyze which data problems most affect behavior.

## Extra topics

- Preference optimization and RLHF
- Adapter merging and multi-adapter serving
- Multilingual and domain adaptation
