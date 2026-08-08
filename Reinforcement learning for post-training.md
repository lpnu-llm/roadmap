## Subtopics

- Policy, action, trajectory, reward, and advantage for language generation
- Reinforcement Learning from AI Feedback (RLAIF)
- Constitutional AI and critique-revision data
- Reinforcement Learning with Verifiable Rewards (RLVR)
- Rule-based verifiers for mathematics, code, and structured outputs
- Group Relative Policy Optimization (GRPO)
- Reward sparsity, KL control, entropy, and response-length growth
- Reliable evaluation against reward hacking

## Reading

- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)

## Resources

- [TRL GRPO trainer](https://huggingface.co/docs/trl/grpo_trainer)
- [verl](https://github.com/volcengine/verl)

## Assignment

1. Run GRPO on a small model and a verifiable task such as a GSM8K subset. Track reward, task accuracy, KL divergence, entropy, response length, and malformed outputs.
2. * Build both an AI-feedback reward and a deterministic verifier for one task. Compare RLAIF and RLVR for sample efficiency, robustness, and reward hacking.

## Extra topics

- Present how GRPO estimates advantages without a learned value model.
- Research process rewards, partial credit, and verifier design.
- Study constitutional rule generation and evaluator bias in RLAIF.
- Compare GRPO with PPO, REINFORCE, and newer policy-gradient variants.
