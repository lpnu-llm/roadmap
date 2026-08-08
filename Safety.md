---
weeks: 3
---

## Subtopics

- Safety goals, threat models, assets, actors, trust boundaries, and risk severity
- Capability evaluation, misuse evaluation, robustness evaluation, and dangerous-capability testing
- Human and automated red teaming; coverage, reproducibility, and responsible disclosure
- Jailbreaks, adversarial suffixes, encoding attacks, multilingual attacks, and adaptive attackers
- Prompt injection: direct and indirect injection, instruction hierarchy, data-control separation, and untrusted content
- Agent security: tool permissions, least privilege, sandboxing, approval gates, secret handling, and excessive agency
- Data poisoning, backdoors, compromised dependencies, model supply chains, and artifact integrity
- Defenses: input and output filters, structured interfaces, isolation, monitoring, rate limits, and incident response
- Measuring defense utility, false positives, false negatives, attack adaptation, and defense in depth
- Safe experiment design: synthetic targets, local environments, no real secrets, and no attacks on systems without permission

## Reading

- Zou et al., [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)
- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- Simon Willison, [Prompt injection](https://simonwillison.net/series/prompt-injection/) and [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- Perez et al., [Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)
- NIST, [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)

## Resources

- [Berkeley course: Understanding LLMs—Foundations and Safety](https://rdi.berkeley.edu/understanding_llms/s24)
- [MITRE ATLAS knowledge base](https://atlas.mitre.org/)
- [garak LLM vulnerability scanner](https://github.com/NVIDIA/garak)

## Assignment

1. Write a threat model for a document-reading LLM agent that can search files and call one external tool. Identify assets, trust boundaries, attacker goals, abuse cases, and likely failure impact. Map at least five risks to OWASP or MITRE ATLAS and propose testable security requirements.
2. Run an authorized red-team exercise against a local model or a sandboxed demo. Build at least 30 tests covering jailbreaks, direct prompt injection, indirect prompt injection, sensitive-data requests, and unsafe tool calls. Record success criteria and results, and do not use real credentials or target third-party systems.
3. Implement two layers of defense for the tested system, such as strict tool schemas, least-privilege permissions, content isolation, approval gates, or output validation. Re-run the same suite, measure attack success and task utility, inspect false positives, and explain what remains unsafe.
4. * Create a small adaptive attack-and-defense study. Let the attack change after observing the first defense, add new held-out tests, and compare at least three defense configurations. Report uncertainty and avoid claiming that passing the suite proves safety.

## Extra topics

- Presentation: analyze a public LLM security incident using a threat model and an attack chain
- Presentation: compare human red teaming with model-assisted red teaming
- Research: evaluate whether a prompt-injection defense generalizes across languages and model families
- Research: design an agent-permission benchmark that measures both security and useful task completion
