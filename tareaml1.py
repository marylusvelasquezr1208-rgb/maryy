import wx


# ==========================================================
# COLORES DEL SISTEMA
# ==========================================================

NEGRO = "#0B0B0B"
NEGRO_CLARO = "#151515"
DORADO = "#D4AF37"
DORADO_CLARO = "#F1D36A"
BLANCO = "#FFFFFF"
GRIS = "#BDBDBD"


# ==========================================================
# PRODUCTOS
# ==========================================================

productos = {
    "Pizza": {
        "precio": 35,
        "stock": 10
    },

    "Hamburguesa": {
        "precio": 25,
        "stock": 8
    },

    "Papas fritas": {
        "precio": 15,
        "stock": 5
    },

    "Pepsi 1 Litro": {
        "precio": 11,
        "stock": 10
    },

    "Guarana 1 Litro": {
        "precio": 11,
        "stock": 3
    }
}


# ==========================================================
# FUENTES
# ==========================================================

def fuente(tamano, negrita=False):

    peso = wx.FONTWEIGHT_NORMAL

    if negrita:
        peso = wx.FONTWEIGHT_BOLD


    return wx.Font(
        tamano,
        wx.FONTFAMILY_MODERN,
        wx.FONTSTYLE_NORMAL,
        peso
    )


# ==========================================================
# CONTROLES PERSONALIZADOS
# ==========================================================

class BotonDorado(wx.Button):
    """Botón plano pintado a mano para conservar el diseño."""

    def __init__(self, padre, texto, funcion, ancho=280, alto=55):

        wx.Button.__init__(
            self,
            padre,
            label=texto,
            style=wx.NO_BORDER
        )

        self.funcion = funcion

        self.fuente = fuente(12, True)

        self.encima = False

        self.SetMinSize(wx.Size(ancho, alto))

        self.SetFont(self.fuente)

        self.SetCursor(wx.Cursor(wx.CURSOR_HAND))

        self.Bind(wx.EVT_BUTTON, self.al_pulsar)

        self.Bind(wx.EVT_ENTER_WINDOW, self.entrar)

        self.Bind(wx.EVT_LEAVE_WINDOW, self.salir)


    def entrar(self, evento):

        self.encima = True

        self.Refresh()

        evento.Skip()


    def salir(self, evento):

        self.encima = False

        self.Refresh()

        evento.Skip()


    def al_pulsar(self, evento):

        self.funcion()

        evento.Skip()


    def OnPaint(self, evento):

        dc = wx.AutoBufferedPaintDC(self)

        color = DORADO

        if self.encima:
            color = DORADO_CLARO

        dc.SetBrush(wx.Brush(color))

        dc.SetPen(wx.Pen(color))

        dc.DrawRectangle(0, 0, *self.GetClientSize())

        dc.SetTextForeground(NEGRO)

        dc.SetFont(self.fuente)

        dc.DrawLabel(
            self.GetLabel(),
            wx.Rect(0, 0, *self.GetClientSize()),
            wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL
        )


class Celda(wx.Panel):
    """Casilla de tabla con fondo propio y borde."""

    def __init__(
        self,
        padre,
        texto,
        tamano_fuente,
        negrita,
        color_texto,
        color_fondo,
        ancho,
        alto
    ):

        wx.Panel.__init__(
            self,
            padre,
            style=wx.FULL_REPAINT_ON_RESIZE
        )

        self.texto = texto

        self.fuente = fuente(tamano_fuente, negrita)

        self.color_texto = color_texto

        self.color_fondo = color_fondo

        self.SetBackgroundColour(color_fondo)

        self.SetMinSize(wx.Size(ancho, alto))


    def OnPaint(self, evento):

        dc = wx.AutoBufferedPaintDC(self)

        dc.SetBackground(wx.Brush(self.color_fondo))

        dc.Clear()

        dc.SetPen(wx.Pen(NEGRO))

        dc.DrawRectangle(0, 0, *self.GetClientSize())

        dc.SetPen(wx.Pen(self.color_texto))

        dc.SetFont(self.fuente)

        dc.DrawLabel(
            self.texto,
            wx.Rect(0, 0, *self.GetClientSize()),
            wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL
        )


