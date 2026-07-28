from capa2.llm import consultar_llm



class EvaluadorPortafolio:


    def evaluar(self, texto):


        prompt = f"""

Evalúa este portafolio académico.

Analiza:

- Coherencia.
- Organización.
- Uso de conceptos.
- Claridad.


Portafolio:

{texto}


Entrega una evaluación:

Coherencia:
Organización:
Uso de conceptos:
Recomendaciones:


"""


        return consultar_llm(prompt)