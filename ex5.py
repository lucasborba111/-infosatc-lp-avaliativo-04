def validaRequisitos(nome):    
    for i in range(0, 5):       
        if(sono=="sim"or sono=="não"):
           if(sono=="não"):
              print("Não apresenta-se totalmente disposto")
        else:
             pass
        if(idade<16 or idade>69):
           print("Não possui idade ideal")
        else:
             pass
        if(peso<50):
           print("Não possui peso ideal")
        else:
            pass
        cadastro = input("Deseja efetuar castro?")
        if(cadastro=="sim"):                 
            nome = input("Escreva seu nome completo")
            cpf = input("Escreva seu cpf:")
            senha = input("Defina uma senha:")
            sangue = input("Apresenta-se apto(a) para doar sangue?")   
            if(sangue=="sim"):
               cliente = ("nome:{}".format(nome),"cpf: {}".format(cpf),"senha: {}".format(senha),"Apto para doar: {}".format(sangue))      
               print("Cadastro",cliente)
               return True
            elif(sangue=="não"):
               return False      
        elif(cadastro=="não"):
             break
        else:
             print("Opção indisponível")       
idade = int(input("Idade:"))
peso = float(input("Peso:"))
sono = input("Dormiu 6 horas nas últimas 24 horas?")
validaRequisitos(sono)    