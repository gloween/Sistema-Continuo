import random
import time

print("Inicia sistema")

while True:
    try:
        if random.random() < 0.5:
            print("ocupado")
        else:
            print("libre")
        
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        print("\nFin")
        break