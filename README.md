![AgentR Awesome RSI](assets/banner.jpg)

# Awesome RSI ![Awesome](https://awesome.re/badge-flat.svg)

An [AgentR](https://agentr.dev) index of **recursive self-improvement**: systems that change a persistent part of themselves and reuse that change in later improvement.

RSI is stronger than revising one answer. The improved object — code, harness, weights, memory, or evaluator — must participate in the next round. Entries here are 2025–present and are the closest empirical or formal work on that loop. None of them establishes unbounded autonomous RSI.

## Contents

- [Papers](#papers)
- [Contributing](#contributing)

## Papers

First public version, usually the first arXiv posting. Source type is not a peer-review claim.

### [ScienceBuddy](https://arxiv.org/abs/2609.17523) — Gen-Verse
*2026-09 · Preprint*

`Scientific & Algorithmic Discovery` `Self-Evolving Agents`

> **Abstract:** Addresses joint improvement of scientific-agent scaffolds and model weights. An inner loop evolves the executable harness while an outer loop updates the policy with reinforcement learning, so each surface supplies training signal for the other. Reports gains on scientific-agent tasks under a fixed alternating protocol.

### [MetaRSI / RSI²](https://arxiv.org/abs/2609.06396) — Authors
*2026-09 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Treats recursive self-improvement as a composition of data, harness, and model operators. A learned meta-policy proposes how those operators are scheduled across rounds rather than running a single fixed recipe. Experiments stay inside a human-specified operator vocabulary.

### [HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution](https://arxiv.org/abs/2609.00829) — Huawei
*2026-09 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Studies harness edits that overfit or forget. Failed runs are aligned to verified reference trajectories to localize errors; candidate harness updates pass quality and held-out performance gates before promotion. Reports more stable harness evolution than unguarded self-edits across several agent benchmarks.

### [WHALE](https://arxiv.org/abs/2609.00196) — KRAFTON
*2026-09 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Asks whether harness search and weight updates can train each other. The method alternates model-parameter training with executable harness search so improvements on one surface become data for the other. Official code is released; the outer alternating schedule remains fixed.

### [Generalized Agent Iteration](https://arxiv.org/abs/2609.13406) — Authors
*2026-09 · Preprint*

`Self-Evolving Agents`

> **Abstract:** Places ordinary policy iteration and recursive self-improvement in one formal frame. Two axes matter: whether the improving mechanism sits inside the agent, and whether evaluation stays externally grounded. The paper is a unifying formalism, not an implemented self-improving agent.

### [Dream-RSI](https://dream-rsi.com/assets/dream-rsi.pdf) — Google / UMD
*2026-09-11 · Preprint*

`Scientific & Algorithmic Discovery` `Self-Evolving Agents`

> **Abstract:** Targets the exploration policy around a fixed coding agent rather than the agent’s full source. Recorded discovery trees become replay worlds in which alternative exploration-policy code is scored and then redeployed on new searches. Evaluated on algorithm engineering, optimization, and GPU kernels; implementation was announced as forthcoming.

### [Recuris: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876) — National University of Singapore
*2026-08-25 · Preprint*

`Self-Evolving Agents` `Memory & Experience`

> **Abstract:** Addresses long-horizon failure from bloated history and misaligned skills. Working memory tracks task state and selects skills from experiential memory; a fixed meta-agent then applies validation-gated updates to skill memory from localized failures. Reports task-success gains on four long-horizon benchmarks across multiple models.

### [Metaⁿ](https://arxiv.org/abs/2608.24735) — Minnesota NLP
*2026-08-25 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Recurses a fixed meta-operation over an evolving solver stack instead of searching a single scaffold once. Generated helpers and layer chains are archived and reused as later solvers. Official code is released; reported recursion acts on generated layers, not on the meta-operation or model weights.

### [HELIX](https://arxiv.org/abs/2608.13951) — HKU DS
*2026-08-14 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Splits agent systems into typed components and co-evolves harness and weights. Harness search produces verified trajectories that become training data for the next model update. Official code is released; reported experiments are on code-repair tasks with a bounded search budget.

### [Ouroboros](https://arxiv.org/abs/2608.08311) — razzant
*2026-08 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Makes the running agent the object of its own evolution. Reviewed commits to tools, prompts, context assembly, and core code become the next runtime and can schedule another cycle. Official code is released; promotion uses a separate-agent review and frozen benchmark snapshots.

### [Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution](https://arxiv.org/abs/2608.07645) — UESTC / LMU Munich
*2026-08 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Extends single-trajectory self-rewriting coding agents with comparative lineage operators. Reaction-norm mutation and cross-lineage hybridization use evidence from multiple tasks or another archive branch. Reports SWE-bench and Polyglot gains versus single-trajectory self-modification; fitness and backbone LLM remain designed and frozen.

### [DarwinX](https://arxiv.org/abs/2608.07545) — Salesforce
*2026-07-31 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Evolves agent harnesses while holding model weights fixed. A population of variants is edited, merged, and admitted only when task coverage grows without regression; an archive stores alternative lineages. Cross-benchmark transfer is reported; selection uses each benchmark’s own verifier.

### [OpenRSI / OpenMLE](https://arxiv.org/abs/2607.28568) — Frontis AI
*2026-07 · Preprint*

`Scientific & Algorithmic Discovery` `Self-Evolving Agents`

> **Abstract:** Builds an AI-for-AI stack of executable ML task environments, learned improvement operators, long-horizon program evolution, and held-out transfer tests. Search experience is written back into operator training. Official code is released; atomic operators and composition rules are human-designed.

### [RHI: Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524) — Sakana AI
*2026-07-17 · Preprint*

`Scientific & Algorithmic Discovery` `Self-Evolving Agents`

> **Abstract:** Treats the user-side harness as a prompt-level spec of the agent loop under model–harness co-evolution. The spec is refined from pairwise feedback on its own revision history. Reports ceiling gains on 30 synthetic ML research tasks with lower inference cost, attributed mainly to context-management changes.

### [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) — Authors
*2026-07 · Preprint*

`Self-Evolving Agents`

> **Abstract:** A taxonomy of self-improvement claims. It separates bounded refinement, persistent self-improvement, recursive improvement, and autonomous research loops, and reviews current systems against those grades. Secondary synthesis; not a primary experimental result.

### [The Red Queen Gödel Machine](https://arxiv.org/abs/2606.26294) — University of Cambridge
*2026-06 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Notes that most self-improving agents assume a stationary evaluator. Search is split into epochs with a fixed within-epoch utility; the evaluator or utility may change at epoch boundaries, including agent-as-a-judge and adversarial objectives. Reports coding, paper-writing, and grading experiments under co-evolving criteria.

### [Self-Harness](https://arxiv.org/abs/2606.09498) — Shanghai AI Laboratory
*2026-06 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Argues that harnesses should be model-specific. The agent mines its own failure traces, proposes minimal executable harness edits, and keeps them only after regression tests on Terminal-Bench, SWE-bench Verified, and AppWorld. Reports held-in and held-out pass-rate gains for three model families; the proposer and test suite stay fixed.

### [EvoTrainer](https://arxiv.org/abs/2606.03108) — Alibaba DAMO
*2026-06 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Co-evolves model policies and their training harnesses under executable feedback. Retained harness changes shape later training rounds rather than only the current run. Official code is released; co-evolution is shown inside designed training loops.

### [MOSS](https://arxiv.org/abs/2605.22794) — HKGAI
*2026-05 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Treats the running TypeScript agent as an editable artifact. Failures drive diagnosis, code edits, isolated replay, and container promotion with approval and rollback. Official code is released; reported results are a bounded repair cycle, not unrestricted deployment.

### [Continual Harness](https://arxiv.org/abs/2605.09998) — Prime Intellect
*2026-05-11 · Preprint*

`Self-Evolving Agents` `Memory & Experience`

> **Abstract:** Automates reset-free harness refinement for long-horizon embodied agents. The agent alternates acting with updates to prompts, subagents, skills, and memory; a separate experiment relabels rollouts with a teacher and updates an open model without resetting the environment. Official code is released; a co-learning setting uses teacher supervision.

### [Escher-Loop](https://arxiv.org/abs/2604.23472) — Shenzhen X-Institute
*2026-04 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Studies mutual evolution of task agents and optimizer agents. Newly generated task-agent scores supply win–loss signal for updating the optimizers, without a separate optimizer benchmark. Reports mathematical-optimization experiments in which optimizer strategy shifts with stronger task agents.

### [Hyperagents](https://arxiv.org/abs/2603.19461) — Meta
*2026-03-19 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Puts a task agent and a meta-agent in one editable program. Evaluated descendants can change both task behavior and the procedure that generates later agents. Official code is released; experiments cover coding, review, reward design, and grading under fixed outer selection rules.

### [Agent0](https://arxiv.org/abs/2511.16043) — Aiming Lab
*2025-11-20 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Couples a curriculum model with a tool-using executor so harder generated tasks become RL data as execution improves. Official code is released. Zero external data still depends on a pretrained backbone, tools, and manual checkpoint selection between iterations.

### [Huxley-Gödel Machine](https://arxiv.org/abs/2510.21614) — MetAuto
*2025-10-24 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Guides self-modifying coding-agent search with estimated lineage value rather than only current score. Descendant performance is used to choose which archive members to rewrite next. Official code is released; clade statistics are not proofs of globally optimal rewrites.

### [Statistical Gödel Machine](https://arxiv.org/abs/2510.10232) — Authors
*2025-10-11 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Replaces proof-gated Gödel-machine adoption with a statistical gate. Candidate edits are tested before adoption while cumulative false-acceptance risk is budgeted across rounds. Official code is released; guarantees assume bounded independent paired measurements and a stable evaluator.

### [SEAL: Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) — MIT
*2025-06-12 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Lets a language model generate self-edits — finetuning data or update directives — that produce persistent weight changes via SFT. An outer RL loop trains better self-edit generation from downstream performance of the updated model. Official code is released; adaptation stays inside a designed SFT/RL recipe.

### [The Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) — UBC / Sakana AI
*2025-05-29 · Preprint*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** An empirical coding-agent analogue of the Gödel machine. The agent modifies its own implementation, evaluates descendants on coding benchmarks, and branches from a growing archive. Official code is released. Reports SWE-bench 20.0% → 50.0% and Polyglot 14.2% → 30.7% under sandboxing; foundation-model weights stay frozen.

### [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) — Tsinghua LeapLab
*2025-05-06 · Preprint*

`Self-Evolving Agents` `Self-Training`

> **Abstract:** Removes curated post-training datasets from a proposer–solver loop. A model proposes tasks and solves them, with a code executor supplying validity and answer rewards. Official code is released. “Zero data” refers to the self-play post-training setup, not an untrained backbone.

### [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) — Maxime Robeyns et al.
*2025-04-21 · Workshop paper*

`Self-Evolving Agents` `Self-Modification`

> **Abstract:** Closes a keep-or-revert loop on the agent’s own repository. The coding agent is evaluated, then run on its codebase to implement an improvement, then evaluated again. Official code is released; LLM weights are fixed and reported gains use sampled coding-benchmark subsets.

## Contributing

This list is an [AgentR](https://agentr.dev) research index. Edit `README.md` directly. Read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

Keep the set small: 2025 or later, at most about 30 papers, and only work whose persistent object is reused in a later improvement round.
