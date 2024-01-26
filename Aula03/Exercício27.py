import string

nome = str(input("Nome completo: "))
nomeSE = nome.strip()
print(f"{nomeSE}")
print(f"O seu primeiro nome é {nomeSE} e o último nome é {(nomeSE) - 1}")


