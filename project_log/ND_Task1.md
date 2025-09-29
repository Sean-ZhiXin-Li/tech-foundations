# Project Log – National Day Task 1 (2025-09-29)

### Title  
**ND_Task1_Pot_LED_Servo.ino**

---

### Goal  
- Use Arduino UNO R4 WiFi  
- Potentiometer input → control servo angle (Servo) & LED brightness (PWM)  
- Serial monitor prints A0 raw value / servo angle / LED PWM value in real time  

---

### Setup & Wiring  
- **Potentiometer**:  
  - VCC → 5V  
  - GND → GND  
  - OUT → A0  
- **Servo**:  
  - Signal → D9  
  - VCC → 5V  
  - GND → GND  
- **LED**:  
  - Anode → D5 (with 220Ω resistor)  
  - Cathode → GND  

---

### Code  
- File name: `ND_Task1_Pot_LED_Servo.ino`  
- Functionality:  
  - `analogRead(A0)` reads potentiometer input (0–1023)  
  - `map()` converts to servo angle (0–180) and LED PWM (0–255)  
  - `Servo.write(angle)` drives the servo  
  - `analogWrite(5, pwm)` controls LED brightness  
  - Serial monitor outputs debug info (115200 baud, once every 0.1s)  

---

### Result  
- LED brightness successfully follows potentiometer rotation.  
- Serial monitor outputs correct values: `A0=... angle=... LED_PWM=...`.  
- Servo moves, but shows **jitter & limited travel**.  

---

### Issues  
- Current potentiometer physical range is only ~30°–130°, so A0 values are compressed, leading to poor servo control accuracy.  
- Potentiometer output is noisy, causing noticeable servo jitter.  
- Power from USB can drive LED + servo, but movement is not smooth enough.  

---

### Next Steps  
- Ordered **Bourns 3590S-2-103L 10-turn precision potentiometer (10kΩ)**, expected to arrive in 2 days.  
- After arrival:  
  - Recalibrate A0 min/max → map to full servo range (0–180°)  
  - Add filtering and slew rate limiting for smoother servo response  
  - Record demonstration video (Pot → Servo + LED)  

---

### Log Summary  
- **Date**: 2025-09-29  
- **Status**: Task 1 base functionality complete   
- **Pending**: Hardware upgrade with precision potentiometer, then video recording   
