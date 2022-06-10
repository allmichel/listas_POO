# Allan Michel - ADS ;)
#===================================================================================
#   3. Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo F(0) = 0, F(1) = 1 e
#   F(n)= F(n-1)+F(n-2). Por exemplo, caso o usuário informe o número 9, o resultado seria: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#===================================================================================
n = int(input("dgt um número: "))
trm1 = 0
trm2 = 1
cont = 0

for cont in range(n+1):
    trm3 = trm1 + trm2
    print("{} -> ".format(trm1), end='')
    trm1 = trm2
    trm2 = trm3
    cont = cont + 1