from capa2.clasificador import Clasificador


def ejecutar_pruebas():
    clasificador = Clasificador()

    casos = [
        {
            "mensaje": "¿Cómo hago el ejercicio 5?",
            "esperada": "Pregunta"
        },
        {
            "mensaje": "Yo lo resolví usando un ciclo for.",
            "esperada": "Respuesta"
        },
        {
            "mensaje": "Gracias profesor.",
            "esperada": "Otro"
        },
        {
            "mensaje": "No entiendo cómo realizar el ejercicio.",
            "esperada": "Pregunta"
        },
        {
            "mensaje": "La fecha de entrega es mañana.",
            "esperada": "Otro"
        }
    ]

    correctas = 0

    print("=" * 50)
    print("PRUEBAS DE CLASIFICACIÓN")
    print("=" * 50)

    for numero, caso in enumerate(casos, start=1):

        resultado = clasificador.clasificar(caso["mensaje"])

        if resultado == caso["esperada"]:
            estado = "CORRECTO"
            correctas += 1
        else:
            estado = "INCORRECTO"

        print(f"\nPrueba {numero}")
        print(f"Mensaje: {caso['mensaje']}")
        print(f"Esperada: {caso['esperada']}")
        print(f"Obtenida: {resultado}")
        print(f"Resultado: {estado}")

    print("\n" + "=" * 50)
    print(f"Pruebas correctas: {correctas}/{len(casos)}")

    if correctas == len(casos):
        print("Todas las pruebas fueron exitosas.")
    else:
        print("Algunas pruebas necesitan revisión.")

    print("=" * 50)


if __name__ == "__main__":
    ejecutar_pruebas()