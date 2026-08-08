## Subtopics

- Fine-tuning through a quantized frozen base model
- 4-bit NormalFloat (NF4) and double quantization
- Paged optimizers and memory spikes
- Compute dtype and quantization dtype
- VRAM, speed, stability, and quality trade-offs
- Saving, loading, and merging quantized adapters

## Reading

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

## Resources

- [Hugging Face bitsandbytes quantization guide](https://huggingface.co/docs/transformers/quantization/bitsandbytes)

## Assignment

1. Fine-tune one model with LoRA in full or half precision and with QLoRA in 4-bit precision. Use the same data and settings, then compare peak VRAM, throughput, quality, and failure cases.
2. * Test NF4 against another 4-bit quantization choice and measure how quantization error changes by layer before and after training.

## Extra topics

- Present NF4 and double quantization with a small numerical example.
- Research LoftQ, QALoRA, and other quantization-aware PEFT methods.
- Study when QLoRA becomes slower than higher-precision LoRA.
