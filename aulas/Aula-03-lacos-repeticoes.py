#!/usr/bin/python3


import time

# LOOP WHILE:
contador = 0
while (contador <= 10):
   print("Numero: ", contador)
   time.sleep(1)
   contador += 1

#=========================================================

# LOOP FOR:
contador = 1
print("Lista de Compras")
for i in ["Abacaxi","maçã","uva","banana","pera"]:
     print(contador,".",i)
     contador += 1
     time.sleep(1)


for i in range(10, 0, -1 ):
   print(i)
   time.sleep(1)





