---
weeks: 3
---

## Subtopics

- Parametric and non-parametric memory
- Sparse retrieval with BM25
- Dense retrieval with bi-encoders and contrastive embeddings
- Reranking with cross-encoders
- Chunking, indexing, query rewriting, and hybrid retrieval
- Grounded generation, citations, and citation faithfulness
- Retrieval and end-to-end evaluation
- Long-context failure modes

## Reading

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511)
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [Speech and Language Processing, Chapter 11: Information Retrieval and RAG](https://web.stanford.edu/~jurafsky/slp3/11.pdf)

## Resources

- [BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/abs/2104.08663)
- [Sentence Transformers documentation](https://www.sbert.net/)

## Assignment

1. Build BM25 and dense bi-encoder retrievers for the same corpus. Create a labeled query set and compare Recall@k, MRR, latency, and errors across query types.
2. Build a small RAG assistant over a real corpus. Implement chunking, indexing, retrieval, answer generation, and source citations; document choices and provide a reproducible evaluation set.
3. Evaluate answer correctness, retrieval recall, citation correctness, and citation completeness separately. Test context order and context length, then analyze unsupported answers and lost-in-the-middle failures.
4. * Add a cross-encoder reranker, hybrid retrieval, query rewriting, or Self-RAG-style critique. Run an ablation study and report quality, latency, and cost trade-offs.

## Extra topics

- Research and present retrieval for rapidly changing knowledge.
- Research and present graph RAG and when graph structure helps.
- Research and present defenses against poisoned or adversarial documents.
