# Allan Michel - ADS ;)
#===================================================================================
arq = open('texto5.txt', 'r+')

linha1 = arq.readline()
linha2 = arq.readline()
linha3 = arq.readline()
linha4 = arq.readline()
linha5 = arq.readline()

arq.close()

arq = open('texto5copia.txt', 'w+')
arq.write(linha3)
arq.write(linha4)
arq.write(linha5)

arq.close()