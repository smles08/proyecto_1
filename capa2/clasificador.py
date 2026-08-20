from capa2.prompts import prompt_clasificacion
from capa2.llm import consultar_llm


class Clasificador:

    def clasificar(self, mensaje):

        texto = mensaje.lower().strip()

        if not texto:
            return "Otro"

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
            "puedo",
            "podría",
            "podria",
            "duda"
        ]

        palabras_respuesta = [
            "yo lo resolví",
            "yo lo resolvi",
            "la solución",
            "la solucion",
            "se realiza",
            "debes usar",
            "utiliza",
            "puedes hacerlo",
            "en mi caso",
            "la respuesta es"
        ]

        if any(palabra in texto for palabra in palabras_pregunta):
            return "Pregunta"

        if any(palabra in texto for palabra in palabras_respuesta):
            return "Respuesta"

        prompt = prompt_clasificacion(mensaje)
        categoria = consultar_llm(prompt)

        categoria = categoria.strip().lower()

        if "pregunta" in categoria:
            return "Pregunta"

        if "respuesta" in categoria:
            return "Respuesta"

        return "Otro"