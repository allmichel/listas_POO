# Allan Michel - ADS ;)
#===================================================================================
#8. Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e
#imprima a data com o mês escrito por extenso.
#Exemplo:
#● Data = 20/02/1995
#Resultado gerado pelo programa:
#● 20 de fevereiro de 1995
#===================================================================================
data_de_nascimento = input('Digite sua data de nascimento (ex:dd/mm/aa): ')
data_de_nascimento = data_de_nascimento.split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
if data_de_nascimento[1] == '01':
    data_de_nascimento[1] = meses[0]
elif data_de_nascimento[1] == '02':
    data_de_nascimento[1] = meses[1]
elif data_de_nascimento[1] == '03':
    data_de_nascimento[1] = meses[2]
elif data_de_nascimento[1] == '04':
    data_de_nascimento[1] = meses[3]
elif data_de_nascimento[1] == '05':
    data_de_nascimento[1] = meses[4]
elif data_de_nascimento[1] == '06':
    data_de_nascimento[1] = meses[5]
elif data_de_nascimento[1] == '07':
    data_de_nascimento[1] = meses[6]
elif data_de_nascimento[1] == '08':
    data_de_nascimento[1] = meses[7]
elif data_de_nascimento[1] == '09':
    data_de_nascimento[1] = meses[8]
elif data_de_nascimento[1] == '10':
    data_de_nascimento[1] = meses[9]
elif data_de_nascimento[1] == '11':
    data_de_nascimento[1] = meses[10]
elif data_de_nascimento[1] == '12':
    data_de_nascimento[1] = meses[11]
print(data_de_nascimento[0], 'de', data_de_nascimento[1], 'de', data_de_nascimento[2])
