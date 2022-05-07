# PRESTACÃO

boleto = float(input("Informe o valor do boleto: "))
percentualJuros = float(input("Informe o juros em percentual: "))
diasAtraso = float(input("Informe os dias em atraso: "))

novoValor = boleto + (boleto * (percentualJuros/100)) * diasAtraso

print("O novo valor a ser pago é: ", novoValor)