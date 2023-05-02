int sensorPin = A0; // select the input pin for the LDR
int sensorValue = 0; // variable to store the value coming from the sensor
int threshold = 100;

void setup() {
  Serial.begin(9600); // sets the serial communication baud rate
}

void loop() {
  sensorValue = analogRead(sensorPin); // read the value from the sensor
  Serial.println(sensorValue); // print the value read from the sensor
  delay(100); // wait for 100ms for the next reading
}