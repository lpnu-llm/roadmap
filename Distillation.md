## Subtopics

- Knowledge distillation for smaller and cheaper models
- Logit, feature, and sequence-level distillation
- Temperature and soft targets
- Teacher-generated instructions and responses
- Distilling reasoning traces from stronger teachers
- Data quality, teacher errors, and student capacity
- Brief introduction to model merging and weight-space methods

## Reading

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)
- [DeepSeek-R1, including the distilled-model section](https://arxiv.org/abs/2501.12948)

## Assignment

1. Distill responses or reasoning traces from a strong open teacher into a small student. Compare against supervised fine-tuning on human-written data at a matched token budget.
2. * Combine sequence-level and logit distillation, then run ablations on temperature and teacher confidence filtering.

## Extra topics

- Present progressive, online, and self-distillation.
- Research how reasoning-trace length and correctness affect the student.
- Study privacy, licensing, and provenance risks in teacher-generated data.
