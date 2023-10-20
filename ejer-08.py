"""
Verificar si una cadena comienza con un prefijo específico.
   Función: `startswith()`

"""
cadena = "wuaky" 
letra=input("Ingrese la letra para ver si la cadena inicia con ella: ")
resultado = cadena.startswith(letra) 
if resultado==True:
    print("la letra concide")
else:
    print("La letra no coincide")

