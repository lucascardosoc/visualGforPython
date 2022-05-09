precoFabrica = float(input("Qual o preco de fábrica desse veículo? "))
percentualLucro = float(input("Qual o percentual de lucro do distribuidor? "))
percentualImpostos = float(input("Qual o percentual de impostos? "))

lucroDistribuidor = precoFabrica * (percentualLucro / 100)
valorImpostos = precoFabrica * (percentualImpostos / 100)
precoFinal = precoFabrica + lucroDistribuidor + valorImpostos

print("O preco final do veículo é R$ %.2f" %(precoFinal))
