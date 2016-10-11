#Vamos na fé que dará certo

lista=[]
while True:
    print("--Agenda--")
    print("Digite: ")
    print("1- Inserir número de telefones:")
    print("2- Pesquisar por telefones: ")
    print("3- Pesquisar por index: ")
    print("4- Excluir item da lista de telefones: ")
    print("5- Exibir lista completa de telefones: ")
    print("6- Excluir lista completa de telefones: ")
    print("0- Sair -")
     #referente a opção do menu
    agenda =int(input("Digite a opção: "))
    #trato logo o caso do sair 
    if agenda == 0:
        break
    elif agenda == 1:
        opc = 1
       
        while True:
            if opc == 0:
                break
            #estabeleço o tamanho exato que eu quero os digitos do telefone
            numero =(input("Digite um número com 8 digitos: "))
            tam = len(numero)
            if tam < 8 or tam > 8:
                print("Número inválido. Digite um número com 8 digitos")
            else:
                #adiciono a lista 
                lista.append(numero)
                #caso eu queira adicionar ou não outro num de telefone
                
                opc=int(input("Digite 1--Sim para repetir a opc e 0-- para não"))
    elif agenda == 2:
        if len(lista) == 0:
            #se a pessoa digitar 2 antes de cadastrar algo
            print("Lista vazia! Cadastre um item antes")
        else:
            cont = 0
            pesqNum = input("Digite o item que quer pesquisar: ")
            while cont < len(lista):
                if lista[cont] == pesqNum:
                    encontreiItem = cont
                    print("Seu telefone foi encontrado e é o índice : %d "%encontreiItem)
                    break
                else:
                    print("Não foi encontrado índice")
                cont+=1
    #
    elif agenda == 3:
            if len(lista) == 0:
                #se a pessoa digitar 3 antes de cadastrar algo
                print("Lista vazia! Cadastre um item antes")
            else:
                cont = 0
                pesqNum = int(input("Digite o index que quer pesquisar: "))
                while cont < len(lista):
                    if pesqNum < (len(lista) - 1) or pesqNum > (len(lista) - 1):
                        print("Não foi encontrado índice")
                        break
                    else:
                        print("Item encontrado: ", lista[pesqNum])
                        break
                    cont+=1
    
    
    
    elif agenda == 4:
        cont=0
        if len(lista) == 0:
            print("Lista vazia! Cadastre um item antes")
        else:
            #trato logo a parte do numeroencontroado como false 
            numeroEncontrado = False
            cont=0
            pesqNum=int(input("Digite o item que quer Excluir: "))
            while cont < len(lista):
                #se encontrar o numero eu deleto ela e paro
                 if lista[cont] == pesqNum:
                    numeroEncontrado = True
                    del lista[cont]
                    break
                 else:
                    cont += 1
            if numeroEncontrado is True:
                print("Número excluido com sucesso!")
            else:
                print("Erro! Numero informado nao pertence a lista!")
    elif agenda == 5:
        cont=0
        if len(lista) == 0:
            print("Lista vazia! Cadastre um item antes")
        else:
            print("agenda: ")
            print(lista)
    #bloco vai deletar toda a lista, dever ser tratado a parte
    #de "deseja realmente excluir esta agenda?", aparecendo mais de uma vez pro usuário
    elif agenda == 6:
        #se a pessoa digitar 5 antes de inserir algo
        if len(lista) == 0:
            print("Lista vazia! Cadastre um item antes")
        else:
            cont = 0
            while cont < len(lista):
                del lista[cont]
                cont+=1
            print("Sua agenda foi excluida")
            
    elif (agenda < 0) or (agenda > 7):
        break
    else:
        print("Digite uma opc válida.")
