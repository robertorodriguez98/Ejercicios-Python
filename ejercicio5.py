from crypt import crypt

f = open ("/home/roberto/shadow.txt")
lineas = f.readlines()
f.close
lista = []
for linea in lineas:
    lista.append(linea.split(":"))

encontrado = False
nombre = input("Nombre: ")
for usuario in lista:
    if nombre == usuario[0]:
        encontrado = True
        contraReal = usuario[1]
        sal=usuario[1][:30]

        contra = input("dime la contraseña: ")
        if crypt(contra,sal) == contraReal:
            print("correcto")
        else:
            print("incorrecto")

if not encontrado:
    print("el usuario no existe")