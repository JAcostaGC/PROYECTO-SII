# coding: utf-8

from ..root import *


# class Datos_Profesor(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
#         # Cabecera
#         self.__imagen_tecnm()
#         self.__label_sii(controller)
#
#     def __imagen_tecnm(self):
#         # Imagen TECNM
#         canvas = tk.Canvas(self, width=334, height=147,
#                            highlightthickness=0)  # highlightthickness quita el borde gris
#         canvas.pack()
#         tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
#         self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
#         # basura de python no lo elimine.
#         # prueba eliminando la línea y verás que la imagen no se carga.
#
#         # Es muy diferente la posición en create_image() y place()
#         # La posición en create_image() hace referencia a la posición DENTRO
#         # del CANVAS.
#         # La posición en place() hace referencia a la posición DENTRO
#         # de la VENTANA.
#         canvas.create_image(0, 0, anchor='nw', image=tecnm)
#         canvas.place(x=0, y=0)
#
#     def __label_sii(self, controller):
#         # Label SII
#         texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
#                          fg=ProgramConstants.AZUL_MARINO,
#                          font=ProgramConstants.FUENTE_NEGRITAS_21,
#                          bg=ProgramConstants.BLANCO, )
#         texto.config(height=1, width=31)
#         texto.place(x=588, y=37)