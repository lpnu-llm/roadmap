---
weeks: 3
---

## Subtopics

- CUDA grids, blocks, warps, and SMs
- GPU memory hierarchy and coalesced access
- Bank conflicts, synchronization, divergence, and occupancy
- Tiling and data reuse
- Launch overhead and kernel fusion
- Triton programming, autotuning, and correctness
- IO-aware attention and FlashAttention
- Kernel profiling and bottleneck analysis

## Reading

- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/)
- [Triton fused softmax tutorial](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)
- [Triton matrix multiplication tutorial](https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html)
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)

## Resources

- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- [Nsight Compute documentation](https://docs.nvidia.com/nsight-compute/)
- [Triton language reference](https://triton-lang.org/main/python-api/triton.language.html)
- [Triton fused attention tutorial](https://triton-lang.org/main/getting-started/tutorials/06-fused-attention.html)

## Assignment

1. **Optimize CUDA vector reduction.** Write CUDA kernels for a vector reduction in two versions: a simple global-memory version and a tiled shared-memory version. Test non-power-of-two input sizes, verify results against PyTorch, and use a profiler to compare memory access, synchronization, occupancy, and runtime.
2. **Implement fused Triton softmax.** Implement numerically stable fused softmax in Triton. Support masked rows and several non-power-of-two widths. Check outputs and gradients against PyTorch, then benchmark multiple shapes and explain when fusion helps and when it does not.
3. **Autotune Triton matrix multiplication.** Implement and autotune a blocked Triton matrix multiplication with a fused activation. Compare correctness and performance with PyTorch across shapes that include small, large, aligned, and unaligned dimensions. Use profiler data to explain the effect of block sizes, warps, and memory reuse.
4. * **Analyze FlashAttention IO savings.** Reproduce a small IO analysis of standard attention and FlashAttention. Measure runtime and peak memory over increasing sequence lengths, estimate high-bandwidth-memory reads and writes, and relate the measurements to the paper's IO-aware algorithm.

## Extra topics

- Read and present one optimized kernel from FlashAttention or a production inference engine
- Tensor Core instructions and asynchronous memory copies
- Persistent kernels and grouped matrix multiplication
- CUDA graphs and kernel launch overhead
- Compiler-generated kernels with `torch.compile`
- Portability of Triton kernels across NVIDIA and AMD GPUs
