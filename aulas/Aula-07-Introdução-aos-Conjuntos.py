# CONJUNTOS

"""
=> Assim como o dicionario, tambem e primo das listas e tuplas;
=> E assim como o dicionario, o conjunto não é ordenado, ou seja, imprime os valoeres mas nao na ordem correta;
=> A vantagem do conjunto e de nao imprimir valores repetidos;
=> E tambem e mais rapido;
"""

conjunto_cores = {
    "vermelho", 
    "vermelho", 
    "azul",
    "azul", 
    "roxo",
    "roxo",
    "rosa",
    "rosa"
}

# o metodo "add" serve para adicionar um elemento no conjunto;
conjunto_cores.add("rosa")

# o metodo "remove" serve para remover um elemento no conjunto
conjunto_cores.remove("roxo")


for i in conjunto_cores:
     print(i)
