## Subtopics

- Helpfulness, honesty, and harmlessness
- Human feedback collection
- Pairwise reward modeling
- PPO and KL control
- Reward hacking and disagreement
- End-to-end RLHF pipelines

## Reading

- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)
- [RLHF Book](https://rlhfbook.com/)
- [SLP3 Ch. 9 — Post-training: Instruction Tuning, Alignment, and Test-Time Compute](https://web.stanford.edu/~jurafsky/slp3/9.pdf)

## Resources

- [TRL PPO trainer](https://huggingface.co/docs/trl/ppo_trainer)

## Assignment

1. **Train a reward model.** Build a small preference dataset, train a pairwise reward model, and evaluate ranking accuracy by prompt category. Document disagreement and reward-model blind spots.
2. * **Diagnose PPO reward hacking.** Run a small PPO update with a reference policy. Track reward, KL divergence, response length, and held-out quality, then identify signs of reward hacking.

## Extra topics

- Present the InstructGPT pipeline and its main engineering costs.
- Research annotator selection, aggregation, and uncertainty.
- Compare PPO-based RLHF with direct preference optimization.
