#colas - primero en llegar primero, primero en salir

#Creamos una lista personas para simular una cola
personas = ['Biansito', 'Sami', 'Zeus', 'Julio', 'Yoli']

personas.append('Juanito') #añadimos un nueva persona a la cola

print(f'Persona {personas[5]}, añadida a la cola') #muestra el valor añadido
print(personas) #muestra nuestra lista o cola actual

registro_actualizado = personas #variable para mostrar nuestro registo actualizado
persona_atendia = personas.pop(0) #eliminamos nuestra primera entrada primero en entrar primero en salir

print(f'Se atendio a: {persona_atendia}') #imprime la persona atendida y salida
print(f'Cola actual: \n{registro_actualizado}') #imprime cola actualizada