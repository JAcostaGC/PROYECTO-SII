# coding: utf-8

from frontend.root import *
import ttk  # Importa clases personalizadas de Tkinter
import pymongo  # Para conectar MongoDB con Python
import tkMessageBox as tkm


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        self.__imagen_tecnm()
        self.__label_sii()
        self._escudo()
        self.__cuadro_sesion(controller)
        self._cajas_texto_(controller, "No. Control:")
        self._cuadro_registro()
        self.__texto__(controller)

    def __imagen_tecnm(self):
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
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def _escudo(self):
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
            canvas.bind("<Button-1>", lambda e, c=controller: self._verificar_alumno(c))
        elif usuario == "Usuario:":
            canvas.bind("<Button-1>", lambda e, c=controller: self._verificar_profesor(c))
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

    def _verificar_alumno(self, controller):
        conexion = pymongo.MongoClient('localhost', 27017)
        mydb = conexion["escuela"]
        coleccionAlumno = mydb["alumno"]
        for x in coleccionAlumno.find({}, {"no_control": entrada_usuario.get(), "nip": entrada_nip.get()}):
            if x["no_control"] == entrada_usuario.get() and x["nip"] == entrada_nip.get():
                self.__boton_sesion_alumno__(controller)
                # dAlumnos = DatosAlumnos( controller)
                # dAlumnos.__datos_alumno__(x["no_control"], x["nip"])
            else:
                tkm.showerror("Usuario o contraseña incorrecta", "Ingresaste mal la contraseña o usuario")

    def _verificar_profesor(self, controller):
        conexion = pymongo.MongoClient('localhost', 27017)
        mydb = conexion["escuela"]
        coleccionProfesor = mydb["profesor"]
        for x in coleccionProfesor.find({}, {"usuario": entrada_usuario.get(), "nip": entrada_nip.get()}):
            if x["usuario"] == entrada_usuario.get() and x["nip"] == entrada_nip.get():
                self.__boton_sesion_profesor__(controller)
            else:
                tkm.showerror("Usuario o contraseña incorrecta", "Ingresaste mal la contraseña o usuario")


class Registro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii()
        self._escudo()
        self.__cuadro_sesion(parent, controller)
        self._cajas_texto_(parent, controller, "No. Control:")
        # self.boton_sesion()
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

    def __cuadro_sesion(self, parent, controller):
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
        self._radio_buttons(parent, controller, soy_alumno)

    def _radio_buttons(self, parent, controller, opcion):
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
            command=lambda: self._cambiar_cajatexto(parent, controller, opcion),
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
            command=lambda: self._cambiar_cajatexto(parent, controller, opcion),
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

    def _cambiar_cajatexto(self, parent, controller, opcion):
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

        self._cajas_texto_(parent, controller, resultado)

    def _cajas_texto_(self, parent, controller, tipouser):
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

        self.boton_sesion(parent, controller, tipouser)

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

    def boton_sesion(self, parent, controller, tipouser):
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
        canvas.config(cursor="hand2")
        # VALIDACIÓN EN LA BASE DE DATOS
        if tipouser == "No. Control:":
            canvas.bind("<Button-1>", lambda e: self._registrar_alumno())
        elif tipouser == "Usuario:":
            canvas.bind("<Button-1>", lambda e: self._registrar_profesor())

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

    def _registrar_alumno(self):
        alumno = {
            "no_control": entrada_usuario_registro.get(),
            "nip": entrada_nip_registro.get(),
            "nombre": entrada_nombre_registro.get(),
        }
        conexion = pymongo.MongoClient('localhost', 27017)
        mydb = conexion["escuela"]
        coleccionAlumno = mydb["alumno"]
        coleccionAlumno.insert_one(alumno)

    def _registrar_profesor(self):
        profesor = {
            "usuario": entrada_usuario_registro.get(),
            "nip": entrada_nip_registro.get(),
            "nombre": entrada_nombre_registro.get(),
            "materias": []
        }
        conexion = pymongo.MongoClient('localhost', 27017)
        mydb = conexion["escuela"]
        coleccionProfesor = mydb["profesor"]
        coleccionProfesor.insert_one(profesor)


