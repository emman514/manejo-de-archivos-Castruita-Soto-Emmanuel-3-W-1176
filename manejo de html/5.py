# Imprimir un espacio en blanco
print(" ")
# Imprimir my nombre
print("Castruita Soto Emmanuel - 3W -1176")
# Imprimir un espacio en blanco
print(" ")
# Abrir el archivo en modo anexar
Act5 = open("Actividad 5.txt", "a")
#ingresa la palabra que quieras ingresar al archivo
texto=input("ingresa lo que quieras  agregar:")
# Escribir en el archivo
Act5.write(texto)
# Cerrar el archivo
Act5.close()
# Abrir el archivo en modo lectura para mostrar el contenido actualizado
Funcion = open("Actividad 5.txt", "r")
print(Funcion.read())
# Cerrar el archivo después de leer
Funcion.close() 