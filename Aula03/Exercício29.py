vel = int(input("Insira a velocidade do veículo em km: "))
difV = vel - 80
val = 7 * difV
if vel > 80:
    print(f"Você foi multado. O valor a ser pago por ultrapassar o limite de velocidade será R${val}.")
else:
    print("Você não foi multado.")