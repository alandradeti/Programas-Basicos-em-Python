# Importando biblioteca Math
import math

# Leitura e declaração das variáveis:
# "y", que representa o valor da distância X;
# "x", que representa o valor da distância Y.
y = float(input("Digite o valor da distância de Y: "))
x = float(input("Digite o valor da distância de X: "))

# Cálculo da hipotenusa.
hipotenusa = math.sqrt(math.pow(y,2) + math.pow(x,2))

# Cálculo do seno.
seno = (y/hip)

# Cálculo do arco-seno.
arcoSeno = math.asin(seno)

# Conversão para graus.
grausArcoSeno = math.degrees(arcoSeno)

# Arredondamento pela função Round.
arcoSenoArredondado = round(grausArcoSeno)
hipotenusaArredondada = round(hip)

# Imprimindo as variáveis "hipotenusa", "hipotenusaArredondada", "arcoSeno", "grausArcoSeno", "arcoSenoArredondado"
print("A distância R é: ", hipotenusa,
      "\nA distância R arredondada: ", hipotenusaArredondada ,
      "\nO Ângulo Alfa em radiano é: ", arcoSeno ,
      "\nO ângulo Alfa em graus é: ", grausArcoSeno ,"º",      
      "\nO ângulo Alfa arredondado em graus é: ", arcoSenoArredondado ,"º")

