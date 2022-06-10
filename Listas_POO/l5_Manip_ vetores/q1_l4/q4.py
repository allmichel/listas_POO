palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
palavra1 = palavra1.strip().lower()
palavra1 = list(palavra1)
palavra2 = palavra2.strip().lower()
palavra2 = list(palavra2)
list.reverse(palavra2)
if palavra1 == palavra2:
        print("As duas são palindromas mútuas!")
else:
    print("Elas não são palíndromas!")