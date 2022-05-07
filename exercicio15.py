candidatoA = float(input("Quantos votos o candidato A recebeu? "))
candidatoB = float(input("Quantos votos o candidato B recebeu? "))
candidatoC = float(input("Quantos votos o candidato C recebeu? "))
votosBrancos = float(input("Qual foi a quantidade de votos em branco? "))
votosNulos = float(input("Qual foi a quantidade de votos nulos? "))

totalEleitores = candidatoA + candidatoB + candidatoC + votosBrancos + votosNulos

porcentagemA = (candidatoA / totalEleitores) * 100
porcentagemB = (candidatoB / totalEleitores) * 100
porcentagemC = (candidatoC / totalEleitores) * 100
porcentagemBrancos = (votosBrancos / totalEleitores) * 100
porcentagemNulos = (votosNulos / totalEleitores) * 100

print("O percentual de votos para o candidato A foi de %.2f" %(porcentagemA),"%")
print("O percentual de votos para o candidato B foi de %.2f" %(porcentagemB),"%")
print("O percentual de votos para o candidato C foi de %.2f" %(porcentagemC),"%")
print("O percentual de votos em branco foi de %.2f" %(porcentagemBrancos),"%")
print("O percentual de votos nulos foi de %.2f" %(porcentagemNulos),"%")

