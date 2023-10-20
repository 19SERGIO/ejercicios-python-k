"""
Comprobar si una cadena contiene solo letras.
    Función: `isalpha()`

"""
cadena=input("ingrese un texto: ")
resultado=cadena.isalpha()

if resultado==True:
    print("el texto ingresado solo contiene letras")
else:
    print("la cadena no es solo de letras")