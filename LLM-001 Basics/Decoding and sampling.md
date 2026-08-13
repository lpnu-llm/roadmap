## Subtopics

- Autoregressive generation loops
- Greedy and beam-search decoding
- Temperature, top-k, and nucleus sampling
- Repetition and stopping constraints
- Degeneration and diversity-quality trade-offs

## Reading

- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751)
- [Hugging Face: Generation Strategies](https://huggingface.co/docs/transformers/generation_strategies)

## Resources

- [Hugging Face generation configuration](https://huggingface.co/docs/transformers/main_classes/text_generation)

## Assignment

1. **Implement core decoding strategies.** Implement greedy decoding, temperature sampling, top-k sampling, and top-p sampling over model logits. Verify edge cases with tests.
2. **Compare decoding parameter tradeoffs.** Sweep decoding parameters for one language model and a fixed prompt set. Compare repetition, diversity, output length, runtime, and task success; include qualitative examples.
3. * **Build constrained beam search.** Implement beam search with length normalization and constrained decoding for a structured-output task.

## Extra topics

- Typical and contrastive decoding
- Speculative decoding
- Watermarking generated text
- Search methods for reasoning models
