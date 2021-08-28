from Data_base.lifestore_file import *                                      # Import base de datos LifeStore.
from datetime import datetime                                               # Import datetime.

def bestproducts_sales (quantity):                                          # -- [1] Productos con mayores ventas.

    temp_sales = []                                                         # Se crea una lista temporal donde se guardan datos.

    for value in lifestore_sales:                                           # For eliminar los sales con reembolso.
        if value[4] == 1:                                                   # Si reembolso = 1 salta el ciclo.
            continue
        temp_sales.append(value)                                            # Si reembolso = 0 anade el valor a la lista temporal.

    del value                                                               # Se limpia la variable.
    best_sales = []                                                         # Creacion de lista para guardar los datos a imprimir.

    for x in lifestore_products:                                            # For para recorrer todos los productos existentes.
        count = 0                                                           # Inicializacion de variable para contar la cantidad de productos que existen en la lista.
        for y in temp_sales:                                                # For para recorrer la lista de ventas.
            if x[0] == y[1]:                                                # If la id_product es igual a la id_product de la lista de ventas, se cuenta + 1.
                count += 1
        best_sales.append([count, x[1]])                                    # Al recorrer toda la lista con los parametros de ese producto se agrega su numbre y la cantidad.

    best_sales.sort(reverse=True)                                           # Se ordena la lista para mostrar de mayor a menor.
    
    try:                                                                    # Try evitar que se caiga el programa al trata de imprimir mas indices de los que existen.
        for i in range(0, int(quantity)):                                   # For imprimir la lista completa.
            print(best_sales[i])                                            
    except:                                                                 # Si crea un error al recorrer la lista evita que se caiga.
        print("Error. Seleccionaste mas datos de los que existen.")


def bestproducts_search (quantity):                                         # -- [2] Productos con mayores busquedas.

    best_search = []                                                        # Se crea una lista temporal donde se guardan datos.

    for x in lifestore_products:                                            # For para recorrer todos los productos existentes
        count = 0
        for y in lifestore_searches:                                        # For para recorrer la lista de busquedas.
            if x[0] == y [1]:                                               # If la id_product de products = id_product de searches cuenta + 1.
                count += 1
        best_search.append([count, x[1]])                                   # Al terminar de recorrer la lista busquedas se agrega la cantidad de veces que se repitio y el nombre.
    
    best_search.sort(reverse=True)                                          # Se ordena la lista para mostrar de mayor a menor.

    try:                                                                    # Try evitar que se caiga el programa al trata de imprimir mas indices de los que existen.
        for i in range(0, int(quantity)):                                   # For imprimir la lista completa.
            print(best_search[i])
    except:                                                                 # Si crea un error al recorrer la lista evita que se caiga.
        print("Error. Seleccionaste mas datos de los que existen.")


def categorys_select():                                                     # -- Funcion mostrar categorias existentes.
    list_category = []                                                      # Se crea una lista temporal donde se guardan datos.

    for value in lifestore_products:                                        # For para recorrer la lista productos. 
        if value[3] not in list_category:                                   # If el valor no existe en la lista categoria se agrega a esta misma lista.
            list_category.append(value[3])  

    for i in range(0, len(list_category)):                                  # For imprimir la lista de categorias existentes.
        print("[" + str(i+1) + "] " + str(list_category[i]))    
        

def worstproducts_sales (quantity, category):                               # -- [3] Productos con menores ventas por categoria.
    
    temp_sales = []                                                         # Se crea una lista temporal donde se guardan datos.

    for value in lifestore_sales:                                           # For para eliminar las ventas reembolsadas.
        if value[4] == 1:
            continue
        temp_sales.append(value)

    del value
    best_sales = []                                                         # Creacion de lista para imprimir.

    list_category = []

    for value in lifestore_products:                                        # For para guardar las categorias existentes.
        if value[3] not in list_category:
            list_category.append(value[3])

    for x in lifestore_products:                                            # For recorrer lista productos.
        count = 0
        for y in temp_sales:                                                # for recorrer la lista temporal de ventas / Sin reembolsos.
            if x[0] == y[1] :                                               # If id_product de product = id_product de ventas, cuenta + 1.
                count += 1
        if x[3] == list_category[int(category) - 1]:                        # iF category_product = al numero de la categoria recibida por parametro se anade.
            best_sales.append([count, x[1]])

    best_sales.sort(reverse=False)                                          # Ordena la lista de menor a mayor.
    
    try:                                                                    # Try evitar que se caiga el programa al trata de imprimir mas indices de los que existen.
        for i in range(0, int(quantity)):                                   # Imprimir la lista a mostrar.
            print(best_sales[i])
    except:                                                                 # Except evitar que se caiga el programa.
        print("Error. Seleccionaste mas datos de los que existen.")


