# Project Log — ND Task 5

## Summary
Today I documented and implemented the **LED Blink circuit** using Arduino UNO R4 WiFi (R3 footprint in Fritzing).  
The circuit was built on a breadboard, with one external LED driven by digital pin D6 through a 220Ω resistor.  
This task is the first step of ND Task 5, which focuses on creating both breadboard and schematic diagrams for earlier circuits.

## What I Did
- Set up breadboard power rails: Arduino **5V → + rail**, **GND → − rail**.
- Connected **D6 → resistor (220Ω) → LED anode (long leg)**.
- Connected **LED cathode (short leg) → GND rail**.
- Verified LED orientation (long = +, short = −).
- Exported Fritzing **breadboard diagram** of the LED Blink circuit.
- Wrote and uploaded simple Arduino **Blink code** (1s on, 1s off).
- Confirmed LED blinking correctly according to the sketch.

## Notes
- No direct 5V supply is required for the LED; the Arduino digital pin provides 5V when set HIGH.
- Current-limiting resistor is necessary to prevent LED damage.
- This diagram will be saved in `/docs/circuits/led_blink/` for later documentation.

## Final Remark
This concludes **all circuit-related work for today**.  
From now on, every time I work on circuits, I will use this same format (breadboard + schematic diagrams from Fritzing) to present my wiring clearly.
