---
weeks: 3
---

## Subtopics

- Goals and limits of interpretability: explanation, prediction, debugging, auditing, and scientific understanding
- Behavioral tests and attribution methods: feature visualization, saliency, gradients, integrated gradients, and causal interventions
- Probing classifiers: control tasks, selectivity, representation quality, and the difference between correlation and use
- Logit lens and tuned lens: reading intermediate predictions and recognizing layer-normalization and basis-alignment limits
- Attention analysis: attention patterns, attention rollout, head ablation, and why attention alone is not an explanation
- Mechanistic interpretability: circuits, induction heads, activation patching, path patching, and causal tracing
- Polysemantic neurons, superposition, sparse autoencoders, feature steering, and feature evaluation
- Scaling interpretability methods from small models to large models
- Reproducibility, cherry-picking, human interpretation bias, and honest reporting of negative results

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

1. Choose a small open transformer and one linguistic or factual feature. Collect positive examples, negative examples, and matched controls. Train a linear probe on activations from several layers. Report accuracy, a selectivity or control-task result, dataset limitations, and why probe success does not prove that the model uses the feature.
2. Use the logit lens and attention visualization on at least 20 prompts with a clear expected continuation. Compare two layers and two attention heads. Then ablate or patch one selected head or activation. Present before-and-after outputs and separate descriptive observations from causal evidence.
3. Reproduce one small circuit result, such as an induction-head pattern, with TransformerLens or equivalent hooks. Define a quantitative metric, run at least one causal intervention and one negative control, save the code and random seeds, and write a short failure analysis.
4. * Train or use a sparse autoencoder on one layer of a small model. Evaluate at least five learned features with activating examples, intervention tests, and counterexamples. Discuss reconstruction error, sparsity, feature splitting, and feature mixing.

## Extra topics

- Presentation: compare probing, attribution, and mechanistic interpretability by the claims each method can support
- Presentation: explain one published circuit and identify its strongest causal evidence
- Research: test whether an interpretability result transfers across model sizes or model families
- Research: design an evaluation for sparse-autoencoder feature quality that is harder to game than top-activating examples
