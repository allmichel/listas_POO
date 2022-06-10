# Allan Michel - ADS ;)
#===================================================================================
#3. Faça um programa que percorre um vetor e imprime na tela a média dos valores do
#vetor e o valor mais próximo da média.
#Exemplo:

#○ Vetor: [2.5, 7.5, 10.0, 4.0]
#○ Média: 6.0
#○ Valor mais próximo da média: 7.5
#===================================================================================
vet = []
soma = 0
n = int(input("Quantidade de notas "))
for i in range(n):
    notas = float(input("Quais são as notas?"))
    vet.append(notas)
for i in range(n):
    soma = soma + vet[i]

med = soma / n
mais_proximo = -1
ID_mais_proximo = -1
diferenca = 0
for i in range(0, n):

    if vet[i] >= med:
        diferenca = vet[i] - med
    else:
        diferenca = med - vet[i]

    if mais_proximo == -1 or diferenca < mais_proximo:
        mais_proximo = diferenca
        ID_mais_proximo = vet[i]

print("\n",vet, "\n")

print("Média = {}".format(med))
print("O valor mais próximo da média é {}".format(ID_mais_proximo))
