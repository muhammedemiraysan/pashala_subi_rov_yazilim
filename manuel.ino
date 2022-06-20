#include <Servo.h>
int servo_hiz = 0;
int servo1_hiz = 0;
int servo2_hiz = 0;
int servo3_hiz = 0;
int servo4_hiz = 0;
int servo5_hiz = 0;
int servo_yon = 0;
int servo1_yon = 1;
int servo2_yon = 1;
int servo3_yon = 1;
int servo4_yon = 1;
int servo5_yon = 1;
int incomingByte = 0;
byte servoPin = 3; byte servoPin1 = 5; byte servoPin2 = 6; byte servoPin3 = 9; byte servoPin4 = 10; byte servoPin5 = 11;
Servo servo; Servo servo1; Servo servo2; Servo servo3; Servo servo4; Servo servo5;

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
  servo_hiz = 170;
  servo_yon = 1;
  servo1_hiz = 170;
  servo1_yon = 1;
  servo2_hiz = 170;
  servo2_yon = 1;
  servo3_hiz = 170;
  servo3_yon = 1;  
  servo4_hiz = 170;
  servo4_yon = 1;
  servo5_hiz = 170;
  servo5_yon = 1;
  
  digitalWrite(13,HIGH);}
if (incomingByte == 50){
  servo_hiz = 0;
  servo_yon = 1;
  servo1_hiz = 0;
  servo1_yon = 1;
  servo2_hiz = 0;
  servo2_yon = 1;
  servo3_hiz = 0;
  servo3_yon = 1;  
  servo4_hiz = 0;
  servo4_yon = 1;
  servo5_hiz = 0;
  servo5_yon = 1;
  digitalWrite(13,LOW);
  }
servo.writeMicroseconds(1470  + (servo_hiz  * servo_yon));
servo1.writeMicroseconds(1470 + (servo1_hiz  * servo1_yon));
servo2.writeMicroseconds(1470 + (servo2_hiz  * servo2_yon));
servo3.writeMicroseconds(1470 + (servo3_hiz  * servo3_yon));
servo4.writeMicroseconds(1470 + (servo4_hiz  * servo4_yon));
servo5.writeMicroseconds(1470 + (servo2_hiz  * servo2_yon));

}
