# ==========================================================
# INSTALACIÓN AUTOMÁTICA DE CUSTOMTKINTER
# ==========================================================

try:

    import customtkinter as ctk

except ModuleNotFoundError:

    import subprocess
    import sys

    print("CustomTkinter no está instalado. Instalando...")

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "customtkinter"]
    )

    import customtkinter as ctk


from tkinter import messagebox


# ==========================================================
# MODO OSCURO PARA TODA LA APLICACIÓN
# ==========================================================

ctk.set_appearance_mode("dark")


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
# CONFIGURACIÓN GENERAL DE BOTONES
# ==========================================================

def crear_boton(ventana, texto, funcion):

    boton = ctk.CTkButton(
        ventana,
        text=texto,
        command=funcion,
        width=290,
        height=60,
        corner_radius=10,
        fg_color=DORADO,
        hover_color=DORADO_CLARO,
        text_color=NEGRO,
        font=("Arial", 14, "bold"),
        cursor="hand2"
    )

    return boton


# ==========================================================
# VENTANA DE BIENVENIDA
# ==========================================================

def ventana_bienvenida():

    bienvenida = ctk.CTkToplevel(ventana)

    bienvenida.title("Bienvenida")

    bienvenida.geometry("500x320")

    bienvenida.configure(fg_color=NEGRO)

    bienvenida.resizable(False, False)


    titulo = ctk.CTkLabel(
        bienvenida,
        text="BIENVENIDO",
        text_color=DORADO,
        font=("Arial", 34, "bold")
    )

    titulo.pack(pady=(45, 5))


    subtitulo = ctk.CTkLabel(
        bienvenida,
        text="SISTEMA DE VENTAS",
        text_color=BLANCO,
        font=("Arial", 16, "bold")
    )

    subtitulo.pack(pady=5)


    linea = ctk.CTkLabel(
        bienvenida,
        text="RESTAURANTE",
        text_color=DORADO_CLARO,
        font=("Arial", 14)
    )

    linea.pack(pady=10)


    boton = crear_boton(
        bienvenida,
        "CONTINUAR",
        bienvenida.destroy
    )

    boton.pack(pady=25)


# ==========================================================
# MOSTRAR PRODUCTOS
# ==========================================================

def mostrar_productos():

    ventana_productos = ctk.CTkToplevel(ventana)

    ventana_productos.title("Productos disponibles")

    ventana_productos.geometry("700x500")

    ventana_productos.configure(fg_color=NEGRO)

    ventana_productos.resizable(False, False)


    titulo = ctk.CTkLabel(
        ventana_productos,
        text="PRODUCTOS DISPONIBLES",
        text_color=DORADO,
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=25)


    tabla = ctk.CTkFrame(
        ventana_productos,
        fg_color="transparent"
    )

    tabla.pack()


    # Encabezado PRODUCTO

    ctk.CTkLabel(
        tabla,
        text="PRODUCTO",
        width=260,
        height=45,
        corner_radius=6,
        fg_color=DORADO,
        text_color=NEGRO,
        font=("Arial", 13, "bold")
    ).grid(row=0, column=0, padx=4, pady=3)


    # Encabezado PRECIO

    ctk.CTkLabel(
        tabla,
        text="PRECIO",
        width=170,
        height=45,
        corner_radius=6,
        fg_color=DORADO,
        text_color=NEGRO,
        font=("Arial", 13, "bold")
    ).grid(row=0, column=1, padx=4, pady=3)


    # Encabezado STOCK

    ctk.CTkLabel(
        tabla,
        text="STOCK",
        width=170,
        height=45,
        corner_radius=6,
        fg_color=DORADO,
        text_color=NEGRO,
        font=("Arial", 13, "bold")
    ).grid(row=0, column=2, padx=4, pady=3)


    fila = 1


    for nombre in productos:

        precio = productos[nombre]["precio"]

        stock = productos[nombre]["stock"]


        ctk.CTkLabel(
            tabla,
            text=nombre,
            width=260,
            height=42,
            corner_radius=6,
            fg_color=NEGRO_CLARO,
            text_color=BLANCO,
            font=("Arial", 12)
        ).grid(row=fila, column=0, padx=4, pady=3)


        ctk.CTkLabel(
            tabla,
            text="Bs " + str(precio),
            width=170,
            height=42,
            corner_radius=6,
            fg_color=NEGRO_CLARO,
            text_color=DORADO_CLARO,
            font=("Arial", 12, "bold")
        ).grid(row=fila, column=1, padx=4, pady=3)


        # Si el stock está en 0, se muestra AGOTADO

        if stock == 0:

            texto_stock = "AGOTADO"

        else:

            texto_stock = str(stock)


        ctk.CTkLabel(
            tabla,
            text=texto_stock,
            width=170,
            height=42,
            corner_radius=6,
            fg_color=NEGRO_CLARO,
            text_color=DORADO_CLARO,
            font=("Arial", 12, "bold")
        ).grid(row=fila, column=2, padx=4, pady=3)


        fila = fila + 1


    boton = crear_boton(
        ventana_productos,
        "CERRAR",
        ventana_productos.destroy
    )

    boton.pack(pady=25)


