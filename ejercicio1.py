articulos = []
precios = []

cantidad = int(input("dime cuantos elementos hay: "))
for elemento in range(0,cantidad):
    articulo = input("Dime el articulo: ")
    precio = int(input("Dime el precio: "))
    articulos.append(articulo)
    precios.append(precio)


print("el precio medio de los articulos es: ",sum(precios)/len(precios))
for posicion in range(0,len(precios)):
    if precios[posicion] >= 100:
        print("El elemento %s vale más de 100€"%articulos[posicion])

pedir_art = input("introduzca el nombre de un articulo: ")
if pedir_art in articulos:
    for posicion in range(0,len(articulos)):
        if articulos[posicion] == pedir_art:
            print("el precio de %s es de %d €"%(pedir_art,precios[posicion]))
else:
    print("ERROR")