# Tech Foundations

> A structured journey into **AI × Robotics × Control × Embedded** systems —  
> inspired by spacecraft drifting silently through the cosmos.  
> From algorithms to simulation to hardware, this repo blends engineering practice with an aerospace-driven narrative.

---

## Main Track (Core Research Path)

- **AI (Artificial Intelligence)**  
  Reinforcement Learning (RL), Imitation Learning (IL), neural network optimization.  
  *Goal:* run baselines, tune rewards/hyperparameters, design fair comparisons.

- **Robotics**  
  ROS 2 (Humble) + Gazebo simulation; URDF/Xacro; AI → ROS 2 → actuators closed-loop control.

- **Control Theory**  
  Classic controllers (PID, LQR) vs RL controllers; quantify gains (≥20% is a highlight).

- **Embedded Systems**  
  Arduino → STM32/ESP32; sensors + servos; small closed-loop hardware demos.

---

## Side Track (Breadth & Showcase)

- **Mechanical Engineering (Fusion 360)** → CAD models (CubeSat frames, robotic end-effectors).  
- **Electrical Engineering (Arduino, KiCad)** → Sensor/servo demos, small PCB sketches.  
- **Data Visualization (Matplotlib, Plotly)** → Training curves, comparison charts, orbit animations.  
- **Scientific Communication (Markdown, LaTeX)** → Logs, reports, English slides.  
- **GitHub Engineering** → CI/CD workflows, reproducible runs.  
- **Aerospace Applications**  
  Inspired by probes like Voyager, Cassini, New Horizons.  
  Every spacecraft eventually faces silence — falling into a star or drifting endlessly.  
  This project reframes that emotion into research questions:  
  - How can an AI controller adapt when communication is lost?  
  - How can fuel be optimized for longer missions?  
  - How can CubeSat swarms coordinate in deep space?  

---

## Tools & Stack

**Programming & Env**  
- Python 3.11, VS Code, Jupyter, Git & GitHub  
- GitHub Actions, `.gitignore`, optional Git LFS, Docker  

**ML / Data**  
- PyTorch (+ TorchVision/Torchaudio, CUDA 12.1 if available)  
- NumPy, Pandas, SciPy, scikit-learn, gymnasium  

**Robotics**  
- ROS 2 Humble, Gazebo, RViz2  
- URDF/Xacro, `ros2_control`  

**Control**  
- PID, LQR baselines  
- python-control, SciPy signal  

**Embedded / Electronics**  
- Arduino IDE (Blink → sensors/servo)  
- PlatformIO (VS Code extension)  
- STM32CubeIDE / ESP-IDF (optional)  
- KiCad (PCB sketches)  

**CAD / Viz / Docs**  
- Fusion 360 (education license)  
- Matplotlib, Plotly  
- Markdown, LaTeX (Overleaf or local TeX)  

---

## Suggested Repo Structure

```
tech-foundations/
├─ ai/                # PyTorch RL/IL experiments
├─ robotics/          # ROS2 packages, Gazebo worlds
├─ control/           # PID/LQR baselines
├─ embedded/          # Arduino/STM32 demos
├─ cad/               # Fusion 360 exports
├─ data_viz/          # plots, notebooks
├─ docs/              # papers, slides
├─ logs/              # project logs
└─ .github/workflows/ # CI pipelines
```

---

## Initial Deliverables (Week 1)

- Minimal MNIST classifier with PyTorch  
- Fusion 360 cube & cylinder models  
- Arduino Blink demo (30–60s LED video)  
- GitHub repo initialized with README + first log  

---

## Week 2 Deliverables

### Main Track: ROS 2 Humble on Windows
- Installed and configured ROS 2 Humble on Windows.  
- Fixed missing library issues (`_rclpy_pybind11`), adjusted PATH, and unblocked files.  
- Verified functionality with **talker/listener demo**:
  - Talker published `"Hello World: XXXX"`.
  - Listener received messages in real time.  
- Outcome: Basic pub-sub communication confirmed.

### Side Track: Arduino UNO R4 WiFi + Servo MG90S
- Wired the servo (Red → 5V, Brown → GND, Orange → D9).  
- Uploaded test program (`servo_demo_code.ino`) using Arduino IDE.  
- Servo rotated between 0° → 90° → 180° with 1s delay, looping continuously.  
- Recorded a demo video as proof of concept.  
- Outcome: First hardware control project completed.

---

## Roadmap

- **Week 1**: Setup (PyTorch, Fusion 360, Arduino IDE).  
- **Week 2–4**: MNIST experiments, CAD expansion, hardware demos.  
- **Week 5+**: Integrated loop (AI + Robotics + Control + Embedded).  
- **Long Term**: Spacecraft-inspired tasks (orbit keeping, fuel optimization, comms-loss autonomy).  

---

## License
MIT License — free to use and share.
