# Autor: Ailton Lima de Andrade.

# Leitura e declaração das variáveis:
# "numero", que representa um número positivo digitado pelo usuário.
numero = int(input("Digite um número positivo: "))

# Verificar se a variável "numero" é um número par ou ímpar.
if(numero %2 == 0):
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")
