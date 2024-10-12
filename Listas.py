# Lista

#Una lista es un conjuntos de datos, de las cueles pueden varias

lista = [1,2,3,4,5,'Ocho', False,True,2.3,'Juanito']

for cada_elemento in lista:
    print(cada_elemento)

# Con append podemos agregar un elemento al final de la lista

lista.append('Hola Mundo')
print(lista)


# Extend con extend podemos extender nuestra lista iniciando al final
lista2 = ['Python es pro',18,'Zeus']

lista.extend(lista2)
print(lista)

#Inserta en una posicion en la que deseemos agregarle

lista.insert(2,'manzana')
print(lista)

# Con remove podemos eliminar cualquier elemento de nuestra lista

lista.remove('manzana') #No por posicion si no por valor
print(lista)

#Elimina un elemento de nuestra lista dependiendo la posicion que querramos eliminar

lista.pop(2)
elemento_eliminado = lista.pop(0)

print(elemento_eliminado)
print(lista)

# Elimina todo los elementos de la lista con Clear

lista.clear()
print(lista)

# Index - Con index podemos buscar un valor determinado de nuestra lista

nueva_lista = [1,2,3,4,5,6,7,8]
print(nueva_lista.index(8))

# Usando Copy para copiar lista (Copias superficial)

respaldo_nueva_lista = nueva_lista.copy()
nueva_lista.append(5)

print(nueva_lista)
print('***'*10)
print(respaldo_nueva_lista)