# Allan Michel - ADS ;)
#===================================================================================
# 5. Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês, sem usar a fórmula de juros compostos

# a. O usuário deve informar quanto será investido por mês e qual será a taxa de juros mensal

# b. O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês considerando os juros compostos),
#     e perguntar ao usuáriose ele deseja que seja calculado o ano seguinte, sucessivamente

# c. Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma taxa de juros de 1% ao mês, o programa forneceria
#     a seguinte saída: Saldo do investimento após 1 ano: R$ 1268.25 Deseja processar mais um ano? (S/N)
#===================================================================================

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
investimento = float(input("Depósito mensal:"))
mês = 1
saldo = depósito
for mês in range(12+1):
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo-depósito))