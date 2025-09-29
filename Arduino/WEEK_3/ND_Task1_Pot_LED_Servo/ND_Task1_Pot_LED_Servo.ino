// National Day Task 1: Potentiometer --> Servo + LED + Serial print
// - Potentiometer: middle --> A0, sides --> 5V & GND
// - Servo: signal --> D9, VCC -> 5V, GND -> GND
// - LED: D5 -> 220Ω --> LED anode, LED cathode --> GND

#include <Servo.h>

const uint8_t PIN_POT = A0;
const uint8_t PIN_SERVO = 9;
const uint8_t LED_PIN = 5;

Servo myServo;

unsigned long lastPrintMs = 0;
const unsigned long PRINT_INTERVAL_MS = 200;

void setup() {
  Serial.begin(115200);
  unsigned long t0 = millis();
  while (!Serial && (millis() - t0 < 1500)){/*wait briefly*/}
  analogReadResolution(10);

  pinMode(LED_PIN, OUTPUT);
  myServo.attach(PIN_SERVO);

  Serial.println(" National Day Task 1: LED + Servo + Serial");
  Serial.println("Pot(A0) --> Servo(D9) angle & LED(D5) brightess");
}

void loop() {
  int potRaw = analogRead(PIN_POT);

  // Map to servo angle (0..180degrees), with clamping
  int angle = map(potRaw, 300, 700, 0, 180);
  if (angle < 0)   angle = 0;
  if (angle > 180) angle = 180;

  // Map to LED PWM (0..225), with clamping
  int pwmVal = map(potRaw, 300, 700, 0, 225);
  if(pwmVal < 0)    pwmVal = 0;
  if (pwmVal > 225) pwmVal = 225;

  myServo.write(angle);
  analogWrite(LED_PIN, pwmVal);

  // Print Values to Serial Monitor at a fixed interval
  unsigned long now = millis();
  if (now - lastPrintMs >= PRINT_INTERVAL_MS){
    lastPrintMs = now;
    Serial.print("A0 = ");
    Serial.print(potRaw);
    Serial.print(" angle = ");
    Serial.print(angle);
    Serial.print(" deg LED_PWM = ");
    Serial.print(pwmVal);
  }

  delay(2); 
}


