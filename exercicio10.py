diasTrabalhados = int(input("Quantos dias trabalhados você tem? "))

valorLiquido = 70 * diasTrabalhados * (8/100)
valorReceber = 70 * diasTrabalhados - valorLiquido

print("O valor líquido a receber é de R$", valorReceber)