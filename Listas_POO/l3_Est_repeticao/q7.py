# Allan Michel - ADS ;)
#===================================================================================
#7. Um número inteiro pode ser igual ao produto de 3 números inteiros consecutivos,
#como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um número n
#do teclado, verifique se n tem essa propriedade. 

#===================================================================================
n = int(input("dgt o número: "))

i = 1
while i * (i+1) * (i+2) < n:
    i += 1
if i * (i+1) * (i+2) == n:
    print("{} é o produto de {} * {} * {}".format(n, i , i+1 , i+2))
else:
    print("{} não tem esta propriedade!".format(n))