class DatosAlumnos(tk.Frame):
    i = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm(controller)
        self.__label_sii(controller)
        self.__datos_alumno__("1", "test")
        self.__cabecera_tabla__()
        self.__datos_tabla__(controller)
        self.__boton_registrar_materia__(controller)
        self.__boton_cerrar_sesion__(controller)

    def __imagen_tecnm(self, controller):
        """
        La imagen de cabecera con el logo del tecnológico nacional de México.
        :param controller: El controlador de la ventana.
        :return: La imagen con el logo del TecNM.
        """
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
        """
        El título del programa Sistema Integral de Información(SII)
        :param controller: El controlador de la ventana.
        :return: Un texto que describe el titulo del programa.
        """
        # Label SII
        texto = tk.Label(self, text="SISTEMA INTEGRAL DE INFORMACIÓN",
                         fg=ProgramConstants.AZUL_MARINO,
                         font=ProgramConstants.FUENTE_NEGRITAS_21,
                         bg=ProgramConstants.BLANCO, )
        texto.config(height=1, width=31)
        texto.place(x=588, y=37)

    def __datos_alumno__(self, nControl, nombreAlumno):
        """
        Los datos traidos de MongoDB desplegados en forma de texto.
        :param controller: El controlador de la ventana.
        :return: Los datos del alumno.
        """
        cal_parciales = tk.Label(self, height=1, width=24, text="Calificaciones Parciales",
                                 fg=ProgramConstants.AZUL_MARINO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO)
        cal_parciales.place(x=547, y=104)
        # INICIO DE CODIGO TEMPORAL, POR MODIFICAR.
        no_control_label = tk.Label(self, height=1, width=24, text="No. De Control: " + nControl,
                                    fg=ProgramConstants.AZUL_MARINO,
                                    font=ProgramConstants.FUENTE_NEGRITAS_18,
                                    bg=ProgramConstants.BLANCO)
        no_control_label.place(x=547, y=138)
        nombre_label = tk.Label(self, height=1, width=33, text="Nombre: " + nombreAlumno,
                                fg=ProgramConstants.AZUL_MARINO,
                                font=ProgramConstants.FUENTE_NEGRITAS_18,
                                bg=ProgramConstants.BLANCO)
        nombre_label.place(x=479, y=172)
        # FIN DE CODIGO TEMPORAL, POR MODIFICAR.

    def __cabecera_tabla__(self):
        """
        La cabecera de las calificaciones con los nombres de las columnas.
        :return: Una imagen representando la cabecera de la tabla.
        """
        canvas = tk.Canvas(self, width=630, height=42,
                           highlightthickness=0)  # highlightthickness quita el borde gris
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

    def __datos_tabla__(self, controller):
        """
        Los datos de la tabla sacados de MongoDB.
        :param controller: El controlador de la ventana.
        :return: Los datos del nombre del profesor, grupo y calificación.
        """
        # FRAME CONTENEDOR DE LOS DATOS.
        canvas = tk.Canvas(self, width=630, height=318, highlightthickness=0)
        canvas.pack()
        marco_contenedor_img = tk.PhotoImage(file="frontend/recursos/bordecontenedor.gif")
        self.marco_contenedor_img = marco_contenedor_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=marco_contenedor_img)
        canvas.place(x=368, y=277)

        # INICIO DE LOS DATOS DE LA TABLA.

        # FIN DE LOS DATOS DE LA TABLA.

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

    def __boton_cerrar_sesion__(self, controller):
        """
        Botón que lleva al menú de inicio de sesión
        :return: Imagen simulando un botón.
        """
        canvas = tk.Canvas(self, width=192, height=36, highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_cerrarsesion_img = tk.PhotoImage(file="frontend/recursos/cerrarsesion.gif")
        self.boton_cerrarsesion_img = boton_cerrarsesion_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_cerrarsesion_img)
        canvas.place(x=1152, y=648)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_iniciosesion__(controller))

    def __ir_iniciosesion__(self, controller):
        self.controller = controller
        controller.show_frame(Main)


