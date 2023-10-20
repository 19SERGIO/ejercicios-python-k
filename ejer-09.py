"""
Verificar si una cadena termina con un sufijo específico.
   Función: `endswith()`

"""
cadena = "wuaky" 
letra=input("Ingrese la letra para ver si la cadena termina con ella: ")
resultado = cadena.endswith(letra) 
if resultado==True:
    print("la ultima letra concide")
else:
    print("La  ultima letra no coincide")
