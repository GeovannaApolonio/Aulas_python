ano = int(input("Digite um ano e descubra se ele é bissexto: "))
if ano/4 % 1:
    print(f"{ano} não é um ano bissexto.")
else:
    print(f"{ano} é um ano bissexto.")