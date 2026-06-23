#include <Servo.h>

Servo baseServo;    //base
Servo shoulderServo; //joint
Servo elbowServo;    //arm
Servo gripperServo;  //to close and open gripper

int baseTarget = 90;
int shoulderTarget = 45;
int elbowTarget = 45;
int gripperTarget = 20;
int baseCurrent = 90;
int shoulderCurrent = 45;
int elbowCurrent = 45;

void setup() {
  Serial.begin(115200); 
  baseServo.attach(9);  
  shoulderServo.attach(10);
  elbowServo.attach(11);
  gripperServo.attach(12);
  baseServo.write(baseCurrent);
  shoulderServo.write(shoulderCurrent);
  elbowServo.write(elbowCurrent);
  gripperServo.write(gripperTarget);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd.startsWith("S1:")) {
      baseTarget = constrain(cmd.substring(3).toInt(), 0, 180);
    } 
    else if (cmd.startsWith("S2:")) {
      shoulderTarget = constrain(cmd.substring(3).toInt(), 0, 90);
    } 
    else if (cmd.startsWith("S3:")) {
      elbowTarget = constrain(cmd.substring(3).toInt(), 0, 90);
    } 
    else if (cmd.startsWith("S4:")) {
      int val = cmd.substring(3).toInt();
      gripperTarget = (val == 1) ? 100 : 20;
      gripperServo.write(gripperTarget); 
    }
  }

  if (baseCurrent != baseTarget) {
    baseCurrent += (baseTarget > baseCurrent) ? 1 : -1;
    baseServo.write(baseCurrent);
    delay(5); 
  }
  if (shoulderCurrent != shoulderTarget) {
    shoulderCurrent += (shoulderTarget > shoulderCurrent) ? 1 : -1;
    shoulderServo.write(shoulderCurrent);
    delay(5);
  }
  if (elbowCurrent != elbowTarget) {
    elbowCurrent += (elbowTarget > elbowCurrent) ? 1 : -1;
    elbowServo.write(elbowCurrent);
    delay(5);
  }
}
