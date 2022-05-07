vendaTotal = float(input("Qual o valor total vendido? "))

comissao = vendaTotal * (3/100)
receber = 1800 + comissao

print("O total a receber desse vendedor com a comissão é R$", receber)