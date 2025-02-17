# Diseñar un taximetro interactivo

# Importo las librerias que voy a necesitar para mi código

import time
import os
import keyboard

# Declaro la función de mis opciones, que le permita al usuario seleccionar para acceder a la aplicación

def options():
    print("Hi user, welcome to the Taximeter!")
    print("Here are the options")
    print("1. Start the taximeter.")
    print("2. Stop the taximeter.")
    print("3. Exit.")

# Uso la clase para las variables que utilizare dentro del programa

class Taximetro:
    
    # Es importante esta función ya que contiene todas las variables que utilizare en el taximetro

    def __init__(self):
        self.start_time = 0
        self.running = False
        self.price_per_sec = 0
        self.price_per_mov = 0
        self.start_fee = 10.20
    
    # Declaro la función que inicia mi taximetro, opcion == 1

    def iniciar_taximetro(self):
        self.start_time = time.time()
        self.running = True

        # Este bucle while se inicia cuando running es True

        while self.running:
            
            # Esta serie de condicionales le indica a mi bucle while que cuando la tecla "w" es presionada, mi taxi avanza
            os.system("cls")

            if keyboard.is_pressed("w"):
                time.sleep(1)
                self.price_per_mov += 0.05
                print("The taximeter is running...")

            # Cuando presiono la "s" mi taxi se detiene, lo cual deja de aumentar la tarifa en 0.05 y decrece en 0.02

            elif keyboard.is_pressed("s"):
                time.sleep(1)
                self.price_per_sec += 0.02
                print("The taxi is stopped...")

            # Cuando la tecla "p" es presionada el taxi se detiene por completo, y regresa al usuario al menu de opciones

            elif keyboard.is_pressed("p"):
                print("You stopped the taximeter.")
                self.running = False  
                os.system("cls")              

    # Declaro mi función que detendra mi taxi y me imprimira por pantalla el tiempo total y la tarifa total

    def detener_taximetro(self):

        # Modifico las variables que utilizare en esta función

        end_time = time.time()
        total_time = end_time - self.start_time
        total_price = self.price_per_mov + self.price_per_sec + self.start_fee

        # Imprimo por pantalla, el taximetro se ha detenido, el precio total y el tiempo que ha tomado el taxi en detenerse por completo

        print("The taximeter is stopped")
        print(f"Your grudge marks {total_price}€")
        print(f"Total time was {total_time / 60:.2f} min")

        # Cuando acaba lo demas, regreso mis variables a 0 para que asi no se acumulen en el bucle

        self.start_time = 0
        self.price_per_mov = 0
        self.price_per_sec = 0

        time.sleep(7)
        os.system("cls")

# Declaro mi función principal que contendra las demas

def main():

    # Paso a una variable mi class

    taximetro = Taximetro()

    # Declaro mi bucle while(True) para que la aplicación no acabe hasta que el usuario salga de esta

    while(True):
        options()
        option = int(input("Enter an option: "))

        # Si el usuario elige la primera opción, se iniciara la función iniciar_taximetro

        if option == 1:
            taximetro.iniciar_taximetro()

        # La función 2 se inicia, por lo cual el usuario decidio detener_taximetro

        elif option == 2:
            taximetro.detener_taximetro()
        
        # El usuario decide terminar el bucle y sale de la aplicación

        elif option == 3:
            print("Bye!")
            break
        else:
            print("Invalid option, please try again.")
            time.sleep(2)
            os.system("cls")

# Llamo a mi función principal

if __name__ == "__main__":
    main()