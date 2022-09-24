nome = input("Nome do aluno: ")
Nota1 = float(input("Primeira nota: "))
Nota2 = float(input("Segunda nota: "))
Nota3 = float(input("Terceira nota: "))

media = (Nota1 + Nota2 + Nota3) / 3

print("===================")
print(nome)
print('Media: ', media)

if media >= 7.0:
    print("Aprovado!!")
else:
    print("Reprovado!!")