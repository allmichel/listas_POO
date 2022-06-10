# Allan Michel - ADS ;)
#===================================================================================
#Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é
#palíndromo. Um número palíndromo é aquele que se lido da esquerda para a direita
#ou da direita para a esquerda possui o mesmo valor (ex.: 15451)
#===================================================================================

n = input('Digite um numero com 5 digitos: ')

if str(n) == "".join(reversed(n)):
	print('{} é palíndromo!'.format(n))
else:
	print('{} não é palíndromo!'.format(n))