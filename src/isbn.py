def normalize_isbn(cadena):
    # Quitar espacios y guiones "-"
    cadena = cadena.replace("-","")
    cadena_split = cadena.split()
    cadena_limpia = "".join(cadena_split) # El método split y join asegura que se eliminen todo tipo de espacios

    # Validar que solo haya dígitos(0-9), permitiendo una 'X' como último carácter
    error = "" # Cadena vacía en caso de error
    validar = True # Bandera que controla el flujo
    digitos = ["0","1","2","3","4","5","6","7","8","9"] # Lista de dígitos aceptados

    if not cadena_limpia: # Verifica que la cadena no esté vacía
        validar = False
    else:
        for caracter in cadena_limpia[:-1]: # Itera sobre todos los caracteres de la cadena excepto el último
            if caracter not in digitos: # Verifica si el carácter es inválido
                validar = False
                break

        if validar:
            ultimo_digito = cadena_limpia[-1].upper() # Guarda el último dígito de la cadena
            if ultimo_digito not in digitos and ultimo_digito != "X": # verifica que el último dígito no esté entre 0-9 y que no sea una "X"
                validar = False

    # Resultado
    if validar:
        return cadena_limpia.upper() # Regresa la cadena normalizada
    else:
        return error # Regresa una cadena vacía en caso de error
    
def is_valid_isbn10(cadena_limpia):
    cadena = cadena_limpia
    peso = 10 # Peso para validar el isbn-10
    valor_peso = 0 # Acumulador para el producto de (dígito * peso)
    suma_pesos = 0 # Variable para ir sumando los valores de peso de cada carácter
    validar = True # Bandera para controlar el flujo

    # Evalúa si la cadena es de 10 caracteres 
    if not len(cadena) == 10:
        validar = False

    if validar:
        for caracter in cadena[:9]: # Revisa solo los primeros 9 caracteres de la cadena
            if not caracter.isdigit(): # Revisa si el carácter es un número 
                validar = False # En caso que no sea un número la bandera cambia de estado y se rompe el ciclo
                break
            valor_peso = int(caracter) * peso # Se convierte el carácter en un número para ser multiplicado
            suma_pesos = suma_pesos + valor_peso # Se suma el valor del peso en la suma_pesos
            peso-=1
    
    if validar:
        ultimo_digito = cadena[-1] # Guarda el último valor de la cadena
        if ultimo_digito == "X": # Evalúa si el último carácter es una "X"
            suma_pesos = suma_pesos + 10 # La "X" final vale 10 (regla ISBN-10)
        elif ultimo_digito.isdigit(): # Evalúa que el último carácter sea un número
            suma_pesos = suma_pesos + int(ultimo_digito) # En caso de que no sea "X" y sea un número se suma a suma_pesos
        else:
            validar = False # Si el último carácter no es una "X" ni es un número la bandera cambia a False

    if validar:
        if not suma_pesos % 11 == 0: # Evalúa que el residuo de la división sea cero
            validar = False

    return validar

def is_valid_isbn13(cadena_limpia):
    cadena = cadena_limpia
    validar = True # Bandera para controlar el flujo
    valor_peso = 0 # Variable para almacenar un producto
    switch = 0 # Variable para alternar entre pesos
    suma_pesos = 0 # Variable para obtener el valor total de los pesos

    # Evalúa si la cadena es de 13 caracteres
    if not len(cadena) == 13:
        validar = False

    if validar:
        for caracter in cadena:
            if not caracter.isdigit(): # Comprueba si el carácter es un número
                validar = False # En caso que no sea un número la bandera cambia de estado y se rompe el ciclo
                break
            if switch == 0: # Switch para multiplicar por el peso '1'
                valor_peso = int(caracter) * 1
                switch = 1 # Cambia de estado el switch para la siguiente vuelta
            elif switch == 1: # Switch para multiplicar por el peso '3'
                valor_peso = int(caracter) * 3
                switch = 0 # Cambia de estado el switch para la siguiente vuelta
            suma_pesos = suma_pesos + valor_peso
    
    if validar:
        if not suma_pesos % 10 == 0: # Evalúa que el residuo de la división sea cero
            validar = False
    
    return validar

def detect_isbn(cadena):
    cadena_n = cadena
    cadena_limpia = normalize_isbn(cadena_n)
    veredicto = "" # Variable que almacena el resultado

    if is_valid_isbn10(cadena_limpia):
        veredicto = "ISBN-10"
    elif is_valid_isbn13(cadena_limpia):
        veredicto = "ISBN-13"
    else:
        veredicto = "INVALID"
    
    return veredicto

cadena = input(str("Ingrese el isbn: "))
print(detect_isbn(cadena))
