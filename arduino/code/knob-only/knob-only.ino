
int knob = 0;


void setup() {
    knob = analogRead(A2);
    Serial.begin(9600);
}

void loop() {

  knob = analogRead(A2);
  Serial.println(knob); 

}
