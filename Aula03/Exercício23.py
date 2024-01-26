# primeira forma#
numA = str(int(input("Digite um número inteiro: ")))
nomeSE = numA.replace("", " ")
print(f"{nomeSE}")


#Segunda forma#
numA = str(input("Digite um número inteiro: "))
for i in numA:
    print(i)