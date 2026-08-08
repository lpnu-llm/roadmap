---
weeks: 2
---

## Subtopics

- Hallucination types and causes
- Factuality, faithfulness, and attribution
- Confidence and probability calibration
- Uncertainty estimation and semantic consistency
- Abstention and selective answering
- Detection with external evidence and self-checks
- Mitigation through retrieval, verification, and constrained generation

## Reading

- [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://arxiv.org/abs/2303.08896)
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)

## Resources

- [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958)
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251)

## Assignment

1. Build a factuality evaluation set for one domain. Split answers into atomic claims, label support with reliable sources, compare at least two models or prompting methods, and report precision with a clear failure taxonomy.
2. Ask a model to answer questions with a confidence score and the option to abstain. Measure calibration error, draw reliability and risk-coverage curves, and choose an abstention threshold for a stated error cost.
3. * Add retrieval grounding, SelfCheckGPT-style sampling, or an external verifier. Measure how the method changes factuality, calibration, coverage, latency, and cost.

## Extra topics

- Research and present semantic entropy for uncertainty estimation.
- Research and present hallucination in summarization and translation.
- Research and present calibration under distribution shift.