# ==========================================================
# UTILIDADES DE VENTANA
# ==========================================================

def crear_ventana(titulo, ancho, alto):

    ventana = wx.Frame(
        None,
        title=titulo,
        style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX
    )

    ventana.SetClientSize(wx.Size(ancho, alto))

    ventana.SetBackgroundColour(NEGRO)

    ventana.Centre()


    # Sin opción de redimensionar

    estilo = ventana.GetWindowStyleFlag()

    ventana.SetWindowStyleFlag(estilo & ~wx.RESIZE_BORDER)

    return ventana


def crear_boton(ventana, texto, funcion):

    return BotonDorado(
        ventana,
        texto,
        funcion
    )


def crear_etiqueta(ventana, texto, tamano, negrita, color, ancho=None):

    etiqueta = wx.StaticText(ventana, label=texto)

    etiqueta.SetFont(fuente(tamano, negrita))

    etiqueta.SetBackgroundColour(NEGRO)

    etiqueta.SetForegroundColour(color)

    if ancho is not None:
        etiqueta.SetMinSize(wx.Size(ancho, 30))

    return etiqueta


def mostrar_error(mensaje, padre=None):

    wx.MessageBox(
        mensaje,
        "Error",
        wx.OK | wx.ICON_ERROR,
        parent=padre
    )


def mostrar_info(mensaje, titulo, padre=None):

    wx.MessageBox(
        mensaje,
        titulo,
        wx.OK | wx.ICON_INFORMATION,
        parent=padre
    )


def mostrar_advertencia(mensaje, titulo, padre=None):

    wx.MessageBox(
        mensaje,
        titulo,
        wx.OK | wx.ICON_WARNING,
        parent=padre
    )


def confirmar(mensaje, titulo, padre=None):

    respuesta = wx.MessageBox(
        mensaje,
        titulo,
        wx.YES_NO | wx.ICON_QUESTION,
        parent=padre
    )

    return respuesta == wx.YES


def crear_entrada(ventana):

    entrada = wx.TextCtrl(
        ventana,
        value="",
        style=wx.TE_PROCESS_ENTER
    )

    entrada.SetFont(fuente(13))

    entrada.SetBackgroundColour(NEGRO_CLARO)

    entrada.SetForegroundColour(DORADO)

    entrada.SetMinSize(wx.Size(250, 38))

    entrada.SetDefaultStyle(
        wx.TextAttr(
            wx.NullColour,
            wx.NullColour,
            fuente(13),
            int(wx.ALIGN_CENTER)
        )
    )

    return entrada


# ==========================================================
# VENTANA DE BIENVENIDA
# ==========================================================

def ventana_bienvenida():

    bienvenida = crear_ventana("Bienvenida", 500, 300)

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        crear_etiqueta(bienvenida, "BIENVENIDO", 28, True, DORADO),
        0,
        wx.ALIGN_CENTER,
        45
    )

    sizer.Add(
        crear_etiqueta(
            bienvenida,
            "SISTEMA DE VENTAS",
            16,
            True,
            BLANCO
        ),
        0,
        wx.ALIGN_CENTER,
        5
    )

    sizer.Add(
        crear_etiqueta(
            bienvenida,
            "RESTAURANTE",
            14,
            False,
            DORADO_CLARO
        ),
        0,
        wx.ALIGN_CENTER,
        10
    )

    boton = crear_boton(
        bienvenida,
        "CONTINUAR",
        bienvenida.Destroy
    )

    sizer.Add(boton, 0, wx.ALIGN_CENTER, 25)

    bienvenida.SetSizer(sizer)

    bienvenida.Show()


# ==========================================================
# MOSTRAR PRODUCTOS
# ==========================================================

