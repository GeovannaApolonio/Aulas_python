print("Respostas apenas em F e M.")
letra = str(input("Digite qual o seu sexo: ")).upper

while letra not in "FM":
    print("Valor inválido, digite novamente!")
    break
print("Valor correto, obrigado!")