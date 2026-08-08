---
weeks: 3
---

## Subtopics

- Zero-shot and few-shot prompting
- System prompts, roles, instructions, and prompt templates
- Choosing and ordering demonstrations
- Chain-of-thought, decomposition, and self-verification
- Structured outputs and constrained generation
- Prompt sensitivity, robustness, and evaluation

## Reading

- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Efficient Guided Generation for Large Language Models](https://arxiv.org/abs/2307.09702)

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Outlines: structured text generation](https://github.com/dottxt-ai/outlines)

## Assignment

1. Design zero-shot, few-shot, and instruction-based prompts for three different tasks. Use a fixed test set and report accuracy, output validity, token use, and common failure types.
2. Measure sensitivity to demonstration choice and order. Run several prompt permutations, summarize the variance, and explain which examples help or hurt performance.
3. Compare direct answers, chain-of-thought prompting, and decomposition on a reasoning task. Add a structured output schema and measure both task accuracy and schema validity.
4. * Build a small automatic prompt search method, compare it with a manually designed prompt under the same evaluation budget, and analyze overfitting to the development set.

## Extra topics

- Research and present prompt compression methods.
- Research and present how prompt injection changes prompt design for untrusted input.
- Research and present multilingual prompt sensitivity.
