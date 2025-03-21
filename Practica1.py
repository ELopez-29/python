def agregar_clave_valor(diccionario, clave, valor):
    """Agrega una nueva clave y su valor al diccionario."""
    diccionario[clave] = valor
    print(f"Parámetros: {diccionario}, Clave: {clave}, Valor: {valor}")
    return diccionario

"""Elimina una clave del diccionario."""
def eliminar_clave(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    print(f"Parámetros: {diccionario}, Clave: {clave}")
    return diccionario

def modificar_valor(diccionario, clave, nuevo_valor):
    """Cambia el valor de una clave existente en el diccionario."""
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print(f"Parámetros: {diccionario}, Clave: {clave}, Nuevo Valor: {nuevo_valor}")
        return True
    print(f"Parámetros: {diccionario}, Clave: {clave}, Nuevo Valor: {nuevo_valor} - Modificación fallida")
    return False

def combinar_diccionarios(dic1, dic2):
    """Combina dos diccionarios en uno nuevo."""
    resultado = {**dic1, **dic2}
    print(f"Parámetros: Diccionario 1: {dic1}, Diccionario 2: {dic2}")
    return resultado

def agregar_a_conjunto(conjunto, elemento):
    """Agrega un elemento a un conjunto."""
    conjunto.add(elemento)
    print(f"Parámetros: {conjunto}, Elemento a agregar: {elemento}")
    return True

def eliminar_de_conjunto(conjunto, elemento):
    """Elimina un elemento de un conjunto."""
    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"Parámetros: {conjunto}, Elemento eliminado: {elemento}")
        return True
    print(f"Parámetros: {conjunto}, Elemento: {elemento} - Eliminación fallida")
    return False

def combinar_conjuntos(conjunto1, conjunto2):
    """Combina dos conjuntos en uno nuevo."""
    resultado = conjunto1.union(conjunto2)
    print(f"Parámetros: Conjunto 1: {conjunto1}, Conjunto 2: {conjunto2}")
    return resultado

def diferencia_conjuntos(conjunto1, conjunto2):
    """Devuelve la diferencia entre dos conjuntos."""
    resultado = conjunto1.difference(conjunto2)
    print(f"Parámetros: Conjunto 1: {conjunto1}, Conjunto 2: {conjunto2}")
    return resultado

def agregar_a_tupla(tupla, elemento):
    """Agrega un elemento a una tupla, creando una nueva."""
    nueva_tupla = tupla + (elemento,)
    print(f"Parámetros: {tupla}, Elemento a agregar: {elemento}")
    return nueva_tupla

def eliminar_de_tupla(tupla, elemento):
    """Elimina un elemento de una tupla, creando una nueva."""
    if elemento in tupla:
        nueva_tupla = tuple(x for x in tupla if x != elemento)
        print(f"Parámetros: {tupla}, Elemento eliminado: {elemento}")
        return nueva_tupla
    print(f"Parámetros: {tupla}, Elemento: {elemento} - Eliminación fallida")
    return tupla

def concatenar_tuplas(tupla1, tupla2):
    """Concatena dos tuplas en una nueva."""
    nueva_tupla = tupla1 + tupla2
    print(f"Parámetros: Tupla 1: {tupla1}, Tupla 2: {tupla2}")
    return nueva_tupla

"""Revierte el orden de una tupla, creando una nueva."""
def revertir_tupla(tupla):
    nueva_tupla = tupla[::-1]
    print(f"Parámetros: {tupla}")
    return nueva_tupla

"""Imprime el diccionario."""
def imprimir_diccionario(diccionario):
    print(f"Diccionario: {diccionario}")

"""Imprime la tupla."""
def imprimir_tupla(tupla):
    print(f"Tupla: {tupla}")

"""Imprime el conjunto."""
def imprimir_conjunto(conjunto):
    print(f"Conjunto: {conjunto}")
