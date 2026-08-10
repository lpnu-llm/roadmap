---
weeks: 3
---

## Subtopics

- Bias sources across data, objectives, decoding, evaluation, and deployment
- Allocative, representational, stereotyping, erasure, and service-quality harms
- Group and individual fairness, calibration, and incompatible goals
- Bias benchmarks and construct-validity limitations
- Performance disparities across languages, dialects, demographics, and intersections
- Population, comparison-group, uncertainty, significance, and testing choices
- Data, training, prompting, decoding, and policy mitigations
- Safety-filter, refusal, dialect, and service-quality trade-offs
- Participatory evaluation, stakeholder input, appeals, and deployment monitoring

## Reading

- Bender et al., [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922)
- Parrish et al., [BBQ: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/abs/2110.08193)
- Liang et al., [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)
- Blodgett et al., [Language (Technology) is Power: A Critical Survey of “Bias” in NLP](https://aclanthology.org/2020.acl-main.485/)
- Weidinger et al., [Taxonomy of Risks Posed by Language Models](https://dl.acm.org/doi/10.1145/3531146.3533088)

## Resources

- [HELM evaluation framework](https://crfm.stanford.edu/helm/)
- [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/index)
- [Fairlearn assessment and mitigation tools](https://fairlearn.org/)

## Assignment

1. **Design a Model Bias Audit.** Define a bias audit for one open model and one use case. Name the affected groups and harms, choose an established benchmark such as BBQ, and add at least 30 custom probes. Explain why each metric fits the stated harm and what important behavior it misses.
2. **Measure Group Performance Disparities.** Run the audit with fixed decoding settings and repeated trials. Break down results by relevant groups and intersections, report sample sizes and uncertainty, and inspect errors qualitatively. Check at least one possible confound such as prompt wording, language variety, or answer-position bias.
3. **Evaluate a Fairness Mitigation.** Apply one mitigation at the data, prompting, decoding, or system-policy level. Re-run the full audit and a general capability test. Report improvements, regressions, and distributional trade-offs rather than reducing the result to one fairness score.
4. * **Conduct a Participatory Audit.** Conduct a participatory audit exercise with a documented, consent-based feedback process or a carefully designed simulation when real participants are not available. Compare stakeholder-defined harms with benchmark metrics and propose an ongoing monitoring and appeal process.

## Extra topics

- Presentation: critique the construct validity of one popular bias benchmark
- Presentation: compare allocative and representational harms in a real LLM product
- Research: measure fairness across low-resource languages or dialects without treating English as the universal baseline
- Research: study whether safety tuning changes refusal rates differently across demographic or dialect groups
