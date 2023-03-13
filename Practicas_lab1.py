#Ejercicio 1
print ("Ejercicio 1")

n = int(input(u"ingrese el tamaño del arreglo"))
m = int(input(u"ingrese el número de múltiplos"))
A = []
for i in range (0,n):
    A.append(i*m)
print (A)

#Ejercicio 2
print ("Ejercicio 2")

A = int(input(u"ingrese el tamaño de los arreglos: "))
B = []
C = []
for i in range (0,A):
    B.append(input("ingrese el nombre de las personas: "))
print (B)

for j in range (0,A):
    C.append(len(B[j]))
print (C)


#Ejercicio 3

print ("Ejercicio 3")
A = [1, 5, 8, 3, 30, 9, 13]
B = []
for i in A:
    if i>3 and 1%2 != 0:
        B.append(i)
    print (B)

#Ejercicio 4

print ("Ejercicio 4")
A = [20, 15, 12, 11, 8, 4, 1]
maxi = 20
mini = maxi
for i in A:
    if i<mini:
        mini = i
        print (u"El promedio más bajo es: ", mini)
        A.remove(mini)
        print (A)
        suma = 0
        for j in A:
            suma +=j
            print (suma)
            print (suma/len(A))

