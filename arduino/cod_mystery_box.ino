#include <Servo.h>
#include <LiquidCrystal_I2C.h>
  LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3,POSITIVE);

const int baudRate = 9600;
const int pin = 2;
const int servoPin = 8;
const int servoClosedPos = 0;
const int servoOpenPos = 100;
     
int servoPos = 0;
int buttonState = 0;
String gunSelection = "";
Servo servo;
bool quit = false;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(baudRate);
    pinMode(pin, INPUT);
    setupServo();
    setupLCD();
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(pin);
 
  if (buttonState == 0 && !quit) {
    lcd.clear();
    lcd.setCursor(0,0);
    servo.write(servoOpenPos);
    Serial.println(buttonState);
    while (Serial.available() == 0) {
      
    }
    lcd.print("Gun Selection:");
    lcd.setCursor(0,2);
    gunSelection = Serial.readString();
    if (gunSelection == "Teddy Bear") {
      quit = true;
    }
    lcd.print(gunSelection);
    servo.write(servoClosedPos);
  }

}

void setupServo() {
  servo.attach(servoPin);
  servo.write(servoPos);
}  

void setupLCD() {

  lcd.begin(20,4);
  lcd.clear();

}

void writeBoxItemToDisplay() {
  
}
