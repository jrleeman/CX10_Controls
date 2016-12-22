#define THROTTLE_PIN 3
#define PITCH_PIN 5
#define YAW_PIN 6
#define ROLL_PIN 9
#define LBUTTON_PIN 10
#define RBUTTON_PIN 11
#define MAX_OUT 174
#define MIN_OUT 0
#define MAX_IN 500
#define MIN_IN -500

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
  digitalWrite(LBUTTON_PIN, LOW);
  digitalWrite(RBUTTON_PIN, LOW);
}

void loop() {

  // If there's any serial data available, read it
  while (Serial.available() > 0) {

    // Look through the serial string and pull out our values
    throttleValue = map(Serial.parseInt(), MIN_IN, MAX_IN, MIN_OUT, MAX_OUT);           
    pitchValue = map(Serial.parseInt(), MIN_IN, MAX_IN, MAX_OUT, MIN_OUT);
    rollValue = map(Serial.parseInt(), MIN_IN, MAX_IN, MAX_OUT, MIN_OUT);
    yawValue = map(Serial.parseInt(), MIN_IN, MAX_IN, MIN_OUT, MAX_OUT); 
    leftbuttonValue = Serial.parseInt();
    rightbuttonValue = Serial.parseInt();
    
    // Look for the newline. That's the end of the
    // sentence. Write out what we know.
    if (Serial.read() == '\n') {
      analogWrite(THROTTLE_PIN, throttleValue);
      analogWrite(PITCH_PIN, pitchValue);
      analogWrite(ROLL_PIN, rollValue);
      analogWrite(YAW_PIN, yawValue);
       
      if (leftbuttonValue == 1) {
        pinMode(LBUTTON_PIN, OUTPUT);
      }
      else {
        pinMode(LBUTTON_PIN, INPUT);
      }

      if (rightbuttonValue == 1) {
        pinMode(RBUTTON_PIN, OUTPUT);
      }
      else {
        pinMode(RBUTTON_PIN, INPUT);
      }
               
    }
  }
}
 
