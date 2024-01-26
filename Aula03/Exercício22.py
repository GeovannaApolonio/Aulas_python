import string


nome = str(input('Digite o seu nome completo: '))
tamanho = nome.split()
nome_maiúscula = nome.upper()
nome_minúsculo = nome.lower()
nomeSE = nome.replace(" ", "")

print(f"Nome com letras maiusculas: {nome_maiúscula}")
print(f"Nome com letras minusculas: {nome_minúsculo}")
print(f"O seu nome tem ao todo {len(nomeSE)} letras")
print(f'O seu primeiro nome tem {len(tamanho[0])} letras')