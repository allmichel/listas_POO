data_de_nascimento = input('Digite sua data de nascimento (ex:dd/mm/aa): ')
data_de_nascimento = data_de_nascimento.split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
meses_numero = ['01','02','03','04','05','06','07','08','09','10','11','12']
if data_de_nascimento[1] == meses_numero[0]:
    data_de_nascimento[1] = meses[0]
elif data_de_nascimento[1] == meses_numero[1]:
    data_de_nascimento[1] = meses[1]
elif data_de_nascimento[1] == meses_numero[2]:
    data_de_nascimento[1] = meses[2]
elif data_de_nascimento[1] == meses_numero[3]:
    data_de_nascimento[1] = meses[3]
elif data_de_nascimento[1] == meses_numero[4]:
    data_de_nascimento[1] = meses[4]
elif data_de_nascimento[1] == meses_numero[5]:
    data_de_nascimento[1] = meses[5]
elif data_de_nascimento[1] == meses_numero[6]:
    data_de_nascimento[1] = meses[6]
elif data_de_nascimento[1] == meses_numero[7]:
    data_de_nascimento[1] = meses[7]
elif data_de_nascimento[1] == meses_numero[8]:
    data_de_nascimento[1] = meses[8]
elif data_de_nascimento[1] == meses_numero[9]:
    data_de_nascimento[1] = meses[9]
elif data_de_nascimento[1] == meses_numero[10]:
    data_de_nascimento[1] = meses[10]
elif data_de_nascimento[1] == meses_numero[11]:
    data_de_nascimento[1] = meses[11]
print(data_de_nascimento[0], 'de', data_de_nascimento[1], 'de', data_de_nascimento[2])