
palabra = input ("INGRESA UN TEXTO: ")
print (len(palabra))

if  len(palabra) < 10:

    print("TEXTO CORTO")

elif len(palabra) >= 10 and len(palabra) < 20:

    print("TEXTO MEDIO")

elif len(palabra) > 20:

    print("TEXTO LARGO")