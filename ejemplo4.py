
num1 = input ("INGRESA EL PRIMER NUMERO: ")
num1 = float(num1)

num2 = input ("INGRESA EL SEGUNDO NUMERO: ")
num2 = float(num2)

print ("OPERACIONES: SUMA(S), RESTA(R), MULTIPLICACION(M) Y DIVISION(D)")
letra = input ("INGRESA LA PRIMER LETRA DE LA OPERACION A REALIZAR: ")

if letra == "S":
    resultado = num1+num2
    resultado = float(resultado)
    print ("EL RESULTADO DE LA SUMA ES: " , resultado)

elif letra == "R":
    resultado = num1-num2
    print ("EL RESULTADO DE LA RESTA ES: " , resultado)
    
elif letra == "M":
    resultado = num1*num2
    print ("EL RESULTADO MULTIPLICACION ES: " , resultado)
     
elif letra == "D":
    resultado = num1/num2
    print ("EL RESULTADO DE LA DIVISION ES: " , resultado)
    


