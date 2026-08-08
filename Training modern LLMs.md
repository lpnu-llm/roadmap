---
weeks: 2
---

## Subtopics

- The end-to-end pretraining pipeline
- Web-scale corpus collection and licensing
- Language identification, quality filtering, and data mixtures
- Exact and approximate deduplication
- Benchmark decontamination
- Token budgets and data documentation
- AdamW, learning-rate warmup, schedules, and gradient clipping
- Mixed precision, gradient accumulation, and checkpointing
- Loss curves, instability, and recovery
- Scaling laws and compute-optimal training
- Multi-stage training and continual pretraining
- Data, tensor, pipeline, and expert parallelism
- ZeRO and fully sharded data parallelism
- Throughput, model FLOP utilization, and reproducibility

## Reading

- [Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus](https://arxiv.org/abs/2104.08758)
- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557)
- [OLMo 2: The Best Fully Open Language Model to Date](https://arxiv.org/abs/2501.00656)
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054)

## Resources

- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)
- [CMU 11-667: Large Language Models Methods and Applications](https://2025.cmu-llms.org/schedule/)
- [The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
- [How to Scale Your Model](https://jax-ml.github.io/scaling-book/)

## Assignment

1. Build a small pretraining-data pipeline from raw documents. Add language or quality filtering, deduplication, train-validation splitting, and contamination checks. Produce a data card with token counts, licenses, removed examples, and known risks.
2. Train several small causal language models under a fixed compute budget. Track throughput, learning rate, gradient norm, validation loss, and checkpoints; fit a simple scaling curve and propose a model-size/data-size plan for a larger budget.
3. * Given a fixed multi-GPU cluster, design a distributed training plan with memory estimates, communication costs, checkpoint recovery, and expected model FLOP utilization. Validate one part with FSDP or another sharding tool if hardware is available.

## Extra topics

- Data governance and opt-out mechanisms
- Data-constrained scaling and repeated data
- Training instability and loss-spike prediction
- Carbon and water accounting for model training
- Reproducible open model development
