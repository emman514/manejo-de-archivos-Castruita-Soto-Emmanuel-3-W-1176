# Imprimir un espacio en blanco
print(" ")
# Imprimir my nombre
print("Castruita Soto Emmanuel - 3W -1176")
# Imprimir un espacio en blanco
print(" ")
import os

# Verificar si el archivo "demofile.txt" existe
if os.path.exists("Acividad 7.txt"):
    # Si existe, eliminar el archivo
    os.remove("Actividad 7.txt")
    print("El archivo 'Actividad 7.txt' ha sido eliminado.")
else:
    # Si no existe, imprimir un mensaje
    print("El archivo 'Actividad 7.txt' no existe.")
