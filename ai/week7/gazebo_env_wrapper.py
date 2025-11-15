import gymnasium as gym
import numpy as np
from gymnasium import spaces


class GazeboEnv(gym.Env):
    """
    Simple 2D reach-target environment, written in Gymnasium style,
    so it can be used with stable-baselines3 >= 2.0.
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()

        # Action: 2D continuous vector in [-1, 1]
        self.action_space = spaces.Box(
            low=-1.0, high=1.0, shape=(2,), dtype=np.float32
        )

        # Observation: 2D continuous state in [-5, 5]
        self.observation_space = spaces.Box(
            low=-5.0, high=5.0, shape=(2,), dtype=np.float32
        )

        # Target point we want to reach
        self.target = np.array([1.0, 1.0], dtype=np.float32)

        # Internal state
        self.state = np.zeros(2, dtype=np.float32)

        # Step counter for truncation
        self.step_count = 0
        self.max_steps = 100

    def reset(self, *, seed=None, options=None):
        """
        Gymnasium reset API:
        must return (obs, info)
        """
        super().reset(seed=seed)

        self.state = np.zeros(2, dtype=np.float32)
        self.step_count = 0

        info = {}
        return self.state, info

    def step(self, action):
        """
        Gymnasium step API:
        must return (obs, reward, terminated, truncated, info)
        """
        self.step_count += 1

        # Clip action to valid range
        action = np.clip(action, self.action_space.low, self.action_space.high)

        # Simple state update: move towards the target
        self.state = self.state + 0.1 * action

        # Compute distance to target
        dist = np.linalg.norm(self.state - self.target)

        # Reward is negative distance
        reward = -dist

        # Episode ends when we are close enough
        terminated = dist < 0.05

        # Or when we hit max steps
        truncated = self.step_count >= self.max_steps

        info = {"distance": dist}

        return self.state, reward, terminated, truncated, info