def mostrar_productos():

    ventana_productos = crear_ventana(
        "Productos disponibles",
        700,
        500
    )

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        crear_etiqueta(
            ventana_productos,
            "PRODUCTOS DISPONIBLES",
            22,
            True,
            DORADO
        ),
        0,
        wx.ALIGN_CENTER,
        25
    )


    tabla = wx.BoxSizer(wx.VERTICAL)

    encabezado = wx.BoxSizer(wx.HORIZONTAL)

    encabezado.Add(
        Celda(
            ventana_productos,
            "PRODUCTO",
            12,
            True,
            NEGRO,
            DORADO,
            260,
            45
        ),
        0
    )

    encabezado.Add(
        Celda(
            ventana_productos,
            "PRECIO",
            12,
            True,
            NEGRO,
            DORADO,
            190,
            45
        ),
        0
    )

    encabezado.Add(
        Celda(
            ventana_productos,
            "STOCK",
            12,
            True,
            NEGRO,
            DORADO,
            190,
            45
        ),
        0
    )

    tabla.Add(encabezado, 0)


    for nombre in productos:

        precio = productos[nombre]["precio"]

        stock = productos[nombre]["stock"]


        fila = wx.BoxSizer(wx.HORIZONTAL)

        fila.Add(
            Celda(
                ventana_productos,
                nombre,
                11,
                False,
                BLANCO,
                NEGRO_CLARO,
                260,
                45
            ),
            0
        )

        fila.Add(
            Celda(
                ventana_productos,
                "Bs " + str(precio),
                11,
                True,
                DORADO_CLARO,
                NEGRO_CLARO,
                190,
                45
            ),
            0
        )


        # Si el stock está en 0, se muestra AGOTADO

        if stock == 0:

            texto_stock = "AGOTADO"

        else:

            texto_stock = str(stock)


        fila.Add(
            Celda(
                ventana_productos,
                texto_stock,
                11,
                True,
                DORADO_CLARO,
                NEGRO_CLARO,
                190,
                45
            ),
            0
        )

        tabla.Add(fila, 0)


    sizer.Add(tabla, 0, wx.ALIGN_CENTER)

    boton = crear_boton(
        ventana_productos,
        "CERRAR",
        ventana_productos.Destroy
    )

    sizer.Add(boton, 0, wx.ALIGN_CENTER, 25)

    ventana_productos.SetSizer(sizer)

    ventana_productos.Show()


# ==========================================================
# VENTANA PARA COMPRAR
# ==========================================================

def comprar_producto():

    ventana_compra = crear_ventana("Comprar producto", 500, 500)

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        crear_etiqueta(
            ventana_compra,
            "REALIZAR COMPRA",
            22,
            True,
            DORADO
        ),
        0,
        wx.ALIGN_CENTER,
        25
    )

    sizer.Add(
        crear_etiqueta(
            ventana_compra,
            "Seleccione un producto:",
            12,
            False,
            BLANCO
        ),
        0,
        wx.ALIGN_CENTER,
        5
    )


    nombres = list(productos.keys())

    lista = wx.ComboBox(
        ventana_compra,
        choices=nombres,
        style=wx.CB_DROPDOWN | wx.CB_READONLY
    )

    lista.SetStringSelection(nombres[0])

    lista.SetFont(fuente(11, True))

    lista.SetBackgroundColour(NEGRO_CLARO)

    lista.SetForegroundColour(DORADO)

    lista.SetMinSize(wx.Size(280, 35))

    sizer.Add(lista, 0, wx.ALIGN_CENTER, 15)

    sizer.Add(
        crear_etiqueta(
            ventana_compra,
            "Cantidad:",
            12,
            False,
            BLANCO
        ),
        0,
        wx.ALIGN_CENTER,
        5
    )

    cantidad = crear_entrada(ventana_compra)

    sizer.Add(cantidad, 0, wx.ALIGN_CENTER, 15)


    def realizar_compra():

        nombre = lista.GetStringSelection()


        try:

            cantidad_comprada = int(cantidad.GetValue())

        except ValueError:

            mostrar_error(
                "Ingrese una cantidad válida.",
                ventana_compra
            )

            return


        if cantidad_comprada <= 0:

            mostrar_error(
                "La cantidad debe ser mayor que cero.",
                ventana_compra
            )

            return


        stock = productos[nombre]["stock"]


        # Producto agotado

        if stock == 0:

            mostrar_advertencia(
                "El producto "
                + nombre
                + " está agotado.\n\n"
                + "Debe renovar el stock.",
                "Producto agotado",
                ventana_compra
            )

            return


        # Stock insuficiente

        if cantidad_comprada > stock:

            mostrar_advertencia(
                "Solo quedan "
                + str(stock)
                + " unidades de "
                + nombre
                + ".",
                "Stock insuficiente",
                ventana_compra
            )

            return


        precio = productos[nombre]["precio"]


        total = cantidad_comprada * precio


        # Descontar stock

        productos[nombre]["stock"] = (
            stock - cantidad_comprada
        )


        mostrar_info(
            "COMPRA REALIZADA\n\n"
            + "Producto: "
            + nombre
            + "\nCantidad: "
            + str(cantidad_comprada)
            + "\nPrecio unitario: Bs "
            + str(precio)
            + "\n----------------------"
            + "\nTOTAL: Bs "
            + str(total),
            "Compra realizada",
            ventana_compra
        )


        ventana_compra.Destroy()


    boton = crear_boton(
        ventana_compra,
        "COMPRAR",
        realizar_compra
    )

    sizer.Add(boton, 0, wx.ALIGN_CENTER, 30)

    ventana_compra.SetSizer(sizer)

    ventana_compra.Show()


