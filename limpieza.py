
# Importo las librerias que voy a usar para mi programa

import os
import time
import keyboard

# Declaro la funcion de opciones la cual permite desplegar las opciones del menu de inicio

def opciones():
    print("Hello user, welcome to the taximeter.")
    print("Here are the options:")
    print("1. Start the taximeter")
    print("2. Stop the taximeter")
    print("3. Exit")

# Declaro la clase Taximetro que contiene los metodos para iniciar y detener mi taximetro

class Taximetro:

    # Declaro mis variables que voy a utilizar

    def __init__(self):

        """Inicializa las variables del taximetro
        km: kilometros recorridos por el taxi
        price_per_km: precio por kilometro recorrido
        start_fee: la tarifa base del taxi
        running: variable que permite saber si el taximetro esta en marcha
        start_time: tiempo en el que se inicia el taximetro"""

        self.km = 0
        self.price_per_km = 3
        self.start_fee = 10.20
        self.running = False
        self.start_time = 0

    # Declaro la funcion que va a iniciar el taximetro

    def iniciar_taximetro(self):
        self.start_time = time.time()
        self.running = True

        # Declaro mi bucle que ejecutara el taximetro

        while self.running:

            # Esta condición lo que hace es, si presiono la tecla "w" el taximetro comienza a avanzar

            if keyboard.is_pressed("w"):
                time.sleep(1)
                self.km += 1
                print(f"Taximeter is running... Distance: {self.km}km")

            # En esta, si presiono la tecla "s" mi taximetro se detendra

            elif keyboard.is_pressed("s"):
                print("You stopped the taximeter.")
                self.running = False
     
    # Declaro la funcion para detener mi taximetro

    def detener_taximetro(self):

        # La variable end_time que me permite saber el tiempo transcurrido del recorrido

        end_time = time.time()
        total_time = end_time - self.start_time
        total_price = self.start_fee + (self.km * self.price_per_km)

        print("The taximeter is stopped.")
        print(f"Total distance: {self.km}km")
        print(f"Your grudge marks: {total_price}€")
        print(f"Total time: {total_time / 60:.2f} minutes")

        # Reinicio mis variables para que el taximetro pueda ser usado nuevamente

        self.km = 0
        self.start_time = 0
        total_price = 0

        time.sleep(10)
        os.system("cls")

def main():

    # Mi main, el cual contendra el bucle completo que ejecutara lo demas

    taximetro = Taximetro()

    # Un while(True) para que el bucle se siga repitiendo hasta que el usuario decida salir

    while(True):
        opciones()
        option = int(input("Enter an option: "))

        if option == 1:
            taximetro.iniciar_taximetro()
        
        elif option == 2:
            taximetro.detener_taximetro()
        
        elif option == 3:
            print("Bye!")
            break
        else:
            print("Invalid option, please try again.")
            time.sleep(2)
            os.system("cls")

# Llamo a mi funcion principal

if __name__ == "__main__":
    main()     