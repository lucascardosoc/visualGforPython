# MILIONÁRIO

salario = float(input("Informe o valor do salário: "))
despesas = float(input("Informe o valor de suas despesas mensais: "))

sobra = (salario - despesas) * 12
milionario = (1000000 / sobra)

print("Será necessário", milionario, "anos para se tornar milionário")