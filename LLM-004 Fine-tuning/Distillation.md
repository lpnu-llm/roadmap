## Subtopics

- Knowledge distillation
- Logit, feature, and sequence-level methods
- Temperature and soft targets
- Teacher-generated instructions and reasoning traces
- Teacher quality and student capacity

## Reading

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)
- [DeepSeek-R1, including the distilled-model section](https://arxiv.org/abs/2501.12948)

## Assignment

1. **Distill teacher-generated reasoning.** Distill responses or reasoning traces from a strong open teacher into a small student. Compare against supervised fine-tuning on human-written data at a matched token budget.
2. * **Ablate distillation design choices.** Combine sequence-level and logit distillation, then run ablations on temperature and teacher confidence filtering.

## Extra topics

- Present progressive, online, and self-distillation.
- Research how reasoning-trace length and correctness affect the student.
- Study privacy, licensing, and provenance risks in teacher-generated data.
