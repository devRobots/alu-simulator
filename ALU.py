import os
import styles as st
import random as rnd
from exceptions import *

operaciones = [
    "DIV", "ADD", "SUB",
    "NEG", "AND", "OR",
    "RST", "EXIT"
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
    "SF": '0b0',  # SF = Resultado negativo
    "ZF": '0b0',  # ZF = Resultado cero
    "CF": '0b0'   # CF = Acarreo
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

        res = a // b

        if not res:
            flags["ZF"] = to_bin(1)

        res_bin = to_bin(res)
        stack[params[0]] = res_bin
    else:
        raise ParametrosIncorrectosExcepcion("DIV", 2)


def operacion_sub(params):
    """
    Metodo que resta 2 posiciones de memoria y
    guarda el resultado en la primera
    """
    if len(params) == 2:
        a = obtener_dir(params[0])
        b = obtener_dir(params[1])

        res = to_bin(a - b)
        stack[params[0]] = res
    else:
        raise ParametrosIncorrectosExcepcion("SUB", 2)


def operacion_add(params):
    """
    Metodo que suma 2 posiciones de memoria y
    guarda el resultado en la primera
    """
    if len(params) == 2:
        a = obtener_dir(params[0])
        b = obtener_dir(params[1])

        res = to_bin(a + b)
        stack[params[0]] = res
    else:
        raise ParametrosIncorrectosExcepcion("ADD", 2)


def operacion_neg(params):
    """
    Metodo que cambia el signo de una direccion
    de memoria
    """
    if len(params) == 1:
        pos = obtener_dir(params[0])
        neg = to_bin(~pos)
        stack[params[0]] = neg
        flags["SF"] = to_bin(1)
    else:
        raise ParametrosIncorrectosExcepcion("NEG", 1)


def operacion_and(params):
    """
    Metodo que realiza la operación AND entre 2 posiciones
    de memoria y guarda el resultado en la primera
    """
    if len(params) == 2:
        a = obtener_dir(params[0])
        b = obtener_dir(params[1])

        res = to_bin(a & b)
        stack[params[0]] = res
    else:
        raise ParametrosIncorrectosExcepcion("AND", 2)


def operacion_or(params):
    """
    Metodo que realiza la operación OR entre 2 posiciones
    de memoria y guarda el resultado en la primera
    """
    if len(params) == 2:
        a = obtener_dir(params[0])
        b = obtener_dir(params[1])

        res = to_bin(a | b)
        stack[params[0]] = res
    else:
        raise ParametrosIncorrectosExcepcion("OR", 2)


def reset(params):
    """
    Metodo que reinicia los valores y limpia la consola
    """
    if not params:
        os.system("cls" if os.name == 'nt' else "clear")
        generar_stack()
        mostrar_operaciones()
    else:
        raise ParametrosIncorrectosExcepcion("RST", 0)


def procesar(entrada):
    """
    Metodo que procesa la entrada del usuario
    """
    intrucciones = entrada.split()

    switch = {
        "DIV": operacion_div,
        "ADD": operacion_add,
        "SUB": operacion_sub,
        "NEG": operacion_neg,
        "AND": operacion_and,
        "OR": operacion_or,
        "RST": reset,
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
        print(st.ROJO + st.NEGRITA + "Error: " +
              st.NORMAL + st.ROJO + str(err) + st.RESET + "\n")


def generar_stack():
    """
    Metodo que genera el stack de forma aletaria
    """
    for key in stack.keys():
        stack[key] = to_bin(rnd.randint(0, (2**8)-1))

    for key in flags.keys():
        flags[key] = to_bin(0)


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


def mostrar_tabla():
    """
    Metodo que muestra la informacion del stack y los flags
    en formato de tabla
    """
    _border_format = st.CIAN + "%s" + st.RESET
    v = _border_format % "│"
    h = _border_format % "─"
    c = st.MORADO + "×" + st.RESET
    s = " "

    fila_inicio = (s * 6) + c + (h * 65) + c + (h * 32) + c + "\n"
    fila_titulos = (s * 6) + v + (s * 30) + st.VERDE + st.NEGRITA + \
        "Stack" + st.RESET + (s * 30) + v + (s * 14) + \
        st.VERDE + st.NEGRITA + "Flags" + st.RESET + (s * 13) + v + "\n"

    fila_separador = c + (h * 5) + c + (((h * 10) + c) * 9) + "\n"
    fila_dir = v + st.VERDE + st.NEGRITA + " Dir " + st.RESET + v + \
        (("   %s    " + v) * 6) + \
        (("    %s    " + v) * 3) + "\n"
    file_val = v + st.VERDE + st.NEGRITA + \
        " Val " + st.RESET + v + (" %s " + v) * 9 + "\n"

    dirs = list()
    vals = list()
    for k, v in dict(stack, **flags).items():
        dirs.append(st.NEGRITA + k + st.RESET)
        vals.append(v[2:])

    tabla = fila_inicio + fila_titulos + fila_separador + \
        (fila_dir % tuple(dirs)) + fila_separador + \
        (file_val % tuple(vals)) + fila_separador

    print(tabla)


def mostrar_operaciones():
    """
    Metodo que muestra las operaciones del programa
    """
    print(st.NEGRITA + st.AMARILLO + "OPERACIONES:", end=st.RESET)
    ops = operaciones
    for i in range(len(ops)):
        if i % 3 == 0:
            print()
        print(st.NEGRITA + st.AZUL + ops[i] +
              st.RESET + "\t" + to_bin(i), end="\t")
    print("\n")


def menu():
    """
    Metodo que muestra el menu principal de la app
    """
    mostrar_operaciones()
    while True:
        mostrar_tabla()
        prompt = st.MORADO + st.NEGRITA + "ALU > "
        print(prompt, end=st.RESET)
        instruccion = input().lower().strip()
        print()
        procesar(instruccion)


if __name__ == "__main__":
    generar_stack()
    menu()
