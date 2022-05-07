anoNascimento = int(input("Qual o ano de nascimento dessa pessoa? "))
anoAtual = int(input("Qual o ano atual? "))

idade = anoAtual - anoNascimento
idadeFutura = 2032 - anoNascimento

print("Essa pessoa tem", idade, "anos atualmente")
print("Essa pessoa terá", idadeFutura, "anos em 2032")