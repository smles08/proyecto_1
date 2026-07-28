from capa2.clasificador import Clasificador

clasificador = Clasificador()

ejemplos = [

    "¿Cómo hago el ejercicio 5?",

    "Yo lo resolví usando un ciclo for.",

    "Gracias profesor.",

    "No entiendo nada.",

    "La fecha de entrega es mañana."

]

for mensaje in ejemplos:

    categoria = clasificador.clasificar(mensaje)

    print("--------------------")
    print("Mensaje:")
    print(mensaje)
    print("Clasificación:")
    print(categoria)