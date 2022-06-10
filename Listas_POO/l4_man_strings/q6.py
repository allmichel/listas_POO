# Allan Michel - ADS ;)
#===================================================================================
# 6. Faça um programa que leia o nome do usuário e mostre o nome de trás para frente,
# utilizando somente letras maiúsculas. Exemplo: Nome = Vanessa. Resultado gerado
# pelo programa: ASSENAV
#===================================================================================
nome = input("Digite um nome: ")
nome = nome[::-1]
nome = nome.upper()
print(nome)
