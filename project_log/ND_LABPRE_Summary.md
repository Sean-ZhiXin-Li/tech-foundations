# ND LABPRE Summary (2025)

**Author:** Zhixin Li (Sean)  
**Duration:** 2025-09-29 → 2025-10-11  
**Goal:** Complete 7 hands-on technical tasks combining electronics, simulation, deep learning, and reinforcement learning to prepare for upcoming Tech Foundations projects.

---

## 🧩 ND Task 1 – Potentiometer → Servo + LED
**Date:** 2025-09-29  
- Built a circuit using Arduino UNO R4 WiFi.  
- Controlled both **servo angle** and **LED brightness** using a potentiometer.  
- Learned analog input mapping, PWM output, and serial debugging.  
- Identified jitter issues and planned upgrade with a precision potentiometer.  
**Status:** ✅ Functional prototype completed.

---

## 🧮 ND Task 2 – AI_ND_1: PPO CartPole Baseline
**Date:** 2025-10-01  
- Learned **Gymnasium** basics and ran **PPO** on `CartPole-v1`.  
- Used Stable-Baselines3 (MlpPolicy) and wrapped the environment with `Monitor` to log episodic rewards.  
- Trained for 20k timesteps and plotted reward curves with a 20-episode moving average.  
- Episode reward climbed from ~20 → ~250–300, best spikes near 500.  
- Artifacts generated:
  - `runs/ND_1_<timestamp>/ppo_cartpole.zip`
  - `runs/ND_1_<timestamp>/monitor.csv`
  - `runs/ND_1_<timestamp>/reward_curve.png`
**Status:** ✅ PPO baseline completed and logged successfully.

---

## ⚙️ ND Task 3 – Webots e-puck Demo
**Date:** 2025-10-03  
- Installed **Webots R2025a** successfully.  
- Ran the official **e-puck_line_demo.wbt** simulation.  
- Verified robot line-following behavior with sensor readouts.  
**Status:** ✅ Environment verified, simulation stable.

---

## 📡 ND Task 4 – Ultrasonic Sensor Test
**Date:** 2025-10-05  
- Connected **HC-SR04** ultrasonic module to Arduino UNO R4 WiFi.  
- Measured real-time distances via serial output with median filtering.  
- Confirmed stable readings and correct timeout behavior.  
**Status:** ✅ Sensor tested and validated.

---

## 💡 ND Task 5 – LED Blink Circuit Documentation
**Date:** 2025-10-06  
- Built and documented LED Blink circuit using Fritzing.  
- Created breadboard and schematic diagrams for clarity.  
- Established a consistent **circuit documentation standard** for all future hardware tasks.  
**Status:** ✅ Completed, used as template for later tasks.

---

## 🧠 ND Task 6 – MNIST Classification (Deep Learning LAB PRE)
**Date:** 2025-10-09  
- Implemented CNN classifier on MNIST using PyTorch.  
- Achieved **98.88% validation accuracy in 5 epochs**.  
- Generated training/validation loss & accuracy curves automatically.  
- Built reproducible experiment logging structure (`runs/mnist_baseline`).  
**Status:** ✅ Fully completed, framework ready for future AI experiments.

---

## 🚀 ND Task 7 – RL Training Curve Mini Report
**Date:** 2025-10-11  
- Practiced full data-to-report workflow on a PPO-like reward curve.  
- Scripted metrics computation, CSV export, and Matplotlib visualization.  
- Wrote structured Markdown + LaTeX report (`nd_task7_rl_report.md`).  
- Clarified this task was for **workflow rehearsal**, not optimized performance.  
**Status:** ✅ Report finalized and reproducible.

---

## 🌐 Overall Reflection
Across the 7 ND LABPRE tasks, the workflow evolved from **basic hardware control** → **simulation** → **deep learning** → **reinforcement learning analytics**.

**Key Achievements**
- Established reproducible pipeline (data → code → visualization → report).  
- Unified Markdown documentation format.  
- Strengthened core skills across **electronics, simulation, and AI control**.  
- Prepared technical and workflow foundation for the **Tech Foundations** main phase.

**Overall Status:** 🌟 Completed — All ND LABPRE objectives achieved.
