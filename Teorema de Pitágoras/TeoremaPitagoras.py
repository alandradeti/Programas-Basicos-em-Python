# Importando biblioteca Math
import math

# Leitura e declaração das variáveis:
# "a", que representa o valor de y;
# "b", que representa o valor de x.
y = float(input("Digite o valor da distância de Y: "))
x = float(input("Digite o valor da distância de X: "))

# Calculo e declaração da variável "resultado", que representa o resultado do teorema de Pitágoras.
resultado = math.sqrt((math.pow(y,2) + math.pow(x,2)))

# Imprimindo a variável "resultado".
print("O resultado é: ", resultado)
