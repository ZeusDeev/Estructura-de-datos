pila = []  # Creamos una lista llamada pila vacía

while True:  # Comienza un bucle infinito hasta que el usuario decida salir
    # Mostramos el menú de opciones
    print('Bienvenido a pilas! \n 1.- para añadir un elemnto a la pila \n 2.- para sacar elemento y \n 3.- para salir')
    
    # Solicitamos al usuario que seleccione una opción
    seleccion = int(input('Ingrese:'))
    
    if seleccion == 1:  # Si la selección es 1, añadimos un nuevo valor a la pila
        nuevo_valor = int(input('añada valor deseado: '))  # Pedimos el valor a añadir
        pila.append(nuevo_valor)  # Añadimos el valor a la pila (al final de la lista)
        
    elif seleccion == 2:  # Si la selección es 2, sacamos el último elemento de la pila
        if len(pila) > 0:  # Comprobamos si la pila tiene elementos
            ultimo = pila.pop()  # Eliminamos y obtenemos el último elemento de la pila
            print(f'Se elimino {ultimo}')  # Mostramos el valor eliminado
        else:  # Si la pila está vacía
            print('No hay existencia en tu lista')  # Indicamos que no hay elementos para eliminar

    elif seleccion == 3:  # Si la selección es 3, salimos del bucle
        break  # Rompemos el bucle y salimos del programa

    # Mostramos el estado actual de la pila
    print(f'pila actual: \n {pila}')

# Cuando el bucle se rompe, mostramos un mensaje de fin de programa
print('Fin del programa...')
