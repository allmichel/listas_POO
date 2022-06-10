frase = input('Digite uma frase: ')
frase = frase.split()
x = input('Qual palavra deseja substituir: ')
y = input('Por qual palavra: ')
for (index, value) in enumerate(frase):
    if value == x:
        frase[index] = y
        frase = ' '.join(frase)
        print(frase)