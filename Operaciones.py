def compruebe(uno, dos):
    """
    Comprueba si los valores dados pueden convertirse a float.

    Parámetros:
    uno (str): El primer valor como cadena.
    dos (str): El segundo valor como cadena.

    Retorna:
    bool: True si ambos valores pueden convertirse a float, de lo 
    contrario False.
    """
    try:
        float(uno)
        float(dos)
        return True
    except ValueError:
        return False
    
def operaciones(uno: float, dos: float, operador: str) -> float:
    """
    Realiza una operación matemática basada en el operador proporcionado.

    Parámetros:
    uno (float): El primer número.
    dos (float): El segundo número.
    operador (str): El operador matemático, como '+', '-', '*', '/'.

    Retorna:
    float: El resultado de la operación.

    Lanza:
    ValueError: Si el operador no es válido o si hay una división por 
    cero.
    """
    if operador in ("+", "-", "*", "/"):
        match operador:
            case "+":
                return uno + dos
            case "-":
                return uno - dos
            case "*":
                return uno * dos
            case "/":
                if dos == 0:
                    raise ValueError("Di NO a la división por cero")
                return uno / dos
    else:
        raise ValueError("Sea serio")

if __name__ == "__main__":
    uno = input("Ingrese el primer número: ")
    dos = input("Ingrese el segundo número: ")
    if compruebe(uno, dos):
        uno = float(uno)
        dos = float(dos)
        operador = input("Ingrese la operación que desea hacer (+, -, *, /): ")
        try:
            resultado = operaciones(uno, dos, operador)
            print("El resultado es:", resultado)
        except ValueError as e:
            print("Error:", e)
        except Exception as error:
            print(f"Error: {error}")
    else:
        print("Por favor, ingrese solo números")
