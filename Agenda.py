AGENDA = {}

def Mostrar_Contatos():
   if AGENDA:
      for contato in AGENDA:
            print(" ")
            
            # COM FATORAÇÃO: (usa-se para evitar codigos repetidos;)
            Buscar_Contato(contato)  

            """
            -> SEM FATORAÇÃO:
            print("Nome:", contato)
            print("Telefone:",AGENDA[contato]["tel"])
            print("Email:",AGENDA[contato]["email"])
            print("Endereço:",AGENDA[contato]["endereco"])
            """        
            print(" ")
            print(10*"===")
   else:
          print("nao há contatos cadastrados")


def Buscar_Contato(contato):
     try:
         print('Nome:', contato)
         print('Telefone:', AGENDA[contato]['tel'])
         print('Email:',    AGENDA[contato]['email'])
         print('Endereço:', AGENDA[contato]['endereco'])
     except KeyError:
         print("contato inexistente")
     except Exception as error:
         print("algo deu errado")
         print(error)
     
def ler_detalhes():
     tel = input("Telefone: ")
     email = input("Email: ")
     endereco = input("endereço: ")
     return tel, email, endereco
     
def Incluir_Editar_Contato(contato,tel,email, endereco):
           
     AGENDA[contato] = {
        "tel": tel,
        "email": email,
        "endereco": endereco
     }
     salvar()
     print("contato {} adicionado/editado com sucesso!!!".format(contato))


def Excluir_contato(contato):
 try:
    # del AGENDA[contato]
    # ou
    AGENDA.pop(contato)
    salvar()
    print("contato {} EXCLUIDO com sucesso!!!".format(contato))
 except KeyError:
    print("contato inexistente")
 except Exception as error:
    print("algo deu errado")
    print(error)

def Exportar_Contatos(nome_do_arquivo):
   try:
     arquivo = open("/home/kali/Documentos/meus-prigramas-em-python/projetos/{}".format(nome_do_arquivo), "w")
     for contato in AGENDA:              
        telefone = AGENDA[contato]["tel"]
        email = AGENDA[contato]["email"]
        endereco = AGENDA[contato]["endereco"]
        arquivo.write("{},{},{},{} \n".format(contato, telefone, email, endereco))
 
   except Exception as error:
      print("deu algum erro")
      print(error)


def Importar_contatos(nome_do_arquivo):
   try:
      with open("/home/kali/Documentos/meus-prigramas-em-python/projetos/{}".format(nome_do_arquivo), "r") as arquivo:
         linhas = arquivo.readlines()
         for linha in linhas:
                detalhe = linha.strip().split(",")
                contato = detalhe[0]
                tel = detalhe[1]
                email = detalhe[2]
                endereco = detalhe[3]
                Incluir_Editar_Contato(contato, tel, email, endereco)   
   except FileNotFoundError:
      print("arquivo nao encontrado")
   except Exception as error:
      print("ocorreu algum erro")
      print(error)
       

def salvar():
       Exportar_Contatos("database.csv")
       
def carregar():
   try:
      with open("/home/kali/Documentos/meus-prigramas-em-python/projetos/database.csv","r") as arquivo:
         linhas = arquivo.readlines()
         for linha in linhas:
                detalhe = linha.strip().split(",")
                
                nome = detalhe[0]
                tel = detalhe[1]
                email = detalhe[2]
                endereco = detalhe[3]
                
                AGENDA[nome] = {
                   "tel": tel,
                   "email": email,
                   "endereco": endereco
               }
         print(">>> database carregado com sucesso;")
         print(" {} Contatos Carregados ".format(len(AGENDA)))
   except FileNotFoundError:
      print("add o primeiro contato para ativar o database")
   except Exception as error:
      print("ocorreu algum erro")
      print(error)


def Imprimir_MENU():
       print(" ")
       print("1 - Mostrar Todos os Contatos da Agenda;")
       print("2 - Buscar Contato;")
       print("3 - Incluir Contato;")
       print("4 - Editar Contato;")
       print("5 - Excluir Contato;")
       print("6 - Exportar contatos para CSV;")
       print("7 - Importar contatos CSV")
       print("0 - sair do programa;")
       print(" ")


# INICIO DO PROGRAMA

carregar()
while True:      
   Imprimir_MENU()
   opcao = input("Escolha uma Opção: ")

   if opcao == "1":
        print("Mostando Contatos: ")
        Mostrar_Contatos()
   elif opcao == "2":
        contato = input("Qual contato Deseja Buscar: ")
        Buscar_Contato(contato)
        
   elif opcao == "3":
        contato = input("nome do contato: ")
      
        try:
           AGENDA[contato]
           print("contato ja existente")
           
        except KeyError:       
           tel, email, endereco = ler_detalhes()
           Incluir_Editar_Contato(contato, tel, email, endereco)
         
   elif opcao == "4":
        contato = input("nome do contato: ")
      
        try:
           AGENDA[contato]
           print("editando contato:", contato)
           tel, email, endereco = ler_detalhes()
           Incluir_Editar_Contato(contato, tel, email, endereco)
           
        except KeyError: 
           print("contato inexistente")      
           
      
   elif opcao == "5":
        contato = input("nome do contado que deseja excluir: ")
        Excluir_contato(contato)
        
   elif opcao == "6":
        nome_do_arquivo = input("nome do arquivo que deseja ser Exportado: ")
        Exportar_Contatos(nome_do_arquivo)
        
   elif opcao == "7":
        nome_do_arquivo = input("nome do arquivo que deseja importar: ")
        Importar_contatos(nome_do_arquivo)
        
   elif opcao == "0":
        print("fechando programa")
        break
     
   else:
        print("opção invalida")
























 


#Buscar_Contato("maria")
#Buscar_Contato("nicolas")
#Mostrar_Contatos()
#Incluir_Editar_Contato("Eduardo", None, None, None)
#Excluir_contato("nicolas")
#Mostrar_Contatos()















# ------------- APENAS IDEIAS ----------------

AGENDA = {
    "joao":{
       "tel":"99999-9999",
       "email": "oila@gmail.com",
       "endereco": "rua dddd"
    },
    
    "pedro":{
       "tel":"99999-9999",
       "email": "oilsdfsdfsa@gmail.com",
       "endereco": "av.asio alves"
    },
    
    "guilherme":{
       "tel":"99999-9999",
       "email": "oila@gmail.com",
       "endereco": "pro alves"
    },
    
    "laura":{
       "tel":"99999-9999",
       "email": "oilsdfsa@gmail.com",
       "endereco": "av.protasio alves" 
    }
}





"""
print(AGENDA["guilherme"]) # => traz tudo sobre o elemento guilherme; 


print(AGENDA["guilherme"]["tel"]) # => podemos filtrar ainda mais;


AGENDA["guilherme"]["endereco"] = "rua teodoro machado" # => podemos sobrescrever valores tambem;


print(AGENDA["guilherme"])


AGENDA["lucas"] = { # => podemos criar novas elementos dessa forma tbm;
   "tel":"933333-00000",
   "gmail": "dhdhhdhd@gmail.com",
   "endereco":"rua cardoso",
}

print(AGENDA["lucas"])

AGENDA.pop("guilherme") # o metodo 'pop' serve para excluir um elemento;
"""

