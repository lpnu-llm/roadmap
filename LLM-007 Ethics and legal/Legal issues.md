---
weeks: 3
---

## Subtopics

- Legal issue spotting across development, release, procurement, and deployment
- Jurisdiction, organizational roles, intended purpose, and sector rules
- EU AI Act risk classes, transparency duties, and general-purpose models
- NIST AI RMF and voluntary governance frameworks
- Privacy, data protection, minimization, transfers, and data-subject rights
- Copyright, text-and-data mining, fair use, and jurisdictional differences
- Dataset provenance, consent signals, licenses, attribution, and deletion history
- Artifact-specific licensing: grants, restrictions, redistribution, derivatives, and termination
- Documentation, accountability, primary sources, assumptions, and legal advice

## Reading

- European Union, [Regulation (EU) 2024/1689: Artificial Intelligence Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- U.S. Copyright Office, [Copyright and Artificial Intelligence, Part 2: Copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) and [Part 3: Generative AI Training](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf)
- European Union, [Directive (EU) 2019/790 on Copyright in the Digital Single Market](https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng), especially the text-and-data-mining provisions
- Longpre et al., [A Large-Scale Audit of Dataset Licensing and Attribution in AI](https://www.nature.com/articles/s42256-024-00878-8)
- Mitchell et al., [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)

## Resources

- European Union, [General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [Data Provenance Initiative](https://www.dataprovenance.org/)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), [BigScience OpenRAIL-M License](https://huggingface.co/spaces/bigscience/license), and [Llama 4 Community License](https://www.llama.com/llama4/license) as examples with materially different terms
- Open Source Initiative, [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition)
- Stanford CRFM, [Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/)
- Stanford CRFM, [Foundation Models report](https://crfm.stanford.edu/report.html)

## Assignment

1. **Map Cross-Jurisdiction Legal Issues.** Prepare a legal-and-governance issue map for a hypothetical LLM product operating in two chosen jurisdictions. State the product purpose, users, data flows, model source, and organizational roles. Use current primary sources to identify questions about AI regulation, privacy, copyright, consumer or sector rules, and contracts. Separate confirmed facts, assumptions, open questions, and items that require qualified local legal advice; do not present the map as a definitive legal opinion.
2. **Audit Training Dataset Provenance.** Audit the provenance of a small training or fine-tuning dataset. Trace original sources, creators, transformations, collection dates, stated licenses, terms or consent signals, attribution requirements, and known gaps. Produce a machine-readable provenance table and a short data card. Treat missing or conflicting metadata as unresolved rather than assuming permission.
3. **Compare Model Package Licenses.** Compare the exact license texts for three model packages: one permissively licensed package, one OpenRAIL-style package, and one community or custom-licensed package. Review code, weights, data, documentation, and output terms separately. Build a table of grants, use restrictions, redistribution, attribution, derivative-model terms, patent clauses, acceptable-use terms, and termination. Recommend a license-review workflow, not a universal conclusion about legality.
4. **Draft a Deployment Governance Memo.** Write a deployment memo using the EU AI Act and NIST AI RMF Generative AI Profile. Classify the scenario only as a reasoned working hypothesis, cite the relevant provisions, define evaluation thresholds, documentation, human oversight, incident escalation, and review dates, and explain how the answer could change with role, use, jurisdiction, or later guidance.
5. * **Analyze a Narrow Copyright Question.** Analyze one narrow copyright question in model training, retrieval, or output generation. Compare an EU source with a U.S. source, distinguish legislation, agency guidance, pending disputes, and your own interpretation, and avoid transferring a conclusion from one jurisdiction to another.

## Extra topics

- Presentation: explain how provider, deployer, importer, and distributor roles can change an EU AI Act analysis
- Presentation: compare open source, open weight, and source-available model releases using actual license text
- Research: build a reproducible method for tracing license inheritance through mixed and transformed datasets
- Research: compare AI transparency obligations and voluntary documentation standards across two jurisdictions
- Research: study how model cards and data cards can support, but not replace, legal and risk review
