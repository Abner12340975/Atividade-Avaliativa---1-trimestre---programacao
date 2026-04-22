# 1. Entrada de dados: convertemos para float para aceitar números com vírgula
numero = float(input("Digite um número: "))

# 2. Estrutura de decisão
if numero > 0:
    print("O número é POSITIVO.")
elif numero < 0:
    print("O número é NEGATIVO.")
else:
    print("O número é ZERO.")