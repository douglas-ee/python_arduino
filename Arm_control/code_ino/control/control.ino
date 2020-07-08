#include <Servo.h>

Servo x_servo, y_servo, w_servo, q_servo, r_servo, s_servo; // Cria dois objetos do tipo Servo.
int eixo =0 , bytelido = 0; // Cria duas variaveis do tipo int.

void setup (){
  Serial.begin(9600); // Configura a velocidade da comunicação serial.
  x_servo.attach(8); // Anexa o objeto x_servo ao pino 9 do arduino.
  y_servo.attach(9); // Anexa o objeto y_servo ao pino 10 do arduino.
  w_servo.attach(10); // Anexa o objeto y_servo ao pino 10 do arduino.
  q_servo.attach(11); // Anexa o objeto y_servo ao pino 10 do arduino.
  r_servo.attach(12); // Anexa o objeto y_servo ao pino 10 do arduino.
  s_servo.attach(13); // Anexa o objeto y_servo ao pino 10 do arduino.

  x_servo.write(130); // posiciona x_servo no angulo zero grau.
  y_servo.write(90); // posiciona y_servo no angulo zero grau.
  w_servo.write(90); // posiciona y_servo no angulo zero grau.
  q_servo.write(90); // posiciona y_servo no angulo zero grau.
  r_servo.write(90); // posiciona y_servo no angulo zero grau.
  s_servo.write(90); // posiciona y_servo no angulo zero grau.
}

void loop(){
  while (Serial.available() > 0){ // Enquanto houver algum byte na entrada serial.
    eixo = Serial.read(); //Lê um byte e armazena na variável eixo.
    if ( eixo == 'x' ) { // Verifica se eixo é igual ao caractere x.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'x', bytelido recebe o valor do 'slider x' da UI em python.
      x_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    }
    if ( eixo == 'y' ) { // Verifica se eixo é igual ao caractere y.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'y', bytelido recebe o valor do 'slider y' da UI em python.
      y_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    }
    if ( eixo == 'w' ) { // Verifica se eixo é igual ao caractere y.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'y', bytelido recebe o valor do 'slider y' da UI em python.
      w_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    } 
    if ( eixo == 'q' ) { // Verifica se eixo é igual ao caractere y.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'y', bytelido recebe o valor do 'slider y' da UI em python.
      q_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    }
    if ( eixo == 'r' ) { // Verifica se eixo é igual ao caractere y.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'y', bytelido recebe o valor do 'slider y' da UI em python.
      r_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    }    
    if ( eixo == 's' ) { // Verifica se eixo é igual ao caractere y.
      delay(10); // Espera 10ms
      bytelido = Serial.read(); // Como eixo igual a 'y', bytelido recebe o valor do 'slider y' da UI em python.
      s_servo.write(bytelido); // Passa para o x_servo o valor de bytelido.
    }       
  }
}

