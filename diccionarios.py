diccionario_frutas = {
    '01':'Manzana',
    '02':'Pera',
    '03':'Uva',
    '04':'Mango',
    '05':'Papaya'
}

#Imprime nuestro diccionario
print(diccionario_frutas)

#Buscamos con el indice de nuestro diccionario para buscar el valor deseado
print(diccionario_frutas['01'])

#Se añade un nuevo valor al final de nuestro diccionario
diccionario_frutas['06'] = 'Maracuya'
print(diccionario_frutas)

#Modificar un valor en diccionarios, o bn los actualiza
diccionario_frutas['04'] = 'Fresa'
print(diccionario_frutas)

#Eliminar un valor deseado de nuestro diccionario

del(diccionario_frutas['04'])
print(diccionario_frutas)

#--------------------------------------------#

#Diccionario con lista
diccionario_personas = {
    'Zeus':[20,1.70],
    'Juanito':[23,1.68],
    'Mariana':[19,1.60],
    'Karen': [23, 1.60]
}

print(diccionario_personas)

#Podemos crear un diccionario pero con otro dentro, ejemplo:

diccionario_personas2 = {
    'Zeus': {'Edad':20,'Estatura':1.70},
    'Juanito':{'Edad':22,'Estatura':1.69},
    'Mariana':{'Edad':19,'Estatura':1.65},
    'Karen': {'Edad':23,'Estatura':1.58}
}

print(diccionario_personas2)

#accedemos al indice o valor deseado y asi comprobar sus valores

print(diccionario_personas2['Karen'])


