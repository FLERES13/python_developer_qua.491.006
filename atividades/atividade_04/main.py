import os
import time
import datetime



while True:
    
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Hora atual: (atual)")
    time.sleep(1)

