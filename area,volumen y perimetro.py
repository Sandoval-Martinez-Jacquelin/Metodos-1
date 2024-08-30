# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:20:04 2024

@author: jocelyn
"""
from math import pi
def area(radio):
    a=pi*pow(radio,2)
    return a
def perimetro(radio):
    per=2*pi*radio
    return per

def volumen(radio):
    vol=(pi*pow(radio,3)*4)/3
    return vol

print("1.Área y perimetro de un circulo ")
print("2.Volumen de un esfera ")
while True:
    try:
        op=int(input("Eliga una opcion "))
        if op==1 or op==2:
            break
    except:
        print("Solo opcion 1 o 2 ")

if op==1:
    while True:
        try:
            r=float(input("Ingrese el radio del circulo "))
            if r>0:
                break
        except:
            print("El radio debe ser mayor a 0")
    print("El área del circulo es ",area(r))
    print("El perimetro del circulo es ",perimetro(r))
else:
    while True:
        try:
            r=float(input("Ingrese el radio de la esfera "))
            if r>0:
                break
        except:
            print("El radio debe ser mayor a 0")
    print("El volumen de la esfera es ",volumen(r))
    
    