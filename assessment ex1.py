#Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.
n1 = int(input())
n2 = int(input())
n3 = int(input())

tupla = (n1,n2,n3)
print(tupla)
lista_da_tupla = list(tupla)
lista_da_tupla.sort()
tupla = tuple(lista_da_tupla)
print(tupla)