# ==========================================================
# VENTANA PARA COMPRAR
# ==========================================================

def comprar_producto():

    ventana_compra = ctk.CTkToplevel(ventana)

    ventana_compra.title("Comprar producto")

    ventana_compra.geometry("500x520")

    ventana_compra.configure(fg_color=NEGRO)

    ventana_compra.resizable(False, False)


    titulo = ctk.CTkLabel(
        ventana_compra,
        text="REALIZAR COMPRA",
        text_color=DORADO,
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=25)


    ctk.CTkLabel(
        ventana_compra,
        text="Seleccione un producto:",
        text_color=BLANCO,
        font=("Arial", 13)
    ).pack(pady=5)


    producto_seleccionado = ctk.StringVar()

    nombres = list(productos.keys())

    producto_seleccionado.set(nombres[0])


    lista = ctk.CTkOptionMenu(
        ventana_compra,
        variable=producto_seleccionado,
        values=nombres,
        width=300,
        height=42,
        corner_radius=8,
        button_color=DORADO,
        button_hover_color=DORADO_CLARO,
        text_color=NEGRO,
        dropdown_fg_color=NEGRO_CLARO,
        dropdown_hover_color=DORADO,
        dropdown_text_color=DORADO,
        font=("Arial", 12, "bold"),
        dropdown_font=("Arial", 12),
        cursor="hand2"
    )

    lista.pack(pady=15)


    ctk.CTkLabel(
        ventana_compra,
        text="Cantidad:",
        text_color=BLANCO,
        font=("Arial", 13)
    ).pack(pady=5)


    cantidad = ctk.CTkEntry(
        ventana_compra,
        width=200,
        height=42,
        corner_radius=8,
        justify="center",
        border_width=1,
        border_color=DORADO,
        fg_color=NEGRO_CLARO,
        text_color=DORADO,
        font=("Arial", 15)
    )

    cantidad.pack(pady=15)


    def realizar_compra():

        nombre = producto_seleccionado.get()


        try:

            cantidad_comprada = int(
                cantidad.get()
            )

        except:

            messagebox.showerror(
                "Error",
                "Ingrese una cantidad válida.",
                parent=ventana_compra
            )

            return


        if cantidad_comprada <= 0:

            messagebox.showerror(
                "Error",
                "La cantidad debe ser mayor que cero.",
                parent=ventana_compra
            )

            return


        stock = productos[nombre]["stock"]


        # Producto agotado

        if stock == 0:

            messagebox.showwarning(
                "Producto agotado",
                "El producto "
                + nombre
                + " está agotado.\n\n"
                + "Debe renovar el stock.",
                parent=ventana_compra
            )

            return


        # Stock insuficiente

        if cantidad_comprada > stock:

            messagebox.showwarning(
                "Stock insuficiente",
                "Solo quedan "
                + str(stock)
                + " unidades de "
                + nombre
                + ".",
                parent=ventana_compra
            )

            return


        precio = productos[nombre]["precio"]


        total = cantidad_comprada * precio


        # Descontar stock

        productos[nombre]["stock"] = (
            stock - cantidad_comprada
        )


        messagebox.showinfo(
            "Compra realizada",
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
            parent=ventana_compra
        )


        ventana_compra.destroy()


    boton = crear_boton(
        ventana_compra,
        "COMPRAR",
        realizar_compra
    )

    boton.pack(pady=30)


