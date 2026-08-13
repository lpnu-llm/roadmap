## Subtopics

- Outcome and process reward models
- Pairwise, scalar, and step-level supervision
- Calibration, uncertainty, and distribution shift
- Best-of-n and rejection sampling
- Self-consistency
- Search and adaptive inference budgets
- Accuracy, latency, and token trade-offs

## Reading

- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
- [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393)

## Resources

- [RLHF Book: reward models](https://rlhfbook.com/c/07-reward-models.html)

## Assignment

1. **Measure test-time scaling trade-offs.** Measure accuracy versus token budget on a reasoning benchmark using greedy decoding, self-consistency, and best-of-n selection with an outcome verifier or reward model.
2. * **Compare process and outcome rewards.** Train a small process reward model from step labels and compare its search decisions, calibration, and final accuracy with an outcome reward model.

## Extra topics

- Present compute-optimal allocation between more samples and longer samples.
- Research adaptive stopping and budget control for easy and hard prompts.
- Study reward-model ensembles, uncertainty, and adversarial candidates.
- Compare tree search, beam search, and learned value-guided search.
