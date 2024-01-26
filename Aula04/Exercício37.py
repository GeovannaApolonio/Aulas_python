#Primeira maneira#
numA = int(input("Digite um número inteiro: "))
cab = print("Escolha em qual você deseja transformar: \n[1] Binário \n[2] Octal \n[3] Hexadecimal")
esc = int(input("Sua escolha: "))
if esc == 1:
    transB = format(numA, "b") 
    print(f"O número {numA} em número binário é {transB}")
if esc == 2:
    transfO = format(numA, "o") 
    print(f"O número {numA} em número Octal é {transfO}")
if esc == 3:
    transH = format(numA, "X")
    print(f"O número {numA} em número binário é {transH}")
    
#segunda maneira#
numA = int(input("Digite um número inteiro: "))
cab = print("Escolha em qual você deseja transformar: \n[1] Binário \n[2] Octal \n[3] Hexadecimal")
esc = int(input("Sua escolha: "))
if esc == 1:
    transB = bin(numA)
    print(f"O número {numA} em número binário é {transB}")
if esc == 2:
    transfO = oct(numA)
    print(f"O número {numA} em número Octal é {transfO}")
if esc == 3:
    transH = hex(numA)
    print(f"O número {numA} em número binário é {transH}")
    
