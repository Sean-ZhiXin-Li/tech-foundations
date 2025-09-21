# Project Log — Week 2

## Main Track: ROS 2 Humble on Windows

### What I Did
- Downloaded and extracted `ros2-humble-*-windows-release-amd64.zip`.
- Set up environment variables:
  - Added `C:\Python38` and ROS 2 paths (`bin`, `Scripts`) to `PATH`.
  - Used `local_setup.ps1` to configure the environment.
- Verified installation:
  - Ran `ros2 doctor --report` and confirmed middleware = `rmw_cyclonedds_cpp`.
  - Successfully launched the **talker** node (`ros2 run demo_nodes_cpp talker`).
  - Successfully launched the **listener** node (`ros2 run demo_nodes_cpp listener`).
  - Messages were published as `"Hello World: XXXX"` and received correctly.

### Issues I Faced
- `ModuleNotFoundError: No module named 'rclpy._rclpy_pybind11'`  
  → Caused by missing `.pyd`/`.dll` files and path misconfiguration.  
 Fixed by downloading the official precompiled Windows release, unblocking files with `Unblock-File`, and correcting PATH.
- `ros2 --version` not recognized  
  → Windows ROS 2 CLI does not support `--version`.  
 Checked version indirectly by running `ros2 doctor` and node demos.
- Multiple warnings in `ros2 doctor` about `PackageReport`/`RosdistroReport`.  
  → Known issue on Windows, did not block functionality.

### Outcome
ROS 2 Humble is now running on Windows. I can successfully run the **talker/listener demo**, which continuously loops publishing and subscribing to messages.

---

## Side Track: Arduino UNO R4 WiFi + Servo MG90S

### What I Did
- Prepared hardware:
  - Arduino UNO R4 WiFi
  - Servo motor TowerPro MG90S
  - Breadboard + jumper wires
  - USB cable for power and programming
- Wiring:
  - **Red → 5V**
  - **Brown → GND**
  - **Orange → D9 (PWM pin)**
- Programming:
  - Installed Arduino IDE, selected `UNO R4 WiFi` board and correct COM port.
  - Uploaded a simple test sketch (`servo_demo_code.ino`):

```cpp
#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(9);  // attach to pin D9
}

void loop() {
  myservo.write(0);
  delay(1000);
  myservo.write(90);
  delay(1000);
  myservo.write(180);
  delay(1000);
}
```

- The servo successfully rotated:
  - From **0° → 90° → 180° → back to 0°**
  - With a **1 second delay between each move**
  - Looping continuously
- Recorded a demo video as deliverable.

### Issues I Faced
- Initially confused by **UNO pin labels (5V, GND, D9)**.  
 Solved by checking board silkscreen and mapping servo wires to power/signal pins.
- Couldn’t visually confirm servo rotation (no horn attached).  
 Temporary fix: attached a plastic horn/alternative pointer to the shaft.

### Outcome
Arduino UNO R4 WiFi successfully controlled the MG90S servo. The demo showed basic PWM angle control, 1-second delays, and continuous looping motion. Deliverables include the working `.ino` code and a recorded video.

---

## Week 2 Summary
- Successfully installed and configured **ROS 2 Humble** on Windows.  
- Verified **talker/listener demo** with continuous pub-sub communication.  
- Learned how to wire and control a **servo motor with Arduino UNO R4 WiFi**.  
- Overcame setup/debugging issues (missing libraries, wiring confusion, no servo horn).  
- Produced deliverables: **ROS 2 screenshot**, **servo demo video**, and **servo_demo_code.ino**.

 Week 2 is complete.
