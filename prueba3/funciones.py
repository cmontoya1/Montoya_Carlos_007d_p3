import os
import time
import numpy as np
os.system('cls')

lista_piso=[1,2]
lista_ruts=[]
lista_nombre_dueño=[]
lista_nombre_mascota=[]
lista_habitaciones=["A","B","C","D","E"]
lista_dias=[]



guarderia=np.zeros((2,5),int)


def habitaciones_disponibles():
    for x in range(2):
        print("piso",lista_piso[x],end="\t")
        for y in range(5):
            print(guarderia[x][y],end="")
        print()

def mostrar_menu(): 
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4.Salir """)
    

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre_mascota():
    while True:
        nombre_mascota = input("Ingrese nombre de la mascota: ")
        if len(nombre_mascota.strip()) >= 3:
            return nombre_mascota
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")


def cantidad_dias():
    while True:
        try:
            cantidad_d=int(input("Ingrese cantidad de días: "))
            if cantidad_d >=0:
                return cantidad_d
            else:
                print("ERROR!Ingrese cantidad de día válida")
        except:
            print("ERROR!ingrese un número entero")


def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3:
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_piso():
    while True:
        try:
            piso=int(input("Ingrese piso"))
            if piso in lista_piso:
                return piso
            else:
                print("ERROR!Ingrese opción válida(1-2)")
        except:
            print("ERROR!Ingrese un número entero")   

def validar_habitacion():
    while True:
        try:
            habitacion=str(input("Ingrese habitación"))
            if habitacion.upper() in lista_habitaciones:
                return habitacion
            else:
                print("Ingrese opción válida(A,B,C,D,E)")
        except:
            print("ERROR, ingrese letras")                         


def grabar():
    rut_dueño=validar_rut()
    nombre_dueño=validar_nombre()
    nombre_mascota=validar_nombre()
    dias=cantidad_dias()
    lista_ruts.append(rut_dueño)
    lista_nombre_dueño.append(nombre_dueño)
    lista_dias.append(dias)
    lista_nombre_mascota.append(nombre_mascota)
    mostrar_menu()
    while True:
        habitaciones_disponibles()
        if 0 not in guarderia:
            print("No existen habitaciones disponibles")
            return
        else:
            piso=validar_piso()
            habitacion=validar_habitacion()
            lista_piso.append(piso)
            lista_habitaciones.append(habitacion)

                
        
def buscar_mascota():
    rut=validar_rut()
    if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                if rut==lista_ruts[x]:
                    posicion_encontrada = x
                    return
            print(lista_nombre_mascota[posicion_encontrada])      
    else:
        print("Mascota no registrada")             
                
def salir():
    while True:

        print("Gracias por preferir Mascota Segura!")
        break
            
def Retirarse(valor):
    rut=validar_rut()
    if rut in lista_ruts:
        for i in range(len(lista_ruts)):
            if rut==lista_ruts[i]:
                


    