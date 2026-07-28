class Salida:
    

    def titulo(self, texto):

        print("\n")
        print("=" * 40)
        print(texto)
        print("=" * 40)



    def mostrar_clasificacion(
            self,
            usuario,
            mensaje,
            categoria
    ):

        print("\n--------------------------")

        print("Usuario:")
        print(usuario)

        print("Mensaje:")
        print(mensaje)

        print("Clasificación:")
        print(categoria)



    def mostrar_texto(self, texto):

        print("\n")
        print(texto)