# demo_reach_target.py
# Visualize the trajectory of the trained PPO policy in the 2D reach-target env.

import os
import numpy as np
import matplotlib.pyplot as plt

from stable_baselines3 import PPO
from gazebo_env_wrapper import GazeboEnv


def rollout_policy(model_path: str, max_steps: int = 100):
    """
    Run one episode using the trained PPO policy and
    collect the visited states.
    """
    # Create a fresh env (same as training)
    env = GazeboEnv()

    # Load trained PPO model
    model = PPO.load(model_path)

    # Gymnasium reset: returns (obs, info)
    obs, info = env.reset()

    states = []
    states.append(env.state.copy())

    for step in range(max_steps):
        # model.predict expects obs with shape (obs_dim,)
        action, _ = model.predict(obs, deterministic=True)

        # Gymnasium step: (obs, reward, terminated, truncated, info)
        obs, reward, terminated, truncated, info = env.step(action)

        states.append(env.state.copy())

        if terminated or truncated:
            print(f"[INFO] Episode ended at step {step+1}, distance={info['distance']:.4f}")
            break

    env.close()

    return np.array(states), env.target.copy()


def plot_trajectory(states: np.ndarray, target: np.ndarray, out_path: str):
    """
    Plot the 2D trajectory of the agent and save as PNG.
    """
    x = states[:, 0]
    y = states[:, 1]

    plt.figure(figsize=(5, 5))
    # Path
    plt.plot(x, y, marker="o", linewidth=1.5, label="Trajectory")
    # Start point
    plt.scatter(x[0], y[0], s=60, marker="s", label="Start")
    # End point
    plt.scatter(x[-1], y[-1], s=60, marker="o", label="End")
    # Target point
    plt.scatter(target[0], target[1], s=80, marker="*", label="Target")

    plt.xlabel("State[0]")
    plt.ylabel("State[1]")
    plt.title("PPO Policy Trajectory in 2D Reach-Target Env")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[INFO] Trajectory plot saved to: {out_path}")


if __name__ == "__main__":
    LOG_DIR = "./runs/week7_reach_target"
    MODEL_PATH = os.path.join(LOG_DIR, "ppo_reach_target")
    OUT_PATH = os.path.join(LOG_DIR, "trajectory.png")

    # 1) Roll out the trained policy
    states, target = rollout_policy(MODEL_PATH, max_steps=100)

    # 2) Plot trajectory
    plot_trajectory(states, target, OUT_PATH)
