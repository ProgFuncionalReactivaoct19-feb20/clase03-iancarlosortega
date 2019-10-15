"""
	Ejercicio 6:
	@iancarlosortega
"""

palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

resultado = filter(lambda x : x =="".join(reversed(x)),palabras)

print(list(resultado))