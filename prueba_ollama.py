from ollama import chat

respuesta = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Di únicamente la palabra Hola."
        }
    ]
)

print(respuesta["message"]["content"])