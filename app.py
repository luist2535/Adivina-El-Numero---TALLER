import random

def main():
    print("¡Bienvenido al Juego de Adivinar el Número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 100): "))
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
