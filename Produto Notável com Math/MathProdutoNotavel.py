# Importando biblioteca Math
import math

# Leitura e declaração das variáveis:
# "a", que representa o valor de A;
# "b", que representa o valor de B.
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Cálculo e declaração da variável "valorFinal", que representa o valor final.
valorFinal = (math.pow(a,2) + 2*(a*b) + math.pow(b,2))

# Imprimir as variáveis "a" e "b" e  "valorFinal".
print("O valor de (a+b)²: ", valorFinal)
