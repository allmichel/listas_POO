# Allan Michel - ADS ;)
#===================================================================================
# 2. Faça um programa que lê uma frase e retorna o número de palavras que a frase
# contém. Considere que a palavra pode começar e/ou terminar por espaços
#===================================================================================
frase = input("Digite uma frase: ")
frase = frase.split()
print(frase)
print("Esta frase contém {} palavras".format(len(frase)))
