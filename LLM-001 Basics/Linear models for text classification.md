## Subtopics

- Bag-of-words and n-gram features
- Vocabulary construction and preprocessing
- Naive Bayes, logistic regression, and linear SVMs
- Regularization and feature selection
- F1, confusion matrices, and error analysis

## Reading

- [Speech and Language Processing, Chapter 4: Naive Bayes, Text Classification, and Sentiment](https://web.stanford.edu/~jurafsky/slp3/4.pdf)
- [Speech and Language Processing, Chapter 5: Logistic Regression](https://web.stanford.edu/~jurafsky/slp3/5.pdf)
- [scikit-learn: Working With Text Data](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

## Resources

- [scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)

## Assignment

1. **Compare linear text classifiers.** Train bag-of-words and bag-of-n-grams classifiers on a movie review dataset. Compare Naive Bayes, logistic regression, and a linear SVM with the same data split.
2. **Tune text classification features.** Study the effects of vocabulary size, maximum n-gram size, preprocessing, and regularization. Report F1 scores and analyze at least 20 errors.
3. * **Implement logistic regression manually.** Implement logistic regression and its gradient update without using a machine-learning model class.

## Extra topics

- Calibration of linear text classifiers
- Interpretable feature weights and dataset artifacts
- Linear classifiers for multilingual text