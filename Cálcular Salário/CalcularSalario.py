# Leitura e declaração das variáveis:
# "horasTrabalhadas", que representa as horas trabalhadas;
# "valorHoras", que representa o valor das horas trabalhadas;
# "percentualDesconto", que representa o percentual de desconto.
horasTrabalhadas = int(input("Digite as horas trabalhadas no mês: "))
valorHoras = float(input("Digite o valor da hora trabalhada: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))

# Calculo e declaração da variável "salarioBruto", que representa o salário bruto.
salarioBruto = horasTrabalhadas*valorHoras

# Calculo e declaração da variável "totalDesconto", que representa o total de desconto.
totalDesconto = (percentualDesconto/100)*salarioBruto

# Calculo e declaração da variável "salarioLiquido", que representa o salário líquido.
salarioLiquido = salarioBruto-totalDesconto

# Imprimir as váriaveis "horasTrabalhadas", "salarioBruto", "totalDesconto" e "salarioLiquido"
print("Horas trabalhadas:",horasTrabalhadas,
      "\nSalário bruto:",salarioBruto,
      "\nTotal de desconto",totalDesconto,
      "\nSalário líquido",salarioLiquido)
