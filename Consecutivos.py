def compruebe(entrada):
    """
    Comprueba si la entrada es una lista válida de números enteros 
    separados por comas.

    Parámetros:
    entrada (str): Cadena de texto con números enteros separados por 
    comas.

    Retorna:
    bool: True si la lista es válida (más de un número y todos enteros),
    False en caso contrario.
    """
    lista = entrada.split(",")
    lista = [elemento.strip() for elemento in lista]
    if len(lista) < 2:
        return False
    for elemento in lista:
        try:
            int(elemento)
        except ValueError:
            return False
    return True

def mas_grandes(entrada):
    """
    Encuentra la suma más grande de dos números consecutivos en una 
    lista de enteros.

    Parámetros:
    entrada (str): Cadena de texto con números enteros separados por 
    comas.

    Retorna:
    int: La suma más grande de dos números consecutivos en la lista.
    """
    lista = entrada.split(",")
    lista = [int(elemento.strip()) for elemento in lista]
    suma_mayor = lista[0] + lista[1]
    for i in range(1, len(lista)-1):
        suma = lista[i] + lista[i + 1]
        if suma > suma_mayor:
            suma_mayor = suma
    return suma_mayor

if __name__ == "__main__":
	try:
		entrada = input("Ingrese su lista de números enteros, separados por comas: ")
		if compruebe(entrada):
			print(f"La suma de los números consecutivos más grandes es: {mas_grandes(entrada)}")
		else:
			print("Por favor, ingrese una lista con más de un número y que estos sean enteros.")
	except Exception as e:
		print(f"Error: {e}")
