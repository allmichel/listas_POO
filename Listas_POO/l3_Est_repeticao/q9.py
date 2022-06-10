# Allan Michel - ADS ;)
#===================================================================================
#9. Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y,
#além do resto da divisão. Não é permitido usar as operações de divisão e resto de
#divisão do Python (use apenas soma e subtração).
#===================================================================================
x = int(input("valor de x: "))
y = int(input("valor de y: "))
cont = 0
acc = 0

for i in range(y, x+1, y):
    cont = cont + 1
    acc  = acc + y
    print ("divisao = ", cont, " resto = ", x-acc)