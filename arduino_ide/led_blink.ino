/*
Example for ESP32 Camera: LED Blinking
By: RoboticX Team
*/

int ledPin = 4;

void setup() {
    pinMode(ledPin, OUTPUT);
}

void loop() {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
}