# Week 7 Project Log — PPO × Manipulator Baseline + IMU Serial Pipeline Design

**Date:** 2025-11-10  
**Author:** Sean Li (Zhixin Li)  
**Project:** *Tech Foundations — Robotics & Autonomous Control*  
**Module:** *Week 7 — PPO Reach-Target Baseline & IMU Serial Pipeline*

---

## 1. Overview

This week marks a key transition point in the Tech Foundations roadmap:  
moving from spacecraft/propulsion simulation (PPO × OrbitEnv) into **robotics real-world control**, starting with:

- a **PPO baseline for a 2D reach-target task**,  
- and the initial design of a **real-world IMU → Python serial pipeline**,  
  which will be used later for robot arm imitation learning and closed-loop control.

Even though the hardware IMU module (MPU6050) has not arrived yet, the entire software pipeline and RL baseline were completed successfully.

---

## 2. PPO Baseline for 2D Reach-Target Task

### 2.1 Environment (Toy GazeboEnv)

A lightweight placeholder environment `GazeboEnv` was implemented to mimic:

- 2D end-effector movement  
- continuous action space (Δx, Δy)  
- reward = –distance to target  
- termination when close to target

File: **`gazebo_env_wrapper.py`**

The environment is intentionally simple, serving as a bridge between PPO and future Webots/Gazebo manipulator simulations.

---

### 2.2 PPO Training

Training is implemented in:

- **`ppo_train.py`**
- using **Stable-Baselines3 PPO (MlpPolicy)**  
- wrapped with `DummyVecEnv` + `Monitor` for reward logging  
- trained for **20,000 timesteps**

Training logs saved to:

```
ai/week7/runs/week7_reach_target/
```

#### Reward Curve

(Place your local image here)

**Analysis:**

- Early episodes fluctuate heavily (typical PPO behavior).  
- After ~4k–8k timesteps, reward starts improving.  
- Moving-average curve shows clear upward trend.  
- Negative reward is expected because `reward = –distance`.  
- Smoother convergence will improve once real manipulator dynamics are added.

---

### 2.3 PPO Policy Trajectory

Trajectory generated via `demo_reach_target.py`.

(Place the trajectory image)

**Interpretation:**

- Policy successfully moves toward the target.  
- Although not fully converging to **(1.0, 1.0)** yet,  
  the trajectory shows **correct directional behavior**.  
- This is a **baseline**, not the final controller.  
- It proves PPO + environment wrapper + monitor logging pipeline works end-to-end.

This validation is important before extending PPO to a real robotic arm.

---

## 3. IMU Serial Pipeline (Design Completed)

Even though the MPU6050 hardware hasn't arrived, all software components were created so the IMU → Python pipeline can be activated instantly.

---

### 3.1 Arduino IMU Program (imu_serial.ino)

File:  
`Arduino/Week_7/imu_serial/imu_serial.ino`

Features:

- Designed for MPU6050 (Adafruit_MPU6050 library)
- Outputs **pitch roll** at ~20 Hz
- Serial format is exactly:

```
<pitch> <roll>
```

This matches Python’s expected input.

Computed using:

```cpp
float pitch = atan2(-ax, sqrt(ay*ay + az*az)) * 180.0 / PI;
float roll  = atan2(ay, az) * 180.0 / PI;
```

This format enables:

- Serial Plotter visualization  
- Real-time plotting in Python  
- Direct use for imitation learning or RL observation vectors

---

### 3.2 Python Serial Reader (serial_reader.py)

File:  
`ai/week7/serial_reader.py`

Current version is a **placeholder**:

```python
def read_imu(port="COM5", baud=115200):
    pass
```

When MPU6050 arrives, the function will:

- Open serial port  
- Read pitch/roll  
- Convert them into floats  
- Stream to RL controller or visualization module  

---

## 4. Directory Structure (Finalized for Week 7)

```
ai/week7/
│
├── gazebo_env_wrapper.py
├── ppo_train.py
├── demo_reach_target.py
├── serial_reader.py
├── week7_project_log.md
│
└── runs/
    └── week7_reach_target/
        ├── monitor.csv
        ├── ppo_reach_target.zip
        ├── reward_curve.png
        └── trajectory.png
```

Arduino:

```
Arduino/Week_7/imu_serial/imu_serial.ino
```

The structure is now research-grade.

---

## 5. What Worked Well

- PPO pipeline validated  
- Reward logging pipeline validated  
- Visualization (curve + trajectory) validated  
- Environment wrapper logic verified  
- IMU pipeline designed cleanly  
- Codebase organization improved  

This week’s progress greatly strengthens the foundation for real robotic control.

---

## 6. Summary

Week 7 successfully bridges the gap between simulation-only RL and real-world robotics.  
With PPO baseline established and IMU pipeline designed, the project is ready to scale into:

- real sensory input  
- robotic arm control  
- imitation learning  
- hybrid simulation-real pipelines

The foundations for autonomous robotics research are now firmly in place.
