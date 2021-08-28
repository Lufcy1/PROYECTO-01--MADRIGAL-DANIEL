from Data_base.login_db import login_list   # Import de lista de usuarios.

def login_validation(user, password):       # -- Funcion para validar si el usuario existe. 
     
    temp_list = [[user, password]]          # Creacion de lista temporal con los parametros recibidos.

    for value in login_list:                # For para recorrer la lista de usuarios existentes.
        if value == temp_list[0]:           # Comparar si los valores recibidos existen en la lista original.
            return True                     # Si existe regresa True.

    del value
    return False                            # No existe regresa False.


def user_creation(user, password):          # -- Funcion creacion de usuarios.

    for value in login_list:             # For para checar si el usuario ya existe.
        if(value[0] == user):                  
            return False                    # Si existe regresa False.

    login_list.append([user, password])     # No existe crea el usuario y contrasena.
    return True                             # Regresa True