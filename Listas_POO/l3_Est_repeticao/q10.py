# Allan Michel - ADS ;)
#===================================================================================
#10. Faça um programa em Python que calcule o valor de Pi, utilizando a fórmula de
#Leibniz

#π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 - ...

#Adicione parcelas no cálculo até que a diferença de uma interação para a seguinte seja
#menor do que um valor de erro aceitável x informado pelo usuário.
#===================================================================================
import math
k = 1
s = 0

for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k

    k += 2

print(s)