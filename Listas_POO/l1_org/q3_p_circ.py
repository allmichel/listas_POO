# Allan Michel - ADS ;)
#===================================================================================
# 3. Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio.
# Dica: perímetro <- 2 * pi * raio.
#===================================================================================
import math
from cmath import pi
raio = float(input("Favor, dgt o raio: "))
p = 2*pi*raio
print("o perimetro da circuferencia de raio {:.2f} é: {:.2f}".format(raio,p)) 