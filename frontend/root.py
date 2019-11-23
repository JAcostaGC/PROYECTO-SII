# coding: utf-8

import Tkinter as tk
from program_constants import *
from frontend.main import Main, Registro, DatosAlumnos, DatosProfesor, \
    RegistroMateriaAlumno, RegistroMateriaProfesor


class Root(tk.Tk):

    """
    Proporciona una ventana raiz acondicionada y reutilizable
    """
    def __init__(self, icono="", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Uso de la clase Wm (Window Manager) para configurar la ventana a nuestro gusto.
        self.geometry(ProgramConstants.TAMANO_PANTALLA)
        self.configure(bg=ProgramConstants.BLANCO)
        self.resizable(0, 0)  # Evita que se pueda maximizar la ventana
        self.title(ProgramConstants.TITULO)

        # Para evitar que el programa no se abra por falta del icono
        try:
            self.iconbitmap(icono)
        except tk.TclError:
            print 'Icono no encontrado'

        # Contenedores
        self.contenedor = tk.Frame(self)
        self.contenedor.config(height=700, width=1366)
        self.contenedor.pack(fill="both", expand=True)

        self.frames = {}
        for F in (Main, Registro, DatosAlumnos, DatosProfesor,
                  RegistroMateriaAlumno, RegistroMateriaProfesor):
            frame = F(parent=self.contenedor, controller=self)
            self.frames[F] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
