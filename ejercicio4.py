"""	
	Ejercicio 4: Funciones de orden superior
	@iancarlosortega
"""

datos = [18,19,20,10,11,12]

resultado = filter(lambda x : x>=18 or x<=10, datos)

print(resultado)
print(list(resultado))