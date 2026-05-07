import random
import time


def clasificar_peso(peso):
    if peso <= 500:
        return "lata normal"
    elif peso <= 1500:
        return "lata grande"
    return "lata gigante"


def clasificar_sodio(sodio):
    if sodio < 5:
        return "baja en sodio"
    elif sodio <= 8:
        return "sodio medio"
    return "alta en sodio"


def clasificar_exportacion(exportacion):
    return f"exportación {exportacion}"


def ejercicio2():
    exportaciones = ["nacional", "internacional"]
    latas = random.randint(1, 10)

    for _ in range(latas):
        peso = random.randint(100, 2000)
        sodio = random.randint(1, 12)
        exportacion = random.choice(exportaciones)

        tipo_peso = clasificar_peso(peso)
        tipo_sodio = clasificar_sodio(sodio)
        tipo_exportacion = clasificar_exportacion(exportacion)

        print(f"Peso: {peso} gramos | Sodio: {sodio} mg | {tipo_peso} | {tipo_sodio} | {tipo_exportacion}")
        time.sleep(1)


ejercicio2()
