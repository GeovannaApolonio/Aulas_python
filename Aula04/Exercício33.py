# Criar uma lista vazia#
num = []
n = str(input("Digite três números separados por espaço: "))

for i in n.split():
    num.append(int(i))
    
print(f"O maior número que você digitou foi {max(num)}  e o menor foi {min(num)}")