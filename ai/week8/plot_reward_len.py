import csv
import numpy as np
import matplotlib.pyplot as plt


def smooth(x, weight=0.9):
    """Exponential moving average smoothing."""
    smoothed = []
    last = x[0]
    for v in x:
        last = weight * last + (1.0 - weight) * v
        smoothed.append(last)
    return np.array(smoothed)


def load_monitor_two_cols(path):
    """Load rewards and episode lengths from SB3 monitor.csv."""
    rewards = []
    lengths = []

    with open(path, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            # skip empty lines
            if len(row) == 0:
                continue

            # skip JSON header and comments
            if row[0].startswith("#"):
                continue

            # skip column header "r,l,t"
            if row[0].strip().lower() == "r":
                continue

            # row format: r, l, t
            r = float(row[0])
            l = float(row[1])

            rewards.append(r)
            lengths.append(l)

    return np.array(rewards), np.array(lengths)


def main():
    monitor_path = r"E:\FT\ai\week7\runs\week7_reach_target\monitor.csv"

    rewards, lengths = load_monitor_two_cols(monitor_path)
    rewards_s = smooth(rewards, weight=0.95)
    lengths_s = smooth(lengths, weight=0.9)

    # Create figure with 2 subplots (shared x-axis)
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    # --- Top: Reward ---
    ax1 = axes[0]
    ax1.plot(rewards, alpha=0.3, label="raw reward")
    ax1.plot(rewards_s, linewidth=2, label="smoothed reward")
    ax1.set_ylabel("Reward")
    ax1.set_title("Week7 PPO Training: Reward & Episode Length")
    ax1.grid(True)
    ax1.legend()

    # --- Bottom: Episode length ---
    ax2 = axes[1]
    ax2.plot(lengths, alpha=0.3, label="raw episode length")
    ax2.plot(lengths_s, linewidth=2, label="smoothed length")
    ax2.set_xlabel("Episode")
    ax2.set_ylabel("Episode Length")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.savefig("reward_length_week7.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