# ==========================================================
# MODIFICAR PRECIOS
# ==========================================================

def modificar_precio():

    ventana_precio = crear_ventana("Modificar precios", 500, 450)

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        crear_etiqueta(
            ventana_precio,
            "MODIFICAR PRECIOS",
            22,
            True,
            DORADO
        ),
        0,
        wx.ALIGN_CENTER,
        25
    )

    sizer.Add(
        crear_etiqueta(
            ventana_precio,
            "Seleccione el producto:",
            12,
            False,
            BLANCO
        ),
        0,
        wx.ALIGN_CENTER,
        5
    )


    nombres = list(productos.keys())

    lista = wx.ComboBox(
        ventana_precio,
        choices=nombres,
        style=wx.CB_DROPDOWN | wx.CB_READONLY
    )

    lista.SetStringSelection(nombres[0])

    lista.SetFont(fuente(11, True))

    lista.SetBackgroundColour(NEGRO_CLARO)

    lista.SetForegroundColour(DORADO)

    lista.SetMinSize(wx.Size(280, 35))

    sizer.Add(lista, 0, wx.ALIGN_CENTER, 15)

    sizer.Add(
        crear_etiqueta(
            ventana_precio,
            "Nuevo precio:",
            12,
            False,
            BLANCO
        ),
        0,
        wx.ALIGN_CENTER,
        5
    )

    precio = crear_entrada(ventana_precio)

    sizer.Add(precio, 0, wx.ALIGN_CENTER, 15)


    def guardar_precio():

        nombre = lista.GetStringSelection()


        try:

            nuevo_precio = float(precio.GetValue())

        except ValueError:

            mostrar_error(
                "Ingrese un precio válido.",
                ventana_precio
            )

            return


        if nuevo_precio <= 0:

            mostrar_error(
                "El precio debe ser mayor que cero.",
                ventana_precio
            )

            return


        productos[nombre]["precio"] = nuevo_precio


        mostrar_info(
            "Precio actualizado correctamente.\n\n"
            + nombre
            + "\nNuevo precio: Bs "
            + str(nuevo_precio),
            "Precio actualizado",
            ventana_precio
        )


        ventana_precio.Destroy()


    boton = crear_boton(
        ventana_precio,
        "GUARDAR PRECIO",
        guardar_precio
    )

    sizer.Add(boton, 0, wx.ALIGN_CENTER, 25)

    ventana_precio.SetSizer(sizer)

    ventana_precio.Show()


# ==========================================================
# PRODUCTOS POR RENOVAR
# ==========================================================

def productos_renovar():

    ventana_renovar = crear_ventana("Productos por renovar", 500, 500)

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        crear_etiqueta(
            ventana_renovar,
            "PRODUCTOS POR RENOVAR",
            20,
            True,
            DORADO
        ),
        0,
        wx.ALIGN_CENTER,
        25
    )


    mensaje = ""


    for nombre in productos:

        stock = productos[nombre]["stock"]


        if stock <= 3:

            mensaje = (
                mensaje
                + nombre
                + "  →  "
                + str(stock)
                + " unidades\n\n"
            )


    if mensaje == "":

        mensaje = (
            "No hay productos que necesiten renovación."
        )


    texto = Celda(
        ventana_renovar,
        mensaje,
        13,
        True,
        DORADO_CLARO,
        NEGRO_CLARO,
        420,
        300
    )

    sizer.Add(texto, 0, wx.ALIGN_CENTER, 10)

    boton = crear_boton(
        ventana_renovar,
        "CERRAR",
        ventana_renovar.Destroy
    )

    sizer.Add(boton, 0, wx.ALIGN_CENTER, 20)

    ventana_renovar.SetSizer(sizer)

    ventana_renovar.Show()


