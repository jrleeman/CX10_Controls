#define THROTTLE_PIN 3
#define PITCH_PIN 5
#define YAW_PIN 6
#define ROLL_PIN 9
#define LBUTTON_PIN 10
#define RBUTTON_PIN 11

int throttleValue;
int pitchValue;
int rollValue;
int yawValue;
byte leftbuttonValue;
byte rightbuttonValue;

void setup() {
  Serial.begin(115200);
  pinMode(THROTTLE_PIN, OUTPUT);
  pinMode(PITCH_PIN, OUTPUT);
  pinMode(YAW_PIN, OUTPUT);
  pinMode(ROLL_PIN, OUTPUT);
  pinMode(LBUTTON_PIN, INPUT);
  pinMode(RBUTTON_PIN, INPUT);
}

void loop() {
/*
  // We could be starting anywhere. Wait for a newline, throwing things
  // away until we find one.
  while (Serial.available() > 0) {
    if(Serial.read() == '\n'){
      break;
    }
  }
*/
   // if there's any serial available, read it:
  while (Serial.available() > 0) {

    // look for the next valid integer in the incoming serial stream:
    throttleValue = map(Serial.parseInt(), -500, 500, 0, 174);
    //Serial.println(throttleValue);                 
    pitchValue = map(Serial.parseInt(), -500, 500, 174, 0);
    rollValue = map(Serial.parseInt(), -500, 500, 174, 0);
    yawValue = map(Serial.parseInt(), -500, 500, 0, 174); 
    leftbuttonValue = Serial.parseInt();
    rightbuttonValue = Serial.parseInt();
    // look for the newline. That's the end of your
    // sentence:
    if (Serial.read() == '\n') {
      analogWrite(THROTTLE_PIN, throttleValue);
      analogWrite(PITCH_PIN, pitchValue);
      analogWrite(ROLL_PIN, rollValue);
      analogWrite(YAW_PIN, yawValue);
       
      if (leftbuttonValue == 1) {
        pinMode(LBUTTON_PIN, OUTPUT);
        digitalWrite(LBUTTON_PIN, LOW);
      }
      else {
        digitalWrite(LBUTTON_PIN, HIGH);
        pinMode(LBUTTON_PIN, INPUT);
      }

      if (rightbuttonValue == 1) {
        pinMode(RBUTTON_PIN, OUTPUT);
        digitalWrite(RBUTTON_PIN, LOW);
      }
      else {
        digitalWrite(RBUTTON_PIN, HIGH);
        pinMode(RBUTTON_PIN, INPUT);
      }
     
          
    }
  }
}
 
