# Allan Michel - ADS ;)
#===================================================================================
#5. Um anagrama é uma palavra que é feita a partir da transposição das letras de outra
#palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva
#um programa que decida se uma string é um anagrama de outra string, ignorando os
#espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo
#caracteres iguais, ou seja, “a” = “A”.
#===================================================================================
palavra = input("Palavra 1: ")
palavrab = input("Palavra 2: ")

if sorted(palavra.strip().lower()) == sorted(palavrab.strip().lower()):
    print('As palavras são anagramas')
else:
    print('As palavras não são anagramas')