class DatosProfesor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        self.__imagen_tecnm()
        self.__label_sii(controller)
        self.__datos_profesores__(controller)
        self.__seleccion_materia__(controller)
        self.__registrar_materia__(controller)
        self.__cerrar_sesion__(controller)

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

    def __datos_profesores__(self, controller):
        """
        Los datos traidos por MongoDB desplegados en forma de texto.
        :param controller: El controlador de la ventana.
        :return: Los datos del profesor.
        """
        cal_parciales = tk.Label(self, height=1, width=24, text="Calificaciones Parciales",
                                 fg=ProgramConstants.AZUL_MARINO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO)
        cal_parciales.place(x=547, y=104)
        # INICIO DEL CODIGO TEMPORAL, POR MODIFICAR.
        global usuario
        usuario = "vhugobarnes"
        usuario_label = tk.Label(self, height=1, width=20, text="Usuario: " + usuario,
                                 fg=ProgramConstants.AZUL_MARINO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO)
        usuario_label.place(x=547, y=138)

        global nombreProfesor
        nombreProfesor = "Víctor Hugo Vázquez Gómez"
        nombreProfesor_label = tk.Label(self, height=1, width=33, text="Nombre: " + nombreProfesor,
                                        fg=ProgramConstants.AZUL_MARINO,
                                        font=ProgramConstants.FUENTE_NEGRITAS_18,
                                        bg=ProgramConstants.BLANCO)
        nombreProfesor_label.place(x=479, y=172)
        # FIN DEL CODIGO TEMPORAL, POR MODIFICAR.

    def __seleccion_materia__(self, controller):
        """
        El menú para que el profesor seleccione la materia que tenga registrada.
        Al iniciar se selecciona por defecto la primera materia en su lista de materias.
        Las materias se seleccionan por medio de un ComboBox.
        :param controller: El controlador de la ventana.
        :return: El ComboBox para elegir la materia.
        """
        borde_materia = tk.Canvas(self, width=1238, height=456, highlightthickness=0)
        borde_materia.pack()
        borde_materia_profesor_img = tk.PhotoImage(file="frontend/recursos/rectangulomainprofesor.gif")
        self.borde_materia_profesor_img = borde_materia_profesor_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        borde_materia.create_image(0, 0, anchor='nw', image=borde_materia_profesor_img)
        borde_materia.place(x=21, y=220)

        materia_label = tk.Label(self, height=1, width=7, text="Materia",
                                 fg=ProgramConstants.GRIS_OSCURO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO_BLANCO)
        materia_label.place(x=42, y=233)
        # INICIO DEL CODIGO TEMPORAL, POR MODIFICAR.
        global lista_materias
        lista_materias = ["Graficación", "Taller de Base de Datos"]
        self.materias_combobox = ttk.Combobox(self, state="readonly")
        self.materias_combobox["values"] = lista_materias
        self.materias_combobox.current(0)
        self.materias_combobox.place(x=145, y=236)
        self.materias_combobox.config(
            background=ProgramConstants.BLANCO,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
        )
        # current_subject = materias_combobox.get()
        self.materias_combobox.bind("<<ComboboxSelected>>", lambda e: self.__alumno_materia__(controller))

        # FINAL DEL CODIGO TEMPORAL, POR MODIFICAR

    def __alumno_materia__(self, controller):
        """
        El sub-menu que se abre al seleccionar una materia.
        Contiene los alumnos registrados en la materia.
        El profesor es capaz de insertar/actualizar calificaciones.
        :param controller: El controlador de la ventana.
        :return: El sub-menu que contiene los alumnos de la materia.
        """
        # MARCO SUB-MENU
        canvas = tk.Canvas(self, width=1169, height=352, highlightthickness=0)
        canvas.pack()
        borde_submenu_profesores_img = tk.PhotoImage(file="frontend/recursos/rectangulosubprofesor.gif")
        self.borde_submenu_profesores_img = borde_submenu_profesores_img
        canvas.create_image(0, 0, anchor='nw', image=borde_submenu_profesores_img)
        canvas.place(x=42, y=304)
        # INICIO DEL CODIGO TEMPORAL, POR MODIFICAR.
        # COMBO BOX
        global lista_alumnos
        lista_alumnos = ["Víctor Hugo Vázquez Gómez", "Nicole Rodriguez González"]
        self.alumnos_combobox = ttk.Combobox(self, state="readonly")
        self.alumnos_combobox["values"] = lista_alumnos
        self.alumnos_combobox.current(0)
        self.alumnos_combobox.place(x=56, y=326)
        self.alumnos_combobox.config(
            background=ProgramConstants.BLANCO,
            font=ProgramConstants.FUENTE_REGULAR_16,
            foreground=ProgramConstants.GRIS,
        )
        # LISTA DE CALIFICACIONES.
        self.lista_calificaciones = ["80", "80", "80", "80", "80", "80", "80"]
        self.alumnos_combobox.bind("<<ComboboxSelected>>", lambda e: self.__calificaciones_alumno__(controller))
        # FINAL DEL CODIGO TEMPORAL, POR MODIFICAR.

    def __calificaciones_alumno__(self, controller):
        """
        Se muestran las etiquetas junto sus Entry para almacenar/actualizar la
        información dentro de la base de datos.
        :param controller: El controlador de la ventana.
        :return: Las Label y Entry para almacenar las calificaciones, además del
                 botón para guardarlas.
        """
        # ETIQUETAS.
        unidad1_label = tk.Label(self, text="Unidad I",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad1_label.place(x=56, y=453)
        unidad2_label = tk.Label(self, text="Unidad II",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad2_label.place(x=56, y=502)
        unidad3_label = tk.Label(self, text="Unidad III",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad3_label.place(x=56, y=551)
        unidad4_label = tk.Label(self, text="Unidad IV",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad4_label.place(x=56, y=600)
        unidad5_label = tk.Label(self, text="Unidad V",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad5_label.place(x=356, y=453)
        unidad6_label = tk.Label(self, text="Unidad VI",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad6_label.place(x=356, y=502)
        unidad7_label = tk.Label(self, text="Unidad VII",
                                 fg=ProgramConstants.GRIS,
                                 font=ProgramConstants.FUENTE_REGULAR_16,
                                 bg=ProgramConstants.BLANCO)
        unidad7_label.place(x=356, y=551)
        # ENTRADAS.
        global unidad1, unidad2, unidad3, unidad4, unidad5, unidad6, unidad7
        vcmd = self.register(self.validate)

        unidad1 = tk.StringVar()
        unidad1_entry = tk.Entry(self, textvariable=unidad1, validate="all", validatecommand=(vcmd, "%S"))
        unidad1.set(self.lista_calificaciones[0])
        unidad1_entry.place(x=166, y=453)

        unidad2 = tk.StringVar()
        unidad2_entry = tk.Entry(self, textvariable=unidad2, validate="all", validatecommand=(vcmd, "%S"))
        unidad2.set(self.lista_calificaciones[1])
        unidad2_entry.place(x=166, y=502)

        unidad3 = tk.StringVar()
        unidad3_entry = tk.Entry(self, textvariable=unidad3, validate="all", validatecommand=(vcmd, "%S"))
        unidad3.set(self.lista_calificaciones[2])
        unidad3_entry.place(x=166, y=551)

        unidad4 = tk.StringVar()
        unidad4_entry = tk.Entry(self, textvariable=unidad4, validate="all", validatecommand=(vcmd, "%S"))
        unidad4.set(self.lista_calificaciones[3])
        unidad4_entry.place(x=166, y=600)

        unidad5 = tk.StringVar()
        unidad5_entry = tk.Entry(self, textvariable=unidad5, validate="all", validatecommand=(vcmd, "%S"))
        unidad5.set(self.lista_calificaciones[4])
        unidad5_entry.place(x=474, y=453)

        unidad6 = tk.StringVar()
        unidad6_entry = tk.Entry(self, textvariable=unidad6, validate="all", validatecommand=(vcmd, "%S"))
        unidad6.set(self.lista_calificaciones[5])
        unidad6_entry.place(x=474, y=502)

        unidad7 = tk.StringVar()
        unidad7_entry = tk.Entry(self, textvariable=unidad7, validate="all", validatecommand=(vcmd, "%S"))
        unidad7.set(self.lista_calificaciones[6])
        unidad7_entry.place(x=474, y=551)

        self.lista_parciales = [unidad1.get(), unidad2.get(), unidad3.get(), unidad4.get(), unidad5.get(),
                                unidad6.get(), unidad7.get()]

        # BOTÓN GUARDAR CALIFICACIONES.
        canvas = tk.Canvas(self, width=192, height=36, highlightthickness=0)
        canvas.pack()
        guardarcambios_img = tk.PhotoImage(file="frontend/recursos/guardarcambios.gif")
        self.guardarcambios_img = guardarcambios_img
        canvas.create_image(0, 0, anchor='nw', image=guardarcambios_img)
        canvas.place(x=916, y=579)
        canvas.config(cursor="hand2")
        # PENDIENTE POR MODIFICAR.
        # canvas.bind("<Button-1>", )

    def validate(self, char):
        return char in "0123456789'"

    def __registrar_materia__(self, controller):
        """
        Botón que lleva a la pantalla para registrar materias.
        :param controller:
        :return:
        """
        canvas = tk.Canvas(self, width=210, height=36, highlightthickness=0)
        canvas.pack()
        registrarmateria_profesor_img = tk.PhotoImage(file="frontend/recursos/registrarmateria.gif")
        self.registrarmateria_profesor_img = registrarmateria_profesor_img
        canvas.create_image(0, 0, anchor='nw', image=registrarmateria_profesor_img)
        canvas.place(x=916, y=652)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_escoger_materia__(controller))

    def __ir_escoger_materia__(self, controller):
        self.controller = controller
        controller.show_frame(RegistroMateriaProfesor)

    def __cerrar_sesion__(self, controller):
        """
        Botón que lleva a la página principal de inicio de sesión.
        :param controller: El controlador de la ventana.
        :return: El botón que lleva a Main
        """
        canvas = tk.Canvas(self, width=192, height=36, highlightthickness=0)
        canvas.pack()
        cerrarsesion_profesor_img = tk.PhotoImage(file="frontend/recursos/cerrarsesion.gif")
        self.cerrarsesion_profesor_img = cerrarsesion_profesor_img
        canvas.create_image(0, 0, anchor='nw', image=cerrarsesion_profesor_img)
        canvas.place(x=1151, y=652)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_iniciosesion__(controller))

    def __ir_iniciosesion__(self, controller):
        self.controller = controller
        controller.show_frame(Main)


class RegistroMateriaAlumno(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        # Cabecera
        self.__imagen_tecnm()
        self.__label_sii(controller)
        self.__datos_alumno__(controller)
        self.__cabecera_tabla__()
        self.__datos_tabla__(controller)
        self.__boton_ver_materias__(controller)
        self.__boton_cerrar_sesion__(controller)

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

    def __datos_alumno__(self, controller):
        """
        Los datos traidos de MongoDB desplegados en forma de texto.
        :param controller: El controlador de la ventana.
        :return: Los datos del alumno.
        """
        esc_materia = tk.Label(self, height=1, width=18, text="Escoge una materia",
                               fg=ProgramConstants.AZUL_MARINO,
                               font=ProgramConstants.FUENTE_NEGRITAS_18,
                               bg=ProgramConstants.BLANCO)
        esc_materia.place(x=534, y=104)
        # INICIO DE CODIGO TEMPORAL, POR MODIFICAR.
        global no_control2
        no_control2 = "17260628"
        no_control_label = tk.Label(self, height=1, width=24, text="No. De Control: " + no_control2,
                                    fg=ProgramConstants.AZUL_MARINO,
                                    font=ProgramConstants.FUENTE_NEGRITAS_18,
                                    bg=ProgramConstants.BLANCO)
        no_control_label.place(x=500, y=138)

        global nombre2
        nombre2 = "Víctor Hugo Vázquez Gómez"
        nombre_label = tk.Label(self, height=1, width=33, text="Nombre: " + nombre2,
                                fg=ProgramConstants.AZUL_MARINO,
                                font=ProgramConstants.FUENTE_NEGRITAS_18,
                                bg=ProgramConstants.BLANCO)
        nombre_label.place(x=445, y=172)
        # FIN DE CODIGO TEMPORAL, POR MODIFICAR.

    def __cabecera_tabla__(self):
        """
        La cabecera de las materias disponibles con los nombres de las
        columnas.
        :return: Imagen representando la cabecera.
        """
        canvas = tk.Canvas(self, width=366, height=40, highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        cabecera_tabla_img = tk.PhotoImage(file="frontend/recursos/cabeceraregistramateriaalumno.gif")
        self.cabecera_tabla_img = cabecera_tabla_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=cabecera_tabla_img)
        canvas.place(x=464, y=281)

    def __datos_tabla__(self, controller):
        """
        Los datos de la tabla sacados de MongoDB.
        :param controller: El controlador de la ventana.
        :return: Los nombres de los profesores y sus grupos.
        """
        # FRAME CONTENEDOR DE LOS DATOS.
        canvas = tk.Canvas(self, width=366, height=318, highlightthickness=0)
        canvas.pack()
        marco_contenedor_profesores_img = tk.PhotoImage(file="frontend/recursos/bordecontenedormaestros.gif")
        self.marco_contenedor_profesores_img = marco_contenedor_profesores_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=marco_contenedor_profesores_img)
        canvas.place(x=464, y=321)
        # INICIO DE LOS DATOS DE LA TABLA.

        # FIN DE LOS DATOS DE LA TABLA.

    def __boton_ver_materias__(self, controller):
        """
        Botón que te lleva a la ventana anterior para ver las materias que estás cursando.
        :param controller: El controlador de la ventana.
        :return: El botón como imagen con un bind para regresar a otro frame.
        """
        canvas = tk.Canvas(self, width=210, height=36, highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_ver_materias_img = tk.PhotoImage(file="frontend/recursos/vermaterias.gif")
        self.boton_ver_materias_img = boton_ver_materias_img
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_ver_materias_img)
        canvas.place(x=917, y=648)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_datos_alumnos__(controller))

    def __ir_datos_alumnos__(self, controller):
        self.controller = controller
        controller.show_frame(DatosAlumnos)

    def __boton_cerrar_sesion__(self, controller):
        """
        Botón que lleva al menú de inicio de sesión
        :return: Imagen simulando un botón.
        """
        canvas = tk.Canvas(self, width=192, height=36, highlightthickness=0)  # highlightthickness quita el borde gris
        canvas.pack()
        boton_cerrarsesion_ = tk.PhotoImage(file="frontend/recursos/cerrarsesion.gif")
        self.boton_cerrarsesion_ = boton_cerrarsesion_
        # Se llama de nuevo a la imagen para que el recolector de
        # basura de python no lo elimine.
        # prueba eliminando la línea y verás que la imagen no se carga.

        # Es muy diferente la posición en create_image() y place()
        # La posición en create_image() hace referencia a la posición DENTRO
        # del CANVAS.
        # La posición en place() hace referencia a la posición DENTRO
        # de la VENTANA.
        canvas.create_image(0, 0, anchor='nw', image=boton_cerrarsesion_)
        canvas.place(x=1152, y=648)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_menu_principal__(controller))

    def __ir_menu_principal__(self, controller):
        self.controller = controller
        controller.show_frame(Main)


class RegistroMateriaProfesor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=ProgramConstants.BLANCO, height=700, width=1366)
        self.__imagen_tecnm()
        self.__label_sii(controller)
        self.__datos_profesor__(controller)
        self.__cabecera_materias__(controller)
        self.__datos_materias__(controller)
        self.__ver_materias__(controller)
        self.__cerrar_sesion__(controller)

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

    def __datos_profesor__(self, controller):
        """
        Los datos traidos por MongoDB desplegados en forma de texto.
        :param controller: El controlador de la ventana.
        :return: Los datos del profesor.
        """
        cal_parciales = tk.Label(self, height=1, width=22, text="Selecciona una materia",
                                 fg=ProgramConstants.AZUL_MARINO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO)
        cal_parciales.place(x=547, y=104)
        # INICIO DEL CODIGO TEMPORAL, POR MODIFICAR.
        global usuario_vermaterias
        usuario_vermaterias = "vhugobarnes"
        usuario_label = tk.Label(self, height=1, width=20, text="Usuario: " + usuario_vermaterias,
                                 fg=ProgramConstants.AZUL_MARINO,
                                 font=ProgramConstants.FUENTE_NEGRITAS_18,
                                 bg=ProgramConstants.BLANCO)
        usuario_label.place(x=547, y=138)

        global nombreProfesor_vermaterias
        nombreProfesor_vermaterias = "Víctor Hugo Vázquez Gómez"
        nombreProfesor_label = tk.Label(self, height=1, width=33, text="Nombre: " + nombreProfesor_vermaterias,
                                        fg=ProgramConstants.AZUL_MARINO,
                                        font=ProgramConstants.FUENTE_NEGRITAS_18,
                                        bg=ProgramConstants.BLANCO)
        nombreProfesor_label.place(x=479, y=172)
        # FIN DEL CODIGO TEMPORAL, POR MODIFICAR.

    def __cabecera_materias__(self, controller):
        """
        La cabecera de la tabla para que el profesor escoja materia.
        :param controller: El controlador de la ventana.
        :return: La cabecera de la tabla.
        """
        canvas = tk.Canvas(self, width=366, height=40, highlightthickness=0)
        canvas.pack()
        cabecera_materias_img = tk.PhotoImage(file="frontend/recursos/cabeceraregistrarmateriaprofe.gif")
        self.cabecera_materias_img = cabecera_materias_img
        canvas.create_image(0, 0, anchor='nw', image=cabecera_materias_img)
        canvas.place(x=471, y=270)

    def __datos_materias__(self, controller):
        """
        Los datos traidos de MongoDB.
        :param controller: El controlador de la ventana.
        :return: Los datos de las materias y sus grupos.
        """
        # FRAME CONTENEDOR DE LOS DATOS.
        canvas = tk.Canvas(self, width=366, height=318, highlightthickness=0)
        canvas.pack()
        marco_contenedormaterias_img = tk.PhotoImage(file="frontend/recursos/bordecontenedormaterias.gif")
        self.marco_contenedormaterias_img = marco_contenedormaterias_img
        canvas.create_image(0, 0, anchor='nw', image=marco_contenedormaterias_img)
        canvas.place(x=471, y=310)
        # INICIO DE LOS DATOS DE LA TABLA.

        # FIN DE LOS DATOS DE LA TABLA.

    def __ver_materias__(self, controller):
        """
        Botón que lleva a la pantalla para registrar materias.
        :param controller:
        :return:
        """
        canvas = tk.Canvas(self, width=210, height=36, highlightthickness=0)
        canvas.pack()
        registrarmateria_profesor_img = tk.PhotoImage(file="frontend/recursos/vermaterias.gif")
        self.registrarmateria_profesor_img = registrarmateria_profesor_img
        canvas.create_image(0, 0, anchor='nw', image=registrarmateria_profesor_img)
        canvas.place(x=916, y=652)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_materias__(controller))

    def __ir_materias__(self, controller):
        self.controller = controller
        controller.show_frame(DatosProfesor)

    def __cerrar_sesion__(self, controller):
        """
        Botón que lleva a la página principal de inicio de sesión.
        :param controller: El controlador de la ventana.
        :return: El botón que lleva a Main
        """
        canvas = tk.Canvas(self, width=192, height=36, highlightthickness=0)
        canvas.pack()
        cerrarsesion_profesor_img = tk.PhotoImage(file="frontend/recursos/cerrarsesion.gif")
        self.cerrarsesion_profesor_img = cerrarsesion_profesor_img
        canvas.create_image(0, 0, anchor='nw', image=cerrarsesion_profesor_img)
        canvas.place(x=1151, y=652)
        canvas.config(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: self.__ir_inicio_sesion__(controller))

    def __ir_inicio_sesion__(self, controller):
        self.controller = controller
        controller.show_frame(Main)
