# Allan Michel - ADS ;)
#===================================================================================
#Escreva um programa que imprime na tela os n primeiros números perfeitos. Um
#número perfeito é aquele que é igual à soma dos seus divisores. Por exemplo, 6 = 1 +
#2 + 3
#===================================================================================
n = int(input("Digite o valor de n: "))
soma = 0
for divisor in range(1, n):
    if n % divisor == 0:
        soma += divisor

if n == soma:
    print("O número {} é perfeito".format(n))
else:
    print("O número {} nao é perfeito\n".format(n))