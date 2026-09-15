
String inputString = "";      // a String to hold incoming data
bool isStringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  if (isStringComplete) {
    if (inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("The LED is now on!");
    } else if (inputString.equals("LED OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("The LED is now off!");    
    } else {
      Serial.println("Unknown command --> ");
      Serial.print(inputString);
    }
    

    // do the command


    // clear the string:
    inputString = "";
    isStringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
