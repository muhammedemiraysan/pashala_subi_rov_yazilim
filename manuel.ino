#include <Servo.h>
int pwmVal = 1470;
int incomingByte = 0;
byte servoPin = 3; byte servoPin1 = 5; byte servoPin2 = 6; byte servoPin3 = 9; byte servoPin4 = 10; byte servoPin5 = 11;
Servo servo; Servo servo1; Servo servo2; Servo servo3; Servo servo4; Servo servo5;
void Run(int pwmVal){servo.writeMicroseconds(pwmVal);}
void Run1(int pwmVal){servo1.writeMicroseconds(pwmVal);}
void Run2(int pwmVal){servo2.writeMicroseconds(pwmVal);}
void Run3(int pwmVal){servo3.writeMicroseconds(pwmVal);}
void Run4(int pwmVal){servo4.writeMicroseconds(pwmVal);}  
void Run5(int pwmVal){servo5.writeMicroseconds(pwmVal);}

void setup() {
pinMode(13,OUTPUT);
Serial.begin(9600); 
servo.attach(servoPin); servo.writeMicroseconds(1470);
servo1.attach(servoPin1); servo1.writeMicroseconds(1470);
servo2.attach(servoPin2); servo2.writeMicroseconds(1470);
servo3.attach(servoPin3); servo3.writeMicroseconds(1470);
servo4.attach(servoPin4); servo4.writeMicroseconds(1470);
servo5.attach(servoPin5); servo5.writeMicroseconds(1470);
delay(7000);
}
void loop() {
if (Serial.available() > 0) {

incomingByte = Serial.read(); // read the incoming byte:

Serial.print(" I received:");

Serial.println(incomingByte);

}
if (incomingByte == 49){
  servo.writeMicroseconds(1600);
  digitalWrite(13,HIGH);
  }
if (incomingByte == 50){
  servo.writeMicroseconds(1470);
  digitalWrite(13,LOW);
  }
//Serial.print(" pwmVal: ");
//Serial.println(pwmVal);
}
