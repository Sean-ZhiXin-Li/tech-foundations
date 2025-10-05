# ND Task 4 – Ultrasonic Sensor Test (Day Log)

**Date:** 2025-10-05  
**Task:** Connect and test ultrasonic sensor (HC-SR04) with Arduino UNO R4 WiFi. Print distance data via serial monitor.

---

## Progress
- Successfully wired the HC-SR04 ultrasonic sensor:  
  - VCC → 5V  
  - GND → GND  
  - Trig → D6  
  - Echo → D7  
- Uploaded test code (`nd_task4_ultrasonic.ino`).  
- Verified that serial output shows real-time distance measurements in centimeters.  
- Sensor responds correctly when moving an object (hand/book) at different distances.

---

## Observations
- Stable readings achieved by using a 3-sample median filter.  
- Serial monitor shows values updating around 10 Hz.  
- Out-of-range cases correctly display `"OutOfRange/Timeout"`.  
- Data integrity confirmed, ready for visualization and demo.

---

## Next Step (Planned for Tomorrow)
- Record a **video demo** showing:  
  - Hardware setup and wiring  
  - Serial monitor output while moving an object in front of the sensor  
  - Optional Serial Plotter visualization  

---

