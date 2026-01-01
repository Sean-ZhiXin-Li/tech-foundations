# ND Task Rewrite — RL Training Curve Analysis

> Source: ND Task 7 (RL Edition)
> Rewrite date: 2025-12-28
> Rule: Rewrite only. No new experiments. No code changes.

---

## 1) Goal

Verify that a reinforcement learning training log can be systematically processed into quantitative metrics and visualizations using a reproducible analysis pipeline.

Success is defined by producing consistent summary metrics and a training curve from an existing Stable-Baselines3 (SB3) monitor log.

---

## 2) Setup

* Code location: `report/nd_task7_rl_plot.py`
* Framework: Stable-Baselines3 (PPO)
* Environment: Python (version not explicitly recorded)
* Data source: `runs/ND_1/monitor.csv`
* Command:

  ```bash
  python report/nd_task7_rl_plot.py --path "runs/ND_1/monitor.csv" --k 20 --threshold 450 --seed 7
  ```

---

## 3) Key Parameters

* algorithm: PPO
* moving average window (k): 20
* reward threshold: 450
* random seed: 7
* metric window for slope computation: last 100 episodes
* input log file: `monitor.csv`

---

## 4) Observations

* Final moving average reward (k = 20): 292.25
* Best moving average reward (k = 20): 299.20
* Moving average did not reach the threshold value of 450 within the recorded episodes.
* Slope of the last 100 episodes: 3.2064
* Raw episode rewards exhibited high variance with an overall upward trend.
* Training curve exported as `nd_task7_rl_plot.png`.
* Processed episode data exported as `nd_task7_rl_data.csv`.

---

## 5) What This Prepares Me For

* Establishes a reproducible pipeline for extracting quantitative metrics from reinforcement learning training logs.
* Provides a standardized method for comparing training curves across different runs or controller variants.
* Supports future ablation studies by separating data processing and visualization from training execution.
* Locks in a reusable reporting structure applicable to larger control or simulation projects.
