#! /usr/bin/env python
# -*- coding: utf-8 -*-

#######################################
# Autor: Douglas dos S. Gomes         #
# GitHub: douglas-ee                  #
# Email: douglas.gomes@ee.ufcg.edu.br #
#######################################

# Informe qual a porta conectada
import time
import serial
from Tkinter import *
porta = '/dev/ttyUSB0'
baud_rate = 9600


# Configuração da porta serial

# Define porta e velocidade de comunicação
ser = serial.Serial(porta, baud_rate)
print ser.portstr  # Imprime a porta em uso
print ('aguarde, incializando a porta...')
time.sleep(3)  # Aguarda 3 segundos


def y_axis(valor):  # Funcão que envia o valor do slide Y para a porta serial
    ser.write('y')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))


def x_axis(valor):  # Funcão que envia o valor do slide X para a porta serial
    ser.write('x')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))

def w_axis(valor):  # Funcão que envia o valor do slide X para a porta serial
    ser.write('w')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))

def q_axis(valor):  # Funcão que envia o valor do slide X para a porta serial
    ser.write('q')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))

def r_axis(valor):  # Funcão que envia o valor do slide X para a porta serial
    ser.write('r')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))

def s_axis(valor):  # Funcão que envia o valor do slide X para a porta serial
    ser.write('s')
    # Converte a variável valor de str para int e de int para char ( byte )
    ser.write(chr(int(valor)))

def sair():  # Função que destrói a Janela principal, antes fecha a porta serial
    ser.close()  # Fecha a porta serial
    print('Fechando a porta serial...')
    time.sleep(1)
    print('Fechando a janela..')
    time.sleep(1)
    root.destroy()  # Destrói a janela

# processo de criação da UI com TKinter


root = Tk()  # Cria a janela
root.title('Servo Motor Arduino Control')  # Define o títula da janela
root.geometry('280x280')  # Define o tamanho

# Cria um objeto Scale que pode varia de 0 a 179, e associa-o à função y_axis

scale = Scale(root, from_=0, to=179, command=y_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela

# Cria um objeto Scale ( Horizontal ) que pode varia de 0 a 179, e associa-o à função x_axis

scale = Scale(root, from_=0, to=179, command=x_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela


scale = Scale(root, from_=0, to=179, command=w_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela


scale = Scale(root, from_=0, to=179, command=q_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela

scale = Scale(root, from_=0, to=179, command=r_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela


scale = Scale(root, from_=0, to=179, command=s_axis, width=9, length=179, orient=HORIZONTAL)
scale.pack(anchor=CENTER)  # Coloca o Scale na janela

# Cria um objeto botão
b = Button(root, text='Exit', command=sair)
b.pack()  # Coloca o botão na janela

root.mainloop()  # Coloca o programa em execução
