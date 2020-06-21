#! /usr/bin/env python
# -*- coding: utf-8 -*-

#######################################
# Autor: Douglas dos S. Gomes         #
# GitHub: douglas-ee                  #
# Email: douglas.gomes@ee.ufcg.edu.br #
#######################################

import serial

# Informa qual a porta conectada
porta = '/dev/ttyUSB1'
baud_rate = 9600

# Escreve o valor na porta serial


def esc_porta():

    try:
        print("Digite:\n")
        valor = (
            raw_input("1 - Acender led.\n2 - Desligar led.\n"))
        #print (valor.portstr)
        Obj_porta = serial.Serial(porta, baud_rate)
        Obj_porta.write(valor)
        ler_porta()
        Obj_porta.close()

    except serial.SerialException:
        print("ERRO: tavlez haja algum dispositivo conectado na porta!")


# Ler na porta serial
def ler_porta():

    try:
        Obj_porta = serial.Serial(porta, baud_rate)
        valor = Obj_porta.readline()
        print("Arduino disse: ", valor)
        Obj_porta.close()

    except serial.SerialException:
        print("ERRO: tavlez haja algum dispositivo conectado na porta!")


if __name__ == '__main__':

    esc_porta()
