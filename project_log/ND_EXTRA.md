# NATION DAY EXTRA — Differential-Drive Obstacle Avoidance (Webots)

**Date:** 2025-10-18  
**Author:** Sean (Zhixin Li)  
**Platform:** Webots R2025a (Windows)  
**Robot:** E-puck (Differential Drive)  
**Controller:** Python

---

## Objectives

- Create a new Webots world with a rectangle arena
- Insert the e-puck differential-drive robot
- Implement a Python obstacle-avoidance controller using IR distance sensors
- Add obstacles to validate detection and avoidance behavior
- Document a stable workflow on Windows to avoid UI freezing

---

## World & Controller Setup

The world contains:
- `E-puck` with `controller "epuck_avoid"`
- Two `Solid` Box obstacles tested for collision avoidance

**Execution workflow (Windows-safe):**
- Avoid clicking the left Scene Tree to prevent UI freeze
- Edit `.wbt` text instead of GUI interaction
- Run simulation with `Ctrl + R`
- Hot-reload the Python controller with `Ctrl + Shift + R`

---

## Key Parameters

| Parameter | Value | Description |
|-----------|--------|-------------|
| TIME_STEP | 64 ms | Standard timestep for e-puck |
| MAX_SPEED | 6.28 rad/s | Motor max velocity |
| base | 0.70 * MAX_SPEED | Forward cruising speed |
| turn | 0.60 * MAX_SPEED | Turning speed when obstacle detected |
| OBSTACLE_THR | 75.0 | IR threshold (bigger = closer) |
| FRONT sensors | ps7, ps0 | Detect forward proximity |
| LEFT arc | ps6, ps5 | Detect left-side proximity |
| RIGHT arc | ps1, ps2 | Detect right-side proximity |

---

## Procedure

1. Created a world and spawned e-puck via manual `.wbt` editing.
2. Assigned the Python controller `epuck_avoid`.
3. Enabled all IR sensors (`ps0`..`ps7`) and collected raw readings.
4. Implemented a threshold-based turning strategy.
5. Added obstacles and confirmed successful avoidance.

---

## Behavior Validation

- Robot drives forward while IR readings remain below threshold.
- When an obstacle is detected, it turns toward the freer side.
- After clearing the obstacle, it resumes forward motion.
- Terminal output from `PRINT_DEBUG` confirms correct detection.

---

## Tuning Notes

- Increase `OBSTACLE_THR` or reduce `turn` if the robot turns too often.
- Decrease `OBSTACLE_THR` or increase `turn` if the robot reacts too late.
- A Braitenberg-based model can be added later for smoother motion.

---

## Known Issue & Workaround

**Issue:** Selecting the robot in the Scene Tree can freeze Webots on Windows.  
**Workaround:**  
- Disable shadows, anti-aliasing, and texture filtering  
- Avoid selecting robot in GUI  
- Use `Ctrl + R` (run) and `Ctrl + Shift + R` (hot reload)

---

## Deliverables

- Differential-drive robot simulation
- Python IR-based avoidance controller
- Working obstacle detection and avoidance
- Stable, reproducible workflow on Windows
