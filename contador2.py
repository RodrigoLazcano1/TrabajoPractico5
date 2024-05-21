import time

def contador_simple(segundos):
    for i in range(segundos):
        print(i+1)
        time.sleep(1)

contador_simple(5)  # Contador de 5 segundos
