---
weeks: 3
---

## Subtopics

- Privacy threat models across pretraining, fine-tuning, retrieval, prompts, logs, outputs, and model release
- Memorization versus generalization; exact, approximate, and semantic memorization
- Training-data extraction, membership inference, attribute inference, and model inversion
- Factors that affect leakage: duplication, rarity, model size, overfitting, prompting, and decoding
- Personally identifiable information detection, redaction, pseudonymization, replacement, and data minimization
- Limits of PII scrubbing: context, indirect identifiers, multilingual text, and re-identification
- Differential privacy: privacy budgets, clipping, noise, utility trade-offs, and limits of interpretation
- Machine unlearning: exact and approximate approaches, evaluation, retraining baselines, and deletion verification
- Privacy risks in retrieval-augmented generation, vector stores, caches, telemetry, and third-party APIs
- Watermarking and AI-text detection: threat models, robustness, false positives, and social risks
- Privacy documentation, access control, retention, deletion, and incident response

## Reading

- Carlini et al., [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805)
- Carlini et al., [Quantifying Memorization Across Neural Language Models](https://arxiv.org/abs/2202.07646)
- Shokri et al., [Membership Inference Attacks Against Machine Learning Models](https://arxiv.org/abs/1610.05820)
- Bourtoule et al., [Machine Unlearning](https://arxiv.org/abs/1912.03817)
- Kirchenbauer et al., [A Watermark for Large Language Models](https://arxiv.org/abs/2301.10226)

## Resources

- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [Microsoft Presidio: data protection and de-identification SDK](https://microsoft.github.io/presidio/)
- [Opacus: differential privacy for PyTorch](https://opacus.ai/)

## Assignment

1. Train a small language model on a corpus seeded with unique canary strings at several duplication rates. Attempt extraction with a fixed query budget and report exposure or another clear memorization metric. Include a control corpus, multiple random seeds, and a discussion of why synthetic canaries do not fully represent real personal data.
2. Build a PII-handling pipeline for a multilingual sample dataset. Define the PII categories, compare rule-based and model-based detection, and measure precision and recall on a manually checked test set. Redact or replace detected values, test for broken meaning and re-identification clues, and document retention and access assumptions.
3. Evaluate one privacy mitigation: differential privacy, deduplication, access-controlled retrieval, or approximate unlearning. Compare privacy attack success and task utility before and after mitigation. Include a strong baseline and state clearly what the experiment cannot guarantee.
4. * Implement a membership-inference or training-data-extraction attack under a strict, ethical threat model. Compare at least two model sizes or training settings, estimate uncertainty, and propose a release decision based on both privacy risk and utility.

## Extra topics

- Presentation: compare differential privacy, data deletion, and machine unlearning for one deployment scenario
- Presentation: explain why watermarking and AI-text detection are not the same privacy problem
- Research: study memorization across languages, scripts, or tokenization choices
- Research: design a deletion-verification test for a retrieval-augmented generation system
