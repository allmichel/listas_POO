# Allan Michel - ADS ;)
#===================================================================================
# 4. Faça um programa para listar todos os divisores de um número ou dizer que o número é primo caso não existam divisores. Ao final,
#   verifique se o usuário deseja analisar outro número
#===================================================================================

n = int(input("Digite um número inteiro positivo: "))
cont = 1

for cont in range(1, n-1):
    if n % cont != 0:
        print("{} não é divisor de {}!". format(n, cont))
    else:
        print("{} é divisor de {}!".format(n, cont))
        cont += 1