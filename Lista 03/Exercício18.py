import math


print("Calcule seno, cosseno e tangente de um ângulo.")
numA = float(input("Digite um ângulo qualquer: "))
rad = math.radians(numA)
numS = float(math.sin(rad))
numC = float(math.cos(rad))
numT = float(math.tan(rad))
print(f"O seno, cosseno e tangente do seu ângulo é respectivamente {numS}, {numC} e {numT}")
