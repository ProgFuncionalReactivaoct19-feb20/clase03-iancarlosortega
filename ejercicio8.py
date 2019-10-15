"""
	Ejercicio 8:
	@iancarlosortega
"""
def funcion (x):
	tamaño = len(x)
	if tamaño%2 == 0:
		return True
	else:
		return False

ciudades = ["Loja","Pichincha","Guayaquil","Zamora","Ibarra", "Manabi","Machala", "Portoviejo","Macas"]

resultado = filter(funcion,ciudades)

print(list(resultado))