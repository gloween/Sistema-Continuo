import random
import time

print("Inicia sistema")

while True:
    try:
        if random.random() < 0.5:
            print("ocupado")
            if random.random() < 0.1: 
                print("SOBRECARGA")
                print("Sistema detenido por sobrecarga")
                break
        else:
            print("libre")
        
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        print("\nFin")
        break