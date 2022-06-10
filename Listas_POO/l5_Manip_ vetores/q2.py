# Allan Michel - ADS ;)
#===================================================================================
#2. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
#armazene os resultados em um vetor. Depois, monte um outro vetor contendo quantas
#vezes cada valor foi obtido. Imprima os dois vetores. Use a função
#random.randint(1,6) para gerar números aleatórios, simulando os lançamentos dos
#dados.
#Exemplo de uma possível saída:
#● [3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
#● [1, 0, 3, 1, 4, 1]
#===================================================================================

import random
lista1 = []
lista2 = []

for i in range(0,99):
    lista1.append(random.randint(1,6))

lista2.append(lista1.count(1))
lista2.append(lista1.count(2))
lista2.append(lista1.count(3))
lista2.append(lista1.count(4))
lista2.append(lista1.count(5))
lista2.append(lista1.count(6))
print(lista1)
print(lista2)