from crypt import crypt

f = open ("/home/roberto/shadow.txt")
lineas = f.readlines()
f.close

lista = []
for linea in lineas:
    lista.append(linea.split(":"))

f = open ("/home/roberto/contrasenas.txt")
contras = f.read().splitlines()
f.close

contrabuena = "no en el archivo"
print(contras)
encontrado = False
nombre = input("Nombre: ")
for usuario in lista:
    if nombre == usuario[0]:
        encontrado = True
        contraReal = usuario[1]
        sal=usuario[1][:30]
        for contra in contras:
            if crypt(contra,sal) == contraReal:
                print("correcto")
                contrabuena = contra

print(contrabuena)
if not encontrado:
    print("el usuario no existe")

