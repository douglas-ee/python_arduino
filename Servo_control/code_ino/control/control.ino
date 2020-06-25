#include <Servo.h>

Servo x_servo;
int eixo = 0;
int byte_lido = 0;

void setup()
{
    Serial.begin(9600);
    x_servo.attach(9);
    x_servo.write(0); // posiciona x_servo no angulo zero grau.
}

void loop()
{
    // Enquanto houver algum byte na entrada serial.
    while (Serial.available() > 0)
    {
        eixo = Serial.read();
        if (eixo == 'x')
        {
            delay(10);
            byte_lido = Serial.read();
            x_servo.write(byte_lido); // Passa para o x_servo o valor de bytelido.
        }
    }
}
