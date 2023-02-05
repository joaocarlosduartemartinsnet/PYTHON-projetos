#!/usr/bin/python3

import sys

print(sys.argv)


if sys.argv[1] == "+":
  print(int(sys.argv[2])+int(sys.argv[3]))
elif sys.argv[1] == "/":
  print(int(sys.argv[2])/int(sys.argv[3]))
else:
  print("argumento matematico invalido")


#==================introduction=======================

#num_1 = int(input("digite um valor: "))
#num_2 = int(input("digite um segundo valor: "))
#print("a soma entre ", num_1,"+",num_2, " e igual a ", num_1+num_2)
