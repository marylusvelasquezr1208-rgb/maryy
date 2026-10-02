import tkinter as tk
from tkinter import messagebox


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

    boton = tk.Button(
        ventana,
        text=texto,
        command=funcion,
        bg=DORADO,
        fg=NEGRO,
        activebackground=DORADO_CLARO,
        activeforeground=NEGRO,
        font=("Arial", 12, "bold"),
        width=28,
        height=2,
        relief="flat",
        cursor="hand2"
    )

    return boton


# ==========================================================
# VENTANA DE BIENVENIDA
# ==========================================================

def ventana_bienvenida():

    bienvenida = tk.Toplevel(ventana)

    bienvenida.title("Bienvenida")

    bienvenida.geometry("500x300")

    bienvenida.configure(bg=NEGRO)

    bienvenida.resizable(False, False)


    titulo = tk.Label(
        bienvenida,
        text="BIENVENIDO",
        bg=NEGRO,
        fg=DORADO,
        font=("Arial", 28, "bold")
    )

    titulo.pack(pady=(45, 5))


    subtitulo = tk.Label(
        bienvenida,
        text="SISTEMA DE VENTAS",
        bg=NEGRO,
        fg=BLANCO,
        font=("Arial", 16, "bold")
    )

    subtitulo.pack(pady=5)


    linea = tk.Label(
        bienvenida,
        text="RESTAURANTE",
        bg=NEGRO,
        fg=DORADO_CLARO,
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

    ventana_productos = tk.Toplevel(ventana)

    ventana_productos.title("Productos disponibles")

    ventana_productos.geometry("700x500")

    ventana_productos.configure(bg=NEGRO)

    ventana_productos.resizable(False, False)


    titulo = tk.Label(
        ventana_productos,
        text="PRODUCTOS DISPONIBLES",
        bg=NEGRO,
        fg=DORADO,
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=25)


    tabla = tk.Frame(
        ventana_productos,
        bg=NEGRO
    )

    tabla.pack()


    # Encabezado PRODUCTO

    tk.Label(
        tabla,
        text="PRODUCTO",
        bg=DORADO,
        fg=NEGRO,
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="solid"
    ).grid(row=0, column=0)


    # Encabezado PRECIO

    tk.Label(
        tabla,
        text="PRECIO",
        bg=DORADO,
        fg=NEGRO,
        font=("Arial", 12, "bold"),
        width=18,
        height=2,
        relief="solid"
    ).grid(row=0, column=1)


    # Encabezado STOCK

    tk.Label(
        tabla,
        text="STOCK",
        bg=DORADO,
        fg=NEGRO,
        font=("Arial", 12, "bold"),
        width=18,
        height=2,
        relief="solid"
    ).grid(row=0, column=2)


    fila = 1


    for nombre in productos:

        precio = productos[nombre]["precio"]

        stock = productos[nombre]["stock"]


        tk.Label(
            tabla,
            text=nombre,
            bg=NEGRO_CLARO,
            fg=BLANCO,
            font=("Arial", 11),
            width=25,
            height=2,
            relief="solid"
        ).grid(row=fila, column=0)


        tk.Label(
            tabla,
            text="Bs " + str(precio),
            bg=NEGRO_CLARO,
            fg=DORADO_CLARO,
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            relief="solid"
        ).grid(row=fila, column=1)


        # Si el stock está en 0, se muestra AGOTADO

        if stock == 0:

            texto_stock = "AGOTADO"

        else:

            texto_stock = str(stock)


        tk.Label(
            tabla,
            text=texto_stock,
            bg=NEGRO_CLARO,
            fg=DORADO_CLARO,
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            relief="solid"
        ).grid(row=fila, column=2)


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

    ventana_compra = tk.Toplevel(ventana)

    ventana_compra.title("Comprar producto")

    ventana_compra.geometry("500x500")

    ventana_compra.configure(bg=NEGRO)

    ventana_compra.resizable(False, False)


    titulo = tk.Label(
        ventana_compra,
        text="REALIZAR COMPRA",
        bg=NEGRO,
        fg=DORADO,
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=25)


    tk.Label(
        ventana_compra,
        text="Seleccione un producto:",
        bg=NEGRO,
        fg=BLANCO,
        font=("Arial", 12)
    ).pack(pady=5)


    producto_seleccionado = tk.StringVar()

    nombres = list(productos.keys())

    producto_seleccionado.set(nombres[0])


    lista = tk.OptionMenu(
        ventana_compra,
        producto_seleccionado,
        *nombres
    )

    lista.config(
        bg=DORADO,
        fg=NEGRO,
        activebackground=DORADO_CLARO,
        activeforeground=NEGRO,
        font=("Arial", 11, "bold"),
        width=25
    )

    lista["menu"].config(
        bg=NEGRO_CLARO,
        fg=DORADO,
        font=("Arial", 11)
    )

    lista.pack(pady=15)


    tk.Label(
        ventana_compra,
        text="Cantidad:",
        bg=NEGRO,
        fg=BLANCO,
        font=("Arial", 12)
    ).pack(pady=5)


    cantidad = tk.Entry(
        ventana_compra,
        width=15,
        justify="center",
        bg=NEGRO_CLARO,
        fg=DORADO,
        insertbackground=DORADO,
        font=("Arial", 13),
        relief="solid"
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
                "Ingrese una cantidad válida."
            )

            return


        if cantidad_comprada <= 0:

            messagebox.showerror(
                "Error",
                "La cantidad debe ser mayor que cero."
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
                + "Debe renovar el stock."
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
                + "."
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
            + str(total)
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

    ventana_precio = tk.Toplevel(ventana)

    ventana_precio.title("Modificar precios")

    ventana_precio.geometry("500x450")

    ventana_precio.configure(bg=NEGRO)

    ventana_precio.resizable(False, False)


    titulo = tk.Label(
        ventana_precio,
        text="MODIFICAR PRECIOS",
        bg=NEGRO,
        fg=DORADO,
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=25)


    nombres = list(productos.keys())


    producto_seleccionado = tk.StringVar()

    producto_seleccionado.set(nombres[0])


    tk.Label(
        ventana_precio,
        text="Seleccione el producto:",
        bg=NEGRO,
        fg=BLANCO,
        font=("Arial", 12)
    ).pack(pady=5)


    lista = tk.OptionMenu(
        ventana_precio,
        producto_seleccionado,
        *nombres
    )

    lista.config(
        bg=DORADO,
        fg=NEGRO,
        activebackground=DORADO_CLARO,
        activeforeground=NEGRO,
        font=("Arial", 11, "bold"),
        width=25
    )

    lista["menu"].config(
        bg=NEGRO_CLARO,
        fg=DORADO
    )

    lista.pack(pady=15)


    tk.Label(
        ventana_precio,
        text="Nuevo precio:",
        bg=NEGRO,
        fg=BLANCO,
        font=("Arial", 12)
    ).pack(pady=5)


    precio = tk.Entry(
        ventana_precio,
        width=15,
        justify="center",
        bg=NEGRO_CLARO,
        fg=DORADO,
        insertbackground=DORADO,
        font=("Arial", 13)
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
                "Ingrese un precio válido."
            )

            return


        if nuevo_precio <= 0:

            messagebox.showerror(
                "Error",
                "El precio debe ser mayor que cero."
            )

            return


        productos[nombre]["precio"] = nuevo_precio


        messagebox.showinfo(
            "Precio actualizado",
            "Precio actualizado correctamente.\n\n"
            + nombre
            + "\nNuevo precio: Bs "
            + str(nuevo_precio)
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

    ventana_renovar = tk.Toplevel(ventana)

    ventana_renovar.title("Productos por renovar")

    ventana_renovar.geometry("500x500")

    ventana_renovar.configure(bg=NEGRO)

    ventana_renovar.resizable(False, False)


    titulo = tk.Label(
        ventana_renovar,
        text="PRODUCTOS POR RENOVAR",
        bg=NEGRO,
        fg=DORADO,
        font=("Arial", 20, "bold")
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


    texto = tk.Label(
        ventana_renovar,
        text=mensaje,
        bg=NEGRO_CLARO,
        fg=DORADO_CLARO,
        font=("Arial", 13, "bold"),
        width=35,
        height=10,
        justify="left"
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
        "¿Está seguro de que desea salir?"
    )


    if respuesta:

        ventana.destroy()


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

ventana = tk.Tk()

ventana.title(
    "Sistema de Ventas - Restaurante"
)

ventana.geometry("850x650")

ventana.configure(bg=NEGRO)

ventana.resizable(False, False)


# ==========================================================
# TÍTULO PRINCIPAL
# ==========================================================

titulo = tk.Label(
    ventana,
    text="SISTEMA DE VENTAS",
    bg=NEGRO,
    fg=DORADO,
    font=("Arial", 30, "bold")
)

titulo.pack(pady=(40, 5))


subtitulo = tk.Label(
    ventana,
    text="RESTAURANTE",
    bg=NEGRO,
    fg=BLANCO,
    font=("Arial", 16, "bold")
)

subtitulo.pack()


linea = tk.Label(
    ventana,
    text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    bg=NEGRO,
    fg=DORADO
)

linea.pack(pady=15)


# ==========================================================
# CONTENEDOR DE BOTONES
# ==========================================================

botones = tk.Frame(
    ventana,
    bg=NEGRO
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

pie = tk.Label(
    ventana,
    text="Sistema de gestión de ventas",
    bg=NEGRO,
    fg=GRIS,
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