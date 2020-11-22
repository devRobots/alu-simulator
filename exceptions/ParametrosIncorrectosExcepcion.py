class ParametrosIncorrectosExcepcion(Exception):
    """
    Clase de Excepcion de cantidad de parametros
    """

    def __init__(self, operacion, cant_params):
        """
        Clase de Excepcion de cantidad de parametros

        Parameters:
            operacion(str): Nombre de la operacion,
            cant_params(int): Cantidad de parametros de la operacion
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
        Metodo toString
        """
        return self.error
