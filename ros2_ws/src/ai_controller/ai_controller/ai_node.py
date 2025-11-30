import random

import rclpy
from rclpy.node import Node


class DummyModel:
    def __init__(self):
        self.step = 0

    def predict(self, obs):
        self.step += 1
        x = float(obs[0]) if len(obs) > 0 else 0.0
        y = float(obs[1]) if len(obs) > 1 else 0.0

        base_ax = -0.1 * x
        base_ay = -0.1 * y

        noise_ax = 0.01 * (random.random() - 0.5)
        noise_ay = 0.01 * (random.random() - 0.5)

        action = [base_ax + noise_ax, base_ay + noise_ay]
        return action, None


class AINode(Node):
    def __init__(self):
        super().__init__("ai_node")

        self.model = DummyModel()
        self.get_logger().info("AI Node started with DummyModel (no PPO yet).")

        self.timer = self.create_timer(0.1, self.control_loop)
        self.obs = [1.0, -1.0]

    def control_loop(self):
        action, _ = self.model.predict(self.obs)
        self.get_logger().info(f"Predicted action: {action}")


def main(args=None):
    rclpy.init(args=args)
    node = AINode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
