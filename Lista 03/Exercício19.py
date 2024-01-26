import random
print("Sorteador de nomes")
nome1 = input("Digite o nome do aluno: ")
nome2 = input("Digite o nome do aluno: ")
nome3 = input("Digite o nome do aluno: ")
nome4 = input("Digite o nome do aluno: ")
nomes = [nome1, nome2, nome3, nome4]
Sort = random.choice(nomes)
print("O aluno sorteado é: {}".format(random.choice(nomes)))
