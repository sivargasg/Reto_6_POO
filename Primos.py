def compruebe(entrada):
    """
    Verifica si todos los elementos en una cadena de entrada separada 
    por comas son números enteros no negativos.

    Parámetros:
    entrada (str): Una cadena de texto donde los elementos están 
    separados por comas.

    Retorna:
    bool: True si todos los elementos pueden convertirse a enteros no 
    negativos, False en caso contrario.
    """
    lista = entrada.split(",")
    lista = [elemento.strip() for elemento in lista]
    for elemento in lista:
        try:
            n = int(elemento)
            if n < 0:  # Verifica que no sea negativo
                return False
        except ValueError:
            return False
    return True

def primos(entrada):
    """
    Procesa una cadena de entrada separada por comas y verifica si 
    cada número es primo.

    Parámetros:
    entrada (str): Una cadena de texto donde los elementos están 
    separados por comas.

    Retorna:
    str: Una cadena con los números primos.
    """
    lista = entrada.split(",")
    lista = [elemento.strip() for elemento in lista]
    lista_primos = []
    for numero in lista:
        numero = int(numero)
        primo = True
        if numero <= 1:
            primo = False
        divisor = 2
        while divisor <= int(numero ** 0.5):
            if numero % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            lista_primos.append(numero)
    return ", ".join(map(str, lista_primos))

if __name__ == "__main__":
	try:
		entrada = input("Ingrese su lista de números naturales, separados por comas: ")
		if compruebe(entrada):
			print("Los números primos de su lista son: " + primos(entrada))
		else:  
			print("Por favor, ingrese solo números naturales.")
	except Exception as e:
		print(f"Error: {e}")
