r = 'S'

while r == 'S':
    num = int(input("Informe a tabuada: "))
    for i in range(1,11):
        print(num, 'x', i, '=', num*i)

    r = str(input("Deseja continuar? [S/N]"))

if r == 'N':
    print("Fim...")


# num = int(input("Display multiplicação


