# Allan Michel - ADS ;)
#===================================================================================
def somar(som, memoria):
    a = som + memoria
    return a


def subtrair(memoria, sub):
    b = memoria - sub
    return b


def multiplicar(mult, memoria):
    c = mult * memoria
    return c


def dividir(div, memoria):
    d = memoria / div
    return d


def limpar_memoria():
    return 0


def escrever_numero(valor):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valor = list(valor)
    extenso = ['Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove']
    for i in range(len(valor)):
        if valor[i] == num[0]:
            valor[i] = extenso[0]
        elif valor[i] == num[1]:
            valor[i] = extenso[1]
        elif valor[i] == num[2]:
            valor[i] = extenso[2]
        elif valor[i] == num[3]:
            valor[i] = extenso[3]
        elif valor[i] == num[4]:
            valor[i] = extenso[4]
        elif valor[i] == num[5]:
            valor[i] = extenso[5]
        elif valor[i] == num[6]:
            valor[i] = extenso[6]
        elif valor[i] == num[7]:
            valor[i] = extenso[7]
        elif valor[i] == num[8]:
            valor[i] = extenso[8]
        elif valor[i] == num[9]:
            valor[i] = extenso[9]
    valor = ' '.join(valor)
    return valor


menu = True
memoria = 0

while menu:
    print("Estado da memória: {}".format(memoria))
    op = int(input(" (1) Somar \n (2) Subtrair \n (3) Multiplicar \n (4) Dividir \n (5) Limpar memória \n (6) Sair do programa \n (7) Escrever número por extenso \n Qual opção você deseja?: "))
    if op == 1:
        valor = int(input("Digite um valor para ser somado: "))
        memoria = somar(valor, memoria)
    elif op == 2:
        valor = int(input("Digite um valor para ser subtraido: "))
        memoria = subtrair(memoria, valor)
    elif op == 3:
        valor = int(input("Digite um valor para ser multiplicado: "))
        memoria = multiplicar(valor, memoria)
    elif op == 4:
        valor = int(input("Digite um valor para ser dividido: "))
        memoria = dividir(valor, memoria)
    elif op == 5:
        memoria = limpar_memoria()
    elif op == 6:
        print('Até a próxima!!!')
        menu = False
    elif op == 7:
        valor = input("Qual número deseja saber por extenso: ")
        print(escrever_numero(valor))
