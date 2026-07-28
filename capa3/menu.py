class Menu:
    

    def mostrar(self):

        print("\n==============================")
        print(" ANALISIS DE PORTAFOLIOS LLM ")
        print("==============================")

        print("1. Clasificar mensajes del foro")
        print("2. Generar resumen del foro")
        print("3. Detectar estudiantes que necesitan ayuda")
        print("4. Evaluar portafolio")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        return opcion