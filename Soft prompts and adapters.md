## Subtopics

- Parameter-efficient fine-tuning
- Soft prompts and prefix tuning
- Bottleneck adapters
- Parameter, memory, and quality trade-offs
- Adapter composition and multitask serving

## Reading

- [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)
- [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751)

## Resources

- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/)

## Assignment

1. **Compare prompts and adapters.** Fine-tune the same small model with a soft prompt and an adapter on one task. Compare quality, trainable parameters, peak memory, training time, and checkpoint size.
2. * **Test multi-adapter task switching.** Compose or route two task-specific adapters in one base model and test whether task switching causes interference.

## Extra topics

- Present prefix tuning and P-tuning v2.
- Research methods for selecting adapter placement and bottleneck size.
- Study adapter fusion and multilingual adapter composition.
