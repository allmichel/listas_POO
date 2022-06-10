# Allan Michel - ADS ;)
#===================================================================================
# 4. Faça um programa que leia dois pontos num espaço bidimensional e calcule a
# distância entre esses pontos. Dica: distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)
#===================================================================================

from math import sqrt

print("==VALORES DE A==")
xA = float(input("favor, dgt xA"))
xB = float(input("favor, dgt xB: "))

print("==VALORES DE B==")
yA = float(input("favor, dgt yA: "))
yB = float(input("favor, dgt yB: "))

distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)

print("A distância entre os pontos A e B é: ",distAB)