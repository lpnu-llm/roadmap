## Subtopics

- Pretraining, full tuning, and PEFT
- End-to-end post-training pipelines
- LoRA and QLoRA constraints
- Quality, safety, and capability retention
- Experiment lineage
- Responsible deployment

## Reading

- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)
- [SLP3 Ch. 9 — Post-training: Instruction Tuning, Alignment, and Test-Time Compute](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
- [RLHF Book](https://rlhfbook.com/)

## Resources

- [HELM](https://crfm.stanford.edu/helm/)
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

## Assignment

1. **Design a post-training plan.** Design an end-to-end post-training plan for a small domain model. Specify the data pipeline, training stages, compute budget, evaluation matrix, safety checks, rollback criteria, and expected trade-offs. Present the plan and defend each choice.
2. * **Implement and document the plan.** Implement a small version of the plan with at least two training stages and one ablation. Produce a model card that reports gains, regressions, costs, and unresolved risks.

## Extra topics

- Present a comparison of major open post-training recipes.
- Research which evaluation results should block model deployment.
- Study reproducibility gaps between published methods and released artifacts.
- Propose a final project that tests one open question from the course.
