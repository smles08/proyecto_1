def prompt_clasificacion(mensaje):
    
    return f"""
Eres un clasificador de mensajes de foros universitarios.

Debes elegir SOLO una categoría:

Pregunta
Respuesta
Otro


REGLAS:

Pregunta:
- El estudiante tiene una duda.
- Solicita ayuda.
- Busca una explicación.
- Ejemplos:
  "¿Cómo hago el ejercicio?"
  "No entiendo este tema"
  "¿Alguien puede explicarme?"


Respuesta:
- El estudiante entrega una solución.
- Explica un procedimiento.
- Ayuda a otro estudiante.
- Ejemplos:
  "Yo lo resolví usando un ciclo for"
  "La solución es utilizar una condición if"


Otro:
- Saludos.
- Agradecimientos.
- Información general.
- Fechas o avisos.
- Ejemplos:
  "Gracias profesor"
  "La fecha de entrega es mañana"


IMPORTANTE:
Devuelve solamente una palabra:
Pregunta
Respuesta
Otro


Mensaje:
{mensaje}
"""