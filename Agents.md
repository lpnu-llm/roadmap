---
weeks: 4
---

## Subtopics

- Tool calling
- Agent loops and recovery
- Memory and skills
- Model Context Protocol
- Browser and coding agents
- Multi-agent collaboration
- Safety and reliability evaluation

## Reading

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
- [GAIA: A Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)

## Resources

- [Berkeley Large Language Model Agents course](https://rdi.berkeley.edu/llm-agents/f24)
- [Berkeley Advanced Large Language Model Agents course](https://rdi.berkeley.edu/adv-llm-agents/sp25)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [AgentBench](https://arxiv.org/abs/2308.03688)

## Assignment

1. **Build a resilient tool caller.** Build a tool-calling assistant with at least three typed tools, including one tool that can fail. Validate arguments, handle tool errors, set stopping conditions, and compare it with a prompt-only baseline.
2. **Evaluate a bounded agent loop.** Implement an agent loop with planning, execution traces, and bounded retries. Evaluate it on a fixed set of multi-step tasks and classify failures in planning, tool selection, execution, and verification.
3. **Compare agent memory strategies.** Add memory to the agent and compare no memory, summary memory, and retrieval memory. Measure task success, token cost, stale-memory errors, and information leakage across sessions.
4. **Audit a practical agent.** Build a repository or browser agent and evaluate it with task success, runtime, cost, and a human-preference rubric. Include logs that make every action auditable and test at least one safety boundary.
5. * **Test multi-agent collaboration.** Implement two collaborating agents with different roles. Compare them with a single agent under the same model and token budget, and analyze coordination failures rather than reporting only average quality.

## Extra topics

- Research and present agent skills as versioned software components.
- Research and present MCP security and trust boundaries.
- Research and present computer-use agents and visual grounding.
- Research and present methods for evaluating long-horizon agents.
