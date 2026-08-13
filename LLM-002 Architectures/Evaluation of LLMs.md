---
weeks: 4
---

## Subtopics

- Intrinsic, task, preference, and calibration metrics
- Benchmark coverage, validity, saturation, dynamic tests
- Prompt/decoding sensitivity and reproducibility
- Contamination and leakage
- Uncertainty, paired tests, confidence intervals, and effect sizes
- Human evaluation and annotator agreement
- LLM-as-judge biases
- Quality, cost, latency, memory, and energy trade-offs
- Error analysis, reporting, and governance

## Reading

- [HELM: Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022)
- [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/abs/2406.01574)
- [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://arxiv.org/abs/2403.07974)
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)

## Resources

- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [HELM documentation](https://crfm-helm.readthedocs.io/)
- [SWE-bench](https://www.swebench.com/)
- [Chatbot Arena](https://lmarena.ai/)

## Assignment

1. **Benchmark open language models.** Evaluate at least two open language models on three tasks with `lm-evaluation-harness`. Fix the prompts and decoding settings, report uncertainty and cost, and perform an error analysis instead of reporting only average scores.
2. **Audit benchmark validity.** Audit one public benchmark for contamination risk and validity. Inspect its source, dates, duplicates, answer format, and likely web exposure, then explain what conclusions the benchmark can and cannot support.
3. **Build a capability evaluation.** Build a small evaluation set for one clearly defined capability. Write task and annotation rules, create simple and difficult examples, establish a baseline, and measure agreement between at least two annotators.
4. **Audit an LLM judge.** Run an LLM-as-judge experiment on paired model answers. Randomize answer order, test verbosity bias and self-preference, compare the judge with human labels, and report agreement with confidence intervals.
5. * **Reproduce an evaluation result.** Reproduce and critique a published LLM evaluation result. Match the original setup as closely as possible, test at least two reasonable protocol changes, and show whether the model ranking remains stable.

## Extra topics

- Student presentation: benchmark saturation and dynamic benchmark design
- Student presentation: contamination detection methods
- Student presentation: evaluation of agents with SWE-bench Verified
- Student presentation: multilingual and culturally aware evaluation
- Student presentation: evaluating long-context models beyond needle retrieval
- Student presentation: red-team evaluation and dangerous capability testing
