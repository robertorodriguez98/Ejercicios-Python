alumnos = []
n_alumnos = int(input("dime cuanta gente hay en la clase: "))
for n in range(0,n_alumnos):
    sublista = []
    listanotas = []
    nombre = input("Dime el nombre del %d alumno: "%(n+1))
    sublista.append(nombre)
    n_notas = int(input("dime la cantidad de notas que tiene: "))
    for i in range(0,n_notas):
        nota = float(input("dime la %d nota: "%(i+1)))
        while nota > 10 or nota < 0:
            nota = float(input("error, la nota debe estar entre 0 y 10: "))
        listanotas.append(nota)
    sublista.append(listanotas)
    alumnos.append(sublista)
print(alumnos)

texmenu = "1. Notas medias\n2. Buscar por nombre\n3. Añadir alumno\n4.Eliminar alumno\n5. Salir\n"
menu = int(input(texmenu))
while menu !=5:
    if menu == 1:
        for elemento in alumnos:
            media = sum(elemento[1])/len(elemento[1])
            print(elemento[0],media,end=" ")
            if media >= 5:
                print("APROBADO", end=" ")
            print()
    elif menu == 2:
        buscar = input("Dime la cadena a buscar: ")
        for elemento in alumnos:
            if elemento[0].startswith(buscar):
                print("el alumno %s tiene las siguientes notas:"%elemento[0],end=" ")
                for nota in elemento[1]:
                    print(nota,end=" ")
                print()
    elif menu == 3:
        sublista = []
        listanotas = []
        nombre = input("Dime el nombre del nuevo alumno: ")
        sublista.append(nombre)
        n_notas = int(input("dime la cantidad de notas que tiene: "))
        for i in range(0,n_notas):
            nota = float(input("dime la %d nota: "%(i+1)))
            listanotas.append(nota)
        sublista.append(listanotas)
        alumnos.append(sublista)
    elif menu == 4:
        buscar = input("Dime el alumno a eliminar: ")
        for i in range(0,len(alumnos)):
            if alumnos[i][0]==buscar:
                alumnos.pop(i)
    texmenu = "1. Notas medias\n2. Buscar por nombre\n3. Añadir alumno\n4.Eliminar alumno\n5. Salir\n"
    menu = int(input(texmenu))
