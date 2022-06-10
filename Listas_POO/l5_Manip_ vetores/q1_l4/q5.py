palavra = input("Digite a palavra a ser analisada: ")
palavrab = input("Digite a palavra a ser analisada: ")
palavra = palavra.strip().lower()
palavra = list(palavra)
palavrab = palavrab.strip().lower()
palavrab = list(palavrab)
list.sort(palavra)
list.sort(palavrab)
if palavra == palavrab:
    print("Temos um anagrama")
else:
    print("Nao temos um anagrama")