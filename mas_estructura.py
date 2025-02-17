
# Importo las librerias que necesito

import keyboard
import time
import os

# Declaro la funcion menu_de_inicio que imprime las opciones del menu

def menu_de_inicio():
    print("\nHello user, welcome to the taximeter.")
    print("Here are the options:")
    print("1. Start the taximeter")
    print("2. Stop the taximeter")
    print("3. Exit")

# Declaro la funcion iniciar_taximetro que inicia el taximetro y calcula el precio

def iniciar_taximetro():

    # Declaro las variables que voy a utilizar

    km = 0
    price_per_km = 3
    start_fee = 10.20
    start_time = time.time()
    running = True
    print("The taximeter has started.")

    # Declaro mi bucle while que ejecuta el taximetro

    while running:

        # Esta condición me dice que al presionar "w" el taximetro empieza a avanzar o el "Taxi"
        
        if keyboard.is_pressed("w"):
            time.sleep(1)
            km += 1
            print(f"Taximeter is running... Distance: {km}km")
        # La siguiente condición indica que cuando presiona la tecla "s" mi taximetro se va a detener

        elif keyboard.is_pressed("s"):
            print("You stopped the taximeter.")
            end_time = time.time()
            total_time = end_time - start_time
            total_price = start_fee + (km * price_per_km)
            print(f"Total distance: {km}km")
            print(f"Total price: {total_price}€")
            print(f"Total time: {total_time / 60:.2f} minutes")
            running = False
            
        return km, price_per_km, start_fee

# Declaro mi función para detener_taximetro que me imprime el precio total y la distancia recorrida

def detener_taximetro(km, price_per_km, start_fee):
    print("You stopped the taximeter.")
    
    # Aca declaró mi variable que continene el precio total del recorrido

    total_price = start_fee + (km * price_per_km)
    print(f"Total distance: {km}km")
    print(f"Total price: {total_price}€")
    time.sleep(3)
    os.system("cls")

# Declaro mi función principal que ejecuta el proceso

def main():
    km = 0
    price_per_km = 3
    start_fee = 10.20
    running = False

    while(True):
        menu_de_inicio()

        # Tipeo mi try, que es para ver si el usuario ingresa un valor correcto prosiga la función

        try:
            option = (int(input("Enter an option: ")))

        # Except lo que hace es, si el usuario introduce un valor no valido, le imprime un erro, y vuelve a ejecutar la función

        except ValueError:
            print("That option is not valid, press the correct key.")
            continue

        # Declaro mis condiciones con su respectiva opción y función

        if option == 1:
            if not running:
                km, price_per_km, start_fee = iniciar_taximetro()
                running = True
            else:
                print("The taximeter is already running.")
        
        elif option == 2:
            if running:
                detener_taximetro(km, price_per_km, start_fee)
                running = False
            else:
                print("The taximeter is not running yet.")
        
        elif option == 3:
            print("Bye!")
            break

        else:
            print("Invalid option, please select 1, 2 or 3.")
            time.sleep(3)
            os.system("cls")

# Ejecuto mi función principal

if __name__ == "__main__":
    main()