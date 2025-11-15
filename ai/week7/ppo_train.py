# ppo_train.py
# PPO training script for the toy 2D reach-target task

import os
import numpy as np
import matplotlib.pyplot as plt

from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

from gazebo_env_wrapper import GazeboEnv


def make_env(log_dir: str):
    """
    Create monitored GazeboEnv for SB3.
    """
    env = GazeboEnv()
    env = Monitor(env, log_dir)  # this will save monitor.csv
    return env


def train_ppo(log_dir: str, total_timesteps: int = 20000):
    """
    Train PPO on the toy 2D reach-target env.
    """
    # Create log dir if needed
    os.makedirs(log_dir, exist_ok=True)

    # Create environment
    env = make_env(log_dir)

    # Build PPO model with default MLP policy
    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
    )

    # Run learning
    model.learn(total_timesteps=total_timesteps)

    # Save trained model
    model_path = os.path.join(log_dir, "ppo_reach_target")
    model.save(model_path)
    print(f"[INFO] Model saved to: {model_path}")

    env.close()


def plot_reward_curve(log_dir: str, window: int = 50):
    """
    Read monitor.csv and plot episode rewards.
    """
    monitor_file = None
    # Find monitor file
    for f in os.listdir(log_dir):
        if f.startswith("monitor") and f.endswith(".csv"):
            monitor_file = os.path.join(log_dir, f)
            break

    if monitor_file is None:
        print("[WARN] No monitor.csv file found, skip plotting.")
        return

    # Read monitor file (skip comment lines)
    rewards = []
    with open(monitor_file, "r", encoding="utf-8") as f:
        for line in f:
            # Skip comment lines
            if line.startswith("#"):
                continue

            parts = line.strip().split(",")

            # Skip header line like: r,l,t
            if len(parts) >= 3 and parts[0] == "r" and parts[1] == "l":
                continue

            if len(parts) >= 1:
                try:
                    r = float(parts[0])
                except ValueError:
                    # Skip any malformed line
                    continue
                rewards.append(r)

    if len(rewards) == 0:
        print("[WARN] Empty reward list.")
        return

    rewards = np.array(rewards)

    # Moving average for smoother curve
    def moving_average(x, k):
        if k <= 1:
            return x
        ret = np.cumsum(x, dtype=float)
        ret[k:] = ret[k:] - ret[:-k]
        return ret[k - 1:] / k

    ma_rewards = moving_average(rewards, window)

    # Plot
    plt.figure()
    plt.plot(rewards, label="Episode reward")
    plt.plot(
        np.arange(len(ma_rewards)) + window - 1,
        ma_rewards,
        label=f"Moving avg (window={window})",
    )
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title("PPO on 2D Reach Target (Toy GazeboEnv)")
    plt.legend()
    out_path = os.path.join(log_dir, "reward_curve.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[INFO] Reward curve saved to: {out_path}")


if __name__ == "__main__":
    # You can adjust this path
    LOG_DIR = "./runs/week7_reach_target"

    # 1) Train PPO
    train_ppo(LOG_DIR, total_timesteps=5000)

    # 2) Plot reward curve
    plot_reward_curve(LOG_DIR, window=20)
