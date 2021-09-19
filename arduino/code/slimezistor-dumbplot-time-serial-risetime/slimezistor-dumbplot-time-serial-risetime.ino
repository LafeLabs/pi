

/*slimezistor dumb plot modified to output times at switch points
 * 
 * measures risetime in miroseconds from 1/4 to 3/4 of max value
 * 
 * use trashrobot5 shield
 * potentiometer is on pin A2, which goes from 5v to ground, tuning from 0 to 1023
 * x is voltage measured on input A1, which goes to one of the electrodes as well as a capacitor to ground
 * pin 9 is a digital output.
 * 
 * range is 256 to 768, which is from 1/4 to 3/4 of max
 *  
 * plot the curve on the arduino serial plotter if you have the IDE with the plotter
 * 
 * this program is of limited utility without a plotter
 * 
 */

int outpin = 9;
int x = 0;
int xmin = 256;
int xmax = 768;
int tprev = 0;
int t = 0;
int tau = 0;

void setup() {
    pinMode(outpin,OUTPUT);
    digitalWrite(outpin,LOW);
    Serial.begin(115200);
    x = analogRead(A1);
    
}

void loop() {
  t = micros();
  x = analogRead(A1);
  if(x > xmax){
    digitalWrite(outpin,LOW);
    tau = t - tprev;
    Serial.println(tau);
    //tprev  = t;   
  }
  if(x < xmin){
    digitalWrite(outpin,HIGH);
    tprev  = t;   
  }

}
