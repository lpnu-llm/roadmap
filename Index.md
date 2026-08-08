
# LLM-001: Basics

1. [[NLP intro and overview]]
2. [[Linear models for text classification]]
3. [[Tokenization]]
4. [[Word embeddings]]
5. Language modeling
  - Next-token prediction
  - Cross-entropy
  - Evaluation, perplexity
6. N-gram LMs
7. RNN LMs
	- Elman RNN
	- LSTM
	- Stacked and bi-directional LSTMs
	- GRU, SRN, SSRN and other cell variants
8. Sequence-to-sequence models
  - Machine translation
  - Attention
9. Transformer
10. Decoding and sampling
	* Greedy, beam search, temperature, top-k, top-p/nucleus sampling, constrained decoding, repetition penalty
11. Masked LMs
	- Encoder-only models, BERT
	- RoBERTa, ModernBERT, Ettin
	- Token classification, part of speech tagging
12. Training modern LLMs
	- Scaling laws
	- Corpus curation
	- Multi-stage training
	- Distributed training

# LLM-002: Architectures

1. Transformer
	1. Self-attention, multi-head attention, MLP blocks, layer norm, output heads
2. Modern Transformer
	1. Positional encodings and RoPE, activation functions, grouped-query attention, Mixture-of-experts
3. State-space models
	1. State-space models (Mamba), linear attention, hybrid architectures
4. Text diffusion models
	1. Discrete/masked diffusion
	2. Block diffusion, trade-offs
5. Evaluation of LLMs
	1. Perplexity, contamination, benchmarks, LLM-as-judge
6. Multimodal models intro
	1. Vision-language, speech, CLIP, LLaVA, Whisper

# LLM-003: Applications (prompt engineering)

1. Prompting techniques
	1. Zero-shot, few-shot, system prompt, prompt template, chain-of-thought reasoning
2. Retrieval-augmented generation
	1. Bi- and cross-encoders, contrastive embeddings, BM25, benchmarks
3. Agents
	1. tool calls, agent loops, skills
	2. memory, MCP, SWE agents, multi-agents
4. Hallucation
	1. Factuality, calibration, uncertainty estimation, mitigation
5. Multilinguality
	1. Multilingual pretraining and cross-lingual transfer, tokenizer fertility
6. Autoresearch
	1. agents for science

# LLM-004: Fine-tuning

1. Introduction and instruction tuning 
2. Continual pretraining 
3. Soft prompts
4. LoRA
5. QLoRa
6. data curation, synthetic data
7. Distillation
8. [[Preference Optimization]]
9. RLHF
10. RLVR, GRPO, RLAIF
11. RL-trained reasoning models
12. Process vs. outcome reward, best-of-n, titans
13. Optimizers, warmup, instability, loss curves, scaling laws
14. Corpus construction: filtering, deduplication, synthetic data
15. End? everything together

# LLM-005: Systems

1. GPU and compute
	1. Memory hierarchy, bandwidth, arithmetic intensity, mixed precision, gradient checkpointing
2. CUDA/Triton
	1. blocks, warps, shared memory, fusion
	2. IO-aware attention (FlashAttention)
3. Quantization
4. Serving and inference optimization
	1. Quantization, KV-cache, paged attention, continuous batching
5. Speculative decoding
	1. Speculative decoding, MEDUSA, EAGLE
6. Long context
	1. RoPE, ALiBI, “Lost in the middle"
7. LLM Ops
	1. Observability, lineage tracking

# LLM-006: Multimodal models

TODO

# LLM-007: Ethics and legal

1. Interpretability
	1. Probing, logits and attention analysis
	2. Mechanistic interpretability, circuits, superposition, sparse autoencoders
2. Safety
	1. jailbreaks, prompt injections, data poisioning, red teaming
3. Privacy
	1. PII scrambling
	2. Machine unlearning
4. Bias and fairness
5. Legal issues
	1. Licensing