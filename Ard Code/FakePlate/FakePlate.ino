
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
    if (inputString.equals("RESET")) {
      delay(500);
      Serial.println("READY, SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
    } else if (inputString.equals("MOVE")) {
      delay(3000);
      Serial.println("READY");
    } else if (inputString.startsWith("X-AXIS")) {
      delay(500);
      Serial.println("READY");              
    } else if (inputString.equals("GRIPPER OPEN")) {
      delay(500);
      Serial.println("READY, OPEN");   
    } else if (inputString.equals("GRIPPER CLOSE")) {
      delay(500);
      Serial.println("READY, CLOSED, NOPLATE");
    } else if (inputString.equals("Z-AXIS EXTEND")) {
      delay(500);
      Serial.println("READY, EXTENDED");     
    } else if (inputString.equals("Z-AXIS RETRACT")) {
      delay(500);
      Serial.println("READY, RETRACTED");

    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
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
