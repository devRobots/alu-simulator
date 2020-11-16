"""
Hola
"""


class ParametrosIncorrectosExcepcion(Exception):
    """
    Clase de Excepcion de cantidad de parametros
    """

    def __init__(self, operacion, cant_params):
        """
        Clase de Excepcion de cantidad de parametros

        Parameters:
            operacion (str): hola xd
            cant_params (int): xd
        """
        self.error = "La operacion %s " % operacion
        if cant_params:
            self.error += "recibe %d parametro" % cant_params

            if cant_params > 1:
                self.error += "s"
        else:
            self.error += "no requiere parametros"

    def __str__(self):
        """
        docstring
        """
        return self.error
