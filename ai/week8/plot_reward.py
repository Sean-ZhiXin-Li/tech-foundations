import numpy as np
import matplotlib.pyplot as plt
import csv

def smooth(x, weight=0.9):
    smoothed = []
    last = x[0]
    for v in x:
        last = weight * last + (1 - weight) * v
        smoothed.append(last)
    return np.array(smoothed)

def load_monitor_csv(path):
    rewards = []

    with open(path, "r") as f:
        reader = csv.reader(f)

        # 跳过 JSON header 或注释行
        for row in reader:
            if len(row) == 0:
                continue
            if row[0].startswith("#"):     # #{"t_start": ...}
                continue
            if row[0] == "r":              # header: r,l,t
                continue
            # 转 float，只取 reward
            rewards.append(float(row[0]))

    return np.array(rewards)

def main():
    path = r"E:\FT\ai\week7\runs\week7_reach_target\monitor.csv"

    rewards = load_monitor_csv(path)
    smoothed = smooth(rewards, 0.95)

    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.4, label="raw")
    plt.plot(smoothed, linewidth=2, label="smoothed")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title("Week7 PPO Training Curve (Smoothed)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("reward_curve_smoothed.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    main()
