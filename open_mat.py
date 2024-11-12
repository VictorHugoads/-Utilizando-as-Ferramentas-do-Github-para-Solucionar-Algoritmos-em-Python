# Solicita ao usuário dois números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Solicita ao usuário a operação matemática que deseja realizar
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Realiza a operação escolhida e imprime o resultado
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)