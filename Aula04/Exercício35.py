print("Verifique se é possível formar um triângulo.")
a = float(input("Insira o valor do primeiro lado do triângulo: "))
b = float(input("Insira o valor do segundo lado do triângulo: "))
c = float(input("Insira o valor do terceiro lado do triângulo: "))

if (a> b + c) or (b> a + c) or (c> b + a):
    print("Com esses valores é possível formar um triângulo.")
else:
    print("Com esses valores é possível não formar um triângulo.")