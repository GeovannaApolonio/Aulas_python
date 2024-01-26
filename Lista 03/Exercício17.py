print("Calcule a hipotenusa do triângulo retângulo.")
compCO = int(input("Qual o comprimento do cateto oposto? "))
compCA = int(input("Qual o comprimento do cateto adjascente? "))
hip = int(compCO**2 + compCA**2)  ** (1/2)
print(f"A hipotenusa desse triângulo é {hip}")

# Usando biblioteca math#
import math
print("Calcule a hipotenusa do triângulo retângulo.")
compCO1 = int(input("Qual o comprimento do cateto oposto? "))
compCA2 = int(input("Qual o comprimento do cateto adjascente? "))
hip = math.hypot(compCO1, compCA2)
print(f"A hipotenusa desse triângulo é {hip}")