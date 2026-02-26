import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from adj_ven import centro
from tema import apply_theme_to_titlebar
from tema import window_theme
from function_lib import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp, graf_rece_gdp

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis de Intercambios de Armas - ONU")
        # self.root.geometry("900x600")
        centro(self.root, 1280, 720)
        self.menu_visible = False
        self.menu_width = 170

        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        p_ancho= self.root.winfo_screenwidth()

        self.menu_frame = tb.Frame(self.root, bootstyle="dark", width=0, height=600)
        self.menu_frame.place(x=0, y=0, height=p_ancho)

        self.toggle_btn = tk.Button(self.root, text="☰", font=("Arial", 16), command=self.toggle_menu)
        self.toggle_btn.place(x=10, y=10)

        self.frames = {
            "Inicio": self.inicio(),
            "Mayores proveedores": self.suppliers(),
            "Mayores receptores": self.recipients(),
            "Mayor proveedor vs \nReceptores": self.mayor_supplier(),
            "Mayor receptor vs \nProveedores": self.mayor_recepient(),
            "Entrega vs PIB": self.graf_arm_pib(),
            "Recepción vs PIB": self.graf_recibido_pib(), 
            "Salir": self.salir()
        }

        opciones = list(self.frames.keys())
        for i, texto in enumerate(opciones):
            btn = tb.Button(self.menu_frame, text=texto, bootstyle="secondary", width=20,
                            command=lambda name=texto: self.mostrar_frame(name))
            btn.place(x=10, y=60 + i * 60, height=50)

        self.mostrar_frame("Inicio")
        apply_theme_to_titlebar(self.root)
        window_theme(self.root)

    def toggle_menu(self):
        if self.menu_visible:
            self.ocultar_menu()
        else:
            self.mostrar_menu()

    def mostrar_menu(self):
        for w in range(0, self.menu_width + 1, 20):
            self.menu_frame.config(width=w)
            self.menu_frame.update()
        self.menu_visible = True

    def ocultar_menu(self):
        for w in range(self.menu_width, -1, -20):
            self.menu_frame.config(width=w)
            self.menu_frame.update()
        self.menu_visible = False

    def mostrar_frame(self, name):
        for frame in self.frames.values():
            frame.place_forget()
        self.frames[name].place(x=0, y=0, relwidth=1, relheight=1)


    def inicio(self):
        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🏠 Bienvenido", font=("Arial", 24), justify="center")
        label.pack(pady=20)

        nombres = tk.Label(
            frame,
            text="Creado por: \nJuan Diego Suárez Agualimpia \nDaniel Hurtado",
            font=fuente_texto,justify="center"
        )
        nombres.pack(pady=10)

        titulo_desc = tk.Label(
            frame,
            text="Análisis de datos de la ONU sobre el comercio de armas",
            font=fuente_texto,
        )
        titulo_desc.pack(pady=10)

        descripcion = tk.Label(
            frame,
            text=(
                "La ONU lleva un registro de los intercambios de armas a nivel mundial, y en esta aplicación se han analizado los datos de este registro para identificar los principales proveedores y receptores de armas a lo largo del tiempo. Además, se han explorado las tendencias en el comercio de armas, incluyendo los tipos de armas más comercializadas y las regiones geográficas involucradas. Este análisis proporciona una visión general de cómo se ha desarrollado el comercio de armas a nivel global y cuáles son los actores clave en este ámbito."
            ),
            font=fuente_descripcion,
            wraplength=700,
            justify="left",
        )
        descripcion.pack(pady=20)

        return frame

    def suppliers(self):

        path=r'Datos'

        frame2=datos_armas(path)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de proveedores de armas", font=("Arial", 24))
        label.pack(pady=20)
 
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los proveedores de armas más importantes.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]


        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                graf_suppliers(frame2, frame_grafico)             

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def recipients(self):

        path=r'Datos'

        frame2=datos_armas(path)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de receptores de armas", font=("Arial", 24))
        label.pack(pady=20)
 
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los receptores de armas más importantes.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]
            # ("Mostrar datos")]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                graf_recipients(frame2, frame_grafico)             
            # elif evento == "Mostrar datos":
            #     mostrar_dataframe(frame2, frame_grafico)

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def mayor_supplier(self):

        path=r'Datos'

        frame2=datos_armas(path)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de mayor proveedor de armas y sus mayores receptores", font=("Arial", 24))
        label.pack(pady=20)
  
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico del proveedor de armas más importante y sus mayores receptores.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                graf_mayor_supplier(frame2, frame_grafico)             

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def mayor_recepient(self):

        path=r'Datos'

        frame2=datos_armas(path)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de mayor receptor de armas y sus proveedores", font=("Arial", 24))
        label.pack(pady=20)
  
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico del receptor de armas más importante y sus proveedores.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                graf_mayor_recipient(frame2, frame_grafico)             

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def tipo_armas(self):

        path=r'Datos'

        frame2=datos_armas(path)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de armas intercambiadas", font=("Arial", 24))
        label.pack(pady=20)
  
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los tipos de armas con un mayor número de intercambios a nivel mundial, en función de la cantidad.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                graf_arma(frame2, frame_grafico)             

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame


    def graf_arm_pib(self):

        path = r'Datos'
        path2 = r'PIB'
        frame2 = datos_armas(path)
        pib = datos_pib(path2)

        country_arms = [
            "Estados Unidos",
            "Reino Unido",
            "Francia",
            "Alemania",
            "Rusia",
            "China",
            "India",
        ]

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de proveedores de armas y su impacto en el PIB", font=("Arial", 24))
        label.pack(pady=20)
 
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los proveedores de armas más importantes, además, se puede observar su impacto en el PIB.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        combobox = ttk.Combobox(frame, values=country_arms, state="readonly", font=fuente_texto)
        combobox.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]
            # ("Mostrar datos")]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                selected_country = combobox.get()
                if selected_country in country_arms:
                    graf_arms_gdp(frame2, pib, selected_country, frame_grafico)             
                else:
                    print("País no válido")
            # elif evento == "Mostrar datos":
            #     mostrar_dataframe(frame2, frame_grafico)

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def graf_recibido_pib(self):

        path = r'Datos'
        path2 = r'PIB'
        frame2 = datos_armas(path)
        pib = datos_pib(path2)

        country_arms = [
            "Estados Unidos",
            "Reino Unido",
            "Francia",
            "Alemania",
            "Rusia",
            "China",
            "India",
        ]

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis de receptores de armas y su impacto en el PIB", font=("Arial", 24))
        label.pack(pady=20)
 
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los receptores de armas más importantes, además, se puede observar su impacto en el PIB.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        combobox = ttk.Combobox(frame, values=country_arms, state="readonly", font=fuente_texto)
        combobox.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),]
            # ("Mostrar datos")]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                selected_country = combobox.get()
                if selected_country in country_arms:
                    graf_rece_gdp(frame2, pib, selected_country, frame_grafico)             
                else:
                    print("País no válido")
            # elif evento == "Mostrar datos":
            #     mostrar_dataframe(frame2, frame_grafico)

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def salir(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🚪 ¿Deseas salir? \nEsperamos que hayas disfrutado del análisis.", font=("Arial", 24))
        label.pack(pady=20)
        btn_salir = tk.Button(frame, text="Cerrar aplicación", command=self.root.destroy)
        btn_salir.pack(pady=10)
        return frame

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()