# coding: utf-8
from ..root import *
from Tkinter import *

class Cuadro_Sesion:
    """
    El cuadro de inicio de sesión.

    Contiene dos radio button para determinar si eres estudiante o profesor.
    Cajas de ingreso personalizadas.
    Y un botón personalizado para ingresar.
    """

    def __init__(self, ventana, cuadro, boton1):
        self.__cuadro_sesion(ventana)

    def __cuadro_sesion(self, ventana):
        """
        Se crea un rectangulo como una imagen.
        :param ventana: La ventana root donde se despliega toda la aplicación
        :return: Un rectangulo donde se conjugan las herramientas necesarioas para iniciar sesión
        """
        canvas = Canvas(ventana, width=452, height=469,
                        highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        cuadro = PhotoImage()