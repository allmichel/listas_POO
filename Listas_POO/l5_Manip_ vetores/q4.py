# Allan Michel - ADS ;)
#===================================================================================
#4. Faça um programa que percorre duas listas e intercala os elementos de ambas,
#formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da
#lista menor.
#Exemplo:
#● lista1 = [1, 2, 3, 4]
#● lista2 = [10, 20, 30, 40, 50, 60]
#● lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]
#===================================================================================

import random

lista1 = []
lista2 = []
lista3 = []
a = random.randint(1, 10)
b = random.randint(1, 10)

for i in range (a):
    lista1.append(random.randint(0, 100))
for i in range (b):
    lista2.append(random.randint(0, 100))
if a < b:
    for i in range(max(a, b)):
        if i < a :
            lista3.append(lista1[i])
        if i < b :
            lista3.append(lista2[i])
if b < a:
    for i in range(max(a, b)):
        if i < b:
            lista3.append(lista2[i])
        if i < a:
            lista3.append(lista1[i])
print(lista1)
print(lista2)
print(lista3)