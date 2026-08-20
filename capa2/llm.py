from ollama import chat


def consultar_llm(prompt):

    try:
        respuesta = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un asistente experto en análisis educativo "
                        "y clasificación de textos."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return respuesta["message"]["content"].strip()

    except Exception as error:
        print("\nError al comunicarse con Ollama.")
        print("Verifica que Ollama esté instalado y ejecutándose.")
        print("También verifica que el modelo llama3.2 esté disponible.")
        print(f"Detalle: {error}")

        return "Otro"