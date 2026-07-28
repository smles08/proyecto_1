from capa2.llm import consultar_llm



class DetectorAyuda:


    def analizar(self, mensajes):


        texto = ""


        for mensaje in mensajes:

            texto += (
                f"Usuario: {mensaje['usuario']}\n"
                f"Mensaje: {mensaje['mensaje']}\n\n"
            )


        prompt = f"""

Analiza mensajes de estudiantes.

Detecta quienes podrían necesitar ayuda.

Considera:

- Confusión.
- Falta de comprensión.
- Comentarios negativos.
- Solicitudes de ayuda.


Mensajes:

{texto}


Responde:

Estudiantes que necesitan ayuda:

Nombre:
Motivo:


Si nadie necesita ayuda escribe:
"Ninguno"


"""


        return consultar_llm(prompt)