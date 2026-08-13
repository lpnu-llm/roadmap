## Subtopics

- AdamW and parameter groups
- Learning-rate schedules and batching
- Gradient clipping and mixed precision
- Instability diagnosis and recovery
- Overfitting and early stopping
- Scaling laws and reproducibility

## Reading

- [OLMo 2: fully open end-to-end training reference](https://arxiv.org/abs/2501.00656)
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264)

## Resources

- [Chinchilla Scaling: A Replication Attempt](https://epoch.ai/blog/chinchilla-scaling-a-replication-attempt)
- [Weights & Biases guide to experiment tracking](https://docs.wandb.ai/guides/track/)

## Assignment

1. **Diagnose fine-tuning instability.** Fine-tune a small model across a controlled learning-rate and warmup sweep. Plot training loss, validation loss, gradient norm, throughput, and task quality, then diagnose unstable runs.
2. * **Fit and test scaling laws.** Fit a small scaling curve across model size, data amount, or training steps and predict the best configuration for a fixed compute budget. Test the prediction with one extra run.

## Extra topics

- Present common signatures of divergence, overfitting, and data bugs in training curves.
- Research schedule-free optimizers, Adafactor, Lion, and low-bit optimizers.
- Study sharpness, gradient noise scale, and batch-size scaling.
- Compare checkpoint averaging, model soups, and weight-space merging.
