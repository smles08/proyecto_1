class LectorArchivo:
    
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_foro(self):
        mensajes = []

        try:

            with open(self.ruta, "r", encoding="utf-8") as archivo:

                for linea in archivo:

                    linea = linea.strip()

                    if linea == "":
                        continue

                    partes = linea.split(",", 2)

                    if len(partes) == 3:

                        usuario = partes[0]
                        fecha = partes[1]
                        mensaje = partes[2]

                        mensajes.append({
                            "usuario": usuario,
                            "fecha": fecha,
                            "mensaje": mensaje
                        })

            return mensajes

        except FileNotFoundError:
            print("No se encontró el archivo.")
            return []

        except Exception as e:
            print(e)
            return []