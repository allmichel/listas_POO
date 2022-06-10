# Allan Michel - ADS ;)
#===================================================================================
#7. Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de
#escada, usando apenas letras maiúsculas.
#Exemplo:
#● Nome = Vanessa
#Resultado gerado pelo programa:
#● V
#● VA
#● VAN
#● ....
#===================================================================================

nome = input('Digite o seu nome: ')
nome = nome.upper()
for i in range (0,len(nome)+1):
    print(nome[:i])