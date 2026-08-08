---
weeks: 2
---

## Subtopics

- Autoregressive and diffusion-based language generation
- Discrete diffusion and masked diffusion objectives
- Forward corruption and reverse denoising processes
- Noise schedules and timestep sampling
- Parallel token prediction and iterative refinement
- Confidence-based and entropy-based token unmasking
- Text infilling, editing, and controllable generation
- Block diffusion and mixed autoregressive-diffusion models
- Speed, quality, diversity, and latency trade-offs
- Current systems including LLaDA, Mercury, and Gemini Diffusion

## Reading

- [Large Language Diffusion Models (LLaDA)](https://arxiv.org/abs/2502.09992)
- [Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524)
- [Mercury: Ultra-Fast Language Models Based on Diffusion](https://arxiv.org/abs/2506.17298)
- [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://arxiv.org/abs/2503.09573)

## Resources

- [LLaDA implementation](https://github.com/ML-GSAI/LLaDA)
- [Masked Diffusion Language Models implementation](https://github.com/ML-GSAI/MDLM)

## Assignment

1. Implement and train a tiny masked-diffusion language model and a matched autoregressive baseline on the same corpus. Compare validation loss, sample quality, generation speed, and infilling ability.
2. Implement at least three denoising schedules, such as random, confidence-based, and fixed left-to-right unmasking. Compare quality and latency across different numbers of denoising steps, and analyze common failure cases.
3. * Implement a small block-diffusion decoder. Vary the block size and explain how it changes parallelism, KV-cache reuse, generation quality, and time to first token.

## Extra topics

- Student presentation: LLaDA and masked diffusion scaling
- Student presentation: Mercury and low-latency diffusion decoding
- Student presentation: Gemini Diffusion and bidirectional generation
- Student presentation: diffusion models for text editing and constrained generation
