//reading Byte check
int incomingByte = 0;
// Horizontal movement variables
int dirPin = 10; 
int stepPin = 11;

int headPos = 0;
int onePos = 40;
int tabPos = 120;
//Vertical movement variables
int downDirPin = 12;
int downStepPin = 13;

int oneDown = 40;
int rowDown = 120;

void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  pinMode(downDirPin, OUTPUT);
  pinMode(downStepPin, OUTPUT);
}

// process the expected messages into byte form
byte start = byte('start');
byte zero = byte('0');
byte one = byte('1');
byte tab = byte('tab');
byte down = byte('down');
byte row = byte('row');
byte done = byte('done');

void loop() {
  // send read only when received data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    if (incomingByte == start){
      //Move all the way to the left, use headPos to calculate the amount to turn back
      rotate(-headPos, 1, dirPin);
      headPos = 0;
    }
    else if (incomingByte == zero){
      //Do not print, move one right
      
      rotate(onePos, 1, dirPin);
      //increment headPos
      headPos = headPos+ onePos;
    }
    else if (incomingByte == one){
      //Print and move one right
      // ---------------------- TODO: PRINT HERE----------------------
       rotate(onePos, 1, dirPin);
       headPos = headPos+ onePos;
    }
    else if (incomingByte == tab){
      //Move a cell gap to the right
      rotate(tabPos, 1, dirPin);
      headPos = headPos+ tabPos;
    }
    else if (incomingByte == down){
      //Move a level down in a cell
      rotate(oneDown, 1, downDirPin);

    }
    else if (incomingByte == row){
      //Move to the next row
      rotate(rowDown, 1, downDirPin);

    }
    else if (incomingByte == done){
      //Print is done, spin out the down to release paper
      rotate(32000, 1, downDirPin);
    }
    
    // ---------------------- TODO: REMOVE AFTER TESTING ----------------------
    //This is the clock for testing only
    if (digitalRead(5) == HIGH){
      digitalWrite(5, LOW);
    }
    else{
      digitalWrite(5, HIGH);
    } // ---------------------- END OF REMOVE ----------------------
    
  }   //end of read

}

void rotate(int steps, float speed, int stepper){ 
  //rotate a specific number of microsteps (8 microsteps per step) - (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (steps > 0)? HIGH:LOW;
  steps = abs(steps);

  digitalWrite(stepper,dir); 

  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(stepper+1, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(stepper+1, LOW); 
    delayMicroseconds(usDelay); 
  } 
} 

void rotateDeg(float deg, float speed, int stepper){ 
  //rotate a specific number of degrees (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (deg > 0)? HIGH:LOW;
  digitalWrite(stepper,dir); 

  int steps = abs(deg)*(1/0.225);
  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(stepper+1, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(stepper+1, LOW); 
    delayMicroseconds(usDelay); 
  }
} 
