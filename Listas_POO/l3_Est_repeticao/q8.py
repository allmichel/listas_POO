# Allan Michel - ADS ;)
#===================================================================================
# Elabore um programa que leia n valores e mostre a soma de seus quadrados.
#===================================================================================
n = int(input("Digite um valor n: "))
soma = 0

for i in range(1, n):
    valores = int(input("Digite os valores: "))
    soma += valores**2
    print ("A soma é: {}".format(soma))