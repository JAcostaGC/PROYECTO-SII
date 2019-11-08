# coding: utf-8

# from ..root import *
from Tkinter import *


class Escudo:
    """
    Simplemente el escudo del Instituto Técnológico de Matamoros.
    """

    def __init__(self, ventana, logoitm):
        canvas = Canvas(ventana, width=370, height=386,
                        highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        itm = PhotoImage(file=logoitm)
        ventana.itm = itm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor=NW, image=itm)
        canvas.place(x=213, y=166)
