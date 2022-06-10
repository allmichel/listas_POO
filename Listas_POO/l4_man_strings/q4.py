# Allan Michel - ADS ;)
#===================================================================================
# 4. Faça um programa que decida se duas strings lidas do teclado são palíndromas
# mútuas, ou seja, se uma é igual à outra quando lida de trás para frente. Exemplo:
# amor e roma.
#===================================================================================

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
if palavra1[::].strip() == palavra2[::-1].strip():
    print("As duas são palíndromas mútuas!")
else:
    print("Elas não são palíndromas!")