# ==========================================================
# SALIR
# ==========================================================

def salir():

    respuesta = confirmar(
        "¿Está seguro de que desea salir?",
        "Salir",
        ventana
    )


    if respuesta:

        ventana.Destroy()


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

aplicacion = wx.App(False)


ventana = crear_ventana(
    "Sistema de Ventas - Restaurante",
    850,
    650
)


sizer = wx.BoxSizer(wx.VERTICAL)

sizer.Add(
    crear_etiqueta(
        ventana,
        "SISTEMA DE VENTAS",
        30,
        True,
        DORADO
    ),
    0,
    wx.ALIGN_CENTER,
    40
)

sizer.Add(
    crear_etiqueta(
        ventana,
        "RESTAURANTE",
        16,
        True,
        BLANCO
    ),
    0,
    wx.ALIGN_CENTER
)

sizer.Add(
    crear_etiqueta(
        ventana,
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        14,
        False,
        DORADO
    ),
    0,
    wx.ALIGN_CENTER,
    15
)


# ==========================================================
# CONTENEDOR DE BOTONES
# ==========================================================

botones = wx.Panel(ventana)

botones.SetBackgroundColour(NEGRO)

rejilla = wx.FlexGridSizer(2, 2, 12, 15)


# ==========================================================
# BOTÓN PRODUCTOS
# ==========================================================

boton_productos = crear_boton(
    botones,
    "PRODUCTOS DISPONIBLES",
    mostrar_productos
)

rejilla.Add(boton_productos, 0, wx.ALIGN_CENTER)


# ==========================================================
# BOTÓN COMPRAR
# ==========================================================

boton_comprar = crear_boton(
    botones,
    "COMPRAR PRODUCTO",
    comprar_producto
)

rejilla.Add(boton_comprar, 0, wx.ALIGN_CENTER)


# ==========================================================
# BOTÓN PRECIOS
# ==========================================================

boton_precios = crear_boton(
    botones,
    "MODIFICAR PRECIOS",
    modificar_precio
)

rejilla.Add(boton_precios, 0, wx.ALIGN_CENTER)


# ==========================================================
# BOTÓN RENOVAR
# ==========================================================

boton_renovar = crear_boton(
    botones,
    "PRODUCTOS POR RENOVAR",
    productos_renovar
)

rejilla.Add(boton_renovar, 0, wx.ALIGN_CENTER)

botones.SetSizer(rejilla)

sizer.Add(botones, 0, wx.ALIGN_CENTER, 15)


# ==========================================================
# BOTÓN SALIR
# ==========================================================

boton_salir = crear_boton(
    ventana,
    "SALIR",
    salir
)

sizer.Add(boton_salir, 0, wx.ALIGN_CENTER, 25)


# ==========================================================
# PIE DE VENTANA
# ==========================================================

pie = wx.StaticText(
    ventana,
    label="Sistema de gestión de ventas"
)

pie.SetFont(fuente(10))

pie.SetBackgroundColour(NEGRO)

pie.SetForegroundColour(GRIS)

sizer.Add(pie, 0, wx.ALIGN_CENTER)

ventana.SetSizer(sizer)

ventana.Show()


# ==========================================================
# MOSTRAR BIENVENIDA
# ==========================================================

temporizador = wx.Timer(ventana)


def mostrar_bienvenida(evento):

    ventana_bienvenida()


ventana.Bind(
    wx.EVT_TIMER,
    mostrar_bienvenida,
    temporizador
)

temporizador.Start(300, wx.TIMER_ONE_SHOT)


# ==========================================================
# EJECUTAR PROGRAMA
# ==========================================================

aplicacion.MainLoop()
