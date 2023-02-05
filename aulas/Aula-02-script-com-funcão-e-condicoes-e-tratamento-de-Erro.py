#!/usr/bin/python3



import sys

#-------------------------------- COM FUNÇÃO junto com Tratamento de erro ----------------------------------------------

def soma(n_um,n_dois):
   return n_um + n_dois

def divisao(n_um,n_dois):
   try:
     res = n_um / n_dois
   except:
     res = "Deu Erro, nao pode-se realizar divisao com o '0' sendo o divisor"

   return res

if len(sys.argv) >= 3:
   if sys.argv[1].isdigit() and sys.argv[2].isdigit():
      n_um = int(sys.argv[1])
      n_dois = int(sys.argv[2])

      print("total: ", soma(n_um,n_dois))
      print("divisao: ", divisao(n_um,n_dois))
   else:
      print("somente valores inteiros numericos")
else:
  print("por favor, passe como argumento 2 valores inteiros;")

#-----------------------------------------------------------------------------------------






#------------------------ SEM FUNÇÃO --------------------------------------------------

#if len(sys.argv) >= 3:
#   if sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[2] != "0" :
#      n_um = int(sys.argv[1])
#      n_dois = int(sys.argv[2])
#
#      print("total: ", n_um + n_dois)
#      print("divisao: ", n_um / n_dois)
#   else:
#      print("somente valores inteiros numericos, e o ultimo argumento nao pode ser '0'")
#else:
#  print("por favor, passe como argumento 2 valores inteiros;")

#----------------------------------------------------------------------------------------





