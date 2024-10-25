# Imprimir un espacio en blanco
print(" ")
# Imprimir my nombre
print("Castruita Soto Emmanuel - 3W -1176")
# Imprimir un espacio en blanco
print(" ")
import os #se pone la vaRIANTE OS PARA ELIMINAR CARPETAS
try:
    os.rmdir("sujeto d3 pruevas con familia")# se indica que eliminar 
    print("La carpeta sujeto d3 pruevas con familia' ha sido eliminada.")# mensaje que se implimira 
except OSError:# si no existe o ya se elimino
    print("NO SE ENCONTRO CARPETA")#implimir este mensaje 
