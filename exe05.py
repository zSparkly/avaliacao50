n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))

operação = input("Digite a operação a realizar (+,-,* ou /):")

if operação == "+":
    resultado = n1 + n2
elif operação == "-":
    resultado = n1 - n2
elif operação == "*":
    resultado = n1 * n2
elif operação == "/":
    resultado = n1 / n2
else:
    print("Operação inválida!")
    resultado = 0

print("Resultado: ", resultado)
