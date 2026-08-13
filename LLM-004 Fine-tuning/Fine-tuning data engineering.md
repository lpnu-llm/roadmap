## Subtopics

- Corpus and instruction-data construction
- Quality and safety filtering
- Exact and near-duplicate removal
- Synthetic instruction generation
- Mixtures and source-grouped splits
- Benchmark decontamination
- Documentation and lineage

## Reading

- [Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus](https://arxiv.org/abs/2104.08758)
- [The FineWeb Datasets](https://arxiv.org/abs/2406.17557)
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)
- [OLMo 2: fully open end-to-end training reference](https://arxiv.org/abs/2501.00656)

## Resources

- [DataComp-LM](https://github.com/mlfoundations/dclm)
- [CMU 11-667 pretraining data lectures](https://2025.cmu-llms.org/schedule/)

## Assignment

1. **Build a data pipeline.** Build a small fine-tuning data pipeline from raw text and instruction examples. Add filtering, deduplication, source-grouped splits, synthetic-data labels, and benchmark decontamination. Publish a data card with decisions and known failure cases.
2. * **Ablate data processing stages.** Run a controlled ablation of raw, filtered, deduplicated, and synthetic-augmented datasets under a matched token budget. Measure both task quality and memorization or leakage.

## Extra topics

- Present MinHash, locality-sensitive hashing, and semantic deduplication.
- Research quality scoring with classifiers, language models, and perplexity.
- Study synthetic-data collapse, diversity loss, and feedback loops.
- Compare open corpus documentation and licensing practices.
