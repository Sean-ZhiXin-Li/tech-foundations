void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // LED on
  delay(1000);                     // wait 1 sec
  digitalWrite(LED_BUILTIN, LOW);  // LED off
  delay(1000);                     // wait 1 sec
}
