int sagx_pin = A1;
int sagy_pin = A0;
int solx_pin = A3;
int soly_pin = A2;
int sagx = 0;  
int sagy = 0;
int solx = 0;  
int soly = 0;

void setup() {
  Serial.begin(9600);           
}

void loop() {
  sagx = analogRead(sagx_pin);  
  sagy = analogRead(sagy_pin);
  solx = analogRead(solx_pin);  
  soly = analogRead(soly_pin);
  if(sagx > 490 && sagx < 550){sagx = 500;}if(sagy > 490 && sagy < 550){sagy = 500;}if(solx > 490 && solx < 550){solx = 500;}if(soly > 490 && soly < 550){soly = 500;}
  sagx = (sagx-500) * -1; sagy = (sagy-500) * -1; solx = (solx-500) * -1; soly = (soly-500) * -1;
  Serial.print(" solx:");
  Serial.print(solx);      
    Serial.print(" soly:");
  Serial.print(soly);          
  Serial.print(" sagx:");
  Serial.print(sagx);      
    Serial.print(" sagy:");
  Serial.println(sagy);      
}
