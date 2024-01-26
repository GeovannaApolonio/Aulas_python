anoA = int(input("Insira o ano atual: "))
anoN = int(input("Insira seu ano de nascimento: "))
idade = anoA - anoN
if idade == 18:
    print("Está na hora exata de você se alistar. Acesse o site https://alistamento.eb.mil.br/alistamento") 
elif idade < 18: 
    anoF = 18 - idade
    print(f"Faltam {anoF} anos para você se alistar.")
else:
    anoD = idade - 18
    if anoD == 1:
        print(f"Já passou o tempo do seu alistamento {anoD} ano, regularize sua situação acesse o site https://alistamento.eb.mil.br/alistamento")
    else:
        print(f"Já passou o tempo do seu alistamento {anoD} anos, regularize sua situação acesse o site https://alistamento.eb.mil.br/alistamento")

