# DICIONARIO

"""
=> o dicionario e primo das listas e tuplas;
=> ele e composto por "chaves" e "seus valores";
=> para criarmos um dicionario basta usar {} para cria-lo;
"""

#=====================================================================

oi = "bom dia"
dicionario = {
         "tijolo": "um objeto para montar muros",
         oi:"e um cumprimento",
         "constituicao": "Lei máxima do Brasil"
}


# para pegar o valor do dicionario temos que usar colchetes
print(dicionario["tijolo"]) # => direto pelo nome;
print(dicionario[oi]) # => atraves de uma variavel;
print(dicionario["constituicao"])

#======================================================================================

pessoas = {
    "joao": 12,
    "kruel": 15,
    "julio": 20,
}

#======================================================================================
#==== AS DUAS FORMAS DE OBTER O VALOR DE CADA CHAVE NO DICIONARIO, ESTAO CORRETAS: ====
#======================================================================================

for i in pessoas.values(): #o metodo '.values()' pega somente o valor de cada chave;
     print(i)

# ou podemos simplesmente usar:

for i in pessoas: 
     print(i, "=>",pessoas[i]) # neste caso eu trabalho com a chave e os valores;

#======================================================================================

