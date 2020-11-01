import random as rnd


stack = {
    "01h": "0b00000000",
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
acum = "0b0"


def operacion_div(params):
    """
    Metodo que divide 2 posiciones de memoria y
    los guarda en la primera
    """
    if len(params) == 2:
        dir1 = stack.get(params[0])
        dir2 = stack.get(params[1])

        if not dir1 or not dir2:
            raise Exception("No se reconoce la direccion de memoria")

        a = int(dir1, 2)
        b = int(dir2, 2)

        res = to_bin(a // b)
        stack[params[0]] = res
        acum = res
    else:
        raise Exception("La operacion DIV recibe 2 parametros")


def operacion_neg(params):
    """
    Metodo que cambia el signo de una direccion
    de memoria
    """
    if len(params) == 1:
        dir = stack.get(params[0])

        if not dir:
            raise Exception("No se reconoce la direccion de memoria")

        pos = int(dir, 2)
        neg = to_bin(~pos)

        stack[params[0]] = neg
        acum = neg
    else:
        raise Exception("La operacion NEG recibe 1 parametro")


def procesar(instruccion):
    """
    Metodo que procesa la entrada del usuario
    """
    instruccion_cut = instruccion.split()

    switch = {
        "div": operacion_div,
        "neg": operacion_neg,
        # "and": operacion_and,
        # "or": operacion_or,
        # "add": operacion_add,
    }

    comando = instruccion_cut[0]
    func = switch.get(comando)

    if func:
        parametros = instruccion_cut[1:]
        try:
            func(parametros)
        except Exception as err:
            print("Error: " + str(err))
    else:
        print("Comando desconocido")


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

        instruccion = leer().lower().strip()
        if instruccion.startswith("exit"):
            break

        procesar(instruccion)


def leer():
    """
    Metodo que lee la entrada del usuario
    """
    return input("ALU > ")


if __name__ == "__main__":
    generar_stack()
    menu()
