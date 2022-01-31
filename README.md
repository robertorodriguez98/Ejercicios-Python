# Ejercicios-Python
Tarea 6 ejercicios python:

	-m cuando add
	-am cuando se modifican
# ENUNCIADOS 
[original](https://fp.josedomingo.org/lmgs/2020-2021/python3/tarea7.html)
1. Queremos guardar el nombre de los artículos de un almacén y sus precios. Como estructura de datos vamos a usar dos listas: artículos, donde vamos a guardar el nombre de los artículos y precios donde vamos a guardar los precios. De tal forma que el artículo en la posición n de la lista artículos tendrá el precio correspondiente a la misma posición en la lista precios. Realiza un programa que pida por teclado artículos y sus precios (el programa pedirá cuantos artículos se van a introducir), al finalizar dará la siguiente información:
	* El precio medio de los artículos.
	* El nombre de los artículos que valen más de 100 euros.
	* Nos pedirá un nombre de un artículo y si existe nos dará su precio, sino nos dará un error.

2. Repite el ejercicio 1 con la siguiente estructura de datos: vamos a usar una lista artículos donde vamos a guardar listas con dos elementos: el nombre del artículo y su precio. Ejemplo: 
	
		articulos=[["fregona",12],["cepillo",14],["recogerdor",23]]

3. Queremos hacer un programa que trabaje con las notas de los alumnos de una clase:

	* El programa pedirá cuantos alumnos tiene la clase.
	* A continuación, pedirá el nombre del alumno, y cuantas notas tiene ese alumno.
	* Se pedirán las notas del alumno introducido (cada alumno puede tener una cantidad de notas distintas). Las notas se validarán para que sea un número del 1 al 10).
	
	Piensa en el estructura de datos donde vas a guardar la información. Al finalizar el programa nos mostrará el siguiente menu:

	1. Notas medias: Nos muestra una lista de alumnos y su nota media. Si su nota media es aprobado aparecerá la palabra “APROBADO” en la línea del alumno.
	2. Buscar por nombre: Nos pide una cadena y nos muestra todos los alumnos que **comienzan por dicha cadena y la lista de sus notas.
	3. Añadir alumno: No pide el nombre de un alumno, cuántas notas tienes y pide las notas.
	4. Eliminar alumno: Nos pide un nombre y elimina el primer alumno que encuentre con ese nombre.
	5. Salir

