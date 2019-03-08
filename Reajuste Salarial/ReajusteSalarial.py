# Leitura e declaração das variáveis:
# "salario", que representa o salário;
# "reajustePercentual", que representa o reajuste percentual.
salario = float(input("Digite o valor do sálario: "))
reajustePercentual = float(input("Digite o valor do reajuste: "))

#Calculo e declaração da variável "salarioFinal", que representa o salário final
salarioFinal = ((salario * reajustePercentual)/100 + salario)

#Imprimir a váriavel "salarioFinal"
print("O sálario final é: R$", salarioFinal)
