"""
Comprobar si una cadena contiene solo dígitos.
    Función: `isdigit()`

"""
cadena=input("ingrese un texto: ")
resultado=cadena.isdigit()

if resultado==True:
    print("el texto ingresado solo contiene numeros")
else:
    print("la cadena no es solo de numero")