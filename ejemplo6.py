
nombre = input ("INGRESA TU NOMBRE COMPLETO: ")
direccion = input ("\nINGRESA TU DIRECCION: ")
edad = input ("\nINGRESA TU EDAD: ")
edad = int(edad)

print ("\nTU NOMBRE ES: " + nombre)
print ("TU DIRECCION ES: " + direccion)
print ("TU EDAD ES: ", edad)

if edad < 18: 
    print ("ERES MENOR DE EDAD")

elif edad >= 18 and edad < 65:
    print ("ERES MAYOR DE EDAD")

elif edad >= 65:
    print ("ERES UN ADULTO MAYOR")