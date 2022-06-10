# Allan Michel - ADS ;)
#===================================================================================
#Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em
#metros elevado ao quadrado) e informe a sua classificação segundo a tabela a seguir,
#obtida na Wikipedia.
#===================================================================================
n = input("Olá :) qual seu nome? ")
massa = float(input("{},digite seu peso: ".format(n)))
altura = float(input("{},digite sua altura: ".format(n) ))
imc = massa/altura**2
print("{}, seu IMC é: {:2f}".format(n,imc))

if imc < 18.5:
	print("Abaixo do peso\n")
	print("Você está abaixo do peso ideal. Isso pode ser apenas uma característica pessoal, mas também pode ser um sinal de desnutrição ou de algum problema de saúde. Caso esteja perdendo peso sem motivo aparente, procure um médico.")

elif 18.6<imc and imc<24.9:
	print("Saudável\n")
	print("Parabéns, você está com o peso normal. Recomendamos que mantenha hábitos saudáveis em seu dia a dia. Especialistas sugerem ingerir de 4 	a 5 porções diárias de frutas, verduras e legumes, além da prática de exercícios físicos - pelo menos 150 minutos semanais.")

elif  25<imc and imc<29.9:
	print("Peso em excesso\n")
	print("Atenção! Alguns quilos a mais já são suficientes para que algumas pessoas desenvolvam doenças associadas, como diabetes e hipertensão. É importante rever seus hábitos. Procure um médico.")

elif 30<imc and imc<34.9:
	print("Obesidade Grau I\n")
	print("Sinal de alerta! O excesso de peso é fator de risco para desenvolvimento de outros problemas de saúde. A boa notícia é que uma pequena perda de peso já traz benefícios à saúde. Procure um médico para definir o tratamento mais adequado para você.")

elif 35<imc and imc>39.9:
	print("Obesidade Grau II (severa)")
	print("Sinal vermelho! Ao atingir este nível de IMC, o risco de doenças associadas está entre alto e muito alto. Busque ajuda de um profissional de saúde; não perca tempo")

else:
	print("Obesidade Grau III (mórbida)\n")
	print("Sinal vermelho! Ao atingir este nível de IMC, o risco de doenças associadas é muito alto. Busque ajuda de um profissional de saúde; não perca tempo")