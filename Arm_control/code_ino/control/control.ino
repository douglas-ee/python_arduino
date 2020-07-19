#include <Servo.h>

Servo um_servo, dois_servo, tres_servo, quatro_servo, cinco_servo, seis_servo;
int eixo = 0, bytelido = 0;

void setup()
{
    Serial.begin(9600);
    um_servo.attach(25);
    dois_servo.attach(27);
    tres_servo.attach(29);
    quatro_servo.attach(31);
    cinco_servo.attach(33);
    seis_servo.attach(35);

    um_servo.write(95);
    dois_servo.write(0);
    tres_servo.write(100);
    quatro_servo.write(145);
    cinco_servo.write(90);
    seis_servo.write(90);
}

void loop()
{
    while (Serial.available() > 0)
    {
        eixo = Serial.read();
        if (eixo == '1')
        {
            delay(10);
            bytelido = Serial.read();
            um_servo.write(bytelido);
        }
        if (eixo == '2')
        {
            delay(10);
            bytelido = Serial.read();
            dois_servo.write(bytelido);
        }
        if (eixo == '3')
        {
            delay(10);
            bytelido = Serial.read();
            tres_servo.write(bytelido);
        }
        if (eixo == '4')
        {
            delay(10);
            bytelido = Serial.read();
            quatro_servo.write(bytelido);
        }
        if (eixo == '5')
        {
            delay(10);
            bytelido = Serial.read();
            cinco_servo.write(bytelido);
        }
        if (eixo == '6')
        {
            delay(10);
            bytelido = Serial.read();
            seis_servo.write(bytelido);
        }
    }
}
