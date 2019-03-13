# Importanto biblioteca Math
import math

# Leitura e declaração das variáveis:
# "peso", que representa o peso;
# "altura", que representa a altura;
peso = int(input("Digite o valor do peso: "))
altura = float(input("Digite o valor da altura: "))

# Cálculo e declaração da variável "imc", que representa o IMC.
imc = (peso/math.pow(altura,2))

# Imprimindo a variável "imc".
print("O valor do IMC é: ", imc)

    
