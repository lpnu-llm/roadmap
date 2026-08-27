## Subtopics

- Capability definitions, test sets, and task metrics
- Prompt and decoding sensitivity
- Factuality, hallucinations, attribution, and abstention
- Human evaluation and annotator agreement
- LLM-as-a-judge and common biases
- Benchmark contamination and data leakage
- Safety, privacy, cost, and latency as evaluation dimensions
- Reproducible reporting and error analysis

## Reading

- [HELM: Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)

## Resources

- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [TruthfulQA](https://arxiv.org/abs/2109.07958)

## Assignment

1. **Audit hallucinations and abstention.** Evaluate factual answers against reliable sources, separate unsupported from incorrect claims, and test a simple abstention policy. Report factual precision, coverage, and representative failures.

## Extra topics

- Dynamic benchmarks and benchmark saturation
- Calibration and risk-coverage curves
- Red teaming and adversarial evaluation
