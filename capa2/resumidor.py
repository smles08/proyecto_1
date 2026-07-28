from capa2.llm import consultar_llm


class Resumidor:


    def resumir(self, mensajes):

        texto = ""

        for mensaje in mensajes:
            texto += (
                f"{mensaje['usuario']}: "
                f"{mensaje['mensaje']}\n"
            )


        prompt = f"""

Analiza los siguientes mensajes de un foro académico.

Realiza:

1. Un resumen general.
2. Extrae los temas principales.
3. Identifica los problemas más frecuentes.


Mensajes:

{texto}


Formato:

Resumen:
-

Temas principales:
-
-
-

Problemas detectados:
-
-

"""


        respuesta = consultar_llm(prompt)

        return respuesta