print("Cauculadora de média. Insira as notas das provas:")
nota1 = float(input("Insira a nota da primeira prova "))
nota2 = float(input("Insira a nota da segunda prova "))
soma = float(nota1 + nota2)
média = float(soma/2)
if média>=7:
    print("A sua média é {}. Parabéns, você foi aprovado. :)".format(média))
else:
    print("Sua média é {}. Você ficou abaixo da média. :(".format(média))
    
    
print("Cauculadora de média. Insira as notas das provas:")
nota1 = float(input("Insira a nota da primeira prova "))
nota2 = float(input("Insira a nota da segunda prova "))
soma = float((nota1 + nota2))
média = float((soma/2))
if média>=7:
    print(f"A sua média é {média}. Parabéns, você foi aprovado. :)")
else:
    print(f"Sua média é {média}. Você ficou abaixo da média. :(")
