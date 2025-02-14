cantidad = int(input("ingrese la cantidad de dinero que quiere convertir: "))
origen = input("Elig¡je la moneda de origen: ")
destino = input("Elije la moneda de destino: ")

if origen == "Euro" and destino == "Dolar": resuldado = (cantidad* 1.05)
elif origen == "Dolar" and destino == "Euro": resuldado = (cantidad * 0.96)
elif origen == "MXN" and destino == "Euro": resuldado = (cantidad * 0.04)
elif origen == "Euro" and destino == "MXN": resuldado = (cantidad * 21.42)
elif origen == "Dolar" and destino == "MXN": resuldado = (cantidad * 20.49)
elif origen == "MXN" and destino == "Dolar": resuldado = (cantidad * 0.05)

print(f"La moneda", origen, "sera pasada a", destino, "y valdra:", resuldado)
