print("Calcule o valor da passagem:")


dist = int(input("Qual a distância da cidade de origem à cidade destino em KM? "))
if dist <= 200:
    val = (dist * 0.50)
    print(f"O valor da passagem será R${val}.")
else:
    val = (dist * 0.45)
    print(f"O valor da passagem será R${val}.")
    