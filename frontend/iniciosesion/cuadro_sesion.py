# # coding: utf-8
# from main import *
#
#
# class Cuadro_Sesion:
#     """
#     El cuadro de inicio de sesión.
#
#     Contiene dos radio button para determinar si eres estudiante o profesor.
#     Cajas de ingreso personalizadas.
#     Y un botón personalizado para ingresar.
#     """
#
#     def __init__(self, ventana, cuadro, boton1):
#         self.__cuadro_sesion(ventana, cuadro)
#         self._cajas_texto_(ventana, "No. Control:")
#         self.boton_sesion(ventana, boton1)
#
#     def __cuadro_sesion(self, ventana, cuadro):
#         """
#         Se crea un rectangulo como una imagen.
#         :param ventana: La ventana root donde se despliega toda la aplicación
#         :return: Un rectangulo donde se conjugan las herramientas necesarioas para iniciar sesión
#         """
#         canvas = Canvas(ventana, width=452, height=469,
#                         highlightthickness=0)  # highlightthickness quita el borde gris
#         canvas.pack()
#         cuadro_blanco = PhotoImage(file=cuadro)
#         ventana.cuadro_blanco = cuadro_blanco
#         # Se llama de nuevo a la imagen para que el recolector de
#         # basura de python no lo elimine.
#         # prueba eliminando la línea y verás que la imagen no se carga.
#
#         # Es muy diferente la posición en create_image() y place()
#         # La posición en create_image() hace referencia a la posición DENTRO
#         # del CANVAS.
#         # La posición en place() hace referencia a la posición DENTRO
#         # de la VENTANA.
#         canvas.create_image(0, 0, anchor=NW, image=cuadro_blanco)
#         canvas.place(x=614, y=114)
#
#         # RadioButton (soy alumno/soy profesor)
#         soy_alumno = StringVar()
#         self._radio_buttons(ventana, soy_alumno)
#
#     def _radio_buttons(self, ventana, opcion):
#         """
#         Para que se tenga un comportamiento propio para el radio button.
#         Hay que asegurarnos que todos los botones estén agrupados en un punto a
#         la misma variable, y usar el parámetro value para especificar representa
#         cada uno.
#         :param ventana: La ventana raíz donde se colocarán los elementos.
#         :param opcion: Es la variable de soy alumno o soy profesor.
#         :return: Conjunto de radio buttons (soy alumno / soy profesor)
#         """
#         opcion.set("alumno")
#
#         alumno = Radiobutton(ventana, variable=opcion,
#                              value="alumno")
#         profesor = Radiobutton(ventana, variable=opcion,
#                                value="profesor")
#         alumno.place(x=647, y=153)
#         profesor.place(x=821, y=153)
#
#         # Se llama de nuevo a la imagen para que el recolector de
#         # basura de python no lo elimine.
#         # prueba eliminando la línea y verás que la imagen no se carga.
#         alumno_imagen_deseleccionado = PhotoImage(file='frontend/recursos/soyalumno2.gif')
#         ventana.alumno_imagen_deseleccionado = alumno_imagen_deseleccionado
#
#         alumno_imagen_seleccionado = PhotoImage(file='frontend/recursos/soyalumno1.gif')
#         ventana.alumno_imagen_seleccionado = alumno_imagen_seleccionado
#
#         profesor_imagen_deseleccionado = PhotoImage(file='frontend/recursos/soyprofesor2.gif')
#         ventana.profesor_imagen_deseleccionado = profesor_imagen_deseleccionado
#
#         profesor_imagen_seleccionado = PhotoImage(file='frontend/recursos/soyprofesor1.gif')
#         ventana.profesor_imagen_seleccionado = profesor_imagen_seleccionado
#
#         alumno.config(
#             indicatoron=False,
#             image=alumno_imagen_deseleccionado,
#             command=lambda: self._cambiar_cajatexto(ventana, opcion),
#             bg=ProgramConstants.BLANCO_BLANCO,
#             height=34,
#             width=160,
#             activebackground=ProgramConstants.BLANCO_BLANCO,
#             borderwidth=0,
#             highlightbackground=ProgramConstants.BLANCO_BLANCO,
#             highlightcolor=ProgramConstants.BLANCO_BLANCO,
#             highlightthickness=0,
#             offrelief=FLAT,
#             relief=FLAT,
#             selectcolor=ProgramConstants.BLANCO_BLANCO,
#             selectimage=alumno_imagen_seleccionado
#         )
#
#         profesor.config(
#             indicatoron=False,
#             image=profesor_imagen_deseleccionado,
#             command=lambda: self._cambiar_cajatexto(ventana, opcion),
#             bg=ProgramConstants.BLANCO_BLANCO,
#             height=34,
#             width=169,
#             activebackground=ProgramConstants.BLANCO_BLANCO,
#             borderwidth=0,
#             highlightbackground=ProgramConstants.BLANCO_BLANCO,
#             highlightcolor=ProgramConstants.BLANCO_BLANCO,
#             highlightthickness=0,
#             offrelief=FLAT,
#             relief=FLAT,
#             selectcolor=ProgramConstants.BLANCO_BLANCO,
#             selectimage=profesor_imagen_seleccionado,
#         )
#
#     def _cambiar_cajatexto(self, ventana, opcion):
#         """
#         Dependiendo de qué opción esté seleccionada se
#         cambiará la primera caja de texto
#         :param opcion: la opción del radio button
#         :return: No. Control Ó Usuario
#         """
#         resultado = " "
#         if opcion.get() == "alumno":
#             resultado = "No. Control:"
#         elif opcion.get() == "profesor":
#             resultado = "Usuario:"
#
#         self._cajas_texto_(ventana, resultado)
#
#     def _cajas_texto_(self, ventana, tipouser):
#         """
#         Las cajas de texto personalizadas para que se ingrese usuario
#         y contraseña
#         :param ventana: la ventana donde se va a mostrar.
#         :param tipouser: El tipo de usuario que se está manejando.
#         :return: Las cajas de texto.
#         """
#
#         # Borde de la caja de usuario(ya que no se puede cambiar)
#         borde_usuario = Canvas(ventana, width=412, height=32,
#                                highlightthickness=0)
#         borde_usuario.pack()
#         borde_usuario.create_rectangle(
#             633, 254,  # x1, y1
#             1045, 286,  # x2, y2
#             width=1,
#             outline=ProgramConstants.GRIS_CEMENTO,
#             fill=ProgramConstants.BLANCO
#         )
#         borde_usuario.place(x=633, y=254)
#
#         # Caja de texto usuario/no. control
#         global entrada_usuario
#         entrada_usuario = StringVar()
#         vcmd = ventana.register(self.validate)
#         global tipo_usuario
#         tipo_usuario = tipouser
#         usuario = Entry(ventana, textvariable=entrada_usuario, validate='all',
#                         validatecommand=(vcmd, "%S"))
#         entrada_usuario.set(tipouser)
#         usuario.place(x=634, y=255)
#         usuario.bind("<Button-1>", lambda e=entrada_usuario: self.__on_click_user__(e))
#
#         usuario.config(
#             background=ProgramConstants.BLANCO,
#             borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
#             font=ProgramConstants.FUENTE_REGULAR_16,
#             foreground=ProgramConstants.GRIS,
#             insertbackground=ProgramConstants.GRIS,
#             width=34,  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
#         )
#
#         # Borde de la caja de NIP (ya que no se puede cambiar)
#         borde_password = Canvas(ventana, width=412, height=32,
#                                highlightthickness=0)
#         borde_password.pack()
#         borde_password.create_rectangle(
#             633, 333,  # x1, y1
#             1045, 365,  # x2, y2
#             width=1,
#             outline=ProgramConstants.GRIS_CEMENTO,
#             fill=ProgramConstants.BLANCO
#         )
#         borde_password.place(x=633, y=333)
#
#         # Caja de texto de NIP
#         global entrada_nip
#         entrada_nip = StringVar()
#         global nip
#         nip = Entry(ventana, textvariable=entrada_nip)
#         entrada_nip.set("NIP:")
#         nip.place(x=634, y=334)
#         nip.bind("<Button-1>", lambda e=entrada_nip, t=tipouser: self.__on_click_password__(e, t))
#
#         nip.config(
#             background=ProgramConstants.BLANCO,
#             borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
#             font=ProgramConstants.FUENTE_REGULAR_16,
#             foreground=ProgramConstants.GRIS,
#             insertbackground=ProgramConstants.GRIS,
#             width=34  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
#         )
#
#     def validate(self, char):
#         if tipo_usuario == "No. Control:":
#             return char in "0123456789"
#         else:
#             pass
#
#     def __on_click_user__(self, e):
#         if entrada_usuario.get() == "No. Control:" or entrada_usuario.get() == "Usuario:":
#             entrada_usuario.set("")
#         else:
#             pass
#         if entrada_nip.get() == "":
#             entrada_nip.set("NIP:")
#             nip.config(show="")
#
#     def __on_click_password__(self, e, t):
#         # Se muestra NIP: correctamente, y cuando das click y pasa 1ms las letras se ponen en "▪"
#         nip.after(1, lambda: nip.config(show="▪"))
#
#         if entrada_nip.get() == "NIP:":
#             nip.config(show="")
#             entrada_nip.set("")
#         else:
#             pass
#
#         if entrada_usuario.get() == "":
#             entrada_usuario.set(t)
#             nip.config(show="▪")
#
#     def boton_sesion(self, ventana, boton1):
#         """
#         Coloca el botón de inicio de sesión
#         :param ventana: La ventana donde se despliega el boton
#         :param boton1: La imagen del botón
#         :return: El botón para iniciar sesión
#         """
#         # Se crea el botón como una imagen.
#         # Si das click en el botón y se cumplen las verificaciones
#         # se muestra otra pantalla.
#
#         # Imagen botón
#         canvas = Canvas(ventana, width=406, height=69,
#                         highlightthickness=0)  # highlightthickness quita el borde gris
#         canvas.pack()
#         boton_imagen = PhotoImage(file=boton1)
#         ventana.boton_imagen = boton_imagen
#         # Se llama de nuevo a la imagen para que el recolector de
#         # basura de python no lo elimine.
#         # prueba eliminando la línea y verás que la imagen no se carga.
#
#         # Es muy diferente la posición en create_image() y place()
#         # La posición en create_image() hace referencia a la posición DENTRO
#         # del CANVAS.
#         # La posición en place() hace referencia a la posición DENTRO
#         # de la VENTANA.
#         canvas.create_image(0, 0, anchor=NW, image=boton_imagen)
#         canvas.place(x=633, y=495)
#
#         # VALIDACIÓN EN LA BASE DE DATOS
#         # canvas.bind("<Button-1>", lambda v: )
#
#         # CÓDIGO TEMPORAL
#         # Te deja entrar no importa lo que ingreses.
#
