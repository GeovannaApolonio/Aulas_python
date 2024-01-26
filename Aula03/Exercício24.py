Cityname = input("Digite o nome de uma cidade: ")

if any(x in Cityname for x in["João","Lucas","Mateus","Santos","Santo","São"]):
    print(f"{Cityname} é uma cidade brasileira que tem um nome religioso.")
else: 
    print(f"{Cityname} é uma cidade brasileira que não tem um nome religioso")