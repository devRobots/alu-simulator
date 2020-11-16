import os
import random as rnd
from exceptions import *

operaciones = [
    "DIV", "ADD", "SUB",
    "NEG", "AND", "OR",
    "CLR", "EXIT"
]
stack = {
    "01h": "0b0",
    "02h": "0b0",
    "03h": "0b0",
    "04h": "0b0",
    "05h": "0b0",
    "06h": "0b0"
}
flags = {
    "SF": 0,
    "ZF": 0,
    "OF": 0
}


def obtener_dir(dir):
    """
    Metodo que obtiene el valor de una
    direccion de memoria
    """
    mem = stack.get(dir)
    if not mem:
        raise DireccionDesconocidaExcepcion(dir)
    else:
        return int(mem, 2)


def operacion_div(params):
    """
    Metodo que divide 2 posiciones de memoria y
    guarda el resultado en la primera
    """
    if len(params) == 2:
        a = obtener_dir(params[0])
        b = obtener_dir(params[1])

        res = to_bin(a // b)
        stack[params[0]] = res
    else:
        raise ParametrosIncorrectosExcepcion("DIV", 2)


def operacion_neg(params):
    """
    Metodo que cambia el signo de una direccion
    de memoria
    """
    if len(params) == 1:
        pos = obtener_dir(params[0])
        neg = to_bin(~pos)
        stack[params[0]] = neg
    else:
        raise ParametrosIncorrectosExcepcion("NEG", 1)


def limpiar(params):
    """
    Metodo que limpia la consola
    """
    if not params:
        os.system("cls" if os.name == 'nt' else "cls")
    else:
        raise ParametrosIncorrectosExcepcion("CLR", 0)


def procesar(entrada):
    """
    Metodo que procesa la entrada del usuario
    """
    intrucciones = entrada.split()

    switch = {
        "DIV": operacion_div,
        # "ADD": operacion_add,
        # "SUB": operacion_sub,
        "NEG": operacion_neg,
        # "AND": operacion_and,
        # "OR": operacion_or,
        "CLR": limpiar,
        "EXIT": exit
    }

    try:
        operacion_bin = str(intrucciones[0])

        if len(operacion_bin) > 3 or not ('1' in operacion_bin or '0' in operacion_bin):
            raise OperacionDesconocidaExcepcion(operacion_bin)

        indice_operacion = int(operacion_bin, 2)
        operacion = operaciones[indice_operacion]
        operacion_func = switch.get(operacion)

        parametros = intrucciones[1:]
        operacion_func(parametros)
    except Exception as err:
        print("Error: " + str(err) + "\n")


def generar_stack():
    """
    Metodo que genera el stack de forma aletaria
    """
    for key in stack.keys():
        stack[key] = to_bin(rnd.randint(0, (2**8)-1))


def to_bin(n):
    """
    Metodo que convierte un numero a binario 
    y lo normaliza a una longitud de 8 bits
    """
    bin_raw = bin(n)
    b_index = bin_raw.index('b') + 1
    res = bin_raw[b_index:]
    while len(res) < 8:
        res = '0' + res
    res = '0b' + res
    return res


def menu():
    """
    Metodo que muestra el menu principal de la app
    """
    while True:
        print("Stack:")
        print(stack)
        print("Flags:")
        print(flags)
        print()

        instruccion = input("ALU > ").lower().strip()
        procesar(instruccion)


if __name__ == "__main__":
    generar_stack()
    menu()
