# Contributing to AgentR Awesome RSI

This index is an [AgentR](https://agentr.dev) research initiative. Keep it precise, high-signal, and consistent with AgentR’s research voice: clean, technical, and evidence-first.

The list is maintained by editing `README.md` directly. Prefer primary sources, official implementations, and reproducible artifacts.

## Voice

Write like the rest of [agentr.dev](https://agentr.dev): short, technical, and specific. Name what persists, what the evidence is, and where the claim stops. Avoid marketing adjectives and unverified performance claims.

## Inclusion criteria

An entry should be directly useful for studying recursive self-improvement, persistent self-improvement, automated AI R&D, evaluation, or associated safety questions.

For any system that claims self-improvement, say:

1. **What persists?** Model weights, generated data, curriculum, code, prompts, memory, tools, skills, workflow, evaluator, environment, or another component.
2. **What supplies the signal?** Formal proof, executable verifier, held-out benchmark, environment reward, model judge, or human review.
3. **What is recursive?** Does the system improve the mechanism that creates later improvements, or only a fixed target component?
4. **What is the evidence?** Multi-generation results, baselines, artifacts, and whether the result is author-reported or independently validated.

One-shot answer revision, generic agent frameworks, marketing-only announcements, duplicate links, and abandoned toys with no distinct technical contribution are out of scope.

Paper-linked repositories stay with the paper. **Active GitHub Projects** is only for runnable systems that are not already an official paper companion.

### Data and dataset evolution

Data-centric work belongs here when the system generates, selects, filters, repairs, or reorganizes experience and a later training or decision round consumes that dataset. State the producer, selection signal, consumer, and whether the cycle repeats. Static synthetic datasets and ordinary augmentation are `Bounded optimization` unless they close that loop.

### Engineering reports and blogs

Official technical blogs, engineering reports, and release notes are welcome when they document an implemented system, an evaluation protocol, or concrete lessons. Prefer the publisher's own post. A blog does not replace a paper as the primary research record.

## Labels

Every entry uses a **Focus** line: one improvement mechanism, then two or three research themes.

**Mechanism** (what kind of loop is demonstrated):

- **Self-modification** — agent code or mutable harness state changes and is used in later improvement.
- **Self-training** — internally generated tasks, trajectories, or supervision update retained model weights across iterations.
- **Bounded optimization** — fixed search or evaluation machinery improves prompts, workflows, programs, or external models.
- **Experience learning** — feedback revises durable memory, playbooks, or skills reused in later tasks.
- **Evaluation** — a study of loop validity, reward hacking, sabotage, or measurement; not a beneficial self-improver.
- **Research agenda** — a proposed route to RSI, separated from demonstrated results.

When uncertain, use the weaker label and state the limitation in **Evidence**. Classification is about the demonstrated system, not its stated ambition. No label proves unbounded autonomous RSI.

## Entry format

Every research item uses this researcher-maintained format:

```markdown
**[Organization — Title](https://example.com)**
Date · Source Type
Focus: Mechanism · Theme · Theme

> One-sentence summary of what the system or paper actually does.

Why it matters: Its research significance, not a restatement of the quote.
Evidence: Who reported the result, and whether independent validation exists.
```

Link official code from **Evidence** when it exists. Do not treat a GitHub star count as scientific validation.

Example:

```markdown
**[Sakana AI — The Darwin Gödel Machine](https://sakana.ai/dgm/)**
May 30, 2025 · Research Blog
Focus: Self-modification · Evolutionary search · Agentic coding

> An agent iteratively rewrites its own code, evaluates descendants on coding benchmarks, and retains successful modifications for further evolution.

Why it matters: Introduces an explicit mechanism for iterative agent self-improvement.
Evidence: Company-reported results; independent replication not established.
```

**Evidence** must distinguish reported results from independent validation. Typical lines:

- `Company-reported results; independent replication not established.`
- `Author-reported results with official code; independent replication not established. [Code](https://github.com/org/repo).`
- `Evaluation protocol; does not itself demonstrate recursive self-improvement.`
- `Formal or position argument; not an empirical demonstration of RSI.`
- `Secondary synthesis; not a primary experimental result.`
- `Public implementation; repository activity is not independent scientific validation.`

A short scientific limit may follow the validation sentence. Do not paste the abstract. Do not report unverified performance claims.

`scripts/format_catalog.py` has `entry()` plus those evidence strings if you want a formatter.

## Pull requests

- Add one item per pull request when practical.
- Place it in the narrowest relevant section.
- Use **Organization — Title** and the canonical paper, publisher, or arXiv abstract.
- Confirm that every added link resolves.

### Placement

- **Papers / Harness** — self-reference and retained control procedures
- **Papers / Models** — iterative weight, curriculum, or evaluator training
- **Papers / Experience** — persistent memory and skills
- **Papers / Theory and Evaluation** — measurement or formal work
- First-party mechanism blogs go in **Mechanisms and Results**. Supporting methods, evaluations, agendas, and historical tutorials go in those subsections.

## Safety

Do not contribute instructions that encourage running self-modifying code with broad host access or production credentials. Projects that execute generated code should document isolation, permissions, resource limits, logs, and rollback behavior.
