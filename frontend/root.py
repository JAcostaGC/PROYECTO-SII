# coding: utf-8

# from Tkinter import *
from program_constants import *
from iniciosesion.main import *


class Root:

    """
    Proporciona una ventana raiz acondicionada y reutilizable
    """

    def __init__(self, logotec, logoitm, cuadro, boton1, boton2, icono=""):
        # Ventana vacía.
        # Uso de la clase Wm (Window Manager) para configurar la ventana a nuestro gusto.
        ventana_raiz = Tk()
        ventana_raiz.geometry(ProgramConstants.TAMANO_PANTALLA)
        ventana_raiz.configure(bg=ProgramConstants.BLANCO)
        ventana_raiz.resizable(0, 0)  # Evita que se pueda maximizar la ventana
        ventana_raiz.title(ProgramConstants.TITULO)

        # Para evitar que el programa no se abra por falta del icono
        try:
            ventana_raiz.iconbitmap(icono)
        except TclError:
            print 'Icono no encontrado'

        # Ventana Principal de inicio de sesión
        main = Main(ventana_raiz, logotec, logoitm, cuadro, boton1, boton2)

        ventana_raiz.mainloop()
