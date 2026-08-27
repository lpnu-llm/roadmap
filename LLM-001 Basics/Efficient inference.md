## Subtopics

- Prefill and autoregressive decoding
- Latency, throughput, and time to first token
- Model weights, activations, and KV-cache memory
- Batching and continuous batching
- Weight quantization and quality trade-offs
- Prefix caching and speculative decoding
- Local inference and model serving

## Reading

- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

## Resources

- [vLLM documentation](https://docs.vllm.ai/)
- [Hugging Face quantization overview](https://huggingface.co/docs/transformers/main/en/quantization/overview)

## Assignment

1. **Profile autoregressive model inference.** Run a small open model with several prompt and output lengths. Measure time to first token, time per output token, throughput, and peak memory, then explain the difference between prefill and decoding.
2. **Compare full and quantized inference.** Run the same model in its default precision and in a quantized configuration. Compare memory, latency, throughput, and output quality on a fixed evaluation set.


## Extra topics

- FlashAttention and fused kernels
- PagedAttention and KV-cache eviction
- Tensor and pipeline parallel inference
