# ND Task 7 (RL Edition) — Training Curve Mini Report

**Date:** 2025-10-11  
**Author:** Zhixin Li (Sean)

---

## 1. Objective
To visualize a reinforcement learning (RL) training process by reading a `monitor.csv` log from Stable-Baselines3 (SB3), computing moving averages, and extracting key learning metrics for a concise experimental report.

---

## 2. Method
- **Data Source:** `runs/ND_1/monitor.csv`
- **Framework:** Stable-Baselines3 (PPO)
- **Visualization Tool:** Matplotlib  
- **Processing:**  
  - Parse monitor file and filter out metadata/header lines  
  - Compute moving average (k = 20)  
  - Extract metrics including:
    - Final average reward
    - Best moving average
    - Episode reaching MA ≥ 450
    - Slope of the last 100 episodes  
  - Export processed data to CSV and render the plot.

---

## 3. Results

**Command**
```bash
python report/nd_task7_rl_plot.py --path "runs/ND_1/monitor.csv" --k 20 --threshold 450 --seed 7
```

**Metrics**
| Metric | Value |
|:--|--:|
| Final MA (k=20) | 292.25 |
| Best MA (k=20) | 299.20 |
| Episodes to MA ≥ 450 | -1 *(not reached)* |
| Slope of last 100 | 3.2064 |

**Figure**  
![RL Training Curve](./nd_task7_rl_plot.png)

---

## 4. Observation
The raw episode rewards exhibit high variance with a gradual upward trend.  
The moving average rises significantly after episode ~240 but remains below 300 at the end of training.  
The overall pattern indicates learning progress but incomplete convergence — consistent with a short, untuned PPO run.

---

## 5. Discussion
This task was conducted as a **practice exercise** rather than a formal training experiment.  
The purpose was to rehearse the full analysis workflow, not to achieve optimal numerical results.

Despite the limited number of episodes and non-optimized hyperparameters,  
the experiment successfully demonstrated:
- Reading and cleaning SB3 monitor logs  
- Computing moving averages and extracting performance metrics  
- Visualizing reward evolution using Matplotlib  
- Generating reproducible CSV and PNG outputs

Future work will focus on **longer training** and **policy stability analysis** once the technical pipeline is fully established.

---

## 6. Files
- `report/nd_task7_rl_plot.py` — plotting and analysis script  
- `nd_task7_rl_data.csv` — processed episode data  
- `nd_task7_rl_plot.png` — visualization output  

---

## 7. Conclusion
The task achieved its learning objective: building a self-contained, reproducible RL reporting workflow.  
Numerical performance was not the priority for this session.

---

## Appendix – Mathematical Notes

The general form of the **discounted return** in reinforcement learning is:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$

where  
- \( G_t \): total discounted reward at time \( t \)  
- \( R_{t+k+1} \): reward received at step \( t+k+1 \)  
- \( \gamma \): discount factor, \( 0 < \gamma < 1 \)

This formulation emphasizes the importance of future rewards while discounting them by a factor of \( \gamma^k \), ensuring that near-term outcomes are prioritized but long-term performance is still considered.
