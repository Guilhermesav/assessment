#Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
#O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
n = int(input())
#N = Numero_final
numeros_pares = []
for i in range(1,n+1):
    if i % 2 == 0:
        numeros_pares.append(i)
        print(i)
soma_dos_numeros_pares = sum(numeros_pares)

print("A soma dos numeros pares de 1 até",n,"é:",soma_dos_numeros_pares) 