import os

# Especificar el directorio a listar
directorio_dev = "C:\\Users"

# Obtener una lista de todos los elementos en el directorio especificado
contenido_dev = os.listdir(directorio_dev)

# Filtrar y listar solo los directorios
directorios_dev = [nombre for nombre in contenido_dev if os.path.isdir(os.path.join(directorio_dev))]

# Imprimir los directorios
for directorio in directorios_dev:
    print(directorio)
print (contenido_dev)

