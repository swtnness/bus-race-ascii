import os
import time
import random

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def dibujar_buses(centro, bello, pista=70):
    bus_centro = [
        "  ________________",
        " |_|_|_|_|_|_|_|_|___",
        " | CENTRO MEDELLIN   |)",
        " |________________   |)",
        "    O            O"
    ]

    bus_bello = [
         " ________________",
        " |_|_|_|_|_|_|_|_|___",
        " | Bello             |)",
        " |________________   |)",
        "    O            O"
    ]

    
    meta_line = "|" + " " * (pista - 2) + "|"
    marco = "-" * pista

    salida = [marco, meta_line]
    

    for linea in bus_centro:
        salida.append(" " * centro + linea)

    salida.append("")  

    
    for linea in bus_bello:
        salida.append(" " * bello + linea)

    salida.append(meta_line)
    salida.append(marco)

    return "\n".join(salida)

def main():
    centro = 0
    bello = 0

    pista = 70
    meta = 50   
    delay = 0.07

    print("CARRERA DE BUSES")
    print("BUS CENTRO MEDELLIN vs BUS BELLO")
    time.sleep(2)

    while centro < meta and bello < meta:
        limpiar()

    
        quien = random.randint(1, 2)

        if quien == 1:
            centro += 1
        else:
            bello += 1

        
        centro = min(centro, pista - 25)
        bello = min(bello, pista - 25)

        print(dibujar_buses(centro, bello, pista))
        time.sleep(delay)

    limpiar()

    print(dibujar_buses(centro, bello, pista))
    if centro >= meta:
        print("\nGANO EL BUS CENTRO MEDELLIN 🏁 (milagro, sin trancon)")
    else:
        print("\nGANO EL BUS BELLO 🏁")

if __name__ == "__main__":
    main()