import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
import  matplotlib.pyplot as plt
import pandas as pd

def make_env():
    env = gym.make("CartPole-v1")
    env = Monitor(env, "runs/ND_1/monitor.csv")
    return env

env = DummyVecEnv([make_env])

model = PPO("MlpPolicy", env, verbose = 1)

model.learn(total_timesteps = 20000)

model.save("runs/ND_1/ppo_cartpole.zip")

df = pd.read_csv("runs/ND_1/monitor.csv", comment = "#")
rewards = df["r"].values

plt.plot(rewards, label = "Episode Reward")
window = 20
smooth = pd.Series(rewards).rolling(window).mean()
plt.plot(smooth, label = "Moving Average (20)")
plt.xlabel("Episode")
plt.ylabel("Rewards")
plt.legend()
plt.title("Cartpole PPO Training")
plt.savefig("reward_curve.png")
plt.show()