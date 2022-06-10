# Allan Michel - ADS ;)
#===================================================================================
# 2. Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do
# usuário e escreva essas informações na forma de um parágrafo de apresentação.
#===================================================================================

nome = input("Favor, digitar seu nome: ")
idade = input("Favor {}, agora digite sua idade: ".format(nome))
altura = input("Favor {}, agora digite sua altura: ".format(nome))
peso =  input("Favor {}, agora digite seu peso: ".format(nome))
nacio =  input("Favor {}, agora digite sua nacionalidade: ".format(nome))
print("Olá, me chamo {}, tenho {} anos, altura de {}, peso {}kg e sou {}".format(nome,idade,altura,peso,nacio))