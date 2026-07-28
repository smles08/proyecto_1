from capa1.lector import LectorArchivo

from capa2.clasificador import Clasificador
from capa2.resumidor import Resumidor
from capa2.ayuda import DetectorAyuda
from capa2.evaluador import EvaluadorPortafolio


from capa3.menu import Menu
from capa3.salida import Salida
from capa3.validador import Validador



class CLI:


    def __init__(self):

        self.menu = Menu()

        self.salida = Salida()

        self.validador = Validador()



        self.lector = LectorArchivo(
            "datos/foro.txt"
        )


        self.mensajes = (
            self.lector.leer_foro()
        )



    def iniciar(self):


        while True:


            opcion = self.menu.mostrar()



            if not self.validador.opcion_menu(opcion):

                print(
                    "Opción inválida"
                )

                continue



            if opcion == "1":

                self.clasificar()



            elif opcion == "2":

                self.resumir()



            elif opcion == "3":

                self.detectar_ayuda()



            elif opcion == "4":

                self.evaluar_portafolio()



            elif opcion == "5":

                print(
                    "\nPrograma finalizado"
                )

                break




    def clasificar(self):


        self.salida.titulo(
            "CLASIFICACIÓN DE MENSAJES"
        )


        clasificador = Clasificador()



        for mensaje in self.mensajes:


            categoria = clasificador.clasificar(
                mensaje["mensaje"]
            )


            self.salida.mostrar_clasificacion(

                mensaje["usuario"],

                mensaje["mensaje"],

                categoria
            )




    def resumir(self):


        self.salida.titulo(
            "RESUMEN DEL FORO"
        )


        resumidor = Resumidor()


        resultado = resumidor.resumir(
            self.mensajes
        )


        self.salida.mostrar_texto(
            resultado
        )




    def detectar_ayuda(self):


        self.salida.titulo(
            "ESTUDIANTES QUE NECESITAN AYUDA"
        )


        detector = DetectorAyuda()



        resultado = detector.analizar(
            self.mensajes
        )


        self.salida.mostrar_texto(
            resultado
        )




    def evaluar_portafolio(self):


        self.salida.titulo(
            "EVALUACIÓN DEL PORTAFOLIO"
        )


        try:


            with open(
                "datos/portafolio.txt",
                encoding="utf-8"
            ) as archivo:


                texto = archivo.read()



            evaluador = EvaluadorPortafolio()



            resultado = evaluador.evaluar(
                texto
            )


            self.salida.mostrar_texto(
                resultado
            )



        except FileNotFoundError:


            print(
                "No existe portafolio.txt"
            )