---
weeks: 2
---

## Subtopics

- Autonomous research loops: propose, implement, run, evaluate, and revise
- Experiment budgets, baselines, controls, and stopping rules
- Machine learning experimentation agents
- Literature search and evidence-grounded hypothesis generation
- Automated evaluators and verifiable discovery
- Reproducibility, provenance, and research logs
- Human oversight, safety, and dual-use risks
- Agents for scientific discovery

## Reading

- [MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://proceedings.mlr.press/v235/huang24y.html)
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)
- [CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark](https://arxiv.org/abs/2409.11363)
- [Mathematical Discoveries from Program Search with Large Language Models](https://www.nature.com/articles/s41586-023-06924-6)

## Resources

- [autoresearch: agents running machine learning experiments automatically](https://github.com/karpathy/autoresearch)
- [The AI Scientist code](https://github.com/SakanaAI/AI-Scientist)
- [AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131)
- [Towards an AI Co-Scientist](https://arxiv.org/abs/2502.18864)
- [Robin: A Multi-Agent System for Automating Scientific Discovery](https://arxiv.org/abs/2505.13400)

## Assignment

1. Build a bounded autoresearch loop for a small machine learning problem. The agent must propose one change at a time, edit code, run a fixed-budget experiment, keep or reject the change using a held-out metric, and write a complete experiment log. Compare it with random search and a simple human-designed baseline.
2. Give an agent a small published experiment to reproduce or a controlled MLAgentBench-style task. Audit dependency setup, data provenance, metric correctness, leakage, failed runs, compute cost, and reproducibility; then write a report separating verified findings from unverified claims.
3. * Add parallel hypothesis generation and an automated evaluator inspired by FunSearch or AlphaEvolve. Use independent verification, compare with the single-agent loop under the same compute budget, and analyze false discoveries.

## Extra topics

- Research and present laboratory-in-the-loop agents for biology or chemistry.
- Research and present multi-agent hypothesis debate and tournament selection.
- Research and present automated peer review and its failure modes.
- Research and present governance for autonomous research systems with dual-use capabilities.
