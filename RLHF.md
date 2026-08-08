## Subtopics

- Alignment goals: helpfulness, honesty, and harmlessness
- Collecting human demonstrations and preferences
- Training a reward model from pairwise comparisons
- Proximal Policy Optimization (PPO) for language models
- Reference-model KL penalties and adaptive KL control
- Reward hacking, objective mismatch, and annotator disagreement
- The full supervised fine-tuning, reward modeling, and RL pipeline

## Reading

- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)
- [RLHF Book](https://rlhfbook.com/)
- [SLP3 Ch. 9 — Post-training: Instruction Tuning, Alignment, and Test-Time Compute](https://web.stanford.edu/~jurafsky/slp3/9.pdf)

## Resources

- [TRL PPO trainer](https://huggingface.co/docs/trl/ppo_trainer)

## Assignment

1. Build a small preference dataset, train a pairwise reward model, and evaluate ranking accuracy by prompt category. Document disagreement and reward-model blind spots.
2. * Run a small PPO update with a reference policy. Track reward, KL divergence, response length, and held-out quality, then identify signs of reward hacking.

## Extra topics

- Present the InstructGPT pipeline and its main engineering costs.
- Research annotator selection, aggregation, and uncertainty.
- Compare PPO-based RLHF with direct preference optimization.
