import random
import time

def simulacion_continua():
    capacidad = 10
    ocupado = 0
    libre = capacidad
    
    print("Simulacion simple")
    print("-" * 30)
    
    for i in range(10):
        print(f"\nNumero {i+1}:")
        
        # Salen 
        salidas = random.randint(0, min(3, ocupado))
        ocupado -= salidas
        libre += salidas
        
        # Entran 
        entradas = random.randint(0, min(3, libre))
        ocupado += entradas
        libre -= entradas
        
        # Mostrar estado
        print(f"  Salidas: {salidas}, Entradas: {entradas}")
        print(f"  Ocupado: {ocupado}, Libre: {libre}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    simulacion_basica()