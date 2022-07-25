from ast import Pass


menu = """ Bienvenido al conversor de monedas. Elija una opcion para comenzar
1- Pesos Uruguayos a Dolares
2- Dolares a Pesos Uruguayos
3- Pesos Argentinos a Dolares Blue
4- Dolares Blue a Pesos Argentinos
Elija el numero de su opcion: """

opcion = input(menu)
if opcion == "1":
    pesos = input("Cantidad de pesos Uruguayos a convertir: ")
    pesos = float(pesos)
    valor_dolar = 42.09
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2) 
    dolar = str(dolar)
    print("$" + dolar + " " "dolares")

elif opcion == "2":
    dolar = input("Cantidad de dolares a convertir a pesos: ")
    dolar = float(dolar)
    valor_peso = 0.024
    pesos = dolar / valor_peso
    pesos = round(pesos, 4)
    pesos = str(pesos)
    print("$" + pesos + " " "pesos")
elif opcion == "3":
    pesos = input("Cantidad de pesos a convertir a dolares blue: ")
    pesos = float(pesos)
    valor_dolar = 339
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2) 
    print("$" + str(dolar) + " " "dolares")
elif opcion == "4" :
    dolar = input("Cantidad de dolares blue a convertir a pesos: ")
    dolar = float(dolar)
    valor_peso = 0.0029
    pesos = dolar / valor_peso
    pesos = round(pesos, 4)
    print("$" + str(pesos) + " " + "pesos")

else :
    opcion = input("Por favor, elija una opcion correcta: ")

