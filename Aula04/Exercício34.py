print("Calcule seu reajuste salarial")
salI = float(input("Insira o valor do sálario atual: "))
if salI > 1250.0:
    salF = salI * 1.10
    print(f"Com o reajuste seu sálario ficou no valor de R${salF:.2f}")
else: 
    salF = salI * 1.15
    print(f"Com o reajuste seu sálario ficou no valor de R${salF:.2f}")
