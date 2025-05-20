import os
import random
import time

participantes = list()
while True:
    
    os.system("cls || clear")
    os.system("color 7c")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    
    
os.system("cls || clear")
print("Particpantes Registrados:")
print(participantes)
x = input("Presione 'Enter' para continuar...",)

cont = 10
while cont > 0:
    os.system("cls || clear")
    print("Sorteando...")
    print("Quedan", cont, "segundos")
    time.sleep(1)
    cont -= 1

fin = len(participantes) - 1
ganador = random.randint(0, fin)
print("El ganador es:", participantes[ganador])
