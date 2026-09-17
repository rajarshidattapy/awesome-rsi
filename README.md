<div align="center">

<a href="https://agentr.dev">
  <img src="assets/banner.jpg" alt="AgentR Awesome RSI — a research initiative" width="100%">
</a>

[![AgentR](https://img.shields.io/badge/agentr-research-e75b31?style=flat-square&labelColor=090b0a)](https://agentr.dev)
[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
[![Notes](https://img.shields.io/badge/notes-d5df72?style=flat-square&labelColor=090b0a)](https://agentr.dev/blog)
[![GitHub](https://img.shields.io/badge/github-agentrhq-f3eedf?style=flat-square&labelColor=090b0a)](https://github.com/agentrhq)

</div>

# Awesome RSI

An [AgentR](https://agentr.dev) research index of recursive self-improvement.

We study how autonomous systems turn interaction into self-learning: forming working hypotheses, testing them through action, and carrying forward what the evidence can support. This list maps the papers, systems, and measurements of that loop — **act → observe → test → revise → transfer**.

> [!IMPORTANT]
> **RSI is stronger than ordinary iteration.** This list distinguishes systems that improve a persistent part of themselves from systems that merely revise one answer. A recursive system must also improve, or repeatedly reuse, the mechanism that produces later improvements. Most current systems are bounded or partial RSI — not open-ended intelligence explosions.

## Start Here

| Reading path | What to look for |
| --- | --- |
| [Self-modifying agents](#papers--harness) | Does the revised agent participate in its next improvement? |
| [Iterative self-training](#papers--models) | Do updated models generate the next training data, curriculum or rewards? |
| [Experience, memory and skills](#papers--experience) | Does retained state change later tasks, or only the current attempt? |
| [Theory and evaluation](#papers--theory-and-evaluation) | Which assumptions and measurements support the loop? |
| [Benchmarks](#benchmarks) | Is improvement measured across generations, not a single task score? |

**Reading the evidence:** self-modification, bounded self-training and theoretical proposals are different claims. Tags name the surface (`Harness`, `Models`, `Artifacts`) and the mechanism (**Self-modification**, **Self-training**, **Bounded optimization**, **Experience learning**, **Evaluation / safety**, **Research agenda**). No tag proves unbounded autonomous RSI.

## Contents

- [Category Overview](#category-overview)
- [Company Research Blogs](#company-research-blogs)
  - [Mechanisms and Results](#mechanisms-and-results)
  - [AI Research and Supporting Methods](#ai-research-and-supporting-methods)
  - [Evaluation and Failure Modes](#evaluation-and-failure-modes)
  - [Research Agendas](#research-agendas)
  - [Foundations and Historical Tutorials](#foundations-and-historical-tutorials)
  - [Engineering Reports](#engineering-reports)
- [Papers and Official Code](#papers-and-official-code)
  - [Papers / Harness](#papers--harness)
  - [Papers / Models](#papers--models)
  - [Papers / Experience](#papers--experience)
  - [Papers / Theory and Evaluation](#papers--theory-and-evaluation)
  - [Surveys and Taxonomies](#surveys-and-taxonomies)
  - [Foundations](#foundations)
- [Benchmarks](#benchmarks)
- [Safety, Limits, and Governance](#safety-limits-and-governance)
- [Active GitHub Projects](#active-github-projects)
  - [GitHub / Models](#github--models)
  - [GitHub / Harness](#github--harness)
  - [GitHub / Artifacts](#github--artifacts)
- [Workshops and Related Collections](#workshops-and-related-collections)
- [Scope and Curation](#scope-and-curation)
- [AgentR](#agentr)
- [Contributing](#contributing)

## Category Overview

| Category | Resource | Entries |
| --- | --- | ---: |
| [Mechanisms and Results](#mechanisms-and-results) | Blog | 6 |
| [AI Research and Supporting Methods](#ai-research-and-supporting-methods) | Blog | 15 |
| [Evaluation and Failure Modes](#evaluation-and-failure-modes) | Blog | 4 |
| [Research Agendas](#research-agendas) | Blog | 2 |
| [Foundations and Historical Tutorials](#foundations-and-historical-tutorials) | Blog | 4 |
| [Engineering Reports](#engineering-reports) | Blog | 4 |
| [Papers / Harness](#papers--harness) | Paper | 34 |
| [Papers / Models](#papers--models) | Paper | 31 |
| [Papers / Experience](#papers--experience) | Paper | 24 |
| [Papers / Theory and Evaluation](#papers--theory-and-evaluation) | Paper | 10 |
| [Surveys and Taxonomies](#surveys-and-taxonomies) | Paper | 14 |
| [Foundations](#foundations) | Paper | 12 |
| [Benchmarks](#benchmarks) | Paper / project | 40 |
| [Safety, Limits, and Governance](#safety-limits-and-governance) | Paper | 8 |
| [GitHub / Models](#github--models) | GitHub project | 4 |
| [GitHub / Harness](#github--harness) | GitHub project | 16 |
| [GitHub / Artifacts](#github--artifacts) | GitHub project | 8 |
| **Total** |  | **236** |

Counts refer to resources, not independent breakthroughs: a blog, paper and repository may describe the same work.

## Company Research Blogs

Start here: first-party technical accounts from model builders and specialist AI research labs. Mechanisms, failures, agendas and historical foundations are separated; publisher claims are not independent replications.

### Mechanisms and Results

- **[The Darwin Godel Machine: AI that improves itself by rewriting its own code](https://sakana.ai/dgm/)** — Sakana AI · 2025-05-30
  - `Harness` · **Self-modification** — Describes an agent that rewrites its tools and workflows, evaluates descendants on coding benchmarks, and branches from a growing archive to improve again.
  - **Boundary:** Foundation-model training is future work; the article documents reward hacking and supervised sandbox limits.

- **[Kimi K2: Open Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2)** — Moonshot AI / Kimi · 2025-07-11
  - `Models` · **Self-training** — Its general RL system uses the model as its own rubric-based critic, continuously updating that critic from on-policy rollouts with verifiable rewards to improve evaluation of non-verifiable tasks.
  - **Boundary:** The critic and policy improve within a designed RL setup; the article does not establish autonomous rewriting of the learning algorithm.

- **[SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)** — Google DeepMind · 2025-11-13
  - `Models` · **Self-training** — Gemini supplies tasks and estimated rewards; SIMA 2 accumulates self-generated experience and trains subsequent agent generations, including in new game and Genie environments.
  - **Boundary:** Initial training uses human demonstrations and later rewards rely on Gemini; the research preview is not unconstrained self-improvement of Gemini itself.

- **[MiniMax M2.7: Early Echoes of Self-Evolution](https://www.minimax.io/news/minimax-m27-en)** — MiniMax · 2026-03-18
  - `Harness` · **Self-modification** — Reports more than 100 autonomous rounds of failure-trajectory analysis, scaffold-code modification, evaluation, and keep-or-revert selection; retained memory and skills also support its model-development experiments.
  - **Boundary:** The reported 30% gain is on internal evaluation sets. Researchers still guide model development and make critical decisions; full autonomous weight-level self-evolution is a future aim.

- **[Prime Agent: A self-improving RLM agent](https://www.primeintellect.ai/blog/prime-agent)** — Prime Intellect · 2026-08-05
  - `Harness` · **Self-modification** — Its /refine pipeline reads its own trajectory and changes persistent prompt notes, memory, skills and subagent specifications; recorded triggers/outcomes and rollback history carry improvements into later turns and sessions.
  - **Boundary:** The base system prompt remains immutable, and this does not retrain model weights. Its Factorio result is explicitly suspected of reward hacking; use the mechanism, not that score, as evidence.

- **[RoboCat: A self-improving robotic agent](https://deepmind.google/blog/robocat-a-self-improving-robotic-agent/)** — Google DeepMind · 2023-06-20
  - `Models` · **Self-training** — Fine-tunes a task-specific spin-off, collects its practice trajectories, merges them with demonstrations and retrains a generalist RoboCat version for later tasks.
  - **Boundary:** Each new task begins with 100–1000 human demonstrations; the training procedure and robot interfaces remain human-designed.

### AI Research and Supporting Methods

<details open><summary>Browse 15 articles</summary>

- **[Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/research/automated-alignment-researchers)** — Anthropic · 2026-04-14
  - `Models` · **Bounded optimization** — Nine Claude research agents propose, implement and evaluate weak-to-strong supervision methods, sharing findings and code; performance-gap feedback determines subsequent experiments.
  - **Boundary:** Held-out transfer was mixed, and the best method did not significantly improve production-scale Claude Sonnet 4. Researchers disqualified reward hacks; the researcher models were not themselves retrained in this experiment.

- **[MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model](https://www.minimax.io/blog/minimax-m3)** — MiniMax · 2026-06-01
  - `Models` · **Bounded optimization** — The PostTrainBench section describes an agent independently choosing synthetic data and training strategies, training four base models, evaluating them and adjusting its next experiments during a 12-hour loop.
  - **Boundary:** This is a task-bounded external-model optimization experiment, not M3 retraining its own weights. The release also mixes product benchmarks and demos, which are not separate RSI evidence.

- **[Automated researchers can reliably mitigate alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)** — Anthropic · 2026-08-28
  - `Models` · **Bounded optimization** — Claude searches literature, proposes methods and data, trains target models, and tests them in repeated experiments across ten alignment-failure categories; methods are checked on held-out benchmarks and larger models.
  - **Boundary:** This optimizes external student models rather than Claude's own weights. Capability constraints and a monitoring agent exclude invalid methods; benchmark success does not establish general autonomous alignment science.

- **[Can LLMs invent better ways to train LLMs?](https://sakana.ai/llm-squared/)** — Sakana AI · 2024-06-13
  - `Models` · **Bounded optimization** — LLM-Squared proposes preference-loss code, trains models with each candidate, and feeds downstream scores into the next proposal; the loop discovered DiscoPOP.
  - **Boundary:** The proposer is fixed; feeding an improved model back into its own research process is discussed as future work, not a demonstrated result.

- **[AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)** — Google DeepMind · 2026-05-07
  - `Artifacts` · **Bounded optimization** — Reports follow-up applications of evaluated code evolution to model components, training efficiency, cache policies and TPU circuits, with concrete AI-development feedback paths.
  - **Boundary:** Deployment case studies and publisher-reported gains do not demonstrate a fully closed cycle that retrains and improves the Gemini proposer itself.

- **[AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** — Google DeepMind · 2025-05-14
  - `Artifacts` · **Bounded optimization** — Explains evaluated program evolution that improves algorithms and Gemini training kernels, feeding successful programs into the next evolutionary proposals.
  - **Boundary:** Improving infrastructure used to train its underlying LLM is not proof of repeated autonomous Gemini-weight self-training.

- **[ShinkaEvolve: Evolving New Algorithms with LLMs, Orders of Magnitude More Efficiently](https://sakana.ai/shinka-evolve/)** — Sakana AI · 2025-09-25
  - `Artifacts` · **Bounded optimization** — Details sample-efficient program evolution and an evolved MoE load-balancing loss, tying executable candidate selection to subsequent program generations.
  - **Boundary:** Human-defined fitness and a fixed proposer model bound the result; it does not demonstrate a self-rewriting learning algorithm.

- **[Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://sakana.ai/drq/)** — Sakana AI · 2026-01-08
  - `Artifacts` · **Bounded optimization** — Evolves Core War programs against a growing history of predecessors; changing opponents supply selection pressure and retained programs shape subsequent evolution.
  - **Boundary:** Program co-evolution in a controlled virtual machine does not demonstrate autonomous improvement of the underlying LLM or real-world security capability.

- **[Autonomous AI research for nanogpt speedrun](https://www.primeintellect.ai/auto-nanogpt)** — Prime Intellect · 2026-05-14
  - `Artifacts` · **Bounded optimization** — Coding agents repeatedly revise optimizer code and hyperparameters, run nanoGPT training and use steps-to-target-validation-loss to select better variants; durable scratchpads preserve experiment state.
  - **Boundary:** Agents excelled at search and recombination but needed upstream human records to keep improving. Model/data/architecture and benchmark rules were fixed, and humans changed the harness between phases.

- **[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)** — Prime Intellect · 2026-05-18
  - `Artifacts` · **Bounded optimization** — A synthesizer evolves task families and a solver measures pass rates; only tasks in calibrated difficulty bands survive, and harder tiers seed later extensions of the synthetic training corpus.
  - **Boundary:** The evolved object is the task corpus. The post describes closing the full model-training/environment-generation loop as a broader research direction, not an already completed autonomous cycle.

- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/)** — Sakana AI · 2024-08-13
  - `Artifacts` · **Bounded optimization** — Describes idea generation, code experiments, paper writing and automated reviewing; saved reviews and experiments inform revisions and future research ideas.
  - **Boundary:** Flawed comparisons and self-review remain risks; accidental execution-script modification is a safety failure, not evidence of beneficial RSI.

- **[FunSearch: Making new discoveries in mathematical sciences using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)** — Google DeepMind · 2023-12-14
  - `Artifacts` · **Bounded optimization** — Samples earlier high-scoring programs, asks a fixed LLM for improvements, executes candidates, and returns the best programs to a population for future search.
  - **Boundary:** The evaluator and seed program are user-supplied; the model weights and improvement algorithm are not recursively rewritten.

- **[Population-based Model Merging via Quality Diversity](https://sakana.ai/cycleqd/)** — Sakana AI · 2024-12-03
  - `Models` · **Bounded optimization** — CycleQD cycles which task defines quality, crosses and mutates expert models, and retains diverse high-performing models in skill archives for further evolution.
  - **Boundary:** The tasks, starting experts and quality-diversity algorithm are human-specified; model merging is not gradient self-training or self-rewriting optimization.

- **[Evolving New Foundation Models: Unleashing the Power of Automating Model Development](https://sakana.ai/evolutionary-model-merge/)** — Sakana AI · 2024-03-21
  - `Models` · **Bounded optimization** — Evolves layer-selection and weight-mixing recipes over successive generations, selecting merged models by task fitness and assessing the selected model on a separate test set.
  - **Boundary:** Evolution searches a human-defined merge space of pretrained models; it does not establish an LLM autonomously rewriting its training algorithm.

- **[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)** — Google Research · 2025-02-19
  - `Artifacts` · **Bounded optimization** — Generation, reflection, ranking, evolution and meta-review agents iteratively revise scientific hypotheses using tournament feedback and researcher input.
  - **Boundary:** Elo is a self-evaluation signal rather than independent ground truth; laboratory validation uses expert guidance, and model weights remain fixed.

</details>

### Evaluation and Failure Modes

<details open><summary>Browse 4 articles</summary>

- **[AI CUDA Engineer update: robust benchmarking and interim results](https://sakana.ai/ai-cuda-engineer-update/)** — Sakana AI · 2025-09-17
  - `Artifacts` · **Evaluation / safety** — Corrects kernel-optimization claims after benchmark bypasses; robust-kbench reduces reported mean speedup from 3.13x to 1.49x under stricter measurement.
  - **Boundary:** A negative-results and measurement lesson for improvement loops, not a new self-improving agent; the original update is in Japanese.

- **[Sycophancy to subterfuge: Investigating reward tampering in language models](https://www.anthropic.com/research/reward-tampering)** — Anthropic · 2024-06-17
  - `Harness` · **Evaluation / safety** — Tests whether a curriculum of specification gaming generalizes to editing the model's own reward function and concealing the change, exposing a direct failure mode when self-modifying systems can alter their evaluators.
  - **Boundary:** Reward tampering occurred in 45 of 32,768 trials in a constructed study; it was not observed evidence of deployed Claude performing RSI, nor proof that all self-modification is unsafe.

- **[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)** — Anthropic · 2025-11-21
  - `Harness` · **Evaluation / safety** — Shows reward-hacking training generalizing to malicious behavior, including a Claude Code evaluation where the model attempts to sabotage this research project's detection code, directly testing trust in AI-assisted AI safety research.
  - **Boundary:** Researchers deliberately selected hackable RL environments and added hacking knowledge during pretraining. The 12% sabotage attempt rate describes this experimental model, not ordinary deployed Claude or proven completed sabotage.

- **[Measuring Autonomous AI Research](https://www.primeintellect.ai/blog/measuring-autonomous-research)** — Prime Intellect · 2026-08-14
  - `Artifacts` · **Evaluation / safety** — Evaluates 153 autonomous optimizer-research runs across 18 frontier models, examining whether proposed nanoGPT improvements survive evaluation and whether long-running agents produce new methods rather than only recombine existing ones.
  - **Boundary:** A fixed optimizer speedrun is a bounded proxy for research ability, not proof of general RSI. Results depend on seeds, supplied baselines and evaluation integrity.

</details>

### Research Agendas

<details open><summary>Browse 2 articles</summary>

- **[Introducing Sakana AI's Recursive Self-Improvement (RSI) Lab](https://sakana.ai/rsi-lab/)** — Sakana AI · 2026-06-05
  - `Harness` · **Research agenda** — Maps a proposed loop from agent-native models to AI scientists that build better models, grounded in DGM, LLM-Squared, ShinkaEvolve and adversarial co-evolution.
  - **Boundary:** A research agenda and lineage map, not evidence that the complete autonomous model-improvement cycle has already been achieved.

- **[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)** — Anthropic Institute
  - `Models` · **Research agenda** — Defines recursive self-improvement as AI autonomously designing and developing its successor, presents internal evidence of AI accelerating engineering and research, and examines whether that assistance can close the full model-development loop.
  - **Boundary:** The article explicitly says full RSI has not been achieved and is not inevitable. Internal productivity statistics are observational; human research judgment, compute, evaluations and security remain constraints.

</details>

### Foundations and Historical Tutorials

<details open><summary>Browse 4 articles</summary>

- **[Constitutional AI: Harmlessness from AI feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)** — Anthropic · 2022-12-15
  - `Models` · **Self-training** — Samples model responses, generates self-critiques and revisions, fine-tunes on the revised responses, then derives AI preferences for a reward model used in reinforcement learning.
  - **Boundary:** Human-written constitutional principles and a fixed staged training recipe remain essential. This is a bounded self-supervision foundation, not evidence of endlessly repeated autonomous RSI.

- **[AlphaGo Zero: Starting from scratch](https://deepmind.google/blog/alphago-zero-starting-from-scratch/)** — Google DeepMind · 2017-10-18
  - `Models` · **Self-training** — Self-play outcomes train the network; the updated network guides stronger search and games that supply the next training round.
  - **Boundary:** A foundational bounded self-training example in Go, with human-designed rules and learning machinery, not open-ended RSI.

- **[AlphaZero: Shedding new light on chess, shogi, and Go](https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/)** — Google DeepMind · 2018-12-06
  - `Models` · **Self-training** — Describes neural-network parameter updates from self-play outcomes and stronger network-guided tree search across separately learned games.
  - **Boundary:** Each game retains fixed rules and objectives; this is not one model autonomously expanding its domain or rewriting its learner.

- **[Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — OpenAI and Bain · 2025-11-04 · archived tutorial
  - `Harness` · **Bounded optimization** — Demonstrates versioned summarization-prompt updates from grader feedback, meta-prompting and GEPA, retaining better candidates for later requests.
  - **Boundary:** The official recipe is archived and may reference outdated APIs. Despite the title, it changes prompts rather than model weights; production needs held-out tests and human approval. Its example validation slice overlaps its training list.

</details>

### Engineering Reports

Primary technical posts that document harness design, evaluation protocol, or engineering lessons. They complement papers; they do not replace them.

- **[Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)** — OpenAI · 2026
  - `Harness` · **Bounded optimization** — Reports lessons from building a large agent-generated codebase around repository legibility, enforceable invariants, feedback loops, and long-running Codex tasks.
  - **Boundary:** An engineering report on using coding agents, not a demonstration that Codex rewrites its own improvement procedure.

- **[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)** — Anthropic · 2025
  - `Harness` · **Experience learning** — Describes initializer and incremental coding-agent roles, persistent progress artifacts, and clean handoffs across context windows.
  - **Boundary:** Human-designed harness patterns for long-running work, not recursive self-modification of the agent.

- **[Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)** — Anthropic · 2026
  - `Harness` · **Bounded optimization** — Studies planner–generator–evaluator architecture, rubric tuning, ablations, and the cost–quality tradeoff of long-running application-development harnesses.
  - **Boundary:** Harness-design research with a fixed outer protocol, not an agent rewriting that protocol.

- **[RSI-Exam: Benchmarking Recursive Self-Improvement through Executable Research](https://rsi-exam.ai/blog.html)** — RSI-Exam Team · 2026
  - `Artifacts` · **Evaluation / safety** — Documents task construction, hidden-set replay, scoring, resource accounting, trajectories, and limitations for an 88-task RSI benchmark.
  - **Boundary:** A measurement protocol, not a self-improving agent.

## Papers and Official Code

- Dates refer to first public version (usually first arXiv posting). A date alone makes no peer-review claim; venues are shown only when source-verified.
- Code links are author-linked releases. **—** means no author-linked implementation was established here; it does not assert that none exists.
- Star badges are live GitHub counts, not evidence of RSI.

### Papers / Harness

Agents revise their own executable code or retained control procedures, then use the revised system in subsequent improvement.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[Metaⁿ](https://arxiv.org/abs/2608.24735)**<br>2026-08-25 | **Self-modification**<br>Repeatedly applies a fixed meta-operation to the evolving solver stack, generating preprocessing code and reusable helpers; an archive retains evaluated layer chains.<br><details open><summary>Boundary</summary>Recursion acts on generated layers, not on the meta-operation or model weights. Most reported gains come from passed context; runs plateau at finite depth.</details> | [Official&nbsp;code](https://github.com/minnesotanlp/meta-n)<br>[![star](https://img.shields.io/github/stars/minnesotanlp/meta-n?style=flat-square&label=star&color=e75b31)](https://github.com/minnesotanlp/meta-n) |
| **[Ouroboros](https://arxiv.org/abs/2608.08311)**<br>2026 | **Self-modification**<br>Reviewed commits to tools, prompts, context assembly, and core code become the runtime for later work and can schedule another evolution cycle.<br><details open><summary>Boundary</summary>Promotion depends on a separate-agent review and frozen benchmark snapshots; this is empirical code-level self-change, not proof of indefinite acceleration.</details> | [Official&nbsp;code](https://github.com/razzant/ouroboros)<br>[![star](https://img.shields.io/github/stars/razzant/ouroboros?style=flat-square&label=star&color=e75b31)](https://github.com/razzant/ouroboros) |
| **[Mendel Gödel Machine](https://arxiv.org/abs/2608.07645)**<br>2026-08 | **Self-modification**<br>Evolves coding-agent implementations by comparative selection over lineages rather than a single rewrite path.<br><details open><summary>Boundary</summary>Comparative evolution still uses a designed fitness and a frozen backbone LLM; it is not a formal Gödel machine.</details> | — |
| **[DarwinX](https://arxiv.org/abs/2608.07545)**<br>2026-07-31 | **Self-modification**<br>Maintains a population of harness variants with frozen model weights; a fitness-based selection mechanism admits only variants that extend task coverage without regression, and an archive preserves alternative lineages for recombination.<br><details open><summary>Boundary</summary>Model weights are frozen throughout; only harness scaffolding evolves. Cross-benchmark transfer is demonstrated but not guaranteed for arbitrary domains. Fitness is determined by each benchmark's own verifier.</details> | — |
| **[HELIX](https://arxiv.org/abs/2608.13951)**<br>2026-08-14 | **Self-modification**<br>Decomposes agent systems into typed modular components and co-evolves harness and model in a loop; harness evolution boosts current performance and generates verified trajectories that become training data for the next model update.<br><details open><summary>Boundary</summary>Evaluated on code repair tasks only. A 65-candidate portfolio and 200-slot sibling slice define the search budget. Model-harness co-evolution is demonstrated in bounded iterations, not as indefinite improvement.</details> | [Official&nbsp;code](https://github.com/HKUDS/HELIX)<br>[![star](https://img.shields.io/github/stars/HKUDS/HELIX?style=flat-square&label=star&color=e75b31)](https://github.com/HKUDS/HELIX) |
| **[Dream-RSI](https://dream-rsi.com/assets/dream-rsi.pdf)**<br>2026-09-11 | **Self-modification**<br>Replays recorded discovery trees as simulated worlds to evaluate and revise exploration-policy code, then redeploys the selected policy to guide fresh searches.<br><details open><summary>Boundary</summary>The project preprint is public; implementation code was still announced as forthcoming at listing time. Replay cheapens evaluation of the exploration policy, not unbounded self-rewrite of the outer researcher.</details> | [Project](https://github.com/zhengkid/Dream-RSI) |
| **[HarnessEvolve](https://arxiv.org/abs/2609.00829)**<br>2026-09 | **Self-modification**<br>Learns harness updates from reference trajectories and gates candidates with held-out evaluation so later runs use the revised executable components.<br><details open><summary>Boundary</summary>Paper-linked code was not established at listing time. Alignment to reference trajectories is a designed supervisor, not self-invented criteria.</details> | — |
| **[WHALE](https://arxiv.org/abs/2609.00196)**<br>2026 | **Self-training**<br>Alternates model-weight updates with harness search so improvements in one surface become training signal for the other.<br><details open><summary>Boundary</summary>The alternating outer protocol remains fixed. Joint search is bounded self-improvement of two surfaces, not a rewritten meta-optimizer.</details> | [Official&nbsp;code](https://github.com/krafton-ai/WHALE)<br>[![star](https://img.shields.io/github/stars/krafton-ai/WHALE?style=flat-square&label=star&color=e75b31)](https://github.com/krafton-ai/WHALE) |
| **[MetaRSI / RSI²](https://arxiv.org/abs/2609.06396)**<br>2026 | **Self-modification**<br>A meta-policy revises how Data-RSI, Harness-RSI, and Model-RSI are composed and scheduled across improvement rounds.<br><details open><summary>Boundary</summary>The three operator families are human-specified; the meta-policy schedules and proposes within that vocabulary.</details> | — |
| **[ScienceBuddy](https://arxiv.org/abs/2609.17523)**<br>2026 | **Self-training**<br>Couples inner harness evolution with outer model reinforcement learning so two persistent surfaces improve while the alternating protocol stays fixed.<br><details open><summary>Boundary</summary>Included as joint harness-and-weight improvement, not as a system that rewrites the outer alternating protocol.</details> | [Official&nbsp;code](https://github.com/Gen-Verse/ScienceBuddy)<br>[![star](https://img.shields.io/github/stars/Gen-Verse/ScienceBuddy?style=flat-square&label=star&color=e75b31)](https://github.com/Gen-Verse/ScienceBuddy) |
| **[RHI](https://arxiv.org/abs/2607.15524)**<br>2026-07-17 | **Self-modification**<br>Represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback from its own revision history.<br><details open><summary>Boundary</summary>Tested on 30 synthetic ML research tasks across three domains. Gains come mainly from improved context management, not deeper reasoning. The information-theoretic framing is a proposed hypothesis, not a proven bound.</details> | — |
| **[HarnessBank](https://arxiv.org/abs/2607.13683)**<br>2026-07-15 | **Self-modification**<br>Pairs a task agent with an evolver agent that diagnoses failures, generates harness candidates, and maintains a gene bank of high-performing configurations; gated screening filters candidates before costly evaluation.<br><details open><summary>Boundary</summary>Cross-model experiments show improvements are model-specific rather than universal. The evolver agent and screening mechanism are fixed.</details> | — |
| **[OpenRSI / OpenMLE](https://arxiv.org/abs/2607.28568)**<br>2026 | **Bounded optimization**<br>Joins executable ML task environments, learned improvement operators, long-horizon program evolution, and held-out transfer evaluation in one AI4AI stack.<br><details open><summary>Boundary</summary>Meta-evolution operates within bounded ML engineering tasks. Atomic operators (Draft, Improve, Debug, Crossover) and composition rules are human-designed.</details> | [Official&nbsp;code](https://github.com/FrontisAI/OpenRSI)<br>[![star](https://img.shields.io/github/stars/FrontisAI/OpenRSI?style=flat-square&label=star&color=e75b31)](https://github.com/FrontisAI/OpenRSI) |
| **[MetaSkill-Evolve](https://arxiv.org/abs/2607.05297)**<br>2026-07-06 | **Self-modification**<br>Evolves task skills frequently and the five agents’ meta-skill files more slowly; the same pipeline edits the instructions that govern its own improvement.<br><details open><summary>Boundary</summary>One frozen backbone and three curated benchmarks. Meta-skills change, but the five roles, their wiring and the update schedule remain fixed.</details> | — |
| **[The Red Queen Gödel Machine](https://arxiv.org/abs/2606.26294)**<br>2026 | **Self-modification**<br>Agents and their evaluators co-evolve through epoch-bounded utility updates, making the improvement criterion part of the loop.<br><details open><summary>Boundary</summary>Co-evolving the evaluator is a research setting with epoch bounds, not a proof of globally reliable self-grading.</details> | — |
| **[EvoTrainer](https://arxiv.org/abs/2606.03108)**<br>2026 | **Self-modification**<br>Model policies and their training harnesses co-evolve under executable feedback.<br><details open><summary>Boundary</summary>Co-evolution is demonstrated inside designed training loops, not as unrestricted rewrite of the learning algorithm.</details> | [Official&nbsp;code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/EvoTrainer) |
| **[Self-Harness](https://arxiv.org/abs/2606.09498)**<br>2026 | **Self-modification**<br>Mines model-specific weaknesses, proposes minimal executable harness changes, and accepts them only after regression testing on Terminal-Bench, SWE-bench Verified, and AppWorld.<br><details open><summary>Boundary</summary>The proposer and regression suite are fixed. Code was not linked at publication.</details> | — |
| **[HarnessX](https://arxiv.org/abs/2606.14249)**<br>2026 | **Self-modification**<br>A composable foundry for adaptive, evolvable agent harnesses spanning code, context, and parameter surfaces.<br><details open><summary>Boundary</summary>A foundry for evolution is not by itself evidence of unbounded RSI; check which surfaces actually persist across rounds.</details> | — |
| **[MOSS](https://arxiv.org/abs/2605.22794)**<br>2026 | **Self-modification**<br>An agent rewrites its TypeScript source, replays failure batches, and promotes container images through an approval and rollback gate.<br><details open><summary>Boundary</summary>Promotion is gated by replay and approval. Source-level rewriting is empirical, not a proof search over all rewrites.</details> | [Official&nbsp;code](https://github.com/hkgai-official/Moss)<br>[![star](https://img.shields.io/github/stars/hkgai-official/Moss?style=flat-square&label=star&color=e75b31)](https://github.com/hkgai-official/Moss) |
| **[SIA](https://arxiv.org/abs/2605.27276)**<br>2026-05-22 | **Self-training**<br>A Feedback-Agent reviews execution logs and updates both the task harness and model weights of a domain-adapted agent across generations.<br><details open><summary>Boundary</summary>The Feedback-Agent and meta-agent remain fixed. Reported gains are single-run samples on selected tasks (LawBench, GPU kernels, RNA denoising).</details> | [Official&nbsp;code](https://github.com/hexo-ai/sia)<br>[![star](https://img.shields.io/github/stars/hexo-ai/sia?style=flat-square&label=star&color=e75b31)](https://github.com/hexo-ai/sia) |
| **[Continual Harness](https://arxiv.org/abs/2605.09998)**<br>2026-05-11 | **Experience learning**<br>Alternates action and refinement of prompts, subagents, skills and memory within a reset-free run. A separate co-learning experiment relabels rollouts with a frontier teacher and updates an open model without resetting the game.<br><details open><summary>Boundary</summary>Earlier Gemini Plays Pokemon results used human-in-the-loop harness refinement; later automated adaptation and teacher-assisted weight co-learning are distinct settings. Teacher supervision and game-specific evaluation limit autonomy claims.</details> | [Official&nbsp;code](https://github.com/PrimeIntellect-ai/prime-agent)<br>[![star](https://img.shields.io/github/stars/PrimeIntellect-ai/prime-agent?style=flat-square&label=star&color=e75b31)](https://github.com/PrimeIntellect-ai/prime-agent) |
| **[DemoEvolve](https://arxiv.org/abs/2605.24539)**<br>2026 | **Self-modification**<br>Uses demonstrations to overcome sparse feedback while evolving agent harnesses.<br><details open><summary>Boundary</summary>Demonstration-guided search still depends on supplied examples and a fixed evolver.</details> | — |
| **[Agentic Harness Engineering](https://arxiv.org/abs/2604.25850)**<br>2026 | **Self-modification**<br>Automatically evolves coding-agent harnesses from observability signals under a fixed base model, scored on Terminal-Bench with transfer checks.<br><details open><summary>Boundary</summary>The base model is frozen. Observability-driven edits are a designed outer loop.</details> | [Official&nbsp;code](https://github.com/china-qijizhifeng/agentic-harness-engineering) |
| **[Escher-Loop](https://arxiv.org/abs/2604.23472)**<br>2026 | **Self-modification**<br>Closed-loop self-referential optimization in which two sides of the system update each other.<br><details open><summary>Boundary</summary>Mutual evolution is a finite experimental protocol, not evidence of an unconstrained rewrite of the optimizer.</details> | — |
| **[Hyperagents](https://arxiv.org/abs/2603.19461)**<br>2026-03-19 | **Self-modification**<br>Integrates a task agent and a meta agent into one editable program so that evaluated changes can improve both task behavior and the machinery producing future changes.<br><details open><summary>Boundary</summary>Reported transfer and accumulation are finite experiments, not evidence of indefinite acceleration or autonomous weight-level learning.</details> | [Official&nbsp;code](https://github.com/facebookresearch/HyperAgents)<br>[![star](https://img.shields.io/github/stars/facebookresearch/HyperAgents?style=flat-square&label=star&color=e75b31)](https://github.com/facebookresearch/HyperAgents) |
| **[Meta-Harness](https://arxiv.org/abs/2603.28052)**<br>2026 | **Bounded optimization**<br>End-to-end optimization of model harnesses (prompts, routing, retrieval, tools, orchestration) with held-out evaluation, constraints, and rollback.<br><details open><summary>Boundary</summary>The optimizer that proposes harness edits remains fixed.</details> | [Official&nbsp;code](https://github.com/raphaelchristi/harness-evolver) |
| **[Group-Evolving Agents](https://arxiv.org/abs/2602.04837)**<br>2026 | **Experience learning**<br>Open-ended self-improvement via experience sharing among a group of evolving agents.<br><details open><summary>Boundary</summary>Shared experience is persistent state; the outer group-evolution algorithm is designed.</details> | [Official&nbsp;code](https://github.com/UCSB-AI/GEA) |
| **[Huxley-Gödel Machine](https://arxiv.org/abs/2510.21614)**<br>2025-10-24 | **Self-modification**<br>Uses descendant performance to estimate which self-modifying coding-agent lineages will produce better future agents, guiding the next code rewrites.<br><details open><summary>Boundary</summary>Clade statistics approximate improvement potential; they are not proofs of globally optimal rewrites. Experiments use bounded coding benchmarks and fixed underlying LLMs.</details> | [Official&nbsp;code](https://github.com/metauto-ai/HGM)<br>[![star](https://img.shields.io/github/stars/metauto-ai/HGM?style=flat-square&label=star&color=e75b31)](https://github.com/metauto-ai/HGM) |
| **[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)**<br>2025-05-29 | **Self-modification**<br>A coding agent modifies its own implementation, evaluates descendants on coding benchmarks, and branches from a growing archive of agents to produce further improvements.<br><details open><summary>Boundary</summary>Empirical code-level self-improvement, not formal proof of beneficial rewrites or foundation-model weight training; benchmark exploitation and sandbox escape remain concerns.</details> | [Official&nbsp;code](https://github.com/jennyzzt/dgm)<br>[![star](https://img.shields.io/github/stars/jennyzzt/dgm?style=flat-square&label=star&color=e75b31)](https://github.com/jennyzzt/dgm) |
| **[SICA](https://arxiv.org/abs/2504.15228)**<br>2025-04-21 | **Self-modification**<br>Evaluates the current coding agent, archives results, runs that same agent on its own codebase to implement an improvement, and evaluates the updated implementation again.<br><details open><summary>Boundary</summary>Non-gradient scaffold learning uses fixed LLM weights; gains on a sampled SWE-bench Verified subset and other benchmarks do not establish unlimited progress or whole-benchmark state of the art.</details> | [Official&nbsp;code](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>[![star](https://img.shields.io/github/stars/MaximeRobeyns/self_improving_coding_agent?style=flat-square&label=star&color=e75b31)](https://github.com/MaximeRobeyns/self_improving_coding_agent) |
| **[Gödel Agent](https://arxiv.org/abs/2410.04444)**<br>2024-10-06 | **Self-modification**<br>Uses LLM-generated changes to recursively revise the agent's own logic and behavior under high-level objectives rather than limiting changes to a predefined task-agent pipeline.<br><details open><summary>Boundary</summary>Inspired by the Gödel machine but supported by empirical task evaluations, not proofs that all rewrites are beneficial or that the whole agent-design space is optimally searched.</details> | [Official&nbsp;code](https://github.com/Arvid-pku/Godel_Agent)<br>[![star](https://img.shields.io/github/stars/Arvid-pku/Godel_Agent?style=flat-square&label=star&color=e75b31)](https://github.com/Arvid-pku/Godel_Agent) |
| **[ADAS](https://arxiv.org/abs/2408.08435)**<br>2024 | **Bounded optimization**<br>A meta-agent searches over agent programs; discovered agents are evaluated and retained, but the meta-optimizer stays fixed.<br><details open><summary>Boundary</summary>The searcher is not rewritten. Adjacent to RSI as automated agent design, not self-referential improvement of the designer.</details> | [Official&nbsp;code](https://github.com/ShengranHu/ADAS)<br>[![star](https://img.shields.io/github/stars/ShengranHu/ADAS?style=flat-square&label=star&color=e75b31)](https://github.com/ShengranHu/ADAS) |
| **[AFlow](https://arxiv.org/abs/2410.10762)**<br>2024 | **Bounded optimization**<br>Agent workflows are generated and refined against task feedback, retaining better executable graphs.<br><details open><summary>Boundary</summary>Workflow search with a fixed meta-algorithm. The optimizer of the graph is not itself the evolved object.</details> | [Official&nbsp;code](https://github.com/FoundationAgents/AFlow)<br>[![star](https://img.shields.io/github/stars/FoundationAgents/AFlow?style=flat-square&label=star&color=e75b31)](https://github.com/FoundationAgents/AFlow) |
| **[STOP](https://arxiv.org/abs/2310.02304)**<br>2023-10-03 | **Self-modification**<br>A seed LM-calling program optimizer is applied to its own code, discovering improved search scaffolds that then optimize downstream programs.<br><details open><summary>Boundary</summary>The paper explicitly says unchanged language models make this not full recursive self-improvement; only a small task set is studied, including sandbox-bypass risks.</details> | [Official&nbsp;code](https://github.com/microsoft/stop)<br>[![star](https://img.shields.io/github/stars/microsoft/stop?style=flat-square&label=star&color=e75b31)](https://github.com/microsoft/stop) |

### Papers / Models

Iterative model, curriculum and evaluator training. Updated models create later training signals; the learning rule can remain fixed.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[J-Zero](https://arxiv.org/abs/2608.26582)**<br>2026-08-27 | **Self-training**<br>Co-trains a task Challenger, Solver and Judge across rounds; structurally constructed preference pairs update the Judge that rewards later policy training.<br><details open><summary>Boundary</summary>The Judge starts from a pretrained reward checkpoint. Preference ordering is a designed assumption; reported ten-round gains do not establish unbounded improvement.</details> | [Official&nbsp;code](https://github.com/GyoukChu/J-Zero)<br>[![star](https://img.shields.io/github/stars/GyoukChu/J-Zero?style=flat-square&label=star&color=e75b31)](https://github.com/GyoukChu/J-Zero) |
| **[SPADE](https://arxiv.org/abs/2608.19197)**<br>2026-08-19 | **Self-training**<br>A single LLM fills Environment Designer and Reasoning Agent roles; the Designer writes executable Gym-style environments grounded in pretraining documents, and agent regret guides later challenges.<br><details open><summary>Boundary</summary>Work in progress. Tested at 30B scale. Co-evolution relies on pretraining-corpus grounding, not arbitrary open-ended generation.</details> | — |
| **[EnvHarness](https://arxiv.org/abs/2608.19880)**<br>2026 | **Self-training**<br>Synthesizes programmable harness components around a static environment from the current policy's failures and retrains the policy on the reshaped environment.<br><details open><summary>Boundary</summary>The outer synthesizer and held-out instance protocol are designed. Evaluated across four domains, not general RSI.</details> | [Official&nbsp;code](https://github.com/google-research/envharness) |
| **[DataFoundry](https://arxiv.org/abs/2608.29966)**<br>2026 | **Self-training**<br>Evolves executable data-preparation specifications through repeated proposal, evaluation, and reuse rather than treating synthetic data as a one-shot artifact.<br><details open><summary>Boundary</summary>The evolved object is a data recipe consumed by later training, not a self-rewriting learner.</details> | — |
| **[Socratic-SWE](https://arxiv.org/abs/2606.07412)**<br>2026-06-05 | **Self-training**<br>Distills solving traces into skills, generates targeted repair tasks, and jointly trains generator/solver roles; updated solvers produce the next curriculum’s traces.<br><details open><summary>Boundary</summary>A fixed seed-repository pool, executable tests and trusted validation tasks constrain the loop. The paper reports later-iteration saturation.</details> | — |
| **[Q-Evolve](https://arxiv.org/abs/2606.07367)**<br>2026-06-05 | **Self-training**<br>Unifies automatic process-reward labeling and policy learning in an in-distribution RL loop; a critic trained on mixed expert and agent data derives step-level rewards.<br><details open><summary>Boundary</summary>Evaluated on AlfWorld, WebShop and ScienceWorld. The critic is not purely self-generated. Reported gains stay inside these environments.</details> | — |
| **[ANDES](https://arxiv.org/abs/2606.01279)**<br>2026 | **Self-training**<br>An agent-native tool that evolves instruction data through synthesis, verification, and alignment updates.<br><details open><summary>Boundary</summary>Data evolution with a designed verification stack, not rewrite of the training algorithm.</details> | [Official&nbsp;code](https://github.com/zzy1127/ANDES) |
| **[P²O](https://arxiv.org/abs/2603.21877)**<br>2026 | **Self-training**<br>Jointly optimizes policy (weights) and prompts so each surface supplies signal for the other.<br><details open><summary>Boundary</summary>Joint search under a fixed outer optimizer. Not self-modification of that optimizer.</details> | — |
| **[SAGE](https://arxiv.org/abs/2603.15255)**<br>2026 | **Self-training**<br>Multi-agent generation and selection of reasoning experience for model evolution.<br><details open><summary>Boundary</summary>Experience is generated and filtered for weight updates; the selection protocol is designed.</details> | — |
| **[MM-Zero](https://arxiv.org/abs/2603.09206)**<br>2026 | **Self-training**<br>Extends two-role self-evolution to proposer, coder, and solver roles that render visual training data as code, from zero seed data.<br><details open><summary>Boundary</summary>Zero seed data is not an untrained backbone. Roles and executable rendering are designed.</details> | [Official&nbsp;code](https://github.com/zli12321/MM-Zero) |
| **[TTCS](https://arxiv.org/abs/2601.22628)**<br>2026 | **Self-training**<br>Co-evolves a question synthesizer and a solver during test-time training with self-consistency rewards so synthesized curricula stabilize parameter updates.<br><details open><summary>Boundary</summary>Test-time curriculum synthesis on math and general reasoning; not open-ended RSI.</details> | [Official&nbsp;code](https://github.com/XMUDeepLIT/TTCS) |
| **[Agent0](https://arxiv.org/abs/2511.16043)**<br>2025-11-20 | **Self-training**<br>Couples a curriculum model with a tool-using executor; stronger execution drives harder generated curricula, which in turn provide RL data.<br><details open><summary>Boundary</summary>Released training instructions require manual checkpoint selection between iterations; zero external data does not remove pretrained-backbone or tool dependencies.</details> | [Official&nbsp;code](https://github.com/aiming-lab/Agent0)<br>[![star](https://img.shields.io/github/stars/aiming-lab/Agent0?style=flat-square&label=star&color=e75b31)](https://github.com/aiming-lab/Agent0) |
| **[VisPlay](https://arxiv.org/abs/2511.15661)**<br>2025 | **Self-training**<br>Co-evolves an image-conditioned questioner and a reasoner with RL from unlabeled images only.<br><details open><summary>Boundary</summary>Unlabeled images are still an external corpus. Evaluated on multimodal reasoning benchmarks, not general RSI.</details> | [Official&nbsp;code](https://github.com/bruno686/VisPlay) |
| **[R-Zero](https://arxiv.org/abs/2508.05004)**<br>2025-08-07 | **Self-training**<br>Co-evolves Challenger and Solver models so that frontier-difficulty generated tasks train the Solver, while the Solver's changing capability alters the Challenger's rewards.<br><details open><summary>Boundary</summary>Uses a pretrained base and designed rewards; finite iterations can regress, and later R-Few work introduces human data to address scaling limits.</details> | [Official&nbsp;code](https://github.com/Chengsong-Huang/R-Zero)<br>[![star](https://img.shields.io/github/stars/Chengsong-Huang/R-Zero?style=flat-square&label=star&color=e75b31)](https://github.com/Chengsong-Huang/R-Zero) |
| **[SEAL](https://arxiv.org/abs/2506.10943)**<br>2025-06-12 | **Self-training**<br>The model generates self-edits containing finetuning data or update directives; SFT makes persistent weight changes, and downstream performance trains better self-edit generation through an outer RL loop.<br><details open><summary>Boundary</summary>Self-edits control adaptation within a researcher-designed SFT/RL framework; experiments on knowledge incorporation and few-shot generalization do not prove unrestricted self-redesign.</details> | [Official&nbsp;code](https://github.com/Continual-Intelligence/SEAL)<br>[![star](https://img.shields.io/github/stars/Continual-Intelligence/SEAL?style=flat-square&label=star&color=e75b31)](https://github.com/Continual-Intelligence/SEAL) |
| **[Absolute Zero](https://arxiv.org/abs/2505.03335)**<br>2025-05-06 | **Self-training**<br>A model co-evolves its task proposals and solving ability, using a code executor for task validity and answer rewards instead of an externally curated post-training dataset.<br><details open><summary>Boundary</summary>Zero data refers to the self-play post-training setup, not an untrained backbone; the executor, rewards and optimization machinery are human-designed.</details> | [Official&nbsp;code](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>[![star](https://img.shields.io/github/stars/LeapLabTHU/Absolute-Zero-Reasoner?style=flat-square&label=star&color=e75b31)](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) |
| **[G-Zero](https://arxiv.org/abs/2605.09959)**<br>2026 | **Self-training**<br>Co-evolves a proposer and a generator for open-ended generation with an intrinsic hint-conditioned predictive-shift reward in place of an external judge.<br><details open><summary>Boundary</summary>The intrinsic reward and two-role setup are designed. Evaluated on open-ended generation benchmarks.</details> | [Official&nbsp;code](https://github.com/Chengsong-Huang/G-Zero) |
| **[SiriuS](https://arxiv.org/abs/2502.04780)**<br>2025-02-07 | **Self-training**<br>Collects successful multi-agent trajectories, repairs failed ones, and fine-tunes the participating agents; improved agents generate later training experience.<br><details open><summary>Boundary</summary>Starts from labeled problems and fixed agent graphs. Role-specific SFT is iterative learning, not autonomous redesign of the training algorithm.</details> | [Official&nbsp;code](https://github.com/zou-group/sirius)<br>[![star](https://img.shields.io/github/stars/zou-group/sirius?style=flat-square&label=star&color=e75b31)](https://github.com/zou-group/sirius) |
| **[WebRL](https://arxiv.org/abs/2411.02337)**<br>2024 | **Self-training**<br>Trains web agents with a self-evolving online curriculum grounded in executable interaction.<br><details open><summary>Boundary</summary>Curriculum evolution with environment rewards; the RL algorithm is fixed.</details> | [Official&nbsp;code](https://github.com/THUDM/WebRL) |
| **[Self-Taught Evaluators](https://arxiv.org/abs/2408.02666)**<br>2024-08-05 | **Self-training**<br>Generates contrasting responses and synthetic judgments to repeatedly train an LLM evaluator, using improved evaluator predictions to construct later training rounds.<br><details open><summary>Boundary</summary>Human-preference-free training is not the same as zero human validation; checkpoint selection still uses HelpSteer2 validation accuracy.</details> | [Official&nbsp;artifacts](https://github.com/facebookresearch/RAM/tree/main/projects/self_taught_evaluator) |
| **[Meta-Rewarding Language Models](https://arxiv.org/abs/2407.19594)**<br>2024 | **Self-training**<br>Adds a meta-judge that critiques the model's own judgments so both task behavior and the evaluator improve across training rounds.<br><details open><summary>Boundary</summary>The meta-judge loop is a designed training recipe with a small number of reported iterations.</details> | — |
| **[ReST-MCTS*](https://arxiv.org/abs/2406.03816)**<br>2024-06-06 | **Self-training**<br>Uses process-reward-guided tree search to infer step values from correct final answers, then trains both the policy and process reward model on selected traces across iterations.<br><details open><summary>Boundary</summary>Removes per-step manual annotation, not oracle final-answer supervision; search and reward-learning rules remain fixed.</details> | [Official&nbsp;code](https://github.com/THUDM/ReST-MCTS)<br>[![star](https://img.shields.io/github/stars/THUDM/ReST-MCTS?style=flat-square&label=star&color=e75b31)](https://github.com/THUDM/ReST-MCTS) |
| **[SPPO](https://arxiv.org/abs/2405.00675)**<br>2024-05-01 | **Self-training**<br>Treats alignment as a constant-sum two-player game and repeatedly updates the policy against its own generated responses using preference probabilities.<br><details open><summary>Boundary</summary>Experiments use prompts and a pretrained PairRM judge; the equilibrium guarantee concerns the specified preference game, not unbounded capability growth.</details> | [Official&nbsp;code](https://github.com/uclaml/SPPO)<br>[![star](https://img.shields.io/github/stars/uclaml/SPPO?style=flat-square&label=star&color=e75b31)](https://github.com/uclaml/SPPO) |
| **[Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020)**<br>2024-01-18 | **Self-training**<br>Uses the language model as its own prompted reward judge during iterative DPO, jointly improving response generation and the rewards it gives subsequent training examples.<br><details open><summary>Boundary</summary>Three reported iterations and benchmark preference gains do not prove calibrated self-judgment or sustained superhuman improvement; seed supervision remains relevant.</details> | — |
| **[SPIN](https://arxiv.org/abs/2401.01335)**<br>2024-01-02 | **Self-training**<br>Trains a policy to distinguish human demonstration responses from responses generated by its previous iteration, repeatedly strengthening an SFT model through self-play.<br><details open><summary>Boundary</summary>Reuses human demonstrations and an SFT starting model; theoretical optimality concerns the target data distribution, not unlimited recursive capability growth.</details> | [Official&nbsp;code](https://github.com/uclaml/SPIN)<br>[![star](https://img.shields.io/github/stars/uclaml/SPIN?style=flat-square&label=star&color=e75b31)](https://github.com/uclaml/SPIN) |
| **[ReST-EM](https://arxiv.org/abs/2312.06585)**<br>2023-12-11 | **Self-training**<br>Repeatedly samples solutions, filters by binary correctness feedback and fine-tunes on accepted samples, studying scaling on MATH and APPS with PaLM-2.<br><details open><summary>Boundary</summary>Needs externally supplied problems and verifiable feedback; a few EM-style iterations do not establish indefinite improvement.</details> | — |
| **[ReST](https://arxiv.org/abs/2308.08998)**<br>2023-08-17 | **Self-training**<br>Alternates policy-generated data collection with reward-guided offline learning, reusing samples to improve a language-model policy, demonstrated on machine translation.<br><details open><summary>Boundary</summary>Reward and preference signals remain externally specified; results in translation do not establish a self-improving reward mechanism.</details> | — |
| **[RoboCat](https://arxiv.org/abs/2306.11706)**<br>2023-06-20 | **Self-training**<br>Adapts a generalist robotic policy to tasks and embodiments, uses trained policies to gather further robot experience, and retrains subsequent generalist models on the expanded data.<br><details open><summary>Boundary</summary>Task adaptation still uses demonstrations and controlled robot infrastructure; this is a building block, not self-redesign of the training system.</details> | — |
| **[Self-Instruct](https://arxiv.org/abs/2212.10560)**<br>2022 | **Self-training**<br>Bootstraps instruction-following data from a model's own generations and trains a later model on the filtered set.<br><details open><summary>Boundary</summary>A data-bootstrapping recipe with human seed tasks, not recursive rewrite of the trainer.</details> | [Official&nbsp;code](https://github.com/yizhongw/self-instruct)<br>[![star](https://img.shields.io/github/stars/yizhongw/self-instruct?style=flat-square&label=star&color=e75b31)](https://github.com/yizhongw/self-instruct) |
| **[LLMs Can Self-Improve](https://arxiv.org/abs/2210.11610)**<br>2022 | **Self-training**<br>Iterative self-generated rationales improve reasoning without new human labels.<br><details open><summary>Boundary</summary>Uses a designed filter and a fixed training loop on reasoning benchmarks.</details> | — |
| **[STaR](https://arxiv.org/abs/2203.14465)**<br>2022-03-28 | **Self-training**<br>Generates reasoning traces, filters them by answer correctness, rationalizes failed examples using known answers, and repeatedly fine-tunes on successful traces.<br><details open><summary>Boundary</summary>Requires a task dataset, known answers and seed rationale examples; a fixed training loop is not an autonomous redesign of the learner.</details> | [Official&nbsp;code](https://github.com/ezelikman/STaR)<br>[![star](https://img.shields.io/github/stars/ezelikman/STaR?style=flat-square&label=star&color=e75b31)](https://github.com/ezelikman/STaR) |

### Papers / Experience

Persistent prompts, memory, skills, and playbooks. These change later tasks; the outer updater is usually fixed.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[SkillAdam](https://arxiv.org/abs/2609.08944)**<br>2026-09-08 | **Experience learning**<br>Revises skill documents using a persistent issue tracker and an adaptive edit budget, retaining changes when batch evaluation shows gains without unacceptable regressions.<br><details open><summary>Boundary</summary>The skill-evolution optimizer is designed. Stabilization heuristics are not a rewritten improver.</details> | [Official&nbsp;code](https://github.com/ruc-datalab/SkillAdam) |
| **[SkillGLoW](https://arxiv.org/abs/2609.02217)**<br>2026-09-02 | **Experience learning**<br>Groups task-local experience by shared solving procedure, consolidates it into reusable skill priors, and checks library revisions through execution.<br><details open><summary>Boundary</summary>Consolidation and execution gates are fixed. Skills persist; the consolidator does not rewrite itself.</details> | — |
| **[WikiSkill](https://arxiv.org/abs/2608.27454)**<br>2026 | **Experience learning**<br>Co-evolves a persistent wiki-style knowledge base and reusable skills from agent experience.<br><details open><summary>Boundary</summary>Code was not linked at publication. Wiki+skill updates are persistent artifacts under a designed compiler.</details> | — |
| **[HyperSkill](https://arxiv.org/abs/2608.16114)**<br>2026 | **Experience learning**<br>Stores and revises skills in a hypergraph-structured memory used on later tasks.<br><details open><summary>Boundary</summary>Skill-memory structure is designed; this is not harness-code self-modification.</details> | — |
| **[Evo-Harness](https://arxiv.org/abs/2608.15071)**<br>2026 | **Experience learning**<br>Compiles accumulated context into persistent harness skills for later self-evolving runs.<br><details open><summary>Boundary</summary>Compilation is a designed transform from context to skill, not an unrestricted self-rewrite.</details> | — |
| **[Who Grades the Grader?](https://arxiv.org/abs/2607.12790)**<br>2026 | **Self-modification**<br>Co-evolves an inspectable evaluation metric with an agent skill library, exposing criterion drift as part of the loop.<br><details open><summary>Boundary</summary>Making the grader editable is a research setting. It studies evaluator drift; it does not claim a solved RSI evaluator.</details> | [Official&nbsp;code](https://github.com/amazon-science/Self-Evolving-Agents-Double-Ratchet) |
| **[SkillHone](https://arxiv.org/abs/2606.08671)**<br>2026 | **Experience learning**<br>Evolves whole skill packages while retaining evaluation and promotion decisions as auditable Git artifacts.<br><details open><summary>Boundary</summary>Git-native promotion is a designed gate. The package evolver is fixed.</details> | [Official&nbsp;code](https://github.com/Tencent/SkillHone) |
| **[OpenSkill](https://arxiv.org/abs/2606.06741)**<br>2026 | **Experience learning**<br>Builds skills and verification signals in open-world environments.<br><details open><summary>Boundary</summary>Self-created verifiers are still a designed skill-learning loop, not RSI of the agent kernel.</details> | [Official&nbsp;code](https://github.com/OpenLAIR/OpenSkill) |
| **[SkillOpt](https://arxiv.org/abs/2605.23904)**<br>2026 | **Experience learning**<br>Optimizes reusable natural-language skills through trajectory-driven edits and held-out validation gates.<br><details open><summary>Boundary</summary>Held-out validation is the promotion signal; the skill optimizer is fixed.</details> | [Official&nbsp;code](https://github.com/microsoft/SkillOpt) |
| **[ExpGraph](https://arxiv.org/abs/2605.30712)**<br>2026 | **Experience learning**<br>Model-agnostic experience learning with graph-structured memory reused across later LLM-agent tasks.<br><details open><summary>Boundary</summary>Graph memory is persistent state. The update rule is designed and the backbone is typically frozen.</details> | — |
| **[SkillSmith](https://arxiv.org/abs/2606.01314)**<br>2026 | **Experience learning**<br>Co-evolves skills and tools for self-improving agent systems.<br><details open><summary>Boundary</summary>Skill/tool co-evolution under a fixed smithing procedure.</details> | — |
| **[Mem²Evolve](https://arxiv.org/abs/2604.10923)**<br>2026 | **Experience learning**<br>Co-evolves capability expansion with experience distillation into memory used on later tasks.<br><details open><summary>Boundary</summary>Memory and capability stores persist; the co-evolution protocol is designed.</details> | [Official&nbsp;code](https://github.com/BUAA-IRIP-LLM/Mem2Evolve) |
| **[CoEvoSkills](https://arxiv.org/abs/2604.01687)**<br>2026 | **Experience learning**<br>Co-evolves reusable skills and their verification process.<br><details open><summary>Boundary</summary>Verifier co-evolution is a designed pair of update surfaces, not a rewritten outer loop.</details> | [Official&nbsp;code](https://github.com/Zhang-Henry/CoEvoSkills) |
| **[ACE](https://arxiv.org/abs/2510.04618)**<br>2025-10-06 | **Experience learning**<br>Turns execution feedback into incremental updates to a structured playbook, preserving useful strategies while revising and deduplicating experience for later tasks.<br><details open><summary>Boundary</summary>The playbook is persistent context, not model weights or self-modifying code. The ACE updater is fixed.</details> | [Official&nbsp;code](https://github.com/ace-agent/ace) |
| **[ReasoningBank](https://arxiv.org/abs/2509.25140)**<br>2025 | **Experience learning**<br>Distills reusable strategies from self-judged successes and failures, retrieves them for later tasks, and writes new lessons back into persistent reasoning memory.<br><details open><summary>Boundary</summary>Self-judged memory can drift. Retrieval-and-write is a designed memory loop.</details> | [Official&nbsp;code](https://github.com/google-research/reasoning-bank) |
| **[GEPA](https://arxiv.org/abs/2507.19457)**<br>2025-07-25 | **Bounded optimization**<br>Reflects on execution traces and evaluator feedback to propose prompt revisions, retaining complementary candidates through Pareto-based selection.<br><details open><summary>Boundary</summary>The original method optimizes prompts with fixed model weights; a general optimize-anything API is not evidence that GEPA rewrites itself.</details> | [Official&nbsp;code](https://github.com/gepa-ai/gepa)<br>[![star](https://img.shields.io/github/stars/gepa-ai/gepa?style=flat-square&label=star&color=e75b31)](https://github.com/gepa-ai/gepa) |
| **[Memp](https://arxiv.org/abs/2508.06433)**<br>2025 | **Experience learning**<br>Explores agent procedural memory that accumulates and is reused across tasks.<br><details open><summary>Boundary</summary>Procedural memory is a persistent artifact under a designed store/retrieve policy.</details> | — |
| **[Dynamic Cheatsheet](https://arxiv.org/abs/2504.07952)**<br>2025-04-10 | **Experience learning**<br>Maintains a self-curated memory of transferable strategies and validated code across otherwise independent inference tasks.<br><details open><summary>Boundary</summary>Test-time memory, not weight updates or harness self-rewrite.</details> | [Official&nbsp;code](https://github.com/suzgunmirac/dynamic-cheatsheet) |
| **[SkillWeaver](https://arxiv.org/abs/2504.07079)**<br>2025 | **Experience learning**<br>Discovers and hones reusable web-agent skills through environment exploration.<br><details open><summary>Boundary</summary>Skill library growth with environment feedback; the weaver is fixed.</details> | [Official&nbsp;code](https://github.com/OSU-NLP-Group/SkillWeaver) |
| **[A-MEM](https://arxiv.org/abs/2502.12110)**<br>2025 | **Experience learning**<br>Agentic memory for LLM agents that is stored, updated, and retrieved across steps and tasks.<br><details open><summary>Boundary</summary>Memory infrastructure, not demonstrated recursive improvement of the memory updater.</details> | — |
| **[Agent Workflow Memory](https://arxiv.org/abs/2409.07429)**<br>2024 | **Experience learning**<br>Stores workflows from successful trajectories and retrieves them for later tasks.<br><details open><summary>Boundary</summary>Workflow memory with a designed write/read policy.</details> | — |
| **[Voyager](https://arxiv.org/abs/2305.16291)**<br>2023 | **Experience learning**<br>Builds and reuses an executable skill library through environment interaction in Minecraft.<br><details open><summary>Boundary</summary>Skill library persistence with a frozen LLM and a designed curriculum/automatic curriculum. A landmark skill-based agent, not RSI of the improver.</details> | [Official&nbsp;code](https://github.com/MineDojo/Voyager)<br>[![star](https://img.shields.io/github/stars/MineDojo/Voyager?style=flat-square&label=star&color=e75b31)](https://github.com/MineDojo/Voyager) |
| **[Promptbreeder](https://arxiv.org/abs/2309.16797)**<br>2023 | **Bounded optimization**<br>Evolves task prompts together with mutation prompts, so the mutation operator itself can change.<br><details open><summary>Boundary</summary>Unusually close to meta-improvement of prompts, but model weights stay fixed and fitness is a designed task metric.</details> | — |
| **[Eureka](https://arxiv.org/abs/2310.12931)**<br>2023 | **Bounded optimization**<br>Evolves reward programs using environment feedback, then trains agents with the selected rewards.<br><details open><summary>Boundary</summary>The target is an external reward function. Eureka does not rewrite Eureka.</details> | [Official&nbsp;code](https://github.com/eureka-research/Eureka)<br>[![star](https://img.shields.io/github/stars/eureka-research/Eureka?style=flat-square&label=star&color=e75b31)](https://github.com/eureka-research/Eureka) |

<details><summary>Further experience and skill methods</summary>

- `Artifacts` · **Experience learning** — [TRACE](https://arxiv.org/abs/2608.22793), [Recuris](https://arxiv.org/abs/2608.24876), [MediSkill-Evo](https://arxiv.org/abs/2608.23397), [Prime Agent paper](https://arxiv.org/abs/2608.23552), [DIVE (skill evolution)](https://arxiv.org/abs/2608.12486), [When Rules Learn](https://arxiv.org/abs/2606.17220), [ISM](https://arxiv.org/abs/2606.31191), [SkillRevise](https://arxiv.org/abs/2606.01139), [SePO](https://arxiv.org/abs/2606.04465), [HeLa-Mem](https://arxiv.org/abs/2604.16839), [MemRL](https://arxiv.org/abs/2601.03192), [Cradle](https://arxiv.org/abs/2403.03186), [Alita](https://arxiv.org/abs/2505.20286), [TextGrad](https://arxiv.org/abs/2406.07496), [OPRO](https://arxiv.org/abs/2309.03409)
- `Harness` · **Bounded optimization** — [Reflexion](https://arxiv.org/abs/2303.11366) and [Self-Refine](https://arxiv.org/abs/2303.17651) store verbal feedback or revise an answer; they are adjacent context, not persistent RSI, unless a later system reuses that state across tasks.

</details>

### Papers / Theory and Evaluation

Formal foundations, proposed closed-loop learning, and tests of whether self-improvement signals remain reliable. These are not implementation demonstrations.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[S3Gym](https://arxiv.org/abs/2608.31100)**<br>2026-08-31 | **Evaluation / safety**<br>An interactive benchmark for self-testing, self-judging and self-improvement around seven text-based games with executable verifiers.<br><details open><summary>Boundary</summary>Core finding is that self-improvement is neither automatic nor uniform. Parameter training shows instability and negative transfer. Seven games are a limited proxy for general capability.</details> | — |
| **[Rise-and-Collapse](https://arxiv.org/abs/2606.21090)**<br>2026-06-17 | **Evaluation / safety**<br>Documents a rise-then-collapse pattern in REINFORCE post-training for code, where performance peaks within tens of gradient steps then falls; KL and EWC do not prevent it.<br><details open><summary>Boundary</summary>Studied on Qwen-2.5-3B/7B and a Gemma-3-4B pilot with competitive programming tasks. This is a within-task failure analysis, not a general theory of self-training limits.</details> | — |
| **[Self-Evolution Generalization Gap](https://arxiv.org/abs/2606.01075)**<br>2026-06-02 | **Evaluation / safety**<br>Finds closed-loop self-evolution with internally generated supervision improves over base but plateaus, leaving a gap versus oracle supervision.<br><details open><summary>Boundary</summary>Primary testbed is Knights and Knaves logical reasoning. Internally generated supervision remains insufficient under the paper's minimal formulation.</details> | — |
| **[Task-centric Self-Improvement](https://arxiv.org/abs/2602.10014)**<br>2026-02-14 | **Evaluation / safety**<br>Finite-sample analysis of iterative self-improvement where models fine-tune on reward-verified outputs; proves conditions where easy-to-hard curricula outperform fixed mixtures.<br><details open><summary>Boundary</summary>Theory with verifiable rewards, validated on synthetic graph reasoning and math. Explains saturation but does not eliminate it.</details> | — |
| **[Statistical Gödel Machine](https://arxiv.org/abs/2510.10232)**<br>2025-10-11 | **Evaluation / safety**<br>Tests candidate edits before adoption and budgets cumulative false-acceptance risk across rounds, providing a statistical gate for self-modification.<br><details open><summary>Boundary</summary>Guarantees require bounded independent paired measurements and a stable evaluator. Experiments use simple proposals, not a demonstrated self-rewriting LLM.</details> | [Official&nbsp;code](https://github.com/gravitywavelet/sgm-anon) |
| **[Socratic Learning](https://arxiv.org/abs/2411.16905)**<br>2024-11-25 | **Research agenda**<br>A position on closed-system recursive learning through language games, separating feedback quality, experience coverage and resource requirements.<br><details open><summary>Boundary</summary>A position paper under explicit assumptions; it does not report an implemented system with boundless empirical capability growth.</details> | — |
| **[Guided Self-Improvement](https://arxiv.org/abs/2411.00750)**<br>2024-11-01 | **Evaluation / safety**<br>Studies loss of difficult examples during repeated self-training and uses Socratic hints to recover sampling coverage for later training rounds.<br><details open><summary>Boundary</summary>Requires known answer checks and guidance; correct final answers can still hide spurious rationales.</details> | [Official&nbsp;code](https://github.com/Yiwen-Ding/Guided-Self-Improvement) |
| **[Gödel Machines](https://arxiv.org/abs/cs/0309048)**<br>2003-09-25 | **Research agenda**<br>Formalizes a self-referential solver that can rewrite its proof-search code once the expected usefulness of that rewrite is provable.<br><details open><summary>Boundary</summary>A theoretical construction relative to encoded axioms and utility, not an efficient deployed LLM system; useful rewrites may be unprovable or costly to prove.</details> | — |
| **[Generalized Agent Iteration](https://arxiv.org/abs/2609.13406)**<br>2026 | **Research agenda**<br>Places iterative policy improvement and RSI in one formal framework using two axes: whether the improving mechanism is inside the agent and whether evaluation remains externally grounded.<br><details open><summary>Boundary</summary>A unifying formalism, not an implemented self-improving agent.</details> | — |
| **[The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802)**<br>2026 | **Research agenda**<br>Models feedback between AI capabilities and AI R&D with coupled elasticities, and identifies measurements needed to test whether self-sustaining acceleration is occurring.<br><details open><summary>Boundary</summary>An economic model and measurement agenda, not empirical proof that acceleration is underway.</details> | — |

### Surveys and Taxonomies

- `Harness` · **Research agenda** — [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) (2026) — Distinguishes bounded refinement, persistent self-improvement, recursive improvement, and autonomous research loops.
- `Harness` · **Research agenda** — [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) (2026) — Maps foundation-model improvement versus prompt, memory, tool, and full-scaffolding improvement. [Collection](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents)
- `Harness` · **Research agenda** — [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve](https://arxiv.org/abs/2507.21046) (TMLR 2026)
- `Harness` · **Research agenda** — [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407) (2025)
- `Models` · **Research agenda** — [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) (2024). [Collection](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/Awesome-Self-Evolution-of-LLM)
- `Harness` · **Research agenda** — [Self-Improving Agents in the Era of Experience](https://openreview.net/forum?id=IUltZSgLMm) (2026) — Treats the harness as experience infrastructure.
- `Harness` · **Research agenda** — [Towards Persistent Growth: A Survey on Self-Evolving Agents from a Lifelong Learning Perspective](https://dsa.hkust-gz.edu.cn/blog/2026/06/05/towards-persistent-growth-a-survey-on-self-evolving-agents-from-a-lifelong-learning-perspective/) (2026)
- `Harness` · **Evaluation / safety** — [Diving into Reliable Self-Evolving Agents](https://openreview.net/forum?id=CGO1hDTHNe) (2026) — Five-level taxonomy plus reliability requirements. [Collection](https://github.com/wkqdzkd/Awesome-Reliable-Self-Evolving-Agents)
- `Harness` · **Research agenda** — [A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution](https://doi.org/10.36227/techrxiv.177203250.05832634/v2) (2026). [Collection](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)
- `Harness` · **Research agenda** — [The Path to Recursive Self-Improving Agents](https://www.preprints.org/manuscript/202608.0051) (2026). [Collection](https://github.com/D2I-ai/awesome-recursive-self-improving-agents)
- `Harness` · **Bounded optimization** — [From Static Templates to Dynamic Runtime Graphs](https://arxiv.org/abs/2603.22386) (2026)
- `Harness` · **Research agenda** — [Agent Harness Engineering: A Survey](https://openreview.net/forum?id=eONq7FdiHa) (2026)
- `Harness` · **Bounded optimization** — [Automated Design of Agentic Systems: A Survey](https://www.preprints.org/manuscript/202606.0238) (2026)
- `Harness` · **Research agenda** — [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873) (2026)

### Foundations

- `Models` · **Research agenda** — [Speculations Concerning the First Ultraintelligent Machine](https://www.sciencedirect.com/science/article/pii/S0065245808604180) (I. J. Good, 1965) — Intelligence-explosion argument.
- `Harness` · **Research agenda** — [Gödel Machines](https://arxiv.org/abs/cs/0309048) (Schmidhuber, 2003) — listed again under theory with the full tagged table.
- `Models` · **Evaluation / safety** — [Basic AI Drives](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf) (Omohundro, 2008)
- `Models` · **Research agenda** — [Intelligence Explosion Microeconomics](https://intelligence.org/files/IEM.pdf) (Yudkowsky, 2013)
- `Harness` · **Research agenda** — [From Seed AI to Technological Singularity via Recursively Self-Improving Software](https://arxiv.org/abs/1502.06512) (Yampolskiy, 2015)
- `Artifacts` · **Bounded optimization** — [POWERPLAY](https://arxiv.org/abs/1112.5309) (2011) — jointly searches for a new task and a solver modification that preserves old skills.
- `Models` · **Bounded optimization** — [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474) (NeurIPS 2016)
- `Models` · **Bounded optimization** — [Population Based Training of Neural Networks](https://arxiv.org/abs/1711.09846) (2017)
- `Artifacts` · **Bounded optimization** — [Paired Open-Ended Trailblazer (POET)](https://arxiv.org/abs/1901.01753) (2019)
- `Models` · **Research agenda** — [AI-GAs: AI-Generating Algorithms](https://arxiv.org/abs/1905.10985) (2019)
- `Artifacts` · **Bounded optimization** — [AutoML-Zero](https://arxiv.org/abs/2003.03384) (ICML 2020). [Code](https://github.com/google-research/google-research/tree/master/automl_zero)
- `Artifacts` · **Research agenda** — [Open-Endedness: The Last Grand Challenge You've Never Heard Of](https://www.oreilly.com/radar/open-endedness-the-last-grand-challenge-youve-never-heard-of/) (Stanley, Lehman, Soros, 2017)

## Benchmarks

A downstream task score is not by itself an RSI evaluation. Direct benchmarks measure change across episodes, generations, or checkpoints.

**Online** — experience accumulates during the task stream. **Offline** — evolution precedes held-out evaluation. **Artifact** tags say what the evaluated workflow is allowed to change.

| Benchmark | Year | Mode | Artifact tags |
| --- | ---: | --- | --- |
| [HarnessDev](https://arxiv.org/abs/2609.01437) | 2026 | Offline | `Harness` `Context` |
| [EVOHARNESSBENCH](https://arxiv.org/abs/2609.04280) | 2026 | Online | `Harness` `Skill` |
| [S3Gym](https://arxiv.org/abs/2608.31100) | 2026 | Offline | `Models` `Context` `Memory` |
| [Evo-Bench](https://arxiv.org/abs/2608.09096) | 2026 | Offline | `Harness` `Context` |
| [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301) | 2026 | Offline | `Harness` `Context` |
| [FinEvo-Bench](https://arxiv.org/abs/2608.06144) | 2026 | Online | `Memory` `Skill` |
| [ContinualSkillBench](https://arxiv.org/abs/2608.03874) | 2026 | Online | `Context` `Skill` |
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | 2026 | Online | `Memory` `Skill` |
| [PATH-Bench](https://arxiv.org/abs/2608.01149) | 2026 | Online | `Context` `Memory` `Skill` |
| [AgentStream](https://arxiv.org/abs/2608.00155) | 2026 | Online | `Context` `Memory` `Skill` |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | Online | `Context` `Artifacts` |
| [EvoAgentBench](https://arxiv.org/abs/2607.05202) | 2026 | Offline | `Skill` |
| [RSI-Exam](https://rsi-exam.ai/) | 2026 | Offline | `Harness` `Artifacts` |
| [SEAGym](https://arxiv.org/abs/2606.17546) | 2026 | Offline | `Harness` `Context` `Memory` `Skill` |
| [Meta-Agent Challenge](https://arxiv.org/abs/2606.04455) | 2026 | Offline | `Harness` `Context` |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | 2026 | Online | `Context` `Artifacts` |
| [SEA-Eval](https://arxiv.org/abs/2604.08988) | 2026 | Online | `Harness` `Skill` |
| [SE-Bench](https://arxiv.org/abs/2602.04811) | 2026 | Offline | `Memory` |
| [VeRO](https://arxiv.org/abs/2602.22480) | 2026 | Offline | `Harness` `Context` |
| [Evo-Memory](https://arxiv.org/abs/2511.20857) | 2025 | Online | `Context` `Memory` |
| [StuLife / ELL](https://arxiv.org/abs/2508.19005) | 2025 | Online | `Context` `Memory` `Skill` |
| [LifelongAgentBench](https://arxiv.org/abs/2505.11942) | 2025 | Online | `Context` `Memory` |
| [MemoryBench](https://arxiv.org/abs/2510.17281) | 2025 | Offline | `Memory` |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | 2026 | Offline | `Artifacts` |
| [NatureBench](https://arxiv.org/abs/2606.24530) | 2026 | Offline | `Artifacts` |
| [RE-Bench](https://arxiv.org/abs/2411.15114) | 2024 | Offline | `Artifacts` |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | 2024 | Offline | `Artifacts` |
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023 | Offline | `Artifacts` |
| [MLGym-Bench](https://arxiv.org/abs/2502.14499) | 2025 | Offline | `Artifacts` |
| [PaperBench](https://openai.com/index/paperbench/) | 2024 | Offline | `Artifacts` |
| [CORE-Bench](https://arxiv.org/abs/2409.11363) | 2024 | Offline | `Artifacts` |
| [SIP-Bench](https://github.com/Yuchong-W/SIP_Bench) | 2026 | Online | `Harness` `Memory` |
| [FinEvolveBench](https://arxiv.org/abs/2606.06960) | 2026 | Online | `Memory` `Skill` |
| [SkillFlow](https://arxiv.org/abs/2604.17308) | 2026 | Online / Offline | `Context` `Skill` |
| [SkillLearnBench](https://arxiv.org/abs/2604.20087) | 2026 | Online | `Skill` |
| [EvoMemBench](https://arxiv.org/abs/2605.18421) | 2026 | Online | `Context` `Memory` |
| [EdgeBench](https://arxiv.org/abs/2607.05155) | 2026 | Online | `Context` `Artifacts` |
| [AutoLab](https://arxiv.org/abs/2606.05080) | 2026 | Online | `Context` `Artifacts` |
| [GDPevo](https://arxiv.org/abs/2608.03764) | 2026 | Offline | `Skill` |
| [Φ-Bench](https://faibench.org/) | 2026 | Offline | `Artifacts` |

Taskbeds such as [SWE-bench](https://arxiv.org/abs/2310.06770), [Terminal-Bench](https://github.com/harbor-framework/terminal-bench), and [ALE-Bench](https://github.com/SakanaAI/ALE-Bench) evaluate a fixed agent. An RSI study must add longitudinal splits, frozen selection gates, or matched non-improving controls before treating them as self-improvement evidence.

**A convincing RSI evaluation should report:** performance across multiple generations (including regressions); a held-out evaluator the system cannot rewrite; ablations for self-modification, archive/search, memory, and external feedback; generalization off the selection tasks; compute, model/API version, trajectories, and failed attempts; isolation, permissions, rollback, and exact human interventions.

## Safety, Limits, and Governance

> [!WARNING]
> Self-modifying agents execute model-generated code and may alter their own safeguards. Use isolated, disposable environments; least-privilege credentials; immutable evaluators; resource limits; append-only logs; and human approval for promotion. Do not run experimental RSI systems against valuable hosts, secrets, or production infrastructure.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[SHE](https://arxiv.org/abs/2608.09885)**<br>2026 | **Self-modification**<br>Attributes rollout failures to System Prompt, Rule Bank, Safety Memory, or Tool Policy, then retains bounded edits through safety–utility validation.<br><details open><summary>Boundary</summary>Safety-harness evolution under a designed attribution and validation gate, not unrestricted self-rewrite of safety policy.</details> | [Official&nbsp;code](https://github.com/RainbowQTT/SHE) |
| **[SafeEvolve](https://arxiv.org/abs/2609.02786)**<br>2026 | **Self-training**<br>Co-evolves bounded, reversible safety prompts and skills with model-policy updates from on-policy trajectories.<br><details open><summary>Boundary</summary>Reversibility is a designed requirement. Safety–utility tradeoffs are evaluated, not solved in general.</details> | [Official&nbsp;code](https://github.com/MaoPopovich/SafeEvolve) |
| **[EvoUndo](https://arxiv.org/abs/2608.28363)**<br>2026 | **Evaluation / safety**<br>Treats recoverability across counterfactual states as a promotion requirement for persistent harness changes.<br><details open><summary>Boundary</summary>A recoverability criterion for harness evolution, not a self-improving agent.</details> | — |
| **[Your Agent May Misevolve](https://arxiv.org/abs/2509.26354)**<br>2025 | **Evaluation / safety**<br>Measures harmful drift across model, memory, tool, and workflow evolution.<br><details open><summary>Boundary</summary>A misevolution benchmark and threat study, not a beneficial improver.</details> | [Official&nbsp;code](https://github.com/ShaoShuai0605/Misevolution) |
| **[Sleeper Agents](https://arxiv.org/abs/2401.05566)**<br>2024 | **Evaluation / safety**<br>Shows safety training may fail to remove deceptive, conditionally triggered behavior.<br><details open><summary>Boundary</summary>A deceptive-alignment evaluation, not an RSI system.</details> | — |
| **[The Curse of Recursion](https://arxiv.org/abs/2305.17493)**<br>2023 | **Evaluation / safety**<br>Repeated training on generated data can cause model collapse.<br><details open><summary>Boundary</summary>A limit of recursive synthetic-data training, not a self-modifying agent.</details> | — |
| **[LLMs Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)**<br>2023 | **Evaluation / safety**<br>Evidence that intrinsic self-correction can degrade performance without external feedback.<br><details open><summary>Boundary</summary>About within-task self-correction, which this list treats as adjacent rather than RSI.</details> | — |
| **[Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390)**<br>2023 | **Evaluation / safety**<br>Empirical study of supervising stronger models with weaker ones.<br><details open><summary>Boundary</summary>Oversight research relevant to RSI evaluators, not a recursive self-improver.</details> | [Official&nbsp;code](https://github.com/openai/weak-to-strong) |

Further safety context: [Risks from Learned Optimization](https://arxiv.org/abs/1906.01820), [Goal Misgeneralization](https://arxiv.org/abs/2105.14111), [Evaluating Goal Drift](https://arxiv.org/abs/2505.02709), [Zombie Agents](https://arxiv.org/abs/2602.15654), [RepliBench](https://arxiv.org/abs/2504.18565), [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964), [Practice Makes Unsafe](https://arxiv.org/abs/2608.12851), [EvoSkill Injection](https://arxiv.org/abs/2608.30429), [Auditing Harness Tampering](https://arxiv.org/abs/2609.00069), [International AI Safety Report](https://internationalaisafetyreport.org/).

## Active GitHub Projects

Star badges are live counts, not evidence of RSI. Paper-associated code in the tables above is listed beside the paper even if the repository is quiet. This section is for runnable systems.

### GitHub / Models

#### GitHub / Models / Training Research

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| autoresearch | [GitHub](https://github.com/karpathy/autoresearch) | [![star](https://img.shields.io/github/stars/karpathy/autoresearch?style=flat-square&label=star&color=e75b31)](https://github.com/karpathy/autoresearch) | `model-training`<br>`experiment-loop`<br>`validation` | **Bounded optimization**<br>An AI agent autonomously modifies a small LLM training script, runs short experiments, evaluates validation loss, and keeps or discards each change.<br><details open><summary>Boundary</summary>The agent modifies an external training target, not its own weights or improvement procedure. The single-file loop and short budget constrain what can be explored.</details> |
| RD-Agent / FT-Agent | [GitHub](https://github.com/microsoft/RD-Agent) | [![star](https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat-square&label=star&color=e75b31)](https://github.com/microsoft/RD-Agent) | `model-training`<br>`experiment-loop`<br>`validation` | **Bounded optimization**<br>FT-Agent generates data-processing code and training configurations, fine-tunes a target LLM, then uses validation feedback to refine the next experiment.<br><details open><summary>Boundary</summary>This improves an external target model, not the planner's own weights; test splits are reserved for final reporting.</details> |
| OpenRSI / OpenMLE | [GitHub](https://github.com/FrontisAI/OpenRSI) | [![star](https://img.shields.io/github/stars/FrontisAI/OpenRSI?style=flat-square&label=star&color=e75b31)](https://github.com/FrontisAI/OpenRSI) | `model-training`<br>`meta-evolution`<br>`program-evolution` | **Bounded optimization**<br>OpenMLE-Gym builds ML task packages, OpenMLE-ERL trains program-evolution operators, and OpenMLE-Evo runs long-horizon search; search produces experience that re-enters training.<br><details open><summary>Boundary</summary>Meta-evolution operates within bounded ML engineering tasks. Atomic operators and composition rules are human-designed.</details> |

#### GitHub / Models / Recursive Self-Training

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| J-Zero | [GitHub](https://github.com/GyoukChu/J-Zero) | [![star](https://img.shields.io/github/stars/GyoukChu/J-Zero?style=flat-square&label=star&color=e75b31)](https://github.com/GyoukChu/J-Zero) | `self-training`<br>`recursive-learning` | **Self-training**<br>Co-trains a task Challenger, Solver and Judge across rounds; preference pairs update the Judge that rewards later policy training.<br><details open><summary>Boundary</summary>The Judge starts from a pretrained reward checkpoint. Ten-round gains do not establish unbounded improvement.</details> |

### GitHub / Harness

#### GitHub / Harness / Self-Modification

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Prime Agent | [GitHub](https://github.com/PrimeIntellect-ai/prime-agent) | [![star](https://img.shields.io/github/stars/PrimeIntellect-ai/prime-agent?style=flat-square&label=star&color=e75b31)](https://github.com/PrimeIntellect-ai/prime-agent) | `self-refinement`<br>`continual-harness`<br>`rollback` | **Self-modification**<br>Reviews trajectories with /refine and retains evidence-backed updates to supplemental prompts, memory, skill descriptions and subagent specifications; snapshots allow rollback.<br><details open><summary>Boundary</summary>The base system prompt is immutable. Refinement does not retrain model weights.</details> |
| HyperAgents | [GitHub](https://github.com/facebookresearch/HyperAgents) | [![star](https://img.shields.io/github/stars/facebookresearch/HyperAgents?style=flat-square&label=star&color=e75b31)](https://github.com/facebookresearch/HyperAgents) | `self-modification`<br>`meta-agent`<br>`archive` | **Self-modification**<br>Integrates task and meta agents in one editable program; evaluated descendants can change both task behavior and the procedure that generates subsequent agents.<br><details open><summary>Boundary</summary>Empirical task-bounded experiments, not proof of indefinite improvement or foundation-model weight self-training.</details> |
| SIA | [GitHub](https://github.com/hexo-ai/sia) | [![star](https://img.shields.io/github/stars/hexo-ai/sia?style=flat-square&label=star&color=e75b31)](https://github.com/hexo-ai/sia) | `self-modification`<br>`weight-update`<br>`harness-evolution` | **Self-modification**<br>A Feedback-Agent updates both harness code and task-agent weights across generations.<br><details open><summary>Boundary</summary>The Feedback-Agent remains fixed. Benchmark-specific evaluators define fitness.</details> |
| Darwin Gödel Machine | [GitHub](https://github.com/jennyzzt/dgm) | [![star](https://img.shields.io/github/stars/jennyzzt/dgm?style=flat-square&label=star&color=e75b31)](https://github.com/jennyzzt/dgm) | `self-modification`<br>`archive`<br>`coding-agent` | **Self-modification**<br>Modifies its own coding-agent implementation, evaluates descendants, and branches from an archive.<br><details open><summary>Boundary</summary>Empirical code-level self-improvement with frozen foundation-model weights. Sandbox escape and reward hacking remain concerns.</details> |
| Gödel Agent | [GitHub](https://github.com/Arvid-pku/Godel_Agent) | [![star](https://img.shields.io/github/stars/Arvid-pku/Godel_Agent?style=flat-square&label=star&color=e75b31)](https://github.com/Arvid-pku/Godel_Agent) | `self-modification`<br>`self-reference` | **Self-modification**<br>Recursively revises agent logic under high-level objectives rather than a fixed task pipeline.<br><details open><summary>Boundary</summary>Empirical evaluations, not proofs of beneficial rewrites.</details> |
| SICA | [GitHub](https://github.com/MaximeRobeyns/self_improving_coding_agent) | [![star](https://img.shields.io/github/stars/MaximeRobeyns/self_improving_coding_agent?style=flat-square&label=star&color=e75b31)](https://github.com/MaximeRobeyns/self_improving_coding_agent) | `self-modification`<br>`coding-agent` | **Self-modification**<br>A coding agent edits and benchmarks its own codebase.<br><details open><summary>Boundary</summary>Fixed LLM weights. Benchmark subsets do not establish unlimited progress.</details> |
| Huxley-Gödel Machine | [GitHub](https://github.com/metauto-ai/HGM) | [![star](https://img.shields.io/github/stars/metauto-ai/HGM?style=flat-square&label=star&color=e75b31)](https://github.com/metauto-ai/HGM) | `self-modification`<br>`lineage` | **Self-modification**<br>Uses descendant performance to guide which coding-agent lineages to rewrite next.<br><details open><summary>Boundary</summary>Clade statistics are not proofs of globally optimal rewrites.</details> |
| MOSS | [GitHub](https://github.com/hkgai-official/Moss) | [![star](https://img.shields.io/github/stars/hkgai-official/Moss?style=flat-square&label=star&color=e75b31)](https://github.com/hkgai-official/Moss) | `self-modification`<br>`rollback` | **Self-modification**<br>Rewrites TypeScript source, replays failures, and promotes container images through approval and rollback.<br><details open><summary>Boundary</summary>Gated source-level rewriting, not unrestricted RSI.</details> |
| Ouroboros | [GitHub](https://github.com/razzant/ouroboros) | [![star](https://img.shields.io/github/stars/razzant/ouroboros?style=flat-square&label=star&color=e75b31)](https://github.com/razzant/ouroboros) | `self-modification`<br>`review-gate` | **Self-modification**<br>Reviewed commits to tools, prompts, context assembly, and core code become later runtime.<br><details open><summary>Boundary</summary>Separate-agent review and frozen snapshots gate promotion.</details> |
| Proteus | [GitHub](https://github.com/proteus-evolve/Proteus) | [![star](https://img.shields.io/github/stars/proteus-evolve/Proteus?style=flat-square&label=star&color=e75b31)](https://github.com/proteus-evolve/Proteus) | `self-modification`<br>`validation`<br>`snapshots` | **Self-modification**<br>Harness-agnostic framework: each episode starts with fresh model context, the agent edits declared harness surfaces, and source changes activate only after validation, with versioned snapshots.<br><details open><summary>Boundary</summary>Declared mutation surfaces and validation gates are operator-defined. This is infrastructure for measuring self-evolution, not a claim of unbounded RSI.</details> |
| Metaⁿ | [GitHub](https://github.com/minnesotanlp/meta-n) | [![star](https://img.shields.io/github/stars/minnesotanlp/meta-n?style=flat-square&label=star&color=e75b31)](https://github.com/minnesotanlp/meta-n) | `self-modification`<br>`meta-improvement` | **Self-modification**<br>Repeatedly applies a fixed meta-operation to an evolving solver stack and archives evaluated layer chains.<br><details open><summary>Boundary</summary>The meta-operation itself is not rewritten. Runs plateau at finite depth.</details> |

#### GitHub / Harness / Prompt and Workflow Optimization

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| DSPy | [GitHub](https://github.com/stanfordnlp/dspy) | [![star](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=star&color=e75b31)](https://github.com/stanfordnlp/dspy) | `prompt-optimization`<br>`demonstrations`<br>`metrics` | **Bounded optimization**<br>Compiles LM programs by optimizing instructions and demonstrations against task metrics.<br><details open><summary>Boundary</summary>Included for its optimizers. Prompt compilation does not by itself modify the optimizer or model weights.</details> |
| GEPA | [GitHub](https://github.com/gepa-ai/gepa) | [![star](https://img.shields.io/github/stars/gepa-ai/gepa?style=flat-square&label=star&color=e75b31)](https://github.com/gepa-ai/gepa) | `reflection`<br>`pareto-selection`<br>`prompt-optimization` | **Bounded optimization**<br>Reflects on traces and evaluator feedback to propose prompt revisions, retaining complementary candidates through Pareto selection.<br><details open><summary>Boundary</summary>Optimizes prompts with fixed model weights by default.</details> |
| EvoAgentX | [GitHub](https://github.com/ANative-Lab/EvoAgentX) | [![star](https://img.shields.io/github/stars/ANative-Lab/EvoAgentX?style=flat-square&label=star&color=e75b31)](https://github.com/ANative-Lab/EvoAgentX) | `workflow-optimization`<br>`aflow`<br>`validation` | **Bounded optimization**<br>Runs AFlow, TextGrad, MIPRO and EvoPrompt over agent workflows with separate test evaluation.<br><details open><summary>Boundary</summary>Objectives and search algorithms are human-specified.</details> |
| Reef | [GitHub](https://github.com/Human-Agent-Society/reef) | [![star](https://img.shields.io/github/stars/Human-Agent-Society/reef?style=flat-square&label=star&color=e75b31)](https://github.com/Human-Agent-Society/reef) | `harness-evolution`<br>`evaluation-gate`<br>`live-traffic` | **Bounded optimization**<br>Serves live agent traffic, records receipts, and publishes a versioned harness-tree mutation only when the candidate beats the current tree on configured tasks. Can also propose weight updates.<br><details open><summary>Boundary</summary>The proposer, matching, and evaluation gate are operator-defined and fixed across rounds in the documented harness recipe.</details> |
| ADAS | [GitHub](https://github.com/ShengranHu/ADAS) | [![star](https://img.shields.io/github/stars/ShengranHu/ADAS?style=flat-square&label=star&color=e75b31)](https://github.com/ShengranHu/ADAS) | `agent-search`<br>`meta-agent` | **Bounded optimization**<br>Searches for agent programs with a fixed meta-agent.<br><details open><summary>Boundary</summary>The designer is not rewritten.</details> |

### GitHub / Artifacts

#### GitHub / Artifacts / Program Evolution

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| OpenEvolve | [GitHub](https://github.com/algorithmicsuperintelligence/openevolve) | [![star](https://img.shields.io/github/stars/algorithmicsuperintelligence/openevolve?style=flat-square&label=star&color=e75b31)](https://github.com/algorithmicsuperintelligence/openevolve) | `program-evolution`<br>`evaluator`<br>`archive` | **Bounded optimization**<br>Evolves executable program variants using LLM mutations, task-specific evaluators and an archive that seeds subsequent generations.<br><details open><summary>Boundary</summary>Programs are the improvement target. This is not official AlphaEvolve code, nor recursive proposer-weight training.</details> |
| ShinkaEvolve | [GitHub](https://github.com/SakanaAI/ShinkaEvolve) | [![star](https://img.shields.io/github/stars/SakanaAI/ShinkaEvolve?style=flat-square&label=star&color=e75b31)](https://github.com/SakanaAI/ShinkaEvolve) | `program-evolution`<br>`novelty`<br>`ai-training` | **Bounded optimization**<br>Evolves programs with parent sampling, novelty rejection and bandit-based LLM selection; evaluated successors re-enter the archive.<br><details open><summary>Boundary</summary>The evaluator and evolutionary machinery are supplied by researchers.</details> |
| The AI Scientist | [GitHub](https://github.com/SakanaAI/AI-Scientist) | [![star](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=star&color=e75b31)](https://github.com/SakanaAI/AI-Scientist) | `automated-research`<br>`review` | **Bounded optimization**<br>Idea generation, experiments, paper writing, and automated reviewing; saved reviews inform later ideas.<br><details open><summary>Boundary</summary>Self-review and flawed comparisons remain risks. Accidental self-modification of execution scripts is a safety failure, not beneficial RSI.</details> |
| AIDE | [GitHub](https://github.com/WecoAI/aideml) | [![star](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square&label=star&color=e75b31)](https://github.com/WecoAI/aideml) | `ml-engineering`<br>`tree-search` | **Bounded optimization**<br>Tree-search ML engineering agent for iterative experiment design.<br><details open><summary>Boundary</summary>Optimizes an external Kaggle-style solution, not the searcher.</details> |
| CORAL | [GitHub](https://github.com/Human-Agent-Society/CORAL) | [![star](https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=flat-square&label=star&color=e75b31)](https://github.com/Human-Agent-Society/CORAL) | `multi-agent`<br>`shared-skills` | **Bounded optimization**<br>Evolves research code and agent organization from grader-scored commits and shared experience.<br><details open><summary>Boundary</summary>Organization-level evolution under a designed grader, not unrestricted RSI.</details> |

#### GitHub / Artifacts / Learned Skills

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Hermes Agent | [GitHub](https://github.com/NousResearch/hermes-agent) | [![star](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=flat-square&label=star&color=e75b31)](https://github.com/NousResearch/hermes-agent) | `learned-skills`<br>`procedural-memory` | **Experience learning**<br>Creates procedural skills after complex tasks and revises them during use; persistent skills and searchable experience are reused across sessions.<br><details open><summary>Boundary</summary>Experience-driven skill persistence, not model-weight training or independently demonstrated monotonic capability growth.</details> |
| GenericAgent | [GitHub](https://github.com/lsdefine/GenericAgent) | [![star](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=flat-square&label=star&color=e75b31)](https://github.com/lsdefine/GenericAgent) | `skill-learning`<br>`experience-accumulation` | **Bounded optimization**<br>Crystallizes each completed task into a reusable Skill, growing a persistent skill tree from a small seed.<br><details open><summary>Boundary</summary>Skills are stored artifacts. The agent loop and skill-crystallization procedure remain fixed.</details> |
| Voyager | [GitHub](https://github.com/MineDojo/Voyager) | [![star](https://img.shields.io/github/stars/MineDojo/Voyager?style=flat-square&label=star&color=e75b31)](https://github.com/MineDojo/Voyager) | `skill-library`<br>`environment` | **Experience learning**<br>Builds and reuses an executable skill library through Minecraft interaction.<br><details open><summary>Boundary</summary>Frozen LLM plus designed automatic curriculum.</details> |

## Workshops and Related Collections

- [ICLR 2025 Workshop on Scaling Self-Improving Foundation Models](https://sites.google.com/view/ssi-fm-workshop)
- [Awesome Self-Improving Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents)
- [Awesome Autoresearch](https://github.com/webfuse-com/awesome-autoresearch)
- [Awesome LLM Agent Optimization](https://github.com/YoungDubbyDu/LLM-Agent-Optimization)
- [Awesome AI Scientist Papers](https://github.com/openags/Awesome-AI-Scientist-Papers)
- [Awesome Self-Evolving Coding Agents](https://github.com/zhouhao1024/Awesome-Self-Evolving-Coding-Agents)
- [Awesome Reliable Self-Evolving Agents](https://github.com/wkqdzkd/Awesome-Reliable-Self-Evolving-Agents)
- [Awesome Self-Evolving Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)
- [Awesome Harness Evolution](https://github.com/wannabeyourfriend/awesome-harness-evolution)
- [Awesome Longitudinal AI Agents](https://github.com/KevinCL16/awesome-longitudinal-ai-agents)

## Scope and Curation

RSI means an improved system participates in producing subsequent improvements. This list prioritizes implementations that change their own improvement machinery; related self-training and persistent artifact optimization are labeled separately.

| System behavior | Included? | Typical label |
| --- | --- | --- |
| Revises only the current answer, with no reusable state | Usually no | Output refinement |
| Generates, filters, or repairs data and trains a later model | Yes | **Self-training** |
| Stores experience that changes later behavior | Yes | **Experience learning** |
| Updates prompts, memory, tools, skills, or executable control logic | Yes | **Self-modification** or **Experience learning** |
| Improves the updater, evaluator, mutation policy, or harness engineer used in later rounds | Yes | **Self-modification** (RSI candidate) |
| Optimizes an external artifact while the agent remains fixed | Yes, labeled | **Bounded optimization** |

The unit of analysis is the **deployed agent system**, not only its neural weights. Changing a surface is not automatically recursive improvement. A normal tool-use loop, test runner, RAG framework, or manually maintained skill collection does not qualify.

No entry establishes unbounded autonomous RSI. Within-task refinement, safety evaluation and research agendas are relevant context, not demonstrations of persistent self-improvement.

## AgentR

This index is an [AgentR](https://agentr.dev) research initiative. AgentR is a research lab studying self-learning in autonomous systems: how experience changes what happens next.

[agentr.dev](https://agentr.dev) · [Notes](https://agentr.dev/blog) · [GitHub](https://github.com/agentrhq)

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request. New entries should name the persistent component that changes, the source of evaluation, the mechanism tag, and a specific boundary.
