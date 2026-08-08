## Subtopics

- Continual pretraining for domain and task adaptation
- Domain-adaptive pretraining (DAPT) and task-adaptive pretraining (TAPT)
- Causal language-model objectives and domain corpora
- Vocabulary shift, learning-rate choice, and data mixing
- Catastrophic forgetting and general-capability retention
- Choosing continual pretraining, instruction tuning, or both

## Reading

- [Don't Stop Pretraining: Adapt Language Models to Domains and Tasks](https://arxiv.org/abs/2004.10964)
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)

## Resources

- [Hugging Face causal language modeling guide](https://huggingface.co/docs/transformers/tasks/language_modeling)

## Assignment

1. Continue pretraining a small model on a domain corpus, then compare it with pure supervised fine-tuning on the same downstream tasks. Measure domain gains and general-task regressions.
2. * Repeat the experiment with a mixed domain/general corpus and tune the mixing ratio to reduce forgetting without losing the domain gain.

## Extra topics

- Present case studies of continual pretraining for medicine, law, finance, or code.
- Research replay, regularization, and model merging as ways to limit forgetting.
- Compare DAPT and TAPT when only a small amount of domain text is available.
