#Escreva uma função em Python que leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.

def separacao(lista):
    #for i in range(n+1):
        #valor = int(input())
        #lista.append(valor)

    tupla = tuple(lista)
    print(tupla)
    tupla_de_pos_pares = []

    for i in range(1,len(lista)):
        if (i+1) % 2 == 0:
            tupla_de_pos_pares.append(lista[i])
    for i in lista:
        if i % 2 == 0:
            lista.remove(i)
            

    tupla_de_pos_pares = tuple(tupla_de_pos_pares)
    
    return tupla_de_pos_pares, lista

#n = int(input()) #Tamanho da tupla inicial

lista = [1,3,2,7,5,5,7,14,9,16,11]


print(separacao(lista))