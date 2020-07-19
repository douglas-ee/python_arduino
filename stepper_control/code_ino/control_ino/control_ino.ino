#include <Stepper.h> //INCLUSÃO DE BIBLIOTECA

const int stepsPerRevolution = 180;   //NÚMERO DE PASSOS POR VOLTA

Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11); //INICIALIZA O MOTOR UTILIZANDO OS PINOS DIGITAIS 8, 9, 10, 11

int eixo = 0;

void setup()
{
    myStepper.setSpeed(300); //VELOCIDADE DO MOTOR
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
            stepsPerRevolution = Serial.read();
            myStepper.step(stepsPerRevolution); //GIRA O MOTOR NO SENTIDO ANTI-HORÁRIO
        }
    }
}