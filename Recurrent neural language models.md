## Subtopics

- Recurrent computation and hidden state
- Elman recurrent neural networks
- Training through time
- Vanishing and exploding gradients
- Gradient clipping
- Long short-term memory (LSTM)
- Gated recurrent units (GRU)
- Stacked and bidirectional recurrent networks
- Simple recurrent unit variants
- Recurrent language-model training and generation

## Reading

- [Speech and Language Processing, Chapter 9: RNNs and LSTMs](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
- [Finding Structure in Time](https://crl.ucsd.edu/~elman/Papers/fsit.pdf)
- [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf)
- [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078)

## Resources

- [PyTorch sequence models tutorial](https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html)

## Assignment

1. Implement an Elman RNN language model and train it on a small corpus. Plot training and validation loss, apply gradient clipping, and generate samples.
2. Replace the recurrent cell with an LSTM or GRU. Compare perplexity, training speed, gradient behavior, and long-context predictions.
3. * Implement an LSTM cell from basic tensor operations and check its output against a framework implementation.

## Extra topics

- Recurrent highway networks
- Quasi-recurrent and simple recurrent units
- Recurrent models with external memory
