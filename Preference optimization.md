## Subtopics

- Pairwise preference data
- Direct Preference Optimization
- Reference policies and beta
- Alternative preference objectives
- Data quality and over-optimization

## Reading

- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)

## Resources

- [TRL DPO trainer](https://huggingface.co/docs/trl/dpo_trainer)

## Assignment

1. **Compare SFT and DPO.** Compare supervised fine-tuning and DPO on the same task and base model. Analyze which outputs improve, regress, or become over-stylized, and inspect sensitivity to beta.
2. * **Implement and verify DPO.** Implement the DPO loss directly, verify it against a library implementation, and compare DPO with one related preference objective under a matched compute budget.

## Extra topics

- Present the derivation of DPO from the KL-constrained reinforcement-learning objective.
- Research preference optimization with binary, scalar, or unpaired feedback.
- Study length bias, verbosity, and preference-data contamination.
