// ND TASK 4: HC-SR04 distance via Serial (UNO R4 WiFi)
// Pins: Trig=D6, Echo=D7
// Notes: 5V logic on UNO R4; add timeout and simple median filter.
// Serial Monitor: 115200 baud. Also compatible with Serial Plotter (prints a number line by line).

const uint8_t TRIG_PIN = 6;
const uint8_t ECHO_PIN = 7;

// One-way speed of sound is accounted by dividing by 2 later
// duration(us) * 0.0343 (cm/us) / 2 = distance in cm
float measureOnceCm(unsigned long timeout_us = 25000UL){
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long duration = pulseIn(ECHO_PIN, HIGH, timeout_us);
  if (duration == 0){
    return -1.0f;
  }
  return (duration * 0.0343f) / 2.0f;
}

float measureMedian3Cm(){
  float a = measureOnceCm();
  float b = measureOnceCm();
  float c = measureOnceCm();

  if (a < 0 && b < 0 && c < 0) return -1.0f;

  float x = a, y = b, z = c;
  if (x > y) {float t = x; x = y; y = t;}
  if (y > z) {float t = y; y = z; z = t;}
  if (x > y) {float t = x; x = y; y = t;}
  if (y >= 0) return y;
  if(x >= 0) return x;
  return z;
}

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(115200);
  // tiny warmup
  delay(200);
  Serial.println("HC-SR04 distance test (cm)");
}

void loop() {
  float d = measureMedian3Cm();
  if (d < 0){
    Serial.print("OutOfRange/TimeOut");
  }else{
    // For Serial Plotter, you can print only the number:
    // Serial.println(d, 1);
    Serial.print("Distance: ");
    Serial.print(d, 1);
    Serial.println("cm");
  }
  delay(100);
}
