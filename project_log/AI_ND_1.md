# Ai_ND · Day 1 — CartPole PPO Baseline

**Goal:** Learn Gymnasium basics, run PPO on CartPole-v1, and visualize the reward curve.

**What I did**
- Built a minimal training pipeline with Gymnasium + Stable-Baselines3 (PPO, MlpPolicy).
- Wrapped the env with `Monitor` to log episodic rewards to CSV.
- Trained for 20k timesteps on CPU and saved the model.
- Plotted episode rewards with a 20-episode moving average.

**Results**
- Episode reward climbed from ~20 to ~250–300 (best spikes near 500).
- Value function fit improved (explained variance peaked ~0.9).

**Artifacts**
- `runs/ND_1_<timestamp>/ppo_cartpole.zip`
- `runs/ND_1_<timestamp>/monitor.csv`
- `runs/ND_1_<timestamp>/reward_curve.png`

**Notes / Next**
- Increase `total_timesteps` to 100k for a smoother curve.
- Try `window=50` for plotting to reduce noise.
- Next: add a short evaluation script and move to imitation vs RL comparison.
