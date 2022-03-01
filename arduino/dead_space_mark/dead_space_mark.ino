
int led_pins[6] = {3, 5, 6, 9, 10, 11}; // Arduino Nano PWM pins
int led_values[6] = {200, 200, 200, 200, 200, 200};
int delay_ms = 1;


void setupLedPins() {
  /*
   * assign ids to pins
   */
  for (int i = 0; i < 6; i++) {
    pinMode(led_pins[i], OUTPUT);
  }
}

void setLedValues() {
  /*
   * writes data to leds
   */
  for (int i = 0; i < 6; i++) {
    analogWrite(led_pins[i], led_values[i]);
  }
}

void setLedValue(int led_pin, int led_value) {
  /*
   * led pins indexed from 0 to 6
   * led values between 1 and 256
   */
    if (led_pin >= 1 && led_pin <= 6) {
      led_values[led_pin - 1] = max(min(led_value, 256), 1) - 1;
    }
}


void setup() {
  setupLedPins();
  setLedValues();
  
  Serial.begin(115200);
  Serial.setTimeout(100);
  Serial.println("alive");
}

void loop() {
  if (Serial.available() > 0) {
    char control = Serial.read();
    if (control == '.') {
      int led_pin = Serial.parseInt();
      int led_value = Serial.parseInt();
      setLedValue(led_pin, led_value);
    }
  }
  setLedValues();
  delay(delay_ms);
}
