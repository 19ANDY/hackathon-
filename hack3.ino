#include<SoftwareSerial.h>
SoftwareSerial mySerial(9,10);
int read_count=0,tag_count=0;
int j=0; 
char data_temp, RFID_data[12], data_store[12];
boolean disp_control;
int data;
const int in_1 = 11 ;
const int in_2 = 12 ;
void setup()
{
mySerial.begin(9600);
Serial.begin(9600);
pinMode(in_1,OUTPUT) ; 
pinMode(in_2,OUTPUT) ;
digitalWrite (LED_BUILTIN, LOW);
}

void loop()
{
RecieveData();
StoreData();
PrintData();
checkdata1();
while (Serial.available()){
data = Serial.read();
}
do
{
if(data == '1')
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite (LED_BUILTIN, HIGH);
delay(1000);
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
digitalWrite (LED_BUILTIN, LOW);
delay(6000);
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
delay(1000); 
}

else if (data == '0')
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,HIGH) ;
digitalWrite (LED_BUILTIN, LOW);
delay(1000);
}
}while(0);
}

void RecieveData()
{
if(mySerial.available()>0)
{
data_temp=mySerial.read();
RFID_data[read_count]=data_temp;
read_count++;
}
}

void StoreData()
{

if(read_count==12)
{
disp_control=true;  
for(j=0;j<12;j++)
{
data_store[j]=RFID_data[j];
}
read_count=0;
}
}

void PrintData()
{
if(disp_control==true)
{
 
    for(j=0;j<12;j++)
  {
    if(data_store[0]==0)
    { break;}
    Serial.write(data_store[j]);
  }
  Serial.println();
disp_control=false;
}
}
void checkdata1()
{
if(disp_control==true)
{
  for(j=0;j<12;j++)
  {
    if(data_store[11]==9)
    {Serial.write(0);}
  }
 Serial.println();
disp_control=false;
}
}
