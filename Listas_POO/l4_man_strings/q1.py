# Allan Michel - ADS ;)
#===================================================================================
#Escreva um programa que lê uma frase, uma palavra antiga e uma palavra nova. O
#programa deve imprimir a frase com as ocorrências da palavra antiga substituídas pela
#palavra nova.
#===================================================================================
frase = input('Digite uma frase: ')
x = input('Qual palavra deseja substituir? ')
y = input('qual palavra da frase? ')
frase = frase.replace(x, y)
print(frase)