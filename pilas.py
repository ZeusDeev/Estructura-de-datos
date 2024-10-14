#Pilas, en pilas se considera el LIFO, es decir: Last input First ouput, un utimo en llegar primero en salir

pila = [1,2,3,4]

#Añadimos un ultimo elemento a nuestra pila
pila.append(5)
pila.append(6)

#Hacemos el utimo en llegar, primero en salir
pila.pop()

print(pila)

pila = []  # Inicializamos la pila vacía
