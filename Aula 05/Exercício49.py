num = int(input("Digite um número inteiro para calcular sua tabuada: "))
value = -1
for i in range(0,11):
    value += 1
    print(f"{num} X {value} = {num * value} ✔") 