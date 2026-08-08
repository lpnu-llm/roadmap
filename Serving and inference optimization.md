---
weeks: 4
---

## Subtopics

- Inference workload phases: prefill and autoregressive decode
- Service metrics: time to first token, time per output token, end-to-end latency, throughput, and tail latency
- Realistic workload design: prompt lengths, output lengths, arrival rates, and concurrency
- Model memory, activation memory, and KV-cache memory
- Weight and activation quantization; calibration and quality checks
- Static batching, dynamic batching, and continuous batching
- KV-cache allocation, PagedAttention, prefix caching, and cache eviction
- Request scheduling, fairness, admission control, and overload behavior
- Tensor, pipeline, and data parallelism for inference
- Speculative decoding, draft-model selection, and acceptance rate
- Production serving engines and OpenAI-compatible APIs
- Capacity planning and cost per generated token

## Reading

- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102)
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104)

## Resources

- [vLLM documentation](https://docs.vllm.ai/)
- [vLLM production metrics](https://docs.vllm.ai/en/stable/usage/metrics/)
- [Hugging Face Transformers quantization overview](https://huggingface.co/docs/transformers/main/en/quantization/overview)
- [NVIDIA GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html)

## Assignment

1. Build a reproducible benchmark for one open model and serving engine. Generate workloads with at least three prompt-length distributions, three output lengths, and several concurrency levels. Report time to first token, time per output token, p50 and p95 end-to-end latency, output-token throughput, peak memory, and errors.
2. Serve the same model in full precision and in at least two quantized configurations. Measure model size, GPU memory, throughput, and latency, and evaluate output quality on a fixed task set. Identify the quality-performance trade-off and any operators that remain unquantized.
3. Compare a simple request-at-a-time server with continuous batching and PagedAttention. Add one repeated-prefix workload to test prefix caching. Plot latency and throughput against offered load, inspect KV-cache use and queue length, and explain the saturation point and tail-latency behavior.
4. Add speculative decoding with a smaller draft model. Measure acceptance rate, target-model calls, latency, and throughput on at least two text domains and several draft lengths. Find the break-even workload and verify that the output distribution or task quality remains acceptable.
5. * Write a capacity plan for a service with a stated traffic profile and latency objective. Select hardware, replicas, quantization, batching limits, and an overload policy; estimate monthly cost and support each choice with benchmark data.

## Extra topics

- Disaggregated prefill and decode
- Multi-LoRA serving and adapter scheduling
- Cache-aware routing across replicas
- Fair scheduling for short and long requests
- Energy use and cost per useful output token
- Presentation: compare the architecture of vLLM, SGLang, TensorRT-LLM, and TGI
- Research: learned draft models such as Medusa and EAGLE
