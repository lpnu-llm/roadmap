## Subtopics

- Low-rank updates to frozen weight matrices
- Rank, scaling factor, dropout, and target modules
- LoRA for attention and MLP layers
- Merging adapters into base weights
- Memory, speed, and quality trade-offs
- Multi-adapter training and serving

## Reading

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

## Resources

- [Hugging Face PEFT LoRA guide](https://huggingface.co/docs/peft/conceptual_guides/lora)

## Assignment

1. Train LoRA adapters with at least two ranks on the same task and token budget. Compare task quality, trainable parameters, memory, speed, and merged-model output.
2. * Analyze the singular values of learned updates across layers and relate effective rank to task performance.

## Extra topics

- Present AdaLoRA, DoRA, and rank-stabilized LoRA.
- Research which attention and MLP modules should receive adapters.
- Study safe merging of several LoRA adapters.
