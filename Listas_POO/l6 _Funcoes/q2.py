# Allan Michel - ADS ;)
#===================================================================================
def status(a):
    if a < 4:
        print("Reprovado!")
    elif 4 <= a <= 6:
        print("Verificação Suplementar")
    elif a > 6:
        print("Aprovado")


sala = int(input("Alunos matriculados: "))
for i in range (1, sala+1):
    nota = float(input("Qual a média do aluno {}: ".format(i)))
    status(nota)
