
import datetime
import psutil
import shutil

def imprimir_hora_sistema():
    ahora = datetime.datetime.now()
    print("Hora del sistema:", ahora.strftime("%Y-%m-%d %H:%M:%S"))

def imprimir_estado_memoria_ram():
    memoria = psutil.virtual_memory()
    print("Estado de la memoria RAM:")
    print(f"  Total: {memoria.total / (1024 ** 3):.2f} GB")
    print(f"  Disponible: {memoria.available / (1024 ** 3):.2f} GB")
    print(f"  Usada: {memoria.used / (1024 ** 3):.2f} GB")
    print(f"  Porcentaje usado: {memoria.percent}%")

def imprimir_almacenamiento_disponible():
    total, usado, libre = shutil.disk_usage("/")
    print("Almacenamiento en la partición montada en '/':")
    print(f"  Total: {total / (1024 ** 3):.2f} GB")
    print(f"  Usado: {usado / (1024 ** 3):.2f} GB")
    print(f"  Disponible: {libre / (1024 ** 3):.2f} GB")

def main():
    imprimir_hora_sistema()
    imprimir_estado_memoria_ram()
    imprimir_almacenamiento_disponible()

if __name__ == "__main__":
    main()
