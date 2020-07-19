#! /usr/bin/env python
# -*- coding: utf-8 -*-

#######################################
# Autor: Douglas dos S. Gomes         #
# GitHub: douglas-ee                  #
# Email: douglas.gomes@ee.ufcg.edu.br #
#######################################

import time
import serial
from Tkinter import *
porta = '/dev/ttyUSB0'
baud_rate = 9600

ser = serial.Serial(porta, baud_rate)
print ser.portstr
print ('aguarde, incializando a porta...')
time.sleep(3)


def um_axis(valor):  # Funcão que envia o valor do slide 1 para a porta serial
    ser.write('1')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))


def dois_axis(valor):
    ser.write('2')
    ser.write(chr(int(valor)))


def tres_axis(valor):
    ser.write('3')
    ser.write(chr(int(valor)))


def quatro_axis(valor):
    ser.write('4')
    ser.write(chr(int(valor)))


def cinco_axis(valor):
    ser.write('5')
    ser.write(chr(int(valor)))


def seis_axis(valor):
    ser.write('6')
    ser.write(chr(int(valor)))


def sair():
    ser.close()
    print('Fechando a porta serial...')
    time.sleep(1)
    print('Fechando a janela..')
    time.sleep(1)
    root.destroy()


root = Tk()  # Cria a janela
root.title('Servo Motor Arduino Control')  # Define o títula da janela
root.geometry('280x280')  # Define o tamanho

scale = Scale(root, from_=95, to=130, command=um_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

scale = Scale(root, from_=0, to=179, command=dois_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

scale = Scale(root, from_=0, to=179, command=tres_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

scale = Scale(root, from_=40, to=145, command=quatro_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

scale = Scale(root, from_=0, to=179, command=cinco_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

scale = Scale(root, from_=0, to=179, command=seis_axis,
              width=10, length=200, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

b = Button(root, text='Exit', command=sair)
b.pack()

root.mainloop()
