from ollama import chat


def consultar_llm(prompt):

    respuesta = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente experto en análisis educativo y clasificación de textos."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return respuesta["message"]["content"].strip()