print("Obrigado pela preferência! \nCalcule o valor final do aluguel.")

numD = int(input("Quantos dias você ficou com o veículo? "))
numKM = float(input("Quantos Km você rodou com o veículo? "))

numVD = int(numD * 60)
numVK = float(numKM * 0.15)
Vtotal = float(numVD + numVK)

print(f"O valor total a ser pago é {Vtotal}. \nQual será a forma de pagamento: \n[1] Débito \n[2] Crédito \n[3] PIX \n[4] Dinheiro")