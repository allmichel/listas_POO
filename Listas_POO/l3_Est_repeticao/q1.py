# Allan Michel - ADS ;)
#===================================================================================
#1. Faça um programa para montar a tabela de multiplicação de números de 1 a 10
#(exemplo: 1 x 1 = 1, 1 x 2 = 2, etc.).
#===================================================================================

tabuada = int(input("Favor, dgt o numero desejado para ver a tabuada: "))

for cont in range(10):
    print("{} x {} = {}".format(tabuada, cont+1, tabuada*(cont+1)))