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
