sal = float(input("Digite o salário do funcionário: "))

if sal <= 1212.00:
    desc = sal / 100 * 7.5
    salf = sal - desc
    print("Desconto do INSS:", desc)
    print("Salário líquido:", salf)

elif sal >= 1212.01 and sal <= 2427.35:
    desc = sal / 100 * 9
    salf = float(sal) - desc
    print("Desconto do INSS:", desc)
    print("Salário líquido:", salf)


elif sal >= 2427.36 and sal <= 3641.03:
    desc = sal / 100 * 12
    salf = float(sal) - desc
    print("Desconto do INSS:", desc)
    print("Salário líquido:", salf)

elif sal >= 3641.04:
    desc = sal / 100 * 14
    salf = float(sal) - desc
    print("Desconto do INSS:", desc)
    print("Salário líquido:", salf)

