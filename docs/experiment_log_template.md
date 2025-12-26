# Experiment Log Template (Tech Foundations)

> Purpose: A standardized, reusable format for recording experiments in Tech Foundations (FT).
> Rule: Every FT experiment log must use exactly the five sections below. Do not add new sections.

---

## 1) Goal

Write 1–3 sentences:
- What question are you trying to answer?
- What would count as a “successful” outcome?

---

## 2) Setup

Describe only what is necessary to reproduce the run:
- Code location (file / folder)
- Environment (OS, Python version, key libs if relevant)
- Command(s) used to run
- Input data or scenario

Keep it short and concrete.

---

## 3) Key Parameters

List only the parameters that matter for interpretation.
Use bullet points or a small table, e.g.:

- seed:
- steps / episodes:
- learning rate (if any):
- controller mode:
- scenario:
- hardware/simulator version (if relevant):

---

## 4) Observations

Report what happened, with evidence:
- Metrics (numbers)
- Plots (file name if saved)
- Failure modes (if any)
- Unexpected behavior

Avoid explanations here. Just state observations.

---

## 5) What This Prepares Me For

Write 2–5 bullets:
- Which future project component does this support?
- What ability does it “lock in”?
- What is the next experiment this enables?

Examples:
- “Provides a baseline for comparing controller variants.”
- “Establishes a reproducible run command and logging format.”
- “Enables ablation testing under the same scenario.”