def worstproducts_search (quantity, category):                              # -- [4] Productos con menores busquedas por categoria.
    
    best_search = []                                                        # Creacion de lista temporal.

    list_category = []

    for value in lifestore_products:                                        # For Agregar a la lista categoria las categorias existentes en products.
        if value[3] not in list_category:
            list_category.append(value[3])
    
    for x in lifestore_products:                                            # For recorrer la lista products
        count = 0
        for y in lifestore_searches:                                        # For recorrer la lista busquedas.
            if x[0] == y[1]:                                                # If id_product de products = id_products de searches cuenta + 1.
                count += 1

        if x[3] == list_category[int(category) - 1]:                        # If la categoria es igual a la categoria seleccionada se agrega.
            best_search.append([count, x[1]])
    
    best_search.sort(reverse=False)                                         # Ordenar lista de menor a mayor.
    try:
        for i in range(0, int(quantity)):                                   # Imprime la cantidad de datos seleccionado.
            print(best_search[i])
    except:
        print("Error. Seleccionaste mas datos de los que existen.")


def bestproducts_score(quantity):                                           # -- [5] Productos con mejores resenas.

    temp_score = []

    for x in lifestore_products:                                            # For recorre la lista products.
        count = 0
        duplicate = 0
        for y in lifestore_sales:                                           # For recorre la lista ventas.
            if x[0] == y[1] :                                               # If id_product de products = id product de sales se suma la la score de esta venta.
                count += y[2]
                duplicate += 1                                              # Se cuenta la cantidad de veces que se repite.

        if duplicate > 0:                                                   # If se repite mas de una vez se saca el promedio del score. (Para evitar dividir por cero.)
            count = count / duplicate           
            
        temp_score.append([format(count,".2f"), x[1]])                      # Se agrega el score con dos digitos despues del decimal y en nombre del producto.
    
    temp_score.sort(reverse=True)                                           # Se reordena la lista de mayor a menor.

    try:                                                                    # Try evitar que se caiga el programa por seleccionar un indice mayor al existente.
        for i in range(0, int(quantity)):                                   # Imprimir la cantidad de datos seleccionado.
            print(temp_score[i])
    except:
        print("Error. Seleccionaste mas datos de los que existen.")


def worstproducts_score(quantity):                                          # -- [6] Productos con peores resenas.
                                                                            # Se hace exactamente lo mismo con la anterior funcion solo se ordena de menor a mayor.
    temp_score = []

    for x in lifestore_products:
        count = 0
        duplicate = 0
        for y in lifestore_sales:
            if x[0] == y[1] :
                count += y[2]
                duplicate += 1

        if duplicate > 0:
            count = count / duplicate
            
        temp_score.append([format(count,".2f"), x[1]])
    
    temp_score.sort(reverse=False)

    try:
        for i in range(0, int(quantity)):
            print(temp_score[i])
    except:
        print("Error. Seleccionaste mas datos de los que existen.")

def bestmonth_sales():                                                      # -- [7] Total de ingresos y ventas promedio mensuales.
    temp_sales = []
    
    for month in range(0,12):                                               # For recorrer la cantidad de meses que existen.
        total = 0
        count = 0

        for y in lifestore_sales:                                           # For recorrer la lista ventas.
            date_sale = datetime.strptime(y[3], '%d/%m/%Y')                 # convertir el string de fecha en ventas a datetime.
            for x in lifestore_products:                                    # For recorrer la lista products.
               if x[0] == y[1] and date_sale.month > month and date_sale.month < month + 2:     # If id_product = id_product en ventas y
                   count += 1                                                                   # la fecha es mayor al X mes pero menos a X mes + 1.
                   total += int(x[2])                                                           # se agrega las veces que se repite y el total de precios.
            
        temp_sales.append([count, total, month + 1])                        # Se agrega la cantidad, el total y el numero del mes en la lista.

    print("[Numero de ventas, total de ingresos, numero de mes]")           
    for i in temp_sales:                                                    # For imprimir la lista.
        print(i)

def total_earnings():                                                       # -- [8] Total anual y meses con mas ventas. / 1
    temp_sales = []

    for value in lifestore_sales:                                           # For para eliminar las ventas con reembolso.
        
        if value[4] == 1:                                                   
            continue
        temp_sales.append(value)

    price = 0
    for x in lifestore_products:                                            # For para recorrer la lista productos.

        for y in temp_sales:                                                # For recorrer la lista y si estan en la lista se suma el precio de este mismo.
            if x[0] == y[1]:
                price += x[2]
    
    print("Total de ingresos anual: $" + str(price))                        # Se imprime el total con dos decimales.

def month_sales():                                                          # -- [8] Total anual y meses con mas ventas. / 2
    temp_sales = []
    
    for month in range(0,12):                                               # For recorrer los meses existentes.
        count = 0
        for value in lifestore_sales:                                       # For recorrer la lista ventas.
            date_sale = datetime.strptime(value[3], '%d/%m/%Y')             # Convertir el string de fechas a datetime.
            if date_sale.month > month and date_sale.month < month + 2:     # If es mayor a X mes pero menor a este X mes + 1
                count += 1                                                  # Se suma + 1.
                
        temp_sales.append([count, month + 1])                               # Se agrega las cantidad y el numero de mes.
    
    temp_sales.sort(reverse=True)                                           # Se ordena la lista de mayor a menor.

    print("Meses con mas ventas")
    print("[Numero de ventas, Numero de mes]")
    for i in temp_sales:                                                    # Imprime la lista.
        print(i)

    