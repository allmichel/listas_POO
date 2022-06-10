# Allan Michel - ADS ;)
#===================================================================================
arq = open('texto2.txt')

linha1 = arq.readline()
linha2 = arq.readline()
linha3 = arq.readline()

arq.close()

dic1 = {linha1[0:7]: linha1[8:14]}
dic2 = {linha2[0:7]: linha2[8:15]}
dic3 = {linha3[0:7]: linha3[8:15]}

print(dic1)
print(dic2)
print(dic3)
