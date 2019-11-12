# coding: utf-8

from ..root import *


class Cuadro_Registro:
    """
    Un rectangulo sencillo que pregunta si aún no tienes cuenta.
    """

    def __init__(self, ventana):
        self._cuadro_registro(ventana)
        self.__texto__(ventana)

    def _cuadro_registro(self, ventana):
        # Recuadro de registro
        canvas = Canvas(ventana, width=452, height=100,
                        highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        rectangulo_registro = PhotoImage(file="frontend/recursos/rectangulo2.gif")
        ventana.rectangulo_registro = rectangulo_registro
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor=NW, image=rectangulo_registro)
        canvas.place(x=614 ,y=593)

    def __texto__(self, ventana):
        texto_principal = Label(ventana, text="¿No tienes una cuenta?")
        texto_principal.place(x=674, y=629)
        texto_principal.config(
            anchor=NW,
            background=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            height=1,
            width=23
        )

        texto_registro = Label(ventana, text="Regístrate")
        texto_registro.place(x=897, y=629)
        texto_registro.config(
            anchor=NW,
            background=ProgramConstants.BLANCO_BLANCO,
            cursor="hand2",
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.AZUL_MARINO,
            height=1,
            width=10
        )

        # texto_registro.bind("<Button-1>", lambda e: __texto_registro__(ventana))
