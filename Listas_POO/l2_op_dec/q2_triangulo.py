# Allan Michel - ADS ;)
#===================================================================================
#2. Faça um programa que leia três coordenadas num espaço 2D e indique se formam um
#triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno)
#a. Equilátero: todos os lados iguais
#b. Isósceles: dois lados iguais
#c. Escaleno: todos os lados diferentes
#===================================================================================
a = float(input("dgt valor A: "))
b = float(input("dgt valor B: "))
c = float(input("dgt valor C: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("os valores informados não formam um triangulo :(")

elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')