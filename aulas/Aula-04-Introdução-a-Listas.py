from time import sleep

nome = "joao"
idade = 18

minha_lista = [nome,idade, "azul", "VERMELHO"]

# com o metodo append(ELEMENTO), serve para adicionar um valor a lista que desejamos, esse metodo e muito utilizado para listas;
minha_lista.append("carlitos")

# metodo remove(ELEMENTO), e utilizado em listas serve para remover;
minha_lista.remove("azul")


for i in minha_lista:
     print(i)
     sleep(1)


# os array sao compostos por indices e elementos;
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])


# aqui diz quero ir do indice zero ate o terceiro indice, o ultimo elemento sera disconciderado;
print(minha_lista[0:3])

# se utilizarmos indices  negativos os elementos sao pegos do ultimo ate o inicio
print(minha_lista[-1]) # => VERMELHO
print(minha_lista[-2]) # => azul


# as strings funcionam como se fossem uma lista de caracteres(conjunto de caracteres);
teste = "ola mundo"

for letra in teste:
  print(letra)


"""
====> TIPOS DE COLEÇÕES: <====
- Listas 
- Tuplas
- Dicionarios 
- Conjuntos
"""


