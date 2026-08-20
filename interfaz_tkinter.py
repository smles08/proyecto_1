import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from capa1.lector import LectorArchivo
from capa2.clasificador import Clasificador
from capa2.resumidor import Resumidor
from capa2.ayuda import DetectorAyuda
from capa2.evaluador import EvaluadorPortafolio


class Interfaz:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title("Análisis de Portafolios LLM")
        self.ventana.geometry("900x650")

        self.mensajes = []

        # =========================
        # TÍTULO
        # =========================

        titulo = tk.Label(
            ventana,
            text="ANÁLISIS DE PORTAFOLIOS LLM",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=15)

        # =========================
        # BOTONES
        # =========================

        frame_botones = tk.Frame(ventana)

        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Cargar foro",
            width=18,
            command=self.cargar_foro
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            frame_botones,
            text="Clasificar mensaje",
            width=18,
            command=self.clasificar_mensaje
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            frame_botones,
            text="Resumir foro",
            width=18,
            command=self.resumir_foro
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            frame_botones,
            text="Detectar ayuda",
            width=18,
            command=self.detectar_ayuda
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            frame_botones,
            text="Evaluar portafolio",
            width=18,
            command=self.evaluar_portafolio
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            frame_botones,
            text="Limpiar",
            width=18,
            command=self.limpiar
        ).grid(row=1, column=2, padx=5, pady=5)

        # =========================
        # MENSAJE
        # =========================

        tk.Label(
            ventana,
            text="Escribe un mensaje del foro:",
            font=("Arial", 12, "bold")
        ).pack(pady=(15, 5))

        self.entrada = tk.Text(
            ventana,
            height=5,
            width=95
        )

        self.entrada.pack()

        # =========================
        # RESULTADO
        # =========================

        tk.Label(
            ventana,
            text="Resultado:",
            font=("Arial", 12, "bold")
        ).pack(pady=(15, 5))

        self.resultado = scrolledtext.ScrolledText(
            ventana,
            width=100,
            height=20
        )

        self.resultado.pack(
            padx=10,
            pady=5
        )

    # ==================================================
    # CARGAR FORO
    # ==================================================

    def cargar_foro(self):

        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo del foro",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not ruta:
            return

        try:

            lector = LectorArchivo(ruta)

            self.mensajes = lector.leer_foro()

            self.resultado.delete(
                "1.0",
                tk.END
            )

            self.resultado.insert(
                tk.END,
                "FORO CARGADO CORRECTAMENTE\n"
                "============================\n\n"
            )

            self.resultado.insert(
                tk.END,
                f"Mensajes encontrados: "
                f"{len(self.mensajes)}\n\n"
            )

            for mensaje in self.mensajes:

                self.resultado.insert(
                    tk.END,
                    f"Usuario: {mensaje['usuario']}\n"
                    f"Mensaje: {mensaje['mensaje']}\n"
                    f"{'-' * 60}\n"
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo cargar el foro:\n\n{error}"
            )

    # ==================================================
    # CLASIFICAR MENSAJE
    # ==================================================

    def clasificar_mensaje(self):

        mensaje = self.entrada.get(
            "1.0",
            tk.END
        ).strip()

        if not mensaje:

            messagebox.showwarning(
                "Mensaje vacío",
                "Escribe un mensaje antes de clasificarlo."
            )

            return

        try:

            clasificador = Clasificador()

            categoria = clasificador.clasificar(
                mensaje
            )

            self.resultado.delete(
                "1.0",
                tk.END
            )

            self.resultado.insert(
                tk.END,
                "CLASIFICACIÓN DEL MENSAJE\n"
                "==========================\n\n"
            )

            self.resultado.insert(
                tk.END,
                f"Mensaje:\n{mensaje}\n\n"
                f"Clasificación: {categoria}"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo clasificar el mensaje:\n\n{error}"
            )

    # ==================================================
    # RESUMIR FORO
    # ==================================================

    def resumir_foro(self):

        if not self.mensajes:

            messagebox.showwarning(
                "Sin datos",
                "Primero debes cargar un archivo del foro."
            )

            return

        try:

            resumidor = Resumidor()

            resumen = resumidor.resumir(
                self.mensajes
            )

            self.resultado.delete(
                "1.0",
                tk.END
            )

            self.resultado.insert(
                tk.END,
                "RESUMEN DEL FORO\n"
                "=================\n\n"
            )

            self.resultado.insert(
                tk.END,
                resumen
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo generar el resumen:\n\n{error}"
            )

    # ==================================================
    # DETECTAR AYUDA
    # ==================================================

    def detectar_ayuda(self):

        if not self.mensajes:

            messagebox.showwarning(
                "Sin datos",
                "Primero debes cargar un archivo del foro."
            )

            return

        try:

            detector = DetectorAyuda()

            resultado = detector.analizar(
                self.mensajes
            )

            self.resultado.delete(
                "1.0",
                tk.END
            )

            self.resultado.insert(
                tk.END,
                "ESTUDIANTES QUE NECESITAN AYUDA\n"
                "================================\n\n"
            )

            self.resultado.insert(
                tk.END,
                resultado
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo analizar el foro:\n\n{error}"
            )

    # ==================================================
    # EVALUAR PORTAFOLIO
    # ==================================================

    def evaluar_portafolio(self):

        try:

            ruta = filedialog.askopenfilename(
                title="Seleccionar portafolio",
                filetypes=[
                    ("Archivos de texto", "*.txt"),
                    ("Todos los archivos", "*.*")
                ]
            )

            if not ruta:
                return

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                texto = archivo.read()

            if not texto.strip():

                messagebox.showwarning(
                    "Portafolio vacío",
                    "El archivo seleccionado está vacío."
                )

                return

            evaluador = EvaluadorPortafolio()

            evaluacion = evaluador.evaluar(
                texto
            )

            self.resultado.delete(
                "1.0",
                tk.END
            )

            self.resultado.insert(
                tk.END,
                "EVALUACIÓN DEL PORTAFOLIO\n"
                "=========================\n\n"
            )

            self.resultado.insert(
                tk.END,
                evaluacion
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo evaluar el portafolio:\n\n{error}"
            )

    # ==================================================
    # LIMPIAR
    # ==================================================

    def limpiar(self):

        self.entrada.delete(
            "1.0",
            tk.END
        )

        self.resultado.delete(
            "1.0",
            tk.END
        )


# ======================================================
# EJECUTAR INTERFAZ
# ======================================================

if __name__ == "__main__":

    ventana = tk.Tk()

    app = Interfaz(
        ventana
    )

    ventana.mainloop()