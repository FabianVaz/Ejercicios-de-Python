#Manipular cadenas de caracteres en python

mensaje = "Hola mundo"
print (mensaje)

#Operadores de cadenas de caracteres: Adición y multiplicación
#Concatenar
print ('\nejercicio 2')
mensaje1 = 'Hola' + ' ' + 'Mundo'
print (mensaje1)

#multiplicar

print ('\nEjercicio 3')
mensaje2a = 'hola' *3
mensaje2b = 'Mundo'

print (mensaje2a+mensaje2b)

#Añadir

print ('\nEjercicio 4')
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print (mensaje3)

#Métodos para cadenas de caracteres: Buscar, cambiar
#Extensión
print ('\nEjercicio 5')
mensaje4 = 'Hola' + ' ' + 'mundo'
print(len(mensaje4))

#Encontrar
print ('\nEjercicio 6')
mensaje5 = "Hola mundo"
mensaje5a = mensaje5.find("mundo")
print (mensaje5a)

print ('\nEjercicio 6.2')
mensaje6 = "Hola mundo"
mensaje6a = mensaje6.find("ardilla")
print(mensaje6a)

#Minúsculas
print('\nEjercicio 7')
Mensaje7 = "HOLA MUNDO"
mensaje7a = Mensaje7.lower()
print(mensaje7a)

#Reemplazar
print('\nEjercicio 8')
mensaje8 = "HOLA MUNDO"
mensaje8a = mensaje8.replace("L", "pizza")
print(mensaje8a)

#Cortar
print ('\nEjercicio 9')
mensaje9 = "Hola mundo"
mensaje9a = mensaje9[1:8]
print(mensaje9a)

print ('\nEjercicio 9.2')
mensaje9 = "Hola mundo"
startLoc = 2
endLoc = 8
mensaje9b = mensaje9[startLoc: endLoc]
print(mensaje9b)

print ('\nEjercicio 9.3')
mensaje9 = "Hola mundo"
print(mensaje9[:5].find("d"))

print("\nEjercicio 10")
print(len(Mensaje7))

mensaje7 = "Hola Mundo"
mensaje7a = mensaje7.lower()
print(mensaje7a)


#Secuencias de escape
print('\nEjercicio 11')
print('\"')

print ('el programa imprime \"Hola mundo\"')

print ('Hola\tHola\tHola\nMundo')


