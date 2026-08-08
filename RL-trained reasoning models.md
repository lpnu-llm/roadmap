## Subtopics

- Reasoning models trained with reinforcement learning
- Cold-start supervised data followed by RL
- Emergent long reasoning traces, self-checking, and backtracking
- Verifiable tasks for mathematics and code
- Reasoning accuracy, trace length, and compute cost
- Distillation from RL-trained teachers
- Failure modes: reward hacking, unreadable traces, and weak transfer

## Reading

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)

## Assignment

1. Compare a base, instruction-tuned, and RL-trained reasoning model on a small mathematics or code benchmark. Measure accuracy, token use, self-correction, and common failure types.
2. * Reproduce a small RL reasoning experiment with a verifiable reward and test whether longer traces cause better answers or only higher reward.

## Extra topics

- Present the training stages and results of DeepSeek-R1.
- Research whether reinforcement learning creates new reasoning behavior or improves search over existing behavior.
- Study faithfulness and interpretability of hidden or visible reasoning traces.
