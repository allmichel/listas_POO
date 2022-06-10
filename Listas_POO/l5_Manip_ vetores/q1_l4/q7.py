nome = input('Digite o seu nome: ')
nome = nome.upper()
nome = list(nome)
for i in range(0, len(nome)+1):
    print(nome[:i])