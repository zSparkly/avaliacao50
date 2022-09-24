op = int(input('1. Celsius para Farenheit: \n' +
                       '2. Farenheit para Celsius: '))

if op == 1:
    C = float(input("Graus Celsius: "))
    F = (C * 9 / 5) + 32

    print(F,"F")

elif op == 2:
    F = float(input("Graus Farenheit: "))
    C = (F - 32) * 5 / 9
    print(C,"C")
else:
    print("Opção inválida")



