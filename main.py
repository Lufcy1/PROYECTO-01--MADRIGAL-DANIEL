import os                                                                                   # Import sistema operativo.
import getpass                                                                              # Import contrasena function
from time import sleep                                                                      # Import sleep function
import Functions.login                                                                      # Import de Funciones en login
import Functions.checks

clear = lambda: os.system('cls')                                                            # Creacion de variable / Borrar consola.

print("----- Inicio de Sesion -----\n")

while True:                                                                                 # -- While principal / Mantener aplicacion en funcionamiento.

    choose = input("Cuenta con un usuario existente? y/n: ")                                # Eleccion para registrar o ingresar.

    if choose == "y" or choose == "yes" or choose == "si":                                  # -- If Ingreso de usuario y contrasena.
        while True:                                                                         # While repetir hasta que usuario y contrasena correctos.

            username = input("Ingresa nombre de usuario: ")                                 # Ingreso de usuario.
            userpass = getpass.getpass("Ingresa contrasena de usuario: ")                   # Ingreso de contrasena.

            if Functions.login.login_validation(username, userpass):                        # If chequeo de usuario y contrasena existen.
                print("Ingreso Exitoso.")
                sleep(1.5)
                clear()
                print("----- Bienvenido a LifeStore Application -----\n")

                while True:                                                                 # -- While Seleccion
                    print("\n[1] Productos con mayores ventas.")
                    print("[2] Productos con mayores busquedas.")
                    print("[3] Productos con menores ventas por categoria.")
                    print("[4] Productos con menores busquedas por categoria.")
                    print("[5] Productos con mejores resenas.")
                    print("[6] Productos con peores resenas.")
                    print("[7] Total de ingresos y ventas promedio mensuales.")
                    print("[8] Total anual y meses con mas ventas.")

                    elecction = input("Selecciona una opcion (Numero): ")                   # Selecciona el numero de opcion a elegir.

                    if elecction == '1':
                        print("\n----- Productos con mayores ventas -----")
                        Functions.checks.bestproducts_sales(input("Selecciona la cantidad de productos que desea mostrar: "))
                    
                    elif elecction == '2':
                        print("\n----- Productos con mayores busquedas -----")
                        Functions.checks.bestproducts_search(input("Selecciona la cantidad de productos que desea mostrar: "))

                    elif elecction == '3':
                        print("\n----- Productos con menores ventas por categoria -----")
                        Functions.checks.categorys_select()
                        category = input("Selecciona la categoria (Numero): ")
                        quantity = input("Selecciona la cantidad de productos que desea mostrar: ")
                        Functions.checks.worstproducts_sales(quantity, category)

                    elif elecction == '4':
                        print("\n----- Productos con menores busquedas por categoria -----")
                        Functions.checks.categorys_select()
                        category = input("Selecciona la categoria (Numero): ")
                        quantity = input("Selecciona la cantidad de productos que desea mostrar: ")
                        Functions.checks.worstproducts_search(quantity, category)

                    elif elecction == '5':
                        print("\n----- Productos con mejores resenas -----")
                        Functions.checks.bestproducts_score(input("Selecciona la cantidad de productos que desea mostrar: "))

                    elif elecction == '6':
                        print("\n----- Productos con peores resenas -----")
                        Functions.checks.worstproducts_score(input("Selecciona la cantiadad de productos que desea mostrar: "))
                    
                    elif elecction == '7':
                        print("\n----- Total de ingresos y ventas promedio mensuales -----")
                        Functions.checks.bestmonth_sales()

                    elif elecction == '8':
                        print("\n----- Total anual y meses con mas ventas. -----")
                        Functions.checks.total_earnings()
                        Functions.checks.month_sales()

            else:                                                                           # Else usuario no existe.
                print("Error. Usuario o contrasena incorrecto, intenta nuevamente.\n")      # ! Error. usuario no existente y regresa al inicio del While.


    elif choose == "n" or choose == "no":                                                   # -- Elif Registro de usuario.
        while True:                                                                         # While repetir hasta que se cree usuario.
            
            reg_name = input("Ingresa nombre de usuario de tu preferencia: ")               # Ingreso de usuario a crear.
            
            while True:                                                                     # While repite hasta contrasena iguales.

                reg_pass = getpass.getpass("Ingresa contrasena de usario de tu eleccion: ") # Ingreso de contrasena.
                check_pass = getpass.getpass("Confirma la contrasena: ")                    # Confirmacion de contrasena.

                if reg_pass == check_pass:                                                  # If chequeo de contrasenas iguales.
                    break                                                                   # Si son iguales rompe el While y continua el registro.

                else:
                    print("Error. Contrasenas no coinciden, intenta nuevamente.\n")         # ! Error. No son iguales regresa al inicio del While y se ingresan de nuevo.

            if Functions.login.user_creation(reg_name, reg_pass):                           # If chequeo si usuario ya existe, si no existe regresa True.
                print("Usuario creado exitosamente.")
                sleep(2)
                clear()
                break                                                                       # Rompe el While de Registro de usuario.

            else:
                print("Error. Usuario ya existe, intenta de nuevo.\n")                      # ! Error. regresa al inicio de registro.

    else:
        print("Error. Ingresa un valor correcto.\n")                                        # ! Error. regresa al inicio de la aplicacion.