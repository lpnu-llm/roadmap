---
weeks: 3
---

## Subtopics

- Interpretability goals: explanation, debugging, auditing, and scientific understanding
- Behavioral tests, attribution methods, and causal interventions
- Probing classifiers: controls, selectivity, and representation quality
- Logit and tuned lenses: intermediate predictions and alignment limits
- Attention analysis, rollout, visualization, and head ablation
- Mechanistic interpretability: circuits, activation patching, and causal tracing
- Superposition, sparse autoencoders, feature steering, and feature evaluation
- Scaling, reproducibility, cherry-picking, and human interpretation bias

## Reading

- Elhage et al., [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
- Bricken et al., [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
- Anthropic, [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- Belinkov, [Probing Classifiers: Promises, Shortcomings, and Advances](https://direct.mit.edu/coli/article/48/1/207/106780/Probing-Classifiers-Promises-Shortcomings-and)
- Nanda and Bloom, [Transformers Interpretability](https://arxiv.org/abs/2306.17844)

## Resources

- [ARENA mechanistic interpretability curriculum](https://arena-chapter1-transformer-interp.streamlit.app/)
- [TransformerLens documentation](https://transformerlensorg.github.io/TransformerLens/)
- [Captum model interpretability library](https://captum.ai/)

## Assignment

1. **Probe Linguistic or Factual Features.** Choose a small open transformer and one linguistic or factual feature. Collect positive examples, negative examples, and matched controls. Train a linear probe on activations from several layers. Report accuracy, a selectivity or control-task result, dataset limitations, and why probe success does not prove that the model uses the feature.
2. **Test Attention Causally.** Use the logit lens and attention visualization on at least 20 prompts with a clear expected continuation. Compare two layers and two attention heads. Then ablate or patch one selected head or activation. Present before-and-after outputs and separate descriptive observations from causal evidence.
3. **Reproduce a Transformer Circuit.** Reproduce one small circuit result, such as an induction-head pattern, with TransformerLens or equivalent hooks. Define a quantitative metric, run at least one causal intervention and one negative control, save the code and random seeds, and write a short failure analysis.
4. * **Evaluate Sparse Autoencoder Features.** Train or use a sparse autoencoder on one layer of a small model. Evaluate at least five learned features with activating examples, intervention tests, and counterexamples. Discuss reconstruction error, sparsity, feature splitting, and feature mixing.

## Extra topics

- Presentation: compare probing, attribution, and mechanistic interpretability by the claims each method can support
- Presentation: explain one published circuit and identify its strongest causal evidence
- Research: test whether an interpretability result transfers across model sizes or model families
- Research: design an evaluation for sparse-autoencoder feature quality that is harder to game than top-activating examples
