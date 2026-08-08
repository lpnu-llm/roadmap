---
weeks: 3
---

## Subtopics

- GPU architecture: streaming multiprocessors, CUDA cores, Tensor Cores, and parallel execution
- Memory hierarchy: registers, shared memory, caches, and high-bandwidth device memory
- Memory capacity, memory bandwidth, and compute throughput
- Arithmetic intensity and roofline analysis
- Transformer resource accounting: parameters, gradients, optimizer states, activations, and temporary buffers
- Numerical formats: FP32, TF32, FP16, BF16, FP8, and accumulation precision
- Mixed-precision training and loss scaling
- Activation checkpointing as a compute-memory trade-off
- Reliable benchmarking: warm-up, synchronization, repeated runs, and hardware utilization
- Profiling GPU time and peak memory use

## Reading

- [GPU Performance Background User's Guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html)
- [Matrix Multiplication Background User's Guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/index.html)
- [Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html)
- [How to Scale Your Model](https://jax-ml.github.io/scaling-book/)
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)

## Resources

- [PyTorch automatic mixed precision recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)
- [PyTorch activation checkpointing documentation](https://docs.pytorch.org/docs/stable/checkpoint.html)
- [PyTorch CUDA memory snapshots](https://docs.pytorch.org/docs/stable/torch_cuda_memory.html)
- [NVIDIA Nsight Compute profiling guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/)

## Assignment

1. Make a resource-accounting tool for a transformer layer and a complete decoder-only model. Given model dimensions, sequence length, batch size, optimizer, and numeric format, report parameter, gradient, optimizer-state, activation, and KV memory, plus forward-pass FLOPs. Validate at least three estimates with measurements from a framework profiler and explain the remaining error.
2. Benchmark matrix multiplications across at least six shapes and three numeric formats. Use warm-up runs and GPU synchronization, calculate achieved FLOPs and arithmetic intensity, and compare the results with the GPU's bandwidth and peak compute roofline. Explain which cases are memory-bound or compute-bound.
3. Train the same small transformer with FP32, mixed precision, and mixed precision plus activation checkpointing. Compare peak GPU memory, examples or tokens per second, wall-clock time, and final loss. Check gradients for non-finite values and explain the speed, memory, and numerical trade-offs.
4. * Profile one transformer block with Nsight Compute. Identify its three most expensive kernels, inspect memory traffic and Tensor Core use, and propose one optimization supported by profiler evidence.

## Extra topics

- Compare the memory systems and low-precision support of two recent GPU architectures
- Energy use and useful tokens per joule
- Unified memory, CPU offload, and memory oversubscription
- Reproducible GPU benchmarking under clock and thermal variation
- Presentation: why peak FLOPs alone do not predict LLM performance
