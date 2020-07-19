#! /usr/bin/env python
# -*- coding: utf-8 -*-

#######################################
# Autor: Douglas dos S. Gomes         #
# GitHub: douglas-ee                  #
# Email: douglas.gomes@ee.ufcg.edu.br #
#######################################

from Tkinter import *
import serial
import time

# Informe qual a porta conectada
porta = '/dev/ttyUSB0'
baud_rate = 9600

# Define porta e velocidade de comunicação
ser = serial.Serial(porta, baud_rate)
print ser.portstr
print ("Incializando a porta... ^~^")
time.sleep(3)


# Funcão que envia o valor do slide X para a porta serial
def horario():
    ser.write('x')

# Funcão que envia o valor do slide X para a porta serial


def antihorario():
    ser.write(chr(int(2)))


def sair():
    ser.close()
    print("Fechando a porta... ^~^")
    time.sleep(1)
    print("Fechando a janela... ^~^")
    time.sleep(1)
    root.destroy()


# processo de criação da UI com TKinter
root = Tk()
root.title("Servo Motor Arduino Control")
root.geometry("280x280")

a = Button(root, text='EXIT', command=sair)
a.pack()  # Coloca o botão na janela

b = Button(root, text='Horario', command=horario)
b.pack()  # Coloca o botão na janela

c = Button(root, text='AntiHorario', command=antihorario)
c.pack()  # Coloca o botão na janela


root.mainloop()  # Coloca o programa em execução
