import os
import time
os.system('cls')

numero = int(input("Digite um número para ver a sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    time.sleep(1)