# ==========================================================
# MODIFICAR PRECIOS
# ==========================================================

def modificar_precio():

    ventana_precio = ctk.CTkToplevel(ventana)

    ventana_precio.title("Modificar precios")

    ventana_precio.geometry("500x470")

    ventana_precio.configure(fg_color=NEGRO)

    ventana_precio.resizable(False, False)


    titulo = ctk.CTkLabel(
        ventana_precio,
        text="MODIFICAR PRECIOS",
        text_color=DORADO,
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=25)


    nombres = list(productos.keys())


    producto_seleccionado = ctk.StringVar()

    producto_seleccionado.set(nombres[0])


    ctk.CTkLabel(
        ventana_precio,
        text="Seleccione el producto:",
        text_color=BLANCO,
        font=("Arial", 13)
    ).pack(pady=5)


    lista = ctk.CTkOptionMenu(
        ventana_precio,
        variable=producto_seleccionado,
        values=nombres,
        width=300,
        height=42,
        corner_radius=8,
        button_color=DORADO,
        button_hover_color=DORADO_CLARO,
        text_color=NEGRO,
        dropdown_fg_color=NEGRO_CLARO,
        dropdown_hover_color=DORADO,
        dropdown_text_color=DORADO,
        font=("Arial", 12, "bold"),
        dropdown_font=("Arial", 12),
        cursor="hand2"
    )

    lista.pack(pady=15)


    ctk.CTkLabel(
        ventana_precio,
        text="Nuevo precio:",
        text_color=BLANCO,
        font=("Arial", 13)
    ).pack(pady=5)


    precio = ctk.CTkEntry(
        ventana_precio,
        width=200,
        height=42,
        corner_radius=8,
        justify="center",
        border_width=1,
        border_color=DORADO,
        fg_color=NEGRO_CLARO,
        text_color=DORADO,
        font=("Arial", 15)
    )

    precio.pack(pady=15)


    def guardar_precio():

        nombre = producto_seleccionado.get()


        try:

            nuevo_precio = float(
                precio.get()
            )

        except:

            messagebox.showerror(
                "Error",
                "Ingrese un precio válido.",
                parent=ventana_precio
            )

            return


        if nuevo_precio <= 0:

            messagebox.showerror(
                "Error",
                "El precio debe ser mayor que cero.",
                parent=ventana_precio
            )

            return


        productos[nombre]["precio"] = nuevo_precio


        messagebox.showinfo(
            "Precio actualizado",
            "Precio actualizado correctamente.\n\n"
            + nombre
            + "\nNuevo precio: Bs "
            + str(nuevo_precio),
            parent=ventana_precio
        )


        ventana_precio.destroy()


    boton = crear_boton(
        ventana_precio,
        "GUARDAR PRECIO",
        guardar_precio
    )

    boton.pack(pady=25)


# ==========================================================
# PRODUCTOS POR RENOVAR
# ==========================================================

