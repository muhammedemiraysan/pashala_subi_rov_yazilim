
 
// Define Input Connections
#define CH1 3
#define CH2 5
#define CH3 6
#define CH4 9
#define CH5 10
#define CH6 11
#define CH7 8
// Integers to represent values from sticks and pots
int ch1Value;
int ch2Value;
int ch3Value;
int ch4Value; 
int ch5Value;
int ch6Value;
int sagx = 0;  
int sagy = 0;
int solx = 0;  
int soly = 0;
int chh6;
 
// Read the number of a specified channel and convert to the range provided.
// If the channel is off, return the default value
int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 30000);
  if (ch < 100) return defaultValue;
  return map(ch, 1000, 2000, minLimit, maxLimit);
}
 
// Read the switch channel and return a boolean value
bool readSwitch(byte channelInput, bool defaultValue){
  int intDefaultValue = (defaultValue)? 100: 0;
  int ch = readChannel(channelInput, 0, 100, intDefaultValue);
  return (ch > 50);
}
 
void setup(){
  // Set up serial monitor
  Serial.begin(9600);
  
  // Set all pins as inputs
  pinMode(CH1, INPUT);
  pinMode(CH2, INPUT);
  pinMode(CH3, INPUT);
  pinMode(CH4, INPUT);
  pinMode(CH5, INPUT);
  pinMode(CH6, INPUT);
  pinMode(CH7, INPUT);
}
 
 
void loop() {
  
  // Get values for each channel
  ch1Value = readChannel(CH1, -100,100, 0);
  ch2Value = readChannel(CH2, -100,100, 0);
  ch3Value = readChannel(CH3, -100,100, -100);
  ch4Value = readChannel(CH4, -100,100, 0);
  ch5Value = readChannel(CH5, -512,512, 0);
  ch6Value = readChannel(CH6,-512,512,0);
  sagx = map(ch4Value,-100,100,0,1024);
  sagy = map(ch2Value,-100,100,0,1024);
  soly = map(ch3Value,-100,100,0,1024);
  solx = map(ch1Value,-100,100,0,1024);

if(sagx > 470 && sagx < 530){sagx = 500;}
if(sagy > 470 && sagy < 530){sagy = 500;}
  if(solx > 470 && solx < 530){solx = 500;}if(soly > 470 && soly < 530){soly = 500;}
  sagx = (sagx-500) * -1; sagy = (sagy-500) * 1; solx = (solx-500) * 1; soly = (soly-500) * 1;
  Serial.print(String(sagx));      
  Serial.print("n");
  Serial.print(String(sagy));          
  Serial.print("n");
  Serial.print(String(solx));      
  Serial.print("n");
  Serial.print(String(soly));      
  Serial.print("n");
  Serial.print(String(ch6Value));
  Serial.print("n");
  Serial.print(String(ch5Value));
  Serial.println("n");
  //delay(100);
}
