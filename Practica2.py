# Funciones para trabajar con diccionarios

def agregar_clave_valor(diccionario, clave, valor):
    """Agrega una nueva clave y su valor al diccionario."""
    diccionario[clave] = valor  # Asigna el valor a la clave en el diccionario
    print(f"Parámetros: {diccionario}, Clave: {clave}, Valor: {valor}")
    return diccionario  # Devuelve el diccionario actualizado

def eliminar_clave(diccionario, clave):
    """Elimina una clave del diccionario."""
    if clave in diccionario:
        del diccionario[clave]  # Elimina la clave si existe
    print(f"Parámetros: {diccionario}, Clave: {clave}")
    return diccionario  # Devuelve el diccionario actualizado

def modificar_valor(diccionario, clave, nuevo_valor):
    """Cambia el valor de una clave existente en el diccionario."""
    if clave in diccionario:
        diccionario[clave] = nuevo_valor  # Modifica el valor de la clave
        print(f"Parámetros: {diccionario}, Clave: {clave}, Nuevo Valor: {nuevo_valor}")
        return True  # Indica que la modificación fue exitosa
    print(f"Parámetros: {diccionario}, Clave: {clave}, Nuevo Valor: {nuevo_valor} - Modificación fallida")
    return False  # Indica que la modificación falló

def combinar_diccionarios(dic1, dic2):
    """Combina dos diccionarios en uno nuevo."""
    resultado = {**dic1, **dic2}  # Combina los dos diccionarios
    print(f"Parámetros: Diccionario 1: {dic1}, Diccionario 2: {dic2}")
    return resultado  # Devuelve el nuevo diccionario combinado

# Funciones para trabajar con conjuntos

def agregar_a_conjunto(conjunto, elemento):
    """Agrega un elemento a un conjunto."""
    conjunto.add(elemento)  # Agrega el elemento al conjunto
    print(f"Parámetros: {conjunto}, Elemento a agregar: {elemento}")
    return True  # Indica que la adición fue exitosa

def eliminar_de_conjunto(conjunto, elemento):
    """Elimina un elemento de un conjunto."""
    if elemento in conjunto:
        conjunto.remove(elemento)  # Elimina el elemento si existe
        print(f"Parámetros: {conjunto}, Elemento eliminado: {elemento}")
        return True  # Indica que la eliminación fue exitosa
    print(f"Parámetros: {conjunto}, Elemento: {elemento} - Eliminación fallida")
    return False  # Indica que la eliminación falló

def combinar_conjuntos(conjunto1, conjunto2):
    """Combina dos conjuntos en uno nuevo."""
    resultado = conjunto1.union(conjunto2)  # Combina los dos conjuntos
    print(f"Parámetros: Conjunto 1: {conjunto1}, Conjunto 2: {conjunto2}")
    return resultado  # Devuelve el nuevo conjunto combinado

def diferencia_conjuntos(conjunto1, conjunto2):
    """Devuelve la diferencia entre dos conjuntos."""
    resultado = conjunto1.difference(conjunto2)  # Calcula la diferencia
    print(f"Parámetros: Conjunto 1: {conjunto1}, Conjunto 2: {conjunto2}")
    return resultado  # Devuelve el conjunto resultante

# Funciones para trabajar con tuplas

def agregar_a_tupla(tupla, elemento):
    """Agrega un elemento a una tupla, creando una nueva."""
    nueva_tupla = tupla + (elemento,)  # Crea una nueva tupla con el elemento agregado
    print(f"Parámetros: {tupla}, Elemento a agregar: {elemento}")
    return nueva_tupla  # Devuelve la nueva tupla

def eliminar_de_tupla(tupla, elemento):
    """Elimina un elemento de una tupla, creando una nueva."""
    if elemento in tupla:
        nueva_tupla = tuple(x for x in tupla if x != elemento)  # Crea una nueva tupla sin el elemento
        print(f"Parámetros: {tupla}, Elemento eliminado: {elemento}")
        return nueva_tupla  # Devuelve la nueva tupla
    print(f"Parámetros: {tupla}, Elemento: {elemento} - Eliminación fallida")
    return tupla  # Devuelve la tupla original si no se eliminó nada

def concatenar_tuplas(tupla1, tupla2):
    """Concatena dos tuplas en una nueva."""
    nueva_tupla = tupla1 + tupla2  # Crea una nueva tupla concatenando las dos
    print(f"Parámetros: Tupla 1: {tupla1}, Tupla 2: {tupla2}")
    return nueva_tupla  # Devuelve la nueva tupla

def revertir_tupla(tupla):
    """Revierte el orden de una tupla, creando una nueva."""
    nueva_tupla = tupla[::-1]  # Crea una nueva tupla con el orden invertido
    print(f"Parámetros: {tupla}")
    return nueva_tupla  # Devuelve la nueva tupla

# Funciones para imprimir estructuras

def imprimir_diccionario(diccionario):
    """Imprime el contenido de un diccionario."""
    print(f"Diccionario: {diccionario}")

def imprimir_tupla(tupla):
    """Imprime el contenido de una tupla."""
    print(f"Tupla: {tupla}")

def imprimir_conjunto(conjunto):
    """Imprime el contenido de un conjunto."""
    print(f"Conjunto: {conjunto}")

# Importar Flask
from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Definir las rutas
@app.route('/')
def bienvenido():
    """Ruta principal que muestra un mensaje de bienvenida."""
    return 'Bienvenido'

@app.route('/wellcome')
def bienvenido_simple():
    """Ruta que muestra un mensaje de bienvenida simple."""
    return 'Bienvenido'

@app.route('/wellcome/nombre/<name>')
def bienvenido_nombre(name):
    """Ruta que muestra un mensaje de bienvenida personalizado con el nombre."""
    return f'Bienvenido {name}'

@app.route('/wellcome/control/<int:ncontrol>')
def bienvenido_control(ncontrol):
    """Ruta que muestra el número de control recibido."""
    return f'El número recibido es: {ncontrol}'

@app.route('/wellcome/nombre/<name>/control/<int:ncontrol>')
def bienvenido_nombre_control(name, ncontrol):
    """Ruta que muestra un mensaje de bienvenida con el nombre y el número de control."""
    return f'Bienvenido {name}, tu número de control es: {ncontrol}'

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración
