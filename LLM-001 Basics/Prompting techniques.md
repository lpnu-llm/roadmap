## Subtopics

- Instructions, roles, messages, and chat templates
- Zero-shot and few-shot prompting
- Demonstration choice and ordering
- Decomposition and reasoning prompts
- Structured outputs and schema validation
- Prompt sensitivity, injection, and reproducible evaluation

## Reading

- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608)

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Hugging Face chat templates](https://huggingface.co/docs/transformers/chat_templating)

## Assignment

1. **Compare basic prompting strategies.** Create zero-shot and few-shot prompts for classification, extraction, and generation tasks. Evaluate them on fixed examples and report task quality, format validity, token use, and recurring failures.
2. **Build validated structured output.** Prompt a model to extract records that follow a given schema. Validate the outputs, retry invalid responses with a fixed policy, and measure both semantic accuracy and schema validity.
3. * **Measure prompt order sensitivity.** Permute the order and wording of few-shot demonstrations while keeping the test set fixed. Report the variance and identify examples that consistently help or hurt.

## Extra topics

- Prompt compression and context selection
- Multilingual prompt sensitivity
- System prompt extraction and indirect prompt injection
