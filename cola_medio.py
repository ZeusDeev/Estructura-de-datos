# Creamos un mini sistema básico de banco usando lo aprendido en colas
import sys  # Importa el módulo sys para gestionar la salida del programa

personas = []  # Lista para almacenar los registros de las personas en la cola

while True:  # Bucle infinito para mantener el sistema en funcionamiento
    print('--------------------------------- \n Bienvenido al sistema de banco \n---------------------------------')

    # Pregunta si la persona ya fue atendida
    atendido = input('ya fue atendido? Si o No: ')

    if atendido != 'si':  # Si la persona no ha sido atendida
        nuevo_registro = input('Ingrese su nombre: ')  # Pide el nombre de la persona

        # Muestra las opciones de trámite disponibles
        print('Tramite a realizar para añadirlo a la cola:\n 1.- Retiro efectivo\n 2.- Deposito deuda')
        tramite = input('Seleccione: ')  # Pide al usuario que seleccione un trámite

        # Comprueba si el trámite seleccionado es válido
        if tramite == '1' or tramite == '2':
            personas.append(nuevo_registro)  # Agrega el nuevo registro a la cola
            print(f'Esta en cola: {personas[-1]}')  # Muestra el último registro agregado
            print(personas)  # Imprime la cola actual

        elif tramite != '1' and tramite != '2':  # Si el trámite no es válido
            print('No encontramos su tramite, por favor, añada los tramites correctos a realizar')

    else:  # Si la persona ya fue atendida
        print(f'Usted ya fue atendido, Gracias por su preferencia\n{personas[0]}')  # Agradece al usuario
        personas.pop(0)  # Elimina a la primera persona de la cola (la atendida)

        print(f'Cola actual: {personas}')  # Muestra la cola después de atender

    continuar = input('Desea continuar?: ')  # Pregunta si desea continuar

    if continuar == 'no':  # Si el usuario no desea continuar
        print('Hasta Luego:)')  # Mensaje de despedida
        sys.exit()  # Termina el programa
