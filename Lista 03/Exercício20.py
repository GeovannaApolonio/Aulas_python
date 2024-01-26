import random


print("Sorteador de ordem de apresentação de trabalho.")
nome1 = str(input("Digite o nome do aluno: "))
nome2 = str(input("Digite o nome do aluno: "))
nome3 = str(input("Digite o nome do aluno: "))
nome4 = str(input("Digite o nome do aluno: "))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f"A ordem de apresentação é: {lista}")
