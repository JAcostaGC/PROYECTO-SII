# coding: utf-8

from ..root import *


class Main(tk.Frame):
    """
    Pantalla de inicio de sesión.
    Contiene:
    - Cabecera
    - Escudo
    - Cuadro inicio sesión
    - Cuadro de registro
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii()
        self._escudo()
        self.__cuadro_sesion(controller)
        # self._radio_buttons()
        self._cajas_texto_(controller, "No. Control:")
        # self.boton_sesion(controller)
        self._cuadro_registro()
        self.__texto__(controller)

    def __imagen_tecnm(self):
        # Imagen TECNM
        # highlightthickness quita el borde gris
        canvas = tk.Canvas(self, width=334, height=147, highlightthickness=0)
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def _escudo(self):
        # highlightthickness quita el borde gris
        canvas = tk.Canvas(self, width=370, height=386, highlightthickness=0)
        canvas.pack()
        itm = tk.PhotoImage(file="frontend/recursos/itmatamoros.gif")
        self.itm = itm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=itm)
        canvas.place(x=213, y=166)

    def __cuadro_sesion(self, controller):
        """
        Se crea un rectangulo como una imagen.
        :return: Un rectangulo donde se conjugan las herramientas necesarioas para iniciar sesión
        """
        # highlightthickness quita el borde gris
        canvas = tk.Canvas(self, width=452, height=469, highlightthickness=0)
        canvas.pack()
        cuadro_blanco = tk.PhotoImage(file="frontend/recursos/rectangulo.gif")
        self.cuadro_blanco = cuadro_blanco
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=cuadro_blanco)
        canvas.place(x=614, y=114)

        # RadioButton (soy alumno/soy profesor)
        soy_alumno = tk.StringVar()
        self._radio_buttons(controller, soy_alumno)

    def _radio_buttons(self, controller, opcion):
        """
        Para que se tenga un comportamiento propio para el radio button.
        Hay que asegurarnos que todos los botones estén agrupados en un punto a
        la misma variable, y usar el parámetro value para especificar representa
        cada uno.
        :param opcion: Es la variable de soy alumno o soy profesor.
        :return: Conjunto de radio buttons (soy alumno / soy profesor)
        """
        opcion.set("alumno")

        alumno = tk.Radiobutton(self, variable=opcion, value="alumno")
        profesor = tk.Radiobutton(self, variable=opcion, value="profesor")
        alumno.place(x=647, y=153)
        profesor.place(x=821, y=153)
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.
        alumno_imagen_deseleccionado = tk.PhotoImage(file='frontend/recursos/soyalumno2.gif')
        self.alumno_imagen_deseleccionado = alumno_imagen_deseleccionado

        alumno_imagen_seleccionado = tk.PhotoImage(file='frontend/recursos/soyalumno1.gif')
        self.alumno_imagen_seleccionado = alumno_imagen_seleccionado

        profesor_imagen_deseleccionado = tk.PhotoImage(file='frontend/recursos/soyprofesor2.gif')
        self.profesor_imagen_deseleccionado = profesor_imagen_deseleccionado

        profesor_imagen_seleccionado = tk.PhotoImage(file='frontend/recursos/soyprofesor1.gif')
        self.profesor_imagen_seleccionado = profesor_imagen_seleccionado

        alumno.config(
            indicatoron=False,
            image=alumno_imagen_deseleccionado,
            command=lambda: self._cambiar_cajatexto(controller, opcion),
            bg=ProgramConstants.BLANCO_BLANCO,
            height=34,
            width=160,
            activebackground=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            highlightbackground=ProgramConstants.BLANCO_BLANCO,
            highlightcolor=ProgramConstants.BLANCO_BLANCO,
            highlightthickness=0,
            offrelief=tk.FLAT,
            relief=tk.FLAT,
            selectcolor=ProgramConstants.BLANCO_BLANCO,
            selectimage=alumno_imagen_seleccionado
        )

        profesor.config(
            indicatoron=False,
            image=profesor_imagen_deseleccionado,
            command=lambda: self._cambiar_cajatexto(controller, opcion),
            bg=ProgramConstants.BLANCO_BLANCO,
            height=34,
            width=169,
            activebackground=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            highlightbackground=ProgramConstants.BLANCO_BLANCO,
            highlightcolor=ProgramConstants.BLANCO_BLANCO,
            highlightthickness=0,
            offrelief=tk.FLAT,
            relief=tk.FLAT,
            selectcolor=ProgramConstants.BLANCO_BLANCO,
            selectimage=profesor_imagen_seleccionado,
        )

    def _cambiar_cajatexto(self, controller, opcion):
        """
        Dependiendo de qué opción esté seleccionada se
        cambiará la primera caja de texto
        :param opcion: la opción del radio button
        :return: No. Control Ó Usuario
        """
        resultado = " "
        if opcion.get() == "alumno":
            resultado = "No. Control:"
        elif opcion.get() == "profesor":
            resultado = "Usuario:"

        self._cajas_texto_(controller, resultado)

    def _cajas_texto_(self, controller, tipouser):
        """
        Las cajas de texto personalizadas para que se ingrese usuario
        y contraseña
        :param tipouser: El tipo de usuario que se está manejando.
        :return: Las cajas de texto.
        """

        # Borde de la caja de usuario(ya que no se puede cambiar)
        borde_usuario = tk.Canvas(self, width=412, height=28, highlightthickness=0)
        borde_usuario.pack()
        borde_usuario.create_rectangle(
            633, 254,  # x1, y1
            1045, 286,  # x2, y2
            width=1,
            outline=ProgramConstants.GRIS_CEMENTO,
            fill=ProgramConstants.BLANCO
        )
        borde_usuario.place(x=633, y=254)

        # Caja de texto usuario/no. control
        global entrada_usuario
        entrada_usuario = tk.StringVar()
        vcmd = self.register(self.validate)
        global tipo_usuario
        tipo_usuario = tipouser
        usuario_sesion = tk.Entry(self, textvariable=entrada_usuario, validate='all',
                           validatecommand=(vcmd, "%S"))
        entrada_usuario.set(tipouser)
        usuario_sesion.place(x=634, y=255)
        usuario_sesion.bind("<Button-1>", lambda e=entrada_usuario: self.__on_click_user__(e))

        usuario_sesion.config(
            background=ProgramConstants.BLANCO,
            borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            insertbackground=ProgramConstants.GRIS,
            width=34,  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
        )

        # Borde de la caja de NIP (ya que no se puede cambiar)
        borde_password = tk.Canvas(self, width=412, height=28,
                                   highlightthickness=0)
        borde_password.pack()
        borde_password.create_rectangle(
            633, 333,  # x1, y1
            1045, 365,  # x2, y2
            width=1,
            outline=ProgramConstants.GRIS_CEMENTO,
            fill=ProgramConstants.BLANCO
        )
        borde_password.place(x=633, y=333)

        # Caja de texto de NIP
        global entrada_nip
        entrada_nip = tk.StringVar()
        global nip_sesion
        nip_sesion = tk.Entry(self, textvariable=entrada_nip, validate='all',
                           validatecommand=(vcmd, "%S"))
        entrada_nip.set("NIP:")
        nip_sesion.place(x=634, y=334)
        nip_sesion.bind("<Button-1>", lambda e=entrada_nip, t=tipouser: self.__on_click_password1__(e, t))

        nip_sesion.config(
            background=ProgramConstants.BLANCO,
            borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            insertbackground=ProgramConstants.GRIS,
            width=34  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
        )

        self.boton_sesion(controller, tipouser)

    def validate(self, char):
        if tipo_usuario == "No. Control:":
            return char in "0123456789"
        else:
            pass

    def __on_click_user__(self, e):
        if entrada_usuario.get() == "No. Control:" or entrada_usuario.get() == "Usuario:":
            entrada_usuario.set("")
        else:
            pass
        if entrada_nip.get() == "":
            entrada_nip.set("NIP:")
            nip_sesion.config(show="")

    def __on_click_password1__(self, e, t):
        # Se muestra NIP: correctamente, y cuando das click y pasa 1ms las letras se ponen en "▪"
        nip_sesion.after(1, lambda: nip_sesion.config(show="▪"))

        if entrada_nip.get() == "NIP:":
            nip_sesion.config(show="")
            entrada_nip.set("")
        else:
            pass

        if entrada_usuario.get() == "":
            entrada_usuario.set(t)
            nip_sesion.config(show="▪")

    def boton_sesion(self, controller, usuario):
        """
        Coloca el botón de inicio de sesión
        :return: El botón para iniciar sesión
        """
        # Se crea el botón como una imagen.
        # Si das click en el botón y se cumplen las verificaciones
        # se muestra otra pantalla.

        # Imagen botón
        canvas = tk.Canvas(self, width=406, height=69,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_imagen = tk.PhotoImage(file="frontend/recursos/boton1.gif")
        self.boton_imagen = boton_imagen
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_imagen)
        canvas.place(x=633, y=495)
        canvas.config(cursor="hand2")

        # VALIDACIÓN EN LA BASE DE DATOS
        # canvas.bind("<Button-1>", lambda v: )
        if usuario == "No. Control:":
            canvas.bind("<Button-1>", lambda e, c=controller: self.__boton_sesion_alumno__(c))
        elif usuario == "Usuario:":
            canvas.bind("<Button-1>", lambda e, c=controller: self.__boton_sesion_profesor__(c))
        # CÓDIGO TEMPORAL
        # Te deja entrar no importa lo que ingreses.

    def _cuadro_registro(self):
        # Recuadro de registro
        canvas = tk.Canvas(self, width=452, height=100,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        rectangulo_registro = tk.PhotoImage(file="frontend/recursos/rectangulo2.gif")
        self.rectangulo_registro = rectangulo_registro
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=rectangulo_registro)
        canvas.place(x=614, y=593)

    def __texto__(self, controller):
        self.controller = controller
        texto_principal = tk.Label(self, text="¿No tienes una cuenta?")
        texto_principal.place(x=674, y=629)
        texto_principal.config(
            anchor='nw',
            background=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            height=1,
            width=23
        )

        texto_registro = tk.Label(self, text="Regístrate")
        texto_registro.place(x=897, y=629)
        texto_registro.config(
            anchor='nw',
            background=ProgramConstants.BLANCO_BLANCO,
            cursor="hand2",
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.AZUL_MARINO,
            height=1,
            width=10
        )

        texto_registro.bind("<Button-1>", lambda e, c=controller: self.__texto_sesion__(c))

    def __texto_sesion__(self, c):
        self.c = c
        c.show_frame(Registro)

    def __boton_sesion_alumno__(self, c):
        self.c = c
        c.show_frame(DatosAlumnos)

    def __boton_sesion_profesor__(self, c):
        self.c = c
        c.show_frame(DatosProfesor)


class Registro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii()
        self._escudo()
        self.__cuadro_sesion()
        # self._radio_buttons()
        self._cajas_texto_("No. Control:")
        self.boton_sesion()
        self._cuadro_registro()
        self.__texto__(controller)

    def __imagen_tecnm(self):
        # Imagen TECNM
        canvas = tk.Canvas(self, width=334, height=147,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def _escudo(self):
        # highlightthickness quita el borde gris
        canvas = tk.Canvas(self, width=370, height=386, highlightthickness=0)
        canvas.pack()
        itm = tk.PhotoImage(file="frontend/recursos/itmatamoros.gif")
        self.itm = itm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=itm)
        canvas.place(x=213, y=166)

    def __cuadro_sesion(self):
        """
        Se crea un rectangulo como una imagen.
        :return: Un rectangulo donde se conjugan las herramientas necesarioas para iniciar sesión
        """
        # highlightthickness quita el borde gris
        canvas = tk.Canvas(self, width=452, height=469, highlightthickness=0)
        canvas.pack()
        cuadro_blanco = tk.PhotoImage(file="frontend/recursos/rectangulo.gif")
        self.cuadro_blanco = cuadro_blanco
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=cuadro_blanco)
        canvas.place(x=614, y=114)

        # RadioButton (soy alumno/soy profesor)
        soy_alumno = tk.StringVar()
        self._radio_buttons(soy_alumno)

    def _radio_buttons(self, opcion):
        """
        Para que se tenga un comportamiento propio para el radio button.
        Hay que asegurarnos que todos los botones estén agrupados en un punto a
        la misma variable, y usar el parámetro value para especificar representa
        cada uno.
        :param opcion: Es la variable de soy alumno o soy profesor.
        :return: Conjunto de radio buttons (soy alumno / soy profesor)
        """
        opcion.set("alumno")

        alumno = tk.Radiobutton(self, variable=opcion, value="alumno")
        profesor = tk.Radiobutton(self, variable=opcion, value="profesor")
        alumno.place(x=647, y=153)
        profesor.place(x=821, y=153)

        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.
        alumno_imagen_deseleccionado = tk.PhotoImage(file='frontend/recursos/soyalumno2.gif')
        self.alumno_imagen_deseleccionado = alumno_imagen_deseleccionado

        alumno_imagen_seleccionado = tk.PhotoImage(file='frontend/recursos/soyalumno1.gif')
        self.alumno_imagen_seleccionado = alumno_imagen_seleccionado

        profesor_imagen_deseleccionado = tk.PhotoImage(file='frontend/recursos/soyprofesor2.gif')
        self.profesor_imagen_deseleccionado = profesor_imagen_deseleccionado

        profesor_imagen_seleccionado = tk.PhotoImage(file='frontend/recursos/soyprofesor1.gif')
        self.profesor_imagen_seleccionado = profesor_imagen_seleccionado

        alumno.config(
            indicatoron=False,
            image=alumno_imagen_deseleccionado,
            command=lambda: self._cambiar_cajatexto(opcion),
            bg=ProgramConstants.BLANCO_BLANCO,
            height=34,
            width=160,
            activebackground=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            highlightbackground=ProgramConstants.BLANCO_BLANCO,
            highlightcolor=ProgramConstants.BLANCO_BLANCO,
            highlightthickness=0,
            offrelief=tk.FLAT,
            relief=tk.FLAT,
            selectcolor=ProgramConstants.BLANCO_BLANCO,
            selectimage=alumno_imagen_seleccionado
        )

        profesor.config(
            indicatoron=False,
            image=profesor_imagen_deseleccionado,
            command=lambda: self._cambiar_cajatexto(opcion),
            bg=ProgramConstants.BLANCO_BLANCO,
            height=34,
            width=169,
            activebackground=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            highlightbackground=ProgramConstants.BLANCO_BLANCO,
            highlightcolor=ProgramConstants.BLANCO_BLANCO,
            highlightthickness=0,
            offrelief=tk.FLAT,
            relief=tk.FLAT,
            selectcolor=ProgramConstants.BLANCO_BLANCO,
            selectimage=profesor_imagen_seleccionado,
        )

    def _cambiar_cajatexto(self, opcion):
        """
        Dependiendo de qué opción esté seleccionada se
        cambiará la primera caja de texto
        :param opcion: la opción del radio button
        :return: No. Control Ó Usuario
        """
        resultado = " "
        if opcion.get() == "alumno":
            resultado = "No. Control:"
        elif opcion.get() == "profesor":
            resultado = "Usuario:"

        self._cajas_texto_(resultado)

    def _cajas_texto_(self, tipouser):
        """
        Las cajas de texto personalizadas para que se ingrese usuario
        y contraseña
        :param tipouser: El tipo de usuario que se está manejando.
        :return: Las cajas de texto.
        """

        # Borde de la caja de usuario(ya que no se puede cambiar)
        borde_usuario_registro = tk.Canvas(self, width=412, height=28, highlightthickness=0)
        borde_usuario_registro.pack()
        borde_usuario_registro.create_rectangle(
            633, 254,  # x1, y1
            1045, 286,  # x2, y2
            width=1,
            outline=ProgramConstants.GRIS_CEMENTO,
            fill=ProgramConstants.BLANCO
        )
        borde_usuario_registro.place(x=633, y=254)

        # Caja de texto usuario/no. control
        global entrada_usuario_registro
        entrada_usuario_registro = tk.StringVar()
        vcmd = self.register(self.validate)
        global tipo_usuario
        tipo_usuario = tipouser
        usuario_registro = tk.Entry(self, textvariable=entrada_usuario_registro, validate='all',
                           validatecommand=(vcmd, "%S"))
        entrada_usuario_registro.set(tipouser)
        usuario_registro.place(x=634, y=255)
        usuario_registro.bind("<Button-1>", lambda e=entrada_usuario_registro: self.__on_click_user_registro__(e))

        usuario_registro.config(
            background=ProgramConstants.BLANCO,
            borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            insertbackground=ProgramConstants.GRIS,
            width=34,  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
        )

        # Borde de la caja de NIP (ya que no se puede cambiar)
        borde_password = tk.Canvas(self, width=412, height=28,
                                   highlightthickness=0)
        borde_password.pack()
        borde_password.create_rectangle(
            633, 333,  # x1, y1
            1045, 365,  # x2, y2
            width=1,
            outline=ProgramConstants.GRIS_CEMENTO,
            fill=ProgramConstants.BLANCO
        )
        borde_password.place(x=633, y=306)

        # Caja de texto de NIP
        global entrada_nip_registro
        entrada_nip_registro = tk.StringVar()
        global nip_registro
        nip_registro = tk.Entry(self, textvariable=entrada_nip_registro, validate='all',
                                validatecommand=(vcmd, "%S"))
        entrada_nip_registro.set("NIP:")
        nip_registro.place(x=634, y=307)
        nip_registro.bind("<Button-1>", lambda e=entrada_nip_registro, t=tipouser: self.__on_click_password_registro__(e, t))

        nip_registro.config(
            background=ProgramConstants.BLANCO,
            borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            insertbackground=ProgramConstants.GRIS,
            width=34  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
        )

        # Borde de la caja de Nombre completo (ya que no se puede cambiar)
        borde_nombre_registro = tk.Canvas(self, width=412, height=28, highlightthickness=0)
        borde_nombre_registro.pack()
        borde_nombre_registro.create_rectangle(
            633, 358,
            1045, 384,
            width=1,
            outline=ProgramConstants.GRIS_CEMENTO,
            fill=ProgramConstants.BLANCO
        )
        borde_nombre_registro.place(x=633, y=358)

        # Caja de texto Nombre completo.
        global caja_nombre_registro
        global entrada_nombre_registro
        entrada_nombre_registro = tk.StringVar()
        caja_nombre_registro = tk.Entry(self, textvariable=entrada_nombre_registro)
        entrada_nombre_registro.set("Nombre completo:")
        caja_nombre_registro.place(x=634, y=359)

        caja_nombre_registro.config(
            background=ProgramConstants.BLANCO,
            borderwidth=0,  # Quitamos el borde porque por defecto está muy feo.
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            insertbackground=ProgramConstants.GRIS,
            width=34  # La cantidad de caracteres que se pueden visualizar en la caja de texto.
        )

        caja_nombre_registro.bind("<Button-1>", lambda tipo=tipouser: self.__on_click_name_registro__(tipo))


    def validate(self, char):
        if tipo_usuario == "No. Control:":
            return char in "0123456789"
        else:
            pass

    def __on_click_user_registro__(self, e):
        if entrada_usuario_registro.get() == "No. Control:" or entrada_usuario_registro.get() == "Usuario:":
            entrada_usuario_registro.set("")
        else:
            pass
        if entrada_nip_registro.get() == "":
            entrada_nip_registro.set("NIP:")
            nip_registro.config(show="")
        if entrada_nombre_registro.get() == "":
            entrada_nombre_registro.set("Nombre completo:")

    def __on_click_password_registro__(self, e, t):
        # Se muestra NIP: correctamente, y cuando das click y pasa 1ms las letras se ponen en "▪"
        nip_registro.after(1, lambda: nip_registro.config(show="▪"))
        if entrada_nip_registro.get() == "NIP:":
            nip_registro.config(show="")
            entrada_nip_registro.set("")
        else:
            pass

        if entrada_usuario_registro.get() == "":
            entrada_usuario_registro.set(t)
            nip_registro.config(show="▪")

        if entrada_nombre_registro.get() == "":
            entrada_nombre_registro.set("Nombre completo:")

    def __on_click_name_registro__(self, tipo):
        if entrada_nombre_registro.get() == "Nombre completo:":
            entrada_nombre_registro.set("")
        else:
            pass

        if entrada_usuario_registro.get() == "":
            entrada_usuario_registro.set(tipo_usuario)

        if entrada_nip_registro.get() == "":
            entrada_nip_registro.set("NIP:")
            nip_registro.config(show="")

    def boton_sesion(self):
        """
        Coloca el botón de inicio de sesión
        :return: El botón para iniciar sesión
        """
        # Se crea el botón como una imagen.
        # Si das click en el botón y se cumplen las verificaciones
        # se muestra otra pantalla.

        # Imagen botón
        canvas = tk.Canvas(self, width=406, height=69,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_imagen = tk.PhotoImage(file="frontend/recursos/boton2.gif")
        self.boton_imagen = boton_imagen
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_imagen)
        canvas.place(x=633, y=495)

        # VALIDACIÓN EN LA BASE DE DATOS
        # canvas.bind("<Button-1>", lambda v: )

        # CÓDIGO TEMPORAL
        # Te deja entrar no importa lo que ingreses.

    def _cuadro_registro(self):
        # Recuadro de registro
        canvas = tk.Canvas(self, width=452, height=100,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        rectangulo_registro = tk.PhotoImage(file="frontend/recursos/rectangulo2.gif")
        self.rectangulo_registro = rectangulo_registro
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=rectangulo_registro)
        canvas.place(x=614, y=593)

    def __texto__(self, controller):
        self.controller = controller
        texto_principal = tk.Label(self, text="¿Ya tienes una cuenta?")
        texto_principal.place(x=674, y=629)
        texto_principal.config(
            anchor='nw',
            background=ProgramConstants.BLANCO_BLANCO,
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
            height=1,
            width=23
        )

        texto_registro = tk.Label(self, text="Inicia Sesión")
        texto_registro.place(x=897, y=629)
        texto_registro.config(
            anchor='nw',
            background=ProgramConstants.BLANCO_BLANCO,
            cursor="hand2",
            borderwidth=0,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.AZUL_MARINO,
            height=1,
            width=10
        )

        texto_registro.bind("<Button-1>", lambda e, c=controller: self.__texto_registro__(c))

    def __texto_registro__(self, c):
        self.c = c
        c.show_frame(Main)


class DatosAlumnos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm(controller)
        self.__label_sii(controller)
        self.__cabecera_tabla__()
        self.__boton_registrar_materia__(controller)

    def __imagen_tecnm(self, controller):
        # Imagen TECNM
        canvas = tk.Canvas(self, width=334, height=147,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self, controller):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def __datos_alumno__(self):
        pass

    def __cabecera_tabla__(self):
        """
        La cabecera de las calificaciones.
        :return:
        """
        canvas = tk.Canvas(self, width=630, height=42,
                           highlightthickness=0) # highlightthickness quita el borde gris
        canvas.pack()
        cabecera_tabla = tk.PhotoImage(file="frontend/recursos/cabeceraalumno.gif")
        self.cabecera_tabla = cabecera_tabla
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=cabecera_tabla)
        canvas.place(x=368, y=237)

    def __datos_tabla__(self):
        pass

    def __boton_registrar_materia__(self, controller):
        """
        Botón que lleva a la pantalla para registrar una materia
        en la reticula.
        :return: El botón para registrar materia en imagen.
        """
        canvas = tk.Canvas(self, width=210, height=36,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_registrar_img = tk.PhotoImage(file="frontend/recursos/registrarmateria.gif")
        self.boton_registrar_img = boton_registrar_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_registrar_img)
        canvas.place(x=917, y=648)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_registro_materias__(controller))

    def __ir_registro_materias__(self, controller):
        self.controller = controller
        controller.show_frame(RegistroMateriaAlumno)

    def __boton_cerrar_sesion__(self):
        pass


class DatosProfesor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii(controller)

    def __imagen_tecnm(self):
        # Imagen TECNM
        canvas = tk.Canvas(self, width=334, height=147,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self, controller):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def __datos_profesor__(self):
        pass

    # defl


class RegistroMateriaAlumno(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii(controller)

    def __imagen_tecnm(self):
        # Imagen TECNM
        canvas = tk.Canvas(self, width=334, height=147,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self, controller):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)


class RegistroMateriaProfesor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii(controller)

    def __imagen_tecnm(self):
        # Imagen TECNM
        canvas = tk.Canvas(self, width=334, height=147,
                           highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        tecnm = tk.PhotoImage(file="frontend/recursos/tecnm.gif")
        self.tecnm = tecnm  # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=tecnm)
        canvas.place(x=0, y=0)

    def __label_sii(self, controller):
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)
