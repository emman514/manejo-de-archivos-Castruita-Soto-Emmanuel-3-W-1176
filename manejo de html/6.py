# Imprimir un espacio en blanco
print(" ")
# Imprimir my nombre
print("Castruita Soto Emmanuel - 3W -1176")
# Imprimir un espacio en blanco
print(" ")
# Abrir el archivo en para poder modificar su contenido por w
Act6 = open("Act6.txt", "w")
#ingresa la palabra que quieras agregar al archivo
palabra=input("ingresa la palabra a agregar:")
Act6.write(palabra)
# Cerrar el archivo
Act6.close()
# Abrir el archivo para mostrar el nuevo contenido
Funcion = open("Act6.txt", "r")
print(Funcion.read())
# Cerrar el archivo después de leer
Funcion.close()
