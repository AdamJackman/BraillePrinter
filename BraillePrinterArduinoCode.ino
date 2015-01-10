#include <QueueArray.h>

//#define HEAD_LEFT '1'
#define HEAD_RIGHT '2'
#define ROLLER_FORWARD '3'
#define ROLLER_BACKWARD '4'
#define HEAD_DOWN '5'

#define HEAD_RIGHT_IN_CELL '6'
#define ROLLER_FORWARD_IN_CELL '7'
#define HEAD_LEFT_IN_CELL '8'
#define DONE '1'
#define ROLLOUT 'r'
#define ROLLIN 'g'


#define DIR_PIN_HEAD 2
#define STEP_PIN_HEAD 3
#define DIR_PIN_ROLLER 4
#define STEP_PIN_ROLLER 5
#define SOLENOID_PIN 9
#define LED 13

int STATUS = 0;
int cur = 0;
int cur_rollout = 0;

QueueArray<int> ops;

void setup() {
  Serial.begin(9600);
  pinMode(DIR_PIN_HEAD, OUTPUT); 
  pinMode(STEP_PIN_HEAD, OUTPUT); 
  pinMode(DIR_PIN_ROLLER, OUTPUT); 
  pinMode(STEP_PIN_ROLLER, OUTPUT); 
  pinMode(SOLENOID_PIN, OUTPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (!ops.isEmpty()) {
    switch(ops.pop()) {
    /*case HEAD_LEFT:
      rotate(-450, 0.25, DIR_PIN_HEAD, STEP_PIN_HEAD);
      break;
      */
    case HEAD_LEFT_IN_CELL:
      rotate(-100, 0.25, DIR_PIN_HEAD, STEP_PIN_HEAD);
      break;
      
    case HEAD_RIGHT_IN_CELL:
      rotate(100, 0.25, DIR_PIN_HEAD, STEP_PIN_HEAD);
      cur += 100;
      break;
    
    case HEAD_RIGHT:
      rotate(225, 0.25, DIR_PIN_HEAD, STEP_PIN_HEAD);
      cur += 225;
      break;

    case ROLLER_FORWARD:
      rotate(250, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
      cur_rollout += 250; 
      break;
      
    case ROLLER_FORWARD_IN_CELL:
      rotate(70, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
      cur_rollout += 70;
      break;

    case ROLLER_BACKWARD:
      rotate(-200, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
      cur_rollout -= 200;
      break;

    case HEAD_DOWN:
      digitalWrite(SOLENOID_PIN, HIGH);
      delay(80);
      digitalWrite(SOLENOID_PIN, LOW);
      break;

    case '9':
    rotate(1600, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
    break;

    case DONE:
       rotate(-1*cur, 0.25, DIR_PIN_HEAD, STEP_PIN_HEAD);
       cur = 0;
       break;
       
    case ROLLOUT:
      rotate(13*500 - cur_rollout + 250, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
      cur_rollout = 0;
      break;
     
    case ROLLIN:
      rotate(250*9, 0.25, DIR_PIN_ROLLER, STEP_PIN_ROLLER);
      cur_rollout += 250*8;
      
    default:
      break;
    }
  }
}


void serialEvent() {
  while (Serial.available()) {
    ops.enqueue(Serial.read());
    digitalWrite(LED, HIGH);
  }
}


void rotate(int steps, float speed, int DIR_PIN, int STEP_PIN){ 
  //rotate a specific number of microsteps (8 microsteps per step) - (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (steps > 0)? HIGH:LOW;
  steps = abs(steps);

  digitalWrite(DIR_PIN,dir); 

  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(STEP_PIN, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(STEP_PIN, LOW); 
    delayMicroseconds(usDelay); 
  } 
}









