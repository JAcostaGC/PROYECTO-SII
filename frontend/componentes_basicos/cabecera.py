# coding: utf-8

from ..root import *
from Tkinter import *


class Cabecera:
    """
    Proporciona la cabecera principal de el programa.
    Consta de la imagen del TecNM y una etiqueta (SII)
    """

    def __init__(self, ventana, logotec):
        # Imagen TECNM
        self.__imagen_tecnm(ventana, logotec)
        # Label SII
        self.__label_sii(ventana)

    def __imagen_tecnm(self, ventana, logotec):
        # Imagen TECNM
        canvas = Canvas(ventana, width=334, height=147,
                        highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = PhotoImage(file=logotec)
        ventana.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor=NW, image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self, ventana):
        # Label SII
        texto = Label(ventana, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                      fg=ProgramConstants.AZUL_MARINO,
                      font=ProgramConstants.FUENTE_NEGRITAS_21,
                      bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)
