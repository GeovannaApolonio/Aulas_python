frase = input("Insira uma frase: ").upper()

print(f"A frase {frase} tem a letra A {frase.count('A')} vezes.")
print(f"Sendo a primeira na posição {frase.find('A')}.")
print(f"E a última na posição {frase.rfind('A')}.")