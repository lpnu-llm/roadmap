---
weeks: 4
---

## Subtopics

- Intrinsic evaluation: cross-entropy, perplexity, and bits per byte
- Task metrics: exact match, F1, pass@k, preference rate, and calibration
- Benchmark design, task coverage, and construct validity
- Saturated benchmarks such as MMLU, GSM8K, and HumanEval
- Current benchmarks such as GPQA, MMLU-Pro, LiveCodeBench, and SWE-bench Verified
- Prompt sensitivity, few-shot selection, decoding settings, and reproducibility
- Data contamination, benchmark leakage, and dynamic test sets
- Statistical uncertainty, paired tests, confidence intervals, and effect sizes
- Human evaluation design and inter-annotator agreement
- LLM-as-judge uses and position, verbosity, and self-preference biases
- Cost, latency, memory, energy use, and quality trade-offs
- Error analysis, reporting, and evaluation governance

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

1. Evaluate at least two open language models on three tasks with `lm-evaluation-harness`. Fix the prompts and decoding settings, report uncertainty and cost, and perform an error analysis instead of reporting only average scores.
2. Audit one public benchmark for contamination risk and validity. Inspect its source, dates, duplicates, answer format, and likely web exposure, then explain what conclusions the benchmark can and cannot support.
3. Build a small evaluation set for one clearly defined capability. Write task and annotation rules, create simple and difficult examples, establish a baseline, and measure agreement between at least two annotators.
4. Run an LLM-as-judge experiment on paired model answers. Randomize answer order, test verbosity bias and self-preference, compare the judge with human labels, and report agreement with confidence intervals.
5. * Reproduce and critique a published LLM evaluation result. Match the original setup as closely as possible, test at least two reasonable protocol changes, and show whether the model ranking remains stable.

## Extra topics

- Student presentation: benchmark saturation and dynamic benchmark design
- Student presentation: contamination detection methods
- Student presentation: evaluation of agents with SWE-bench Verified
- Student presentation: multilingual and culturally aware evaluation
- Student presentation: evaluating long-context models beyond needle retrieval
- Student presentation: red-team evaluation and dangerous capability testing
