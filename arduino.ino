int salida = 8;
int numero = 0;
int b0 = A5, b1 = A4, b2 = A3, b3 = A2, b4 = A1, b5 = A0, b6 = 12, b7 = 13;
int s0 = 4, s1 = 5, s2 = 6, s3 = 7, s4 = 8, s5 = 9, s6 = 10, s7 = 11;

#define BIT(n,i) (n>>i&1)

void setup() {
  Serial.begin(115200);

  //Configuración de los bits como entradas o salidas
  pinMode(b0, INPUT); pinMode(b1, INPUT); pinMode(b2, INPUT); pinMode(b3, INPUT); pinMode(b4, INPUT); pinMode(b5, INPUT); pinMode(b7, INPUT); pinMode(b7, INPUT);
  pinMode(s0,OUTPUT);pinMode(s1,OUTPUT);pinMode(s2,OUTPUT);pinMode(s3,OUTPUT);pinMode(s4,OUTPUT);pinMode(s5,OUTPUT);pinMode(s6,OUTPUT);pinMode(s7,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String cadena = Serial.readStringUntil(';');

    numero = cadena.toInt();
    
    //Escritura a la entrada
    digitalWrite(s0, BIT(numero, 0));
    digitalWrite(s1, BIT(numero, 1));
    digitalWrite(s2, BIT(numero, 2));
    digitalWrite(s3, BIT(numero, 3));
    digitalWrite(s4, BIT(numero, 4));
    digitalWrite(s5, BIT(numero, 5));
    digitalWrite(s6, BIT(numero, 6));
    digitalWrite(s7, BIT(numero, 7));
    delay(1);
   //Lectura de la salida
    numero = (int)digitalRead(b0) * pow(2, 0) + (int)digitalRead(b1) * pow(2, 1) + (int)digitalRead(b2) * pow(2, 2) + (int)digitalRead(b3) * pow(2, 3) + (int)digitalRead(b4) * pow(2, 4) + (int)digitalRead(b5) * pow(2, 5) + (int)digitalRead(b6)*pow(2,6)+ (int)digitalRead(b7)*pow(2,7);
    Serial.write(numero);
  }
}
