# coding: utf-8

from ..componentes_basicos.cabecera import *
from ..componentes_basicos.escudo import *
from cuadro_sesion import *

class Main:

    """
    Pantalla de inicio de sesión.
    """

    def __init__(self, ventana, logotec, logoitm, cuadro, boton1, boton2):

        # Cabecera
        cabecera = Cabecera(ventana, logotec)

        # Escudo escuela
        escudo = Escudo(ventana, logoitm)

        # Cuadro inicio sesión
        cuadro_inicio_sesion = Cuadro_Sesion(ventana, cuadro, boton1)
