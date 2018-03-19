int data;
//const int pwm = 2 ;  //initializing pin 2 as pwm
const int in_1 = 11 ;
const int in_2 = 12 ;

void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
 // pinMode(, OUTPUT); //make the LED pin (13) as output
//pinMode(pwm,OUTPUT) ;   //we have to set PWM pin as output
pinMode(in_1,OUTPUT) ;  //Logic pins are also set as output
pinMode(in_2,OUTPUT) ;
digitalWrite (LED_BUILTIN, LOW);
Serial.println("Hi!, I am Arduino");
}

void loop() {
while (Serial.available()){
  data = Serial.read();
}
do
{
if  (data == '1')
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
//analogWrite(pwm,255) ;
digitalWrite (LED_BUILTIN, HIGH);
delay(1000);
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
//analogWrite(pwm,255) ;
digitalWrite (LED_BUILTIN, LOW);
delay(6000);
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
//analogWrite(pwm,255) ;
//digitalWrite (LED_BUILTIN, HIGH);
delay(1000); 
}

else if (data == '0')
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
//analogWrite(pwm,255) ;
digitalWrite (LED_BUILTIN, LOW);
delay(1000);
}
}while(0);


}
