from capa2.prompts import prompt_clasificacion
from capa2.llm import consultar_llm


class Clasificador:

    def clasificar(self, mensaje):

        texto = mensaje.lower()


        # Validaciones directas

        palabras_pregunta = [
            "cómo",
            "como",
            "qué",
            "que",
            "por qué",
            "porque",
            "alguien sabe",
            "no entiendo",
            "ayuda",
            "puedo"
        ]


        palabras_respuesta = [
            "yo lo resolví",
            "la solución",
            "se realiza",
            "debes usar",
            "utiliza",
            "puedes hacerlo"
        ]


        if any(palabra in texto for palabra in palabras_pregunta):
            return "Pregunta"


        if any(palabra in texto for palabra in palabras_respuesta):
            return "Respuesta"


        # Si no coincide, usa el LLM

        prompt = prompt_clasificacion(mensaje)

        categoria = consultar_llm(prompt)


        categoria = categoria.strip().lower()


        if "pregunta" in categoria:
            return "Pregunta"

        elif "respuesta" in categoria:
            return "Respuesta"

        else:
            return "Otro"