def productos_renovar():

    ventana_renovar = ctk.CTkToplevel(ventana)

    ventana_renovar.title("Productos por renovar")

    ventana_renovar.geometry("500x500")

    ventana_renovar.configure(fg_color=NEGRO)

    ventana_renovar.resizable(False, False)


    titulo = ctk.CTkLabel(
        ventana_renovar,
        text="PRODUCTOS POR RENOVAR",
        text_color=DORADO,
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=25)


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


    texto = ctk.CTkLabel(
        ventana_renovar,
        text=mensaje,
        width=380,
        height=250,
        corner_radius=10,
        fg_color=NEGRO_CLARO,
        text_color=DORADO_CLARO,
        font=("Arial", 14, "bold"),
        anchor="w",
        justify="left",
        wraplength=340
    )

    texto.pack(pady=10)


    boton = crear_boton(
        ventana_renovar,
        "CERRAR",
        ventana_renovar.destroy
    )

    boton.pack(pady=20)


# ==========================================================
# SALIR
# ==========================================================

def salir():

    respuesta = messagebox.askyesno(
        "Salir",
        "¿Está seguro de que desea salir?",
        parent=ventana
    )


    if respuesta:

        ventana.destroy()


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

ventana = ctk.CTk()

ventana.title(
    "Sistema de Ventas - Restaurante"
)

ventana.geometry("850x650")

ventana.configure(fg_color=NEGRO)

ventana.resizable(False, False)


# ==========================================================
# TÍTULO PRINCIPAL
# ==========================================================

titulo = ctk.CTkLabel(
    ventana,
    text="SISTEMA DE VENTAS",
    text_color=DORADO,
    font=("Arial", 32, "bold")
)

titulo.pack(pady=(40, 5))


subtitulo = ctk.CTkLabel(
    ventana,
    text="RESTAURANTE",
    text_color=BLANCO,
    font=("Arial", 16, "bold")
)

subtitulo.pack()


linea = ctk.CTkLabel(
    ventana,
    text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    text_color=DORADO,
    font=("Arial", 14)
)

linea.pack(pady=15)


# ==========================================================
# CONTENEDOR DE BOTONES
# ==========================================================

botones = ctk.CTkFrame(
    ventana,
    fg_color="transparent"
)

botones.pack(pady=15)


# ==========================================================
# BOTÓN PRODUCTOS
# ==========================================================

boton_productos = crear_boton(
    botones,
    "PRODUCTOS DISPONIBLES",
    mostrar_productos
)

boton_productos.grid(
    row=0,
    column=0,
    padx=15,
    pady=12
)


# ==========================================================
# BOTÓN COMPRAR
# ==========================================================

boton_comprar = crear_boton(
    botones,
    "COMPRAR PRODUCTO",
    comprar_producto
)

boton_comprar.grid(
    row=0,
    column=1,
    padx=15,
    pady=12
)


# ==========================================================
# BOTÓN PRECIOS
# ==========================================================

boton_precios = crear_boton(
    botones,
    "MODIFICAR PRECIOS",
    modificar_precio
)

boton_precios.grid(
    row=1,
    column=0,
    padx=15,
    pady=12
)


# ==========================================================
# BOTÓN RENOVAR
# ==========================================================

boton_renovar = crear_boton(
    botones,
    "PRODUCTOS POR RENOVAR",
    productos_renovar
)

boton_renovar.grid(
    row=1,
    column=1,
    padx=15,
    pady=12
)


# ==========================================================
# BOTÓN SALIR
# ==========================================================

boton_salir = crear_boton(
    ventana,
    "SALIR",
    salir
)

boton_salir.pack(pady=25)


# ==========================================================
# PIE DE VENTANA
# ==========================================================

pie = ctk.CTkLabel(
    ventana,
    text="Sistema de gestión de ventas",
    text_color=GRIS,
    font=("Arial", 10)
)

pie.pack()


# ==========================================================
# MOSTRAR BIENVENIDA
# ==========================================================

ventana.after(
    300,
    ventana_bienvenida
)


# ==========================================================
# EJECUTAR PROGRAMA
# ==========================================================

ventana.mainloop()