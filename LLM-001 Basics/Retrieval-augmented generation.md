## Subtopics

- Parametric knowledge, external knowledge, and the RAG pipeline
- Sparse retrieval with TF-IDF and BM25
- Sentence embeddings and dense retrieval
- Chunking, indexing, and metadata
- Reranking, context construction, and grounded generation
- Retrieval and answer evaluation

## Reading

- [Speech and Language Processing, Chapter 11: Information Retrieval and RAG](https://web.stanford.edu/~jurafsky/slp3/11.pdf)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)

## Resources

- [Sentence Transformers documentation](https://www.sbert.net/)
- [BEIR retrieval benchmark](https://arxiv.org/abs/2104.08663)

## Assignment

1. **Compare two retrieval methods.** Build BM25 and dense retrievers over the same small corpus. Create a labeled query set and compare Recall@k, latency, and characteristic errors.
2. **Build a small RAG system.** Implement document loading, chunking, indexing, retrieval, answer generation, and source citations. Evaluate retrieval recall, answer correctness, and whether cited passages support the answer.
3. * **Add reranking and hybrid retrieval.** Combine sparse and dense retrieval or add a cross-encoder reranker. Run an ablation and report quality, latency, and cost changes.

## Extra topics

- Query rewriting and multi-query retrieval
- Long-context models versus retrieval
- Poisoned documents and prompt injection through retrieved content
