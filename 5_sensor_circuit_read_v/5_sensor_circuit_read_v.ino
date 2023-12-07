#include <ros.h>

#define WINDOW_SIZE 5

float minVal = 6 ;
float maxVal = -1 ; 
// float presentVal = 0 ;

int INDEX = 0;
int VALUE = 0.0;
int SUM = 0.0;
int READINGS[WINDOW_SIZE];
int AVERAGED = 0.0;

void setup() {
//  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600) ;
  pinMode(A0,INPUT);

  // pinMode(2, OUTPUT);     
  // digitalWrite(2, HIGH);

  // pinMode(3, OUTPUT);     
  // digitalWrite(3, HIGH);

  // pinMode(4, OUTPUT);     
  // digitalWrite(4, HIGH);

  // pinMode(5, OUTPUT);     
  // digitalWrite(5, HIGH);

  // pinMode(6, OUTPUT);     
  // digitalWrite(6, HIGH);
}


// the loop function runs over and over again forever
void loop() {
  float sensorVal1 = analogRead(A0);
  float voltageVal1 = sensorVal1 * (5.0/1023);

  float sensorVal2 = analogRead(A2);
  float voltageVal2 = sensorVal2 * (5.0/1023);
  
  float sensorVal3 = analogRead(A4);
  float voltageVal3 = sensorVal3 * (5.0/1023);
  
  // float sensorVal4 = analogRead(A3);
  // float voltageVal4 = sensorVal4 * (5.0/1023);

  // float sensorVal5 = analogRead(A4);
  // float voltageVal5 = sensorVal5 * (5.0/1023);


    // SUM = SUM - READINGS[INDEX];       // Remove the oldest entry from the sum
    // VALUE = voltageVal;                // Read the next sensor value
    // READINGS[INDEX] = VALUE;           // Add the newest reading to the window
    // SUM = SUM + VALUE;                 // Add the newest reading to the sum
    // INDEX = (INDEX+1) % WINDOW_SIZE;   // Increment the index, and wrap to 0 if it exceeds the window size

    // AVERAGED = SUM / WINDOW_SIZE;      // Divide the sum of the window by the window size for the result

    // if (voltageVal > maxVal){
    //   maxVal = voltageVal;
    // }
    // if (voltageVal < minVal){
    //   minVal = voltageVal;
    // }

    Serial.print(voltageVal1);
    Serial.print("; ");
    Serial.print(voltageVal2);
    Serial.print("; ");
    Serial.println(voltageVal3);
    // Serial.print("; ");
    // Serial.print(voltageVal4);
    // Serial.print("; ");
    // Serial.println(voltageVal5);
    // showTwoStates(voltageVal,minVal,maxVal);
}

void showTwoStates(float voltageVal,float minVal,float maxVal) {
  float interval = maxVal - minVal;
  float half = interval/2;

  if (voltageVal>1){
    Serial.println("close");
  } else {
    Serial.println("open");
  } 
}

void printValues(float voltageVal,float averageVal,float minVal,float maxVal) {
    Serial.print(voltageVal);
    Serial.print("; ");
    Serial.print(averageVal);
    Serial.print("; ");
    Serial.print(minVal);
    Serial.print("; ");
    Serial.println(maxVal);  
}


// previous code:

//loop () start:
//  presentVal = analogRead(A0);
//  Serial.print(presentVal);
//  Serial.print('\n');
  
//  int presentVal = analogRead(0);
  //  presentVal = map(presentVal, 0, 1023, 0, 5.0);
// loop() end