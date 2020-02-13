# encoding: utf8
#!/usr/bin/python3

#Funcao que verifica os elementos selecionados na lista, se eles tem solucao, caso tenha, ele verifica qual e a solucao
#Apropriada para ele e entao ele resolve pelos metodos e retorna o elemento que veio desta solucao
def verifica(arg1, arg2):

    #Tiramos o "OU" logico para trabalhar apenas com os elementos
    #Se ele tiver o "OU" ele retira, se nao tiver ele mantem, sinal que e um elemento apenas
    try:
        aux1 = arg1.split("v")
    except:
        aux1 = arg1


    try:
        aux2 = arg2.split("v")
    except:
        aux2 = arg2

    resposta = []

    #Se tivermos um caso do tipo: pvp ou qvq ... Tratamos ele primeiramente
    #Se ele for pvp, ele vira apenas p
    if (len(aux1) > 1):
        if (aux1[0] == aux1[1]):
            aux1.remove(aux1[1])

    if (len(aux2) > 1):
        if (aux2[0] == aux2[1]):
            aux2.remove(aux2[1])

    #Se temos algo do tipo pvq , ¬qvp vamos resolver por pares
    if (len(aux1) > 1 and len(aux2) > 1):

        # Comparando o Lado Esquerdo
        if (aux1[0].find("¬") == 0):
            aux = aux1[0].replace("¬", "")
            if (aux == aux2[0]):
                resposta.append(aux1[1] + "v" + aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux1[1] + "v" + aux2[0])
                return resposta[0]
        else:
            aux = "¬" + aux1[0]
            if (aux == aux2[0]):
                resposta.append(aux1[1] + "v" + aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux1[1] + "v" + aux2[0])
                return resposta[0]

        # Lado Direito
        if (aux1[1].find("¬") == 0):
            aux = aux1[1].replace("¬", "")
            if (aux == aux2[0]):
                resposta.append(aux1[0] + "v" + aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux1[0] + "v" + aux2[0])
                return resposta[0]
        else:
            aux = "¬" + aux1[1]
            if (aux == aux2[0]):
                resposta.append(aux1[0] + "v" + aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux1[0] + "v" + aux2[0])
                return resposta[0]

    #Se temos algo do tipo p, ¬pvq resolvemos da seguinte maneira
    elif(len(aux1) == 1 and len(aux2) > 1):

        if (aux1[0].find("¬") == 0):
            aux = aux1[0].replace("¬", "")
            if (aux == aux2[0]):
                resposta.append(aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux2[0])
                return resposta[0]
        else:
            aux = "¬" + aux1[0]
            if (aux == aux2[0]):
                resposta.append(aux2[1])
                return resposta[0]
            elif (aux == aux2[1]):
                resposta.append(aux2[0])
                return resposta[0]

    #Se temos algo inverso ao de cima ¬pvq, p resolvemos de uma maneira igual
    elif(len(aux1) > 1 and len(aux2) == 1):

        if (aux2[0].find("¬") == 0):
            aux = aux2[0].replace("¬", "")
            if (aux == aux1[0]):
                resposta.append(aux1[1])
                return resposta[0]
            elif (aux == aux1[1]):
                resposta.append(aux1[0])
                return resposta[0]
        else:
            aux = "¬" + aux2[0]
            if (aux == aux1[0]):
                resposta.append(aux1[1])
                return resposta[0]
            elif (aux == aux1[1]):
                resposta.append(aux1[0])
                return resposta[0]

    #Aqui e tratado caso seja 1 pra 1, por exemplo temos que: q, q   = q
    elif (len(aux1) == 1 and len(aux2) == 1):
        #Se um for negado e o outro nao
        if(aux1[0].find("¬") == 0):
            aux = aux1[0].replace("¬", "")
            if(aux == aux2[0]):
                return {}

        #Se forem iguais
        if(aux1[0] == aux2[0]):
            reposta = aux1[0]
            return resposta[0]

    # Se nao e retornado falso, pois nao atende a nenhuma das condicoes acima!!
    else:
        return False

#Funcao que converte a sentenca para a notacao utilizada na solucao por resolucao
def converte(arg):
    listaConvert = []
    for i in arg:
        #Se tiver um implica ele quebra, inverte o sinal do primeiro elemento e troca o "->" por "v" (OU logico)
        if("->" in i):

            aux = i.split("->")
            if("¬" in aux[0]):
                aux[0] = aux[0].replace("¬", "")
            else:
                aux[0] = "¬"+aux[0]

            aux = "v".join(aux)
            i = aux

        listaConvert.append(i)

    #Printa a lista de elementos ja convertida
    print(listaConvert)

    return listaConvert

#Nossa funcao de busca e resolucao
def busca(lista):
    listaAux = lista

    #Pega o elemento elemento da lista
    for i in range(len(listaAux)):
        #Compara o elemento selecionado com os outros da lista, se for possivel a solucao, resolve, caso contrario
        #Nao resolve e vai para o proximo elemento da lista
        #Caso o elemento tenha sido escolhido, substituimos ele por -1 na lista, entao ele nao sera mais selecionado
        for j in range(len(listaAux)):
            if(listaAux[i] != -1 and listaAux[j] != -1 and i != j):
                ver = verifica(listaAux[i], listaAux[j])
                print("P" + str(i) +", P"+str(j) +", P Selecionado="+str(listaAux[i])+", P Selecionado="+str(listaAux[j])+ ", Resposta="+ str(ver))
                listaAux.append(ver)
                if(ver!= False):
                    listaAux[i] = -1
                    listaAux[j] = -1
                print(listaAux)

#Funcao principal
def main():

    #Coloque sua sentenca para Q e para P
    x = "Esta chovendo "
    y = "Vou sair "
    z = "Vou ficar em casa"

    #Coloque a 'formula' para ser resolvida
    a = "p, p -> q, q -> r, :- r"
    #a = "¬p -> q, p -> r, r -> q, :- q"

    print("")

    a = a.replace(" ","")
    arg = a.split(",")
    resp = a.split(":-")
    resp.pop(0)
    qtd = len(arg)
    arg.pop(qtd-1)

    listaConvert = converte(arg)
    print(listaConvert)

    #print(qtd)
    #print(arg,resp)

    listaResultadoFinal = []
    busca(listaConvert)
    listaResultadoFinal = listaConvert[len(listaConvert)-1]
    igual = listaResultadoFinal
    listaResultadoFinal = listaResultadoFinal.split("v")

    # Se tivermos um caso do tipo: pvp ou qvq ... Tratamos ele primeiramente
    # Se ele for pvp, ele vira apenas p
    if(len(listaResultadoFinal) > 1):
        if (listaResultadoFinal[0] == listaResultadoFinal[1]):

            listaResultadoFinal.remove(listaResultadoFinal[1])
            igual = listaResultadoFinal[0]
    print("-------------------------------------------------------------------------------")
    print("")
    print("A resposta final obtida pelo metodo da resolucao foi: ")
    for i in range (len(listaResultadoFinal)):

        if ("¬" in listaResultadoFinal[i]):
            listaResultadoFinal[i] = listaResultadoFinal[i].replace("¬", "")
            if(listaResultadoFinal[i] == 'p'):
                print("nao " + str(x))
            elif(listaResultadoFinal[i] == 'q'):
                print("nao "+ str(y))
            elif(listaResultadoFinal[i] == 'r'):
                print("nao" + str(z))
        else:
            if (listaResultadoFinal[i] == 'p'):
                print(x)
            elif (listaResultadoFinal[i] == 'q'):
                print(y)
            elif (listaResultadoFinal[i] == 'r'):
                print(z)
    print("")
    if(igual == resp[0]):
        print("A resposta esta correta! :) ")

    else:
        print("Nao foi possivel chegar no resultado dado...... :( ")

main()