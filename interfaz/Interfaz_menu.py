from interfaz.funciones_menu import Menu
import tkinter as tk

COLOR_FONDO = "#F5F8FA"
COLOR_TITULO = "#1E3A76"
COLOR_BOTON = "#3F5C92"
COLOR_BOTON_HOVER = "#2f4a78"
COLOR_BOTON_TEXTO = "#FFFFFF"
COLOR_SOMBRA = "#C3CFD9"

class InterfazMenu(Menu):
    def __init__(self, usuario, master=None):
        super().__init__(usuario)  # ✅ Inicializa correctamente la clase base Menu
        self.usuario = usuario

        if master is None:
            self.ventana = tk.Tk()
        else:
            self.ventana = master

        self.ventana.title(f"Asistente ZETA - {self.usuario.obtener_primer_nombre()}")
        self.ventana.geometry("500x500")
        self.ventana.configure(bg=COLOR_FONDO)

        titulo = tk.Label(
            self.ventana,
            text="ZETA",
            font=("Poppins", 36, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TITULO
        )
        titulo.pack(pady=60)

        marco_boton = tk.Frame(self.ventana, bg=COLOR_SOMBRA)
        marco_boton.pack(pady=20)

        boton = tk.Button(
            marco_boton,
            text="Iniciar Asistente",
            command=self.iniciar_asistente,
            bg=COLOR_BOTON,
            fg=COLOR_BOTON_TEXTO,
            font=("Poppins", 14, "bold"),
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )

        boton.pack()

        boton.bind("<Enter>", lambda e: boton.config(bg=COLOR_BOTON_HOVER))
        boton.bind("<Leave>", lambda e: boton.config(bg=COLOR_BOTON))

    def iniciar_asistente(self):
        self.ventana.destroy()
        super().ejecutar()  
        
    def mostrar_interfaz(self):
        self.ventana.mainloop()
