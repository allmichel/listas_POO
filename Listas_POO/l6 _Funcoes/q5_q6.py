# Allan Michel - ADS ;)
#===================================================================================
import math

def trianguloArea(b, h):
    a = (b * h) / 2
    return a


def circuloArea(r):
    b = math.pi * r * r
    return b


def retanguloArea(larg, comp):
    c = larg * comp
    return c


def perimetroCirculo(r):
    d = 2 * math.pi * r
    return d


def perimetroTriangulo(l1, l2, l3):
    e = l1 + l2 + l3
    return e

def perimetroRetangulo(larg, comp):
    f = larg * 2 + comp * 2
    return f

figura = input("Qual forma geométrica deseja utilizar (triangulo - circulo - retangulo) : ")
figura = figura.strip().lower()
if figura == "triangulo":
    b = float(input("Digite a base: "))
    a = float(input("Digite a altura: "))
    l1 = float(input("Digite o lado 1: "))
    l2 = float(input("Digite o lado 2: "))
    l3 = float(input("Digite o lado 3: "))
    trianguloArea(b, a)
    perimetroTriangulo(l1, l2, l3)
    print("Área do triângulo = {} e seu perimetro = {}".format(trianguloArea(a, b), perimetroTriangulo(l1, l2, l3)))
elif figura == "retangulo":
    l = float(input("Digite a largura: "))
    c = float(input("Digite o comprimento: "))
    retanguloArea(l, c)
    perimetroRetangulo(l, c)
    print("Área do retângulo = {} e seu perimetro = {}".format(retanguloArea(l, c), perimetroRetangulo(l, c)))
elif figura == 'circulo':
    r = float(input("Digite o raio: "))
    circuloArea(r)
    perimetroCirculo(r)
    print("Área do círculo = {} e seu perímetro = {}".format(circuloArea(r), perimetroCirculo(r)))
else:
    print("ERRO")
