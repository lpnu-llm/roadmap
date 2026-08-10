## Subtopics

- Domain- and task-adaptive pretraining
- Causal objectives and domain corpora
- Vocabulary shift, learning rates, and data mixing
- Catastrophic forgetting
- Pretraining versus instruction tuning

## Reading

- [Don't Stop Pretraining: Adapt Language Models to Domains and Tasks](https://arxiv.org/abs/2004.10964)
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)

## Resources

- [Hugging Face causal language modeling guide](https://huggingface.co/docs/transformers/tasks/language_modeling)

## Assignment

1. **Compare domain adaptation methods.** Continue pretraining a small model on a domain corpus, then compare it with pure supervised fine-tuning on the same downstream tasks. Measure domain gains and general-task regressions.
2. * **Tune data mixing ratios.** Repeat the experiment with a mixed domain/general corpus and tune the mixing ratio to reduce forgetting without losing the domain gain.

## Extra topics

- Present case studies of continual pretraining for medicine, law, finance, or code.
- Research replay, regularization, and model merging as ways to limit forgetting.
- Compare DAPT and TAPT when only a small amount of domain text is available.
