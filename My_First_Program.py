numero1 = input("Presione 1 para dolares a pesos o presione 2 para pesos a dolares ")
numero2 = str(1)
numero3 = str(2)
if numero1 == numero3 : 
    pesos = input("Cantidad de pesos Uruguayos a convertir: ")
    pesos = float(pesos)
    valor_dolar = 42.09
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2) 
    dolar = str(dolar)
    print("$" + dolar + "dolares")

else: 
    dolarA = input("Cantidad de dolares a convertir a pesos: ")
    dolarA = float(dolarA)
    valor_peso = 0.024
    pesosA = dolarA / valor_peso
    pesosA = round(pesosA, 4)
    pesosA = str(pesosA)
    print("$" + pesosA + "pesos")
