#include <ArduinoJson.h>

int x;
float voltsperpoint = 12.46/399;//based on measuring with DVM fully charged battery
float v = 0.0;

void setup() {
 Serial.begin(9600);
}

void loop() {

  x = analogRead(A1);
  v = voltsperpoint*x;//convert to volts
  DynamicJsonDocument measurement(200);
  measurement["x"] = x;
  measurement["v"] = v;
  serializeJson(measurement, Serial);
  Serial.println();

}