from flask import Flask, json, request

app = Flask(__name__)

# Funciones de manejo

def agregar_clave_valor(diccionario, clave, valor):
    """Agrega una nueva clave y su valor al diccionario."""
    diccionario[clave] = valor
    return diccionario

def eliminar_clave(diccionario, clave):
    """Elimina una clave del diccionario."""
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

def modificar_valor(diccionario, clave, nuevo_valor):
    """Cambia el valor de una clave existente en el diccionario."""
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    return False

def combinar_diccionarios(dic1, dic2):
    """Combina dos diccionarios en uno nuevo."""
    return {**dic1, **dic2}

def agregar_a_conjunto(conjunto, elemento):
    """Agrega un elemento a un conjunto."""
    conjunto.add(elemento)
    return True

def eliminar_de_conjunto(conjunto, elemento):
    """Elimina un elemento de un conjunto."""
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    return False

def combinar_conjuntos(conjunto1, conjunto2):
    """Combina dos conjuntos en uno nuevo."""
    return conjunto1.union(conjunto2)

def diferencia_conjuntos(conjunto1, conjunto2):
    """Devuelve la diferencia entre dos conjuntos."""
    return conjunto1.difference(conjunto2)

def agregar_a_tupla(tupla, elemento):
    """Agrega un elemento a una tupla, creando una nueva."""
    return tupla + (elemento,)

def eliminar_de_tupla(tupla, elemento):
    """Elimina un elemento de una tupla, creando una nueva."""
    if elemento in tupla:
        return tuple(x for x in tupla if x != elemento)
    return tupla

def concatenar_tuplas(tupla1, tupla2):
    """Concatena dos tuplas en una nueva."""
    return tupla1 + tupla2

def revertir_tupla(tupla):
    """Revierte el orden de una tupla, creando una nueva."""
    return tupla[::-1]

# Rutas de Flask

@app.route("/agregar/<path:diccio>/<clave>/<valor>", methods=['POST'])
def agregar(diccio, clave, valor):
    """Ruta para agregar una clave y un valor a un diccionario."""
    diccionario = json.loads(diccio)  # Convierte el string JSON a un diccionario
    resultado = agregar_clave_valor(diccionario, clave, valor)  # Llama a la función para agregar
    return json.dumps(resultado)  # Devuelve el diccionario actualizado en formato JSON

@app.route("/eliminar/<path:diccio>/<clave>", methods=['DELETE'])
def eliminar(diccio, clave):
    """Ruta para eliminar una clave de un diccionario."""
    diccionario = json.loads(diccio)  # Convierte el string JSON a un diccionario
    resultado = eliminar_clave(diccionario, clave)  # Llama a la función para eliminar
    return json.dumps(resultado)  # Devuelve el diccionario actualizado en formato JSON

@app.route("/modificar/<path:diccio>/<clave>/<nuevo_valor>", methods=['PUT'])
def modificar(diccio, clave, nuevo_valor):
    """Ruta para modificar el valor de una clave existente en un diccionario."""
    diccionario = json.loads(diccio)  # Convierte el string JSON a un diccionario
    exito = modificar_valor(diccionario, clave, nuevo_valor)  # Llama a la función para modificar
    return json.dumps({"exito": exito})  # Devuelve un objeto JSON indicando el éxito de la modificación

@app.route("/combinar_diccionarios/<path:diccio1>/<path:diccio2>", methods=['POST'])
def combinar(diccio1, diccio2):
    """Ruta para combinar dos diccionarios."""
    diccionario1 = json.loads(diccio1)  # Convierte el primer string JSON a un diccionario
    diccionario2 = json.loads(diccio2)  # Convierte el segundo string JSON a un diccionario
    resultado = combinar_diccionarios(diccionario1, diccionario2)  # Llama a la función para combinar
    return json.dumps(resultado)  # Devuelve el diccionario combinado en formato JSON

@app.route("/agregar_conjunto/<path:conjunto>/<elemento>", methods=['POST'])
def agregar_elemento(conjunto, elemento):
    """Ruta para agregar un elemento a un conjunto."""
    conjunto = set(json.loads(conjunto))  # Convierte el string JSON a un conjunto
    resultado = agregar_a_conjunto(conjunto, elemento)  # Llama a la función para agregar
    return json.dumps({"exito": resultado, "conjunto": list(conjunto)})  # Devuelve el conjunto actualizado en formato JSON

@app.route("/eliminar_conjunto/<path:conjunto>/<elemento>", methods=['DELETE'])
def eliminar_elemento(conjunto, elemento):
    """Ruta para eliminar un elemento de un conjunto."""
    conjunto = set(json.loads(conjunto))  # Convierte el string JSON a un conjunto
    resultado = eliminar_de_conjunto(conjunto, elemento)  # Llama a la función para eliminar
    return json.dumps({"exito": resultado, "conjunto": list(conjunto)})  # Devuelve el conjunto actualizado en formato JSON

@app.route("/combinar_conjuntos/<path:conjunto1>/<path:conjunto2>", methods=['POST'])
def combinar_conjuntos_route(conjunto1, conjunto2):
    """Ruta para combinar dos conjuntos."""
    conjunto1 = set(json.loads(conjunto1))  # Convierte el primer string JSON a un conjunto
    conjunto2 = set(json.loads(conjunto2))  # Convierte el segundo string JSON a un conjunto
    resultado = combinar_conjuntos(conjunto1, conjunto2)  # Llama a la función para combinar
    return json.dumps(list(resultado))  # Devuelve el conjunto combinado en formato JSON

@app.route("/agregar_a_tupla/<path:tupla>/<elemento>", methods=['POST'])
def agregar_a_tupla_route(tupla, elemento):
    """Ruta para agregar un elemento a una tupla."""
    tupla = tuple(json.loads(tupla))  # Convierte el string JSON a una tupla
    nueva_tupla = agregar_a_tupla(tupla, elemento)  # Llama a la función para agregar
    return json.dumps(nueva_tupla)  # Devuelve la nueva tupla en formato JSON

@app.route("/eliminar_de_tupla/<path:tupla>/<elemento>", methods=['DELETE'])
def eliminar_de_tupla_route(tupla, elemento):
    """Ruta para eliminar un elemento de una tupla."""
    tupla = tuple(json.loads(tupla))  # Convierte el string JSON a una tupla
    nueva_tupla = eliminar_de_tupla(tupla, elemento)  # Llama a la función para eliminar
    return json.dumps(nueva_tupla)  # Devuelve la nueva tupla en formato JSON

@app.route("/concatenar_tuplas/<path:tupla1>/<path:tupla2>", methods=['POST'])
def concatenar_tuplas_route(tupla1, tupla2):
    """Ruta para concatenar dos tuplas."""
    tupla1 = tuple(json.loads(tupla1))  # Convierte el primer string JSON a una tupla
    tupla2 = tuple(json.loads(tupla2))  # Convierte el segundo string JSON a una tupla
    nueva_tupla = concatenar_tuplas(tupla1, tupla2)  # Llama a la función para concatenar
    return json.dumps(nueva_tupla)  # Devuelve la nueva tupla en formato JSON

@app.route("/revertir_tupla/<path:tupla>", methods=['GET'])
def revertir_tupla_route(tupla):
    """Ruta para revertir el orden de una tupla."""
    tupla = tuple(json.loads(tupla))  # Convierte el string JSON a una tupla
    nueva_tupla = revertir_tupla(tupla)  # Llama a la función para revertir
    return json.dumps(nueva_tupla)  # Devuelve la nueva tupla en formato JSON

# Ejecución de la aplicación
if __name__ == "__main__":
    app.run(debug=True)
