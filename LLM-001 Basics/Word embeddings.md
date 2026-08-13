## Subtopics

- Distributional semantics and PMI
- Sparse and dense representations
- Word2Vec, negative sampling, and GloVe
- fastText and subword information
- Similarity, analogy, and bias evaluation

## Reading

- [Speech and Language Processing, Chapter 6: Vector Semantics and Embeddings](https://web.stanford.edu/~jurafsky/slp3/6.pdf)
- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [GloVe: Global Vectors for Word Representation](https://aclanthology.org/D14-1162/)
- [Enriching Word Vectors with Subword Information](https://aclanthology.org/Q17-1010/)

## Resources

- [Gensim word-vector tutorial](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html)
- [TensorFlow Embedding Projector](https://projector.tensorflow.org/)

## Assignment

1. **Probe pretrained word embeddings.** Explore pretrained word embeddings in a notebook. Test nearest neighbors, analogies, rare words, and examples that reveal social or cultural bias.
2. **Classify with bag-of-embeddings.** Train a text classifier with a bag-of-embeddings representation. Compare it with bag-of-n-grams, especially with training sets of at most 500 examples.
3. * **Train corpus-specific word embeddings.** Train Word2Vec or fastText embeddings on your own corpus and evaluate them with intrinsic tests and one downstream task.

## Extra topics

- Cross-lingual word embedding alignment
- Debiasing static embeddings
- Diachronic embeddings for language change