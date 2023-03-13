import random
texto = "\nEn 1850, Joshua y Naomi Collins junto a su joven hijo Barnabas salen de Inglaterra para formar una nueva vida en Estados Unidos desde luego, donde construyen un imperio pesquero desde luego en la comunidad de Maine, más no sabían que este cambio los llevarían a una tragedia, ya que cuando el joven Barnabas se enamora de una preciosa dama llamada Josette, sin embargo, este no sabía que la criada de su casa era una bruja la cual estaba perdidamente enamorada de él, luego de enterarse de que Barnabas se casaría con Josette decidió plantar un maleficio en Josette, para así lograr que nunca fuera feliz Barnabas; en su desesperación Barnabas intentó suicidarse para alcanzar a su amada en el más allá, sin embargo, la bruja lo transformó en vampiro para que ambos pudieran disfrutar de forma miserable, la eternidad."
def mostrar_menu():
    print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print (texto+"\n")
    print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Menu xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print ("1.- Buscar cadena\n2.- Comprobar cadena\n3.- Sustraer una cadena\n4.- Insertar una cadena (insertar en lugar random)\n5.- Borrar una cadena\n6.- Reemplazar una cadena\n")

while True:
    mostrar_menu()
    Opcion = input("Seleccione una opción: ")

    if Opcion == "1":
        buscar = input("Teclee la subcadena que desee buscar dentro del texto: ")
        indice = texto.find(buscar)
        if indice != -1:
            print(f"La subcadena '{buscar}' se encuentra en la posición '{indice}' dentro del texto.\n")
        else:
            print(f"La subcadena '{buscar}' no se encontró dentro del texto.\n")
    elif Opcion	 == '2':
        print(texto)
        cadena = input("Teclee la subcadena que desee buscar dentro del texto: ")
        if cadena in texto:
            print(f"La subcadena '{cadena}' se encontró dentro del texto.\n")
        else:
            print(f"La subcadena '{cadena}' no se encontró en el texto.\n")
    elif Opcion == "3":
        print(texto)
        cadenas = texto.split()
        inicio = int(input("\nRegistre el indice de inicio donde requiera sustraer la cadena: "))
        fin = int(input("\nRegistre el indice final donde requiera sustraer la cadena: "))
        cadena2 = cadenas[inicio:fin]
        print(cadena2)

    elif Opcion == "4":
        print(texto)
        cadena3 = input("Teclee la cadena que desee insertar: ")
        indice_insertar = random.radint(0, len(texto))
        texto_mod = texto[:indice_insertar] + cadena3 + texto[indice_insertar:]
        print(texto_mod)
    elif Opcion == "5":
        print(texto+"\n")
        cadena_a_borrar = input("Teclee la cadena a borrar: ")
        if cadena_a_borrar in texto:
            texto_mod = texto.replace(cadena_a_borrar, "")
            print(texto_mod)
        else:
            print(f"La cadena no se encuentra en el texto, por lo que no se puede borrar.")
    elif Opcion == "6":
        print(texto)
        cadena_reemplazar = input("Teclee la cadena que se requiera reemplazar: ")
        if cadena_reemplazar in texto:
            cadena_reemplazo = input("Teclee la cadena que reemplazará: ")
            texto_mod = texto.replace(cadena_reemplazar, cadena_reemplazo)
            print(texto_mod)
        else:
            print("La cadena que deseas reemplazar no se encuentra dentro del texto.\n")
    elif Opcion == "7":
        print("Salió del programa con éxito")
        break
    else:
        print("Elija una opción válida.\n")
