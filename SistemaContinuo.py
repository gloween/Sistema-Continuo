import random
import time

libre = 10
ocupado = 0

print("Estado del sistema:")
print("-" * 20)

while True:
    try:
        if random.choice([True, False]):  
            cambio = random.randint(-1, 1)
            nuevo_ocupado = ocupado + cambio
            if 0 <= nuevo_ocupado <= 10:
                ocupado = nuevo_ocupado
                if ocupado > 0:
                    print("ocupado")
                else:
                    print("libre")
        else:  
            cambio = random.randint(-1, 1)
            nuevo_libre = libre + cambio
            if 0 <= nuevo_libre <= 10:
                libre = nuevo_libre
                if libre < 10:
                    print("ocupado")
                else:
                    print("libre")
        
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        print("\nFin")
        break