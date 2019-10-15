"""
	Ejercicio 7
	@iancarlosortega
"""
def funcion(x):
	
	caracter = x[0]

	letras = ["l","p","a","e","i"]

	if caracter in letras:
		return True
	else:
		return False



placas = [ "lba-001","gma-002", "azx-003", "ess-004","oro-100","mab-001","iaj-002"]

resultado = filter(funcion,placas)

print(list(resultado))