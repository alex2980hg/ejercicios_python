
ladoa = int(input("INGRESA EL LADO A: "))
ladob = int(input("\nINGRESA EL LADO B: "))
ladoc = int(input("\nINGRESA EL LADO C: "))

if ladoa == ladob and ladoc == ladoa: 
    print("ES UN TRIANGULO EQUILATERO")

elif (ladoa == ladob and ladoa != ladoc) or (ladob == ladoc and ladob != ladoa) or (ladoa == ladoc and ladoc != ladob):

    print ("ES UN TRIANGULO ISOSCELES")

else:

    print ("ES UN TRIANGULO ESCALENO")
