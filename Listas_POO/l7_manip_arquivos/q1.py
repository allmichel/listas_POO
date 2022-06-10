# Allan Michel - ADS ;)
#===================================================================================
arq = open('texto.txt', 'r+')
arq.write(input('Diga la > '))
arq.close()

arq = open('texto.txt')
texto = arq.read()
arq.close()

print(texto)
