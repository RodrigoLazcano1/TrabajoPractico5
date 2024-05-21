import time

def contador_simple(segundos):
    for i in range(segundos):
        print(i+1)
        time.sleep(1)

contador_simple(2)  # Contador de 2 segundos
