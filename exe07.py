nome = input("Digite seu nome: ")
trab = float(input("Digite sua nota do trabalho: "))
teste = float(input("Digite sua nota do teste: "))
prova = float(input("Digite sua nota da prova: "))

media = (float(trab) * 4 + float(teste) * 3 + float(prova) * 5) / 12

print("-"*50)

print("Aluno:", nome)
print("Média:", media)
