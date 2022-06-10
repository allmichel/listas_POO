# Allan Michel - ADS ;)
#===================================================================================
def fatorial (num):
    fat = 1
    for c in range (num, 0, -1):
        fat = fat * c
    return fat


N = int(input("Número de alunos na turma: "))
M = int(input("Número de alunos no grupo M: "))

combinacao = fatorial(N)/(fatorial(M) * fatorial(N-M))
print("O numero de combinaçoes possiveis é : {}".format(combinacao))