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

menu = True
memoria = 0

while menu:
    print("\nEstado da memória: {}".format(memoria))
    print("Opções:")
    op = int(input('(1) Somar \n (2) Subtrair \n (3) Multiplicar \n (4) Dividir \n (5) Limpar memória \n (6) Sair do programa \n Qual opção você deseja?: '))
    if op == 1:
        valor = int(input("Digite um valor para ser somado: "))
        memoria = somar(valor, memoria)
    elif op == 2:
        valor = int(input("Digite um valor para ser subtraído: "))
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
        print("Encerrando...")
        menu = False