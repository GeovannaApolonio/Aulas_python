print("Simule aqui o seu emprestimo!")
valC = float(input("Qual o valor da casa pretendida? "))
sal = float(input("Insira o valor do sálario atual: "))
temp = int(input("Em quantos anos pretente pagar? "))
tempM = temp * 12
prest = valC/tempM
porcS = sal * 0.30
if prest > porcS:
    print("Seu empréstimo foi negado.")
else: 
    print("Seu empréstimo foi aprovado.")