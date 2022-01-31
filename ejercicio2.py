articulos=[]


cantidad = int(input("dime cuantos elementos hay: "))
for elemento in range(0,cantidad):
    minilista = []
    articulo = input("Dime el articulo: ")
    precio = int(input("Dime el precio: "))
    minilista.append(articulo)
    minilista.append(precio)
    articulos.append(minilista)

print(articulos)

sum = 0
for elemento in articulos:
    sum += elemento[1]
print("el precio medio de los articulos es: ",sum/len(articulos))
for elemento in articulos:
    if elemento[1] >= 100:
        print("El elemento %s vale más de 100€"%elemento[0])

pedir_art = input("introduzca el nombre de un articulo: ")
art_en_lista = False
for elemento in articulos:
    if elemento[0] == pedir_art:
        print("el precio de %s es de %d €"%(elemento[0],elemento[1]))
        art_en_lista = True

if not art_en_lista:
    print("ERROR")