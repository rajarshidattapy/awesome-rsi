# Contributing to AgentR Awesome RSI

This index is an [AgentR](https://agentr.dev) research initiative. Keep it precise, high-signal, and consistent with AgentR’s research voice: clean, technical, and evidence-first.

The list is maintained by editing `README.md` directly. Prefer primary sources, official implementations, and reproducible artifacts.

Star badges use AgentR orange (`#e75b31`). Do not introduce new badge colors.

## Voice

Write like the rest of [agentr.dev](https://agentr.dev): short, technical, and specific. Name what persists, what the evidence is, and where the claim stops. Avoid marketing adjectives and unverified performance claims.

## Inclusion criteria

An entry should be directly useful for studying recursive self-improvement, persistent self-improvement, automated AI R&D, evaluation, or associated safety questions.

For any system that claims self-improvement, say:

1. **What persists?** Model weights, generated data, curriculum, code, prompts, memory, tools, skills, workflow, evaluator, environment, or another component.
2. **What supplies the signal?** Formal proof, executable verifier, held-out benchmark, environment reward, model judge, or human review.
3. **What is recursive?** Does the system improve the mechanism that creates later improvements, or only a fixed target component?
4. **What is the evidence?** Multi-generation results, baselines, artifacts, and a specific limitation.

One-shot answer revision, generic agent frameworks, marketing-only announcements, duplicate links, and abandoned toys with no distinct technical contribution are out of scope.

### Data and dataset evolution

Data-centric work belongs here when the system generates, selects, filters, repairs, or reorganizes experience and a later training or decision round consumes that dataset. State the producer, selection signal, consumer, and whether the cycle repeats. Static synthetic datasets and ordinary augmentation are `Bounded optimization` / enablers unless they close that loop.

### Engineering reports and blogs

Official technical blogs, engineering reports, and release notes are welcome when they document an implemented system, an evaluation protocol, or concrete lessons. Prefer the publisher's own post. A blog does not replace a paper as the primary research record.

## Labels and tags

Every paper, blog, and project uses one **improvement mechanism** and one **surface** tag.

**Mechanism** (what kind of loop is demonstrated):

- **Self-modification** — agent code or mutable harness state changes and is used in later improvement.
- **Self-training** — internally generated tasks, trajectories, or supervision update retained model weights across iterations.
- **Bounded optimization** — fixed search or evaluation machinery improves prompts, workflows, programs, or external models.
- **Experience learning** — feedback revises durable memory, playbooks, or skills reused in later tasks.
- **Evaluation / safety** — a study of loop validity, reward hacking, sabotage, or measurement; not a beneficial self-improver.
- **Research agenda** — a proposed route to RSI, separated from demonstrated results.

**Surface** (what changes):

- `Harness` — agent implementations, prompts, workflows, control procedures
- `Models` — weights, training processes, curricula, evaluators that update parameters
- `Artifacts` — executable programs, skills, datasets, experiment recipes

When uncertain, use the weaker label and state the limitation. Classification is about the demonstrated system, not its stated ambition. No label proves unbounded autonomous RSI.

## Pull requests

- Add one item per pull request when practical.
- Place it in the narrowest relevant section.
- Use a short display name in the table and link the canonical paper, publisher, or arXiv abstract.
- Link official code when it exists. Use `—` when no author-linked implementation was established; that does not assert that none exists.
- Write a factual mechanism sentence and a specific **Boundary**. Do not copy the abstract. Do not report unverified performance claims.
- Confirm that every added link resolves.

### Papers

```markdown
| **[Short Name](https://arxiv.org/abs/....)**<br>YYYY-MM-DD | **Self-modification**<br>What changes, how it is evaluated, and what is reused later.<br><details open><summary>Boundary</summary>The strongest honest limit.</details> | [Official&nbsp;code](https://github.com/org/repo)<br>[![star](https://img.shields.io/github/stars/org/repo?style=flat-square&label=star&color=e75b31)](https://github.com/org/repo) |
```

Use **Papers / Harness** for self-reference, **Papers / Models** for iterative weight learning, **Papers / Experience** for persistent memory and skills, and **Papers / Theory and Evaluation** for measurement or formal work.

### Blogs

```markdown
- **[Title](https://example.com/post)** — Publisher · YYYY-MM-DD
  - `Harness` · **Self-modification** — What the post documents.
  - **Boundary:** The strongest honest limit.
```

Put first-party mechanism results in **Mechanisms and Results**. Supporting methods, evaluations, agendas, and historical tutorials go in those subsections.

### GitHub projects

```markdown
| Project | [GitHub](https://github.com/org/repo) | [![star](https://img.shields.io/github/stars/org/repo?style=flat-square&label=star&color=e75b31)](https://github.com/org/repo) | `tag-one`<br>`tag-two` | **Self-modification**<br>What the implementation does.<br><details open><summary>Boundary</summary>Limit.</details> |
```

A self-evolving name is not evidence. Record what changes, the feedback, the retained state, and the limitation.

## Safety

Do not contribute instructions that encourage running self-modifying code with broad host access or production credentials. Projects that execute generated code should document isolation, permissions, resource limits, logs, and rollback behavior.
