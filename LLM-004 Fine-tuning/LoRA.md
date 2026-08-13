## Subtopics

- Low-rank frozen-weight updates
- Rank, scaling, dropout, and targets
- Attention and MLP adapters
- Adapter merging
- Memory–quality trade-offs

## Reading

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

## Resources

- [Hugging Face PEFT LoRA guide](https://huggingface.co/docs/peft/conceptual_guides/lora)

## Assignment

1. **Compare LoRA rank settings.** Train LoRA adapters with at least two ranks on the same task and token budget. Compare task quality, trainable parameters, memory, speed, and merged-model output.
2. * **Analyze learned update ranks.** Analyze the singular values of learned updates across layers and relate effective rank to task performance.

## Extra topics

- Present AdaLoRA, DoRA, and rank-stabilized LoRA.
- Research which attention and MLP modules should receive adapters.
- Study safe merging of several LoRA adapters.
