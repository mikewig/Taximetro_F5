# Realizar un taximetro interactivo

import os, time

def taximetro():
    x = input("What is your name?: ")
    print(f"Hi {x}, welcome to the taxi meter!")
    print("Here are the options:")
    
    km = float(0)
    price_per_km = float(3)
    start_fee = float(10.20)
    running = False
    
    while(True):
        print("1. Start the taximeter")
        print("2. Stop the taximeter")
        print("3. Exit")

        option = int(input("Enter an option: "))

        if option == 1:
            if not running:
                print("The taximeter is running...")
                running = True
                while running:
                    time.sleep(2)
                    km += 1
                    stop = input("Do you want to stop the taximeter? (y/n): ")
                    if stop == "y":
                        print(f"{km}km")
                        print("The taxi meter is stopped.")
                        print(f"Total distance: {km}km")
                        print(f"Total price: {start_fee + (km * price_per_km)}€")
                        running = False
                        time.sleep(5)
                        os.system("cls")
                        break
                    else:
                        print("The taximeter is running...")

        elif option == 2:
            if running:
                print("The taxi meter is stopped.")
                print(f"Total distance: {km}km")
                print(f"Total price: {start_fee + (km * price_per_km)}€")
                running = False
                time.sleep(1)
                os.system("cls")
            else:
                print("The taximeter is not running yet.")

        elif option == 3:
            print("Bye!")
            break

        else:
            print("Invalid option")
            time.sleep(1)
            os.system("cls")
taximetro()

        
