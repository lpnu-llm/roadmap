## Subtopics

- Outcome reward models and process reward models
- Pairwise, scalar, and step-level supervision
- Reward-model calibration, uncertainty, and distribution shift
- Best-of-n sampling and rejection sampling
- Self-consistency and majority voting
- Search, verification, and adaptive inference budgets
- Accuracy, latency, token cost, and serving trade-offs

## Reading

- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
- [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393)

## Resources

- [RLHF Book: reward models](https://rlhfbook.com/c/07-reward-models.html)

## Assignment

1. Measure accuracy versus token budget on a reasoning benchmark using greedy decoding, self-consistency, and best-of-n selection with an outcome verifier or reward model.
2. * Train a small process reward model from step labels and compare its search decisions, calibration, and final accuracy with an outcome reward model.

## Extra topics

- Present compute-optimal allocation between more samples and longer samples.
- Research adaptive stopping and budget control for easy and hard prompts.
- Study reward-model ensembles, uncertainty, and adversarial candidates.
- Compare tree search, beam search, and learned value-guided search.
