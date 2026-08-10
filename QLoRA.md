## Subtopics

- Quantized-base LoRA fine-tuning
- NF4 and double quantization
- Paged optimizers
- Compute and quantization dtypes
- VRAM–quality trade-offs

## Reading

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

## Resources

- [Hugging Face bitsandbytes quantization guide](https://huggingface.co/docs/transformers/quantization/bitsandbytes)

## Assignment

1. **Compare LoRA and QLoRA.** Fine-tune one model with LoRA in full or half precision and with QLoRA in 4-bit precision. Use the same data and settings, then compare peak VRAM, throughput, quality, and failure cases.
2. * **Measure layerwise quantization error.** Test NF4 against another 4-bit quantization choice and measure how quantization error changes by layer before and after training.

## Extra topics

- Present NF4 and double quantization with a small numerical example.
- Research LoftQ, QALoRA, and other quantization-aware PEFT methods.
- Study when QLoRA becomes slower than higher-precision LoRA.
