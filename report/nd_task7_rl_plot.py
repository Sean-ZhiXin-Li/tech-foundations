# ND Task 7 (RL Edition): Training Curve Mini Report

import os
import csv
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 0) SB3 monitor.csv reader

def read_sb3_monitor_csv(path):
    """
    Read stable-baselines3 monitor.csv (skips commented metadata lines).
    Returns a NumPy array of episode rewards.
    """
    rows = []
    with open(path, "r", newline="") as f:
        reader = csv.reader(f)
        for r in reader:
            # Skip metadata lines (#...) and header line (starts with 'r')
            if len(r) == 0 or r[0].startswith("#") or r[0] == "r":
                continue
            rows.append(r)
    # SB3 columns are typically: r,l,t (...). We take r as reward.
    rewards = np.array([float(r[0]) for r in rows], dtype=float)
    return rewards

# 1) Synthetic data generator

def generate_ppo_like_rewards(n_episodes=400, reward_cap=500, noise_std=18.0):
    """
    Create a monotonic-in-expectation reward curve that mimics PPO training:
    - Early episodes: low reward, high variance
    - Mid training: sharp improvement
    - Late training: plateau near a cap (e.g., 500 for CartPole)
    """
    x = np.linspace(0, 1, n_episodes)
    # Smooth S-curve baseline (sigmoid-like)
    baseline = reward_cap * (1 / (1 + np.exp(-10 * (x - 0.55))))
    # Add mild curvature so it doesn't look too perfect
    baseline = 0.92 * baseline + 0.08 * reward_cap * np.sqrt(x)
    # Add noise
    rewards = baseline + np.random.normal(0, noise_std, size=n_episodes)
    # Clamp to [0, reward_cap]
    rewards = np.clip(rewards, 0, reward_cap)
    return rewards

# 2) Moving average utility

def moving_average(arr, k=20):
    """
    Compute simple moving average with window k.
    For the first (k-1) points, the window grows gradually.
    """
    out = []
    for i in range(len(arr)):
        left = max(0, i - k + 1)
        out.append(arr[left:i+1].mean())
    return np.array(out)

# 3) Metrics

def compute_metrics(reward, ma, threshold=450.0):
    """
    Basic metrics for a training curve:
    - final_avg: last moving-average value
    - best_avg: best moving-average value
    - episodes_to_threshold: first episode where ma >= threshold (or -1 if never)
    - slope_last_100: linear slope of last 100 raw rewards (trend)
    """
    final_avg = float(ma[-1])
    best_avg = float(ma.max())

    # Episodes to threshold
    idx = np.where(ma >= threshold)[0]
    episodes_to_threshold = int(idx[0]) if len(idx) > 0 else -1

    # Slope via linear regression over last 100 episodes
    tail = min(100, len(reward))
    y = reward[-tail:]
    x = np.arange(tail, dtype=float)
    # slope = cov(x,y)/var(x)
    slope_last_100 = float(np.cov(x, y, bias=True)[0, 1] / (x.var() + 1e-9))
    return dict(
        final_avg=final_avg,
        best_avg=best_avg,
        episodes_to_threshold=episodes_to_threshold,
        slope_last_100=slope_last_100,
    )

# 4) CLI

def parse_args():
    p = argparse.ArgumentParser(description="ND Task 7 (RL Edition): plot RL training curve")
    p.add_argument("--path", type=str, default=os.path.join("runs", "ND_1", "monitor.csv"),
                   help="Path to SB3 monitor.csv. If missing, synthetic data will be generated.")
    p.add_argument("--k", type=int, default=20, help="Moving average window length")
    p.add_argument("--threshold", type=float, default=450.0, help="MA threshold for milestone episode")
    p.add_argument("--seed", type=int, default=7, help="Random seed (for synthetic data)")
    p.add_argument("--out_csv", type=str, default="nd_task7_rl_data.csv", help="Output CSV path")
    p.add_argument("--out_png", type=str, default="nd_task7_rl_plot.png", help="Output PNG path")
    return p.parse_args()

# 5) Main

def main():
    args = parse_args()
    np.random.seed(args.seed)

    # Decide data source
    if os.path.exists(args.path):
        rewards = read_sb3_monitor_csv(args.path)
        source = "SB3 monitor.csv"
    else:
        rewards = generate_ppo_like_rewards(n_episodes=400, reward_cap=500, noise_std=18.0)
        source = "Synthetic PPO-like"

    # Compute moving average
    ma = moving_average(rewards, k=args.k)

    # Save data to CSV
    df = pd.DataFrame({
        "episode": np.arange(1, len(rewards) + 1),
        "reward": rewards,
        "reward_ma": ma
    })
    df.to_csv(args.out_csv, index=False)

    # Compute metrics
    metrics = compute_metrics(rewards, ma, threshold=args.threshold)
    print("[Metrics]")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")

    # Plot (single chart)
    plt.figure(figsize=(9, 5))
    plt.plot(df["episode"], df["reward"], label="Episode Reward", linewidth=1)
    plt.plot(df["episode"], df["reward_ma"], label=f"Moving Average (k={args.k})", linewidth=2)

    # Annotate threshold crossing
    ep_star = metrics["episodes_to_threshold"]
    if ep_star != -1:
        plt.axvline(ep_star, linestyle=":", linewidth=1)
        plt.text(ep_star + 3, args.threshold + 5, f"MA≥{int(args.threshold)} @ ep {ep_star}", fontsize=9)

    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title(f"RL Training Curve ({source})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.out_png, dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
