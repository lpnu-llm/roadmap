---
weeks: 3
---

## Subtopics

- LLM lifecycle and artifact reproducibility
- Dataset, model, prompt, code, and evaluation lineage
- Registries, release manifests, approvals, and audits
- Evaluation gates and deployment strategies
- Rollback and incident response
- Correlated logs, metrics, and traces
- Latency, token, cost, cache, quality, and safety signals
- SLOs, error budgets, alerts, and runbooks
- Drift and regression detection
- GPU autoscaling, admission control, and cost budgets
- Privacy-aware telemetry and access control

## Reading

- [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/)
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [NIST AI RMF: Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)

## Resources

- [OpenTelemetry generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes horizontal pod autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [Kubernetes observability](https://kubernetes.io/docs/concepts/cluster-administration/observability/)
- [vLLM production metrics](https://docs.vllm.ai/en/stable/usage/metrics/)

## Assignment

1. **Create reproducible release lineage.** Create a reproducible release record for a small LLM application. Track the dataset snapshot, base model, adapter or weights, prompt template, code revision, environment, parameters, and evaluation results. Register two versions, reproduce one result from its record, and show a lineage query from a production version back to every input artifact.
2. **Instrument privacy-aware LLM observability.** Instrument an LLM service with correlated logs, metrics, and traces while redacting prompt secrets and personal data. Build a dashboard for traffic, errors, saturation, time to first token, time per output token, token use, cost, and one quality or safety signal. Define two user-centered SLOs, alerts, and short runbooks, then test them with load and injected failures.
3. **Automate safe model deployments.** Build a deployment pipeline that runs unit tests, offline quality and safety evaluations, and performance checks before release. Perform a canary deployment, detect a deliberately bad model or prompt version, and trigger rollback. Submit the gate definitions, release evidence, incident timeline, and a blameless postmortem with follow-up actions.
4. * **Build queue-aware autoscaling.** Design an autoscaling policy driven by queue length or waiting requests rather than CPU alone. Replay bursty traffic, compare it with a fixed deployment and CPU-based scaling, and analyze SLO violations, cold-start delay, GPU utilization, and cost.

## Extra topics

- Online evaluation, human feedback, and statistically safe A/B tests
- Prompt injection monitoring and tool-call audit logs
- Multi-tenant isolation, quotas, and noisy-neighbor control
- Data deletion and lineage-aware unlearning workflows
- Carbon-aware scheduling and energy budgets
- Presentation: when LLM traces become a privacy or security risk
- Research: production quality signals when ground-truth answers arrive late or never arrive
- Research: error budgets that combine reliability, quality, safety, and cost
