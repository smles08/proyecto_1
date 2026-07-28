from capa1.lector import LectorArchivo

lector = LectorArchivo("datos/foro.txt")

mensajes = lector.leer_foro()

for mensaje in mensajes:
    print(mensaje)