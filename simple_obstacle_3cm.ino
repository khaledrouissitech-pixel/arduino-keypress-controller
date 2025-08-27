int sensorPin = 2;  // D0 from KY-032

void setup() {
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int state = digitalRead(sensorPin);

  if (state == LOW) {
    Serial.println("1");
  } else {
    Serial.println("0");
  }

  delay(100);
}
