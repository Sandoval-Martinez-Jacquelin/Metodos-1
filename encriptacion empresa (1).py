# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:49:59 2024

@author: Jacquelin Sandoval Martinez 2MM2
"""

from numpy import *
def encriptados(tclaro):
    tcifrado=""
    d={"Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U"}
    for i in tclaro:
        if i in d:
            tcifrado+=d[i]
        if i.isalpha():
            tcifrado+=i

    posicion=[]
    paquete=[]
    v=0
    for x in tclaro:
        if x in tcifrado:
            p=tclaro.find(x,v)
            posicion.append(p)
            if p<=9:
                paquete.append("0"+str(p)+str(ord(x)))
            else:
                paquete.append(str(p)+str(ord(x)))       
        v+=1
    np=[]
    for x in paquete:
        n0=(int(x[2])+7)%10
        n1=(int(x[3])+7)%10
        n2=(int(x[0])+7)%10
        n3=(int(x[1])+7)%10
        paq=str(n0)+str(n1)+str(n2)+str(n3)
        np.append(paq)
    return np

def desencriptar(paen):
    pa2=[]
    pos={}
    posiciones=[]
    for x in paen:
        num=""
        for i in range(4):
            
            c=int(x[i])+10-7
            if c>=10:
                n=c-10
            
            else:
                n=c
            num+=str(n)
        pa2.append(num)
        if num[2:].startswith("0"):
            p=num[3]
            posiciones.append(num[2])
        else:
            posiciones.append(num[2:])
            p=num[2:]
        pos[p]=num
        

    k=[]
    for x in pos:
        k.append(int(x))
    ma=max(k)+1

    d=zeros(ma,dtype=str)

    for x in k:#sin espacio
        v=pos[str(x)]
        
        d[x]=chr(int(v[0]+v[1]))

    des=""

    for x in list(d):
        des+=x
        if x=="":
            des+=" "
    return des
    
    

        

    
        
print("OPCIONES")
print("1.Encriptar")
print("2.Desencriptar")
while True:
    try:
        op=int(input("Seleccione una opcion "))
        if op==1 or op==2:
            break
    except:
        print("Solo opcion 1 o 2")


if op==1:
    tclaro=input("Ingrese el mensaje ").upper()
    for x in range(len(encriptados(tclaro))):   
        print("Paquete ",x,encriptados(tclaro)[x])
if op==2:
    paq=input("Ingrese el paquetes separados por comas ")
    paen=paq.split(",")

    print("El mensaje desencriptado es ",desencriptar(paen))
