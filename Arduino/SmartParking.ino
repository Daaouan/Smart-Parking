#include <Servo.h> //Appel de la librairie "SERVO"
Servo monservo;
const int rouge = 3; 
const int verte = 4; 
const int servo = 9; 
int var=0;

void setup() {
	Serial.begin(9600);
	monservo.attach(9);
  	monservo.write(0);
	pinMode(rouge, OUTPUT); 
	pinMode(verte, OUTPUT);
}
void loop() {
        
var = Serial.read();

  if (var==49) { 
 	monservo.write(90);
    digitalWrite(verte, HIGH);
    digitalWrite(rouge, LOW);
    delay(3000);
    monservo.write(0);
  }
  else {
    monservo.write(0);
	digitalWrite(rouge, HIGH);
	digitalWrite(verte, LOW);
    delay(1000);

}
}