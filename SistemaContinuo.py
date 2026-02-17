import random #importa la biblioteca random para generar numeros aleatorios
import time # importa la biblioteca time para usar la funcion sleep

print("Inicia sistema")

while True: # Mantiene el sistema en ejecucion hasta que una sobrecarga occurra
    try:
        if random.random() < 0.5: #una probabilidad que el sistema imprima ocupado en vez de libre
            print("ocupado")
            if random.random() < 0.1: # una pequena probabilidad de que el sistema se sobrecargue
                print("SOBRECARGA")
                print("Sistema detenido por sobrecarga")
                break # Detiene el sistema si ocurre una sobrecarga
        else:
            print("libre")
        
        time.sleep(0.5) # Pausa de medio segundo para que no se imprima demasiado rapido
        
    except KeyboardInterrupt: # Permite al usuario detener el sistema manualmente con Ctrl+C
        print("\nFin")
        break