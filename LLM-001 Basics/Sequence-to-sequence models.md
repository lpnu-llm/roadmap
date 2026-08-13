---
weeks: 2
---

## Subtopics

- Conditional encoder-decoder generation
- Teacher forcing and exposure bias
- Attention, masking, and alignment
- Greedy and beam-search decoding
- BLEU, copying, and coverage

## Reading

- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
- [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078)
- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)
- [Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/abs/1508.04025)

## Resources

- [PyTorch translation with attention tutorial](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
- [SacreBLEU](https://github.com/mjpost/sacrebleu)

## Assignment

1. **Train an RNN encoder-decoder.** Implement and train an RNN encoder-decoder for a small translation or transliteration task. Use teacher forcing, masks, validation loss, and reproducible data splits.
2. **Add attention and beam search.** Add an attention mechanism and beam search. Compare the non-attentive and attentive models with BLEU or character error rate, speed, and qualitative error analysis. Visualize several attention alignments.
3. * **Implement copy or coverage.** Add a copy or coverage mechanism and evaluate it on rare words, names, or long inputs.

## Extra topics

- Monotonic attention for streaming tasks
- Unsupervised and low-resource machine translation
- Sequence-to-sequence models for speech recognition
- Alternatives to teacher forcing
