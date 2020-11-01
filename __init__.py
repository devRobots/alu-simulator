import random as rnd


stack = []
flags = {"SF": 0, "ZF": 0, "OF": 0}


def procesar(instruccion):
    """
    Metodo que procesa la entrada del usuario
    """
    instruccion_cut = instruccion.split()
    comando = instruccion_cut[0]
    parametros = instruccion_cut[1:]

    switch = {
        """
        Ejemplo de uso:
        "AND": operacion_and,
        "OR" : operacion_or,
        "ADD": operacion_add,
        ...
        
        Llama a un metodo llamado "operacion_and"
        Lo selecciona teniendo en cuenta que
        el usuario ingreso una instruccion que
        empieza por la palabra "AND"

        NOTA: Todos los metodos reciben como parametros
        una lista de strings con todo lo demas que el
        usuario haya escrito

        NOTA 2: Eliminar esto cuando lo hayas terminado de leer
        """
    }

    try:
        func = switch[comando]
        func(parametros)
    except:
        print("Comando desconocido!")


def generar_stack():
    """
    Metodo que genera el stack de forma aletaria
    """
    for i in range(6):
        stack.append(bin(rnd.randint(0, 15)))


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

        instruccion = leer().upper().strip()
        if instruccion:
            if instruccion.startswith("EXIT"):
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
