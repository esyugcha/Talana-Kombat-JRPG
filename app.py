import os
import json
from juego.personaje import Personaje
from juego.combinacion import Combinacion
from juego.juego import Juego

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            decodificar_json(contenido=contenido)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def decodificar_json(contenido):
    datos = json.loads(contenido)
    iniciar_juego(datos=datos)

def iniciar_juego(datos):
    jugador1 = datos["player1"]
    jugador2 = datos["player2"]

    movimientos_jugador1 = jugador1["movimientos"]
    movimientos_jugador2 = jugador2["movimientos"]

    golpes_jugador1 = jugador1["golpes"]
    golpes_jugador2 = jugador2["golpes"]

    combinacion1_tonyn = Combinacion("DSDP", 3, "Taladoken")
    combinacion2_tonyn = Combinacion("SDK", 2, "Remuyuken")
    combinacion1_arnaldor = Combinacion("SAK", 3, "Remuyuken")
    combinacion2_arnaldor = Combinacion("ASAP", 2, "Taladoken")

    combinaciones_tonyn = [combinacion1_tonyn, combinacion2_tonyn]
    combinaciones_arnaldor = [combinacion1_arnaldor, combinacion2_arnaldor]

    player1 = Personaje(nombre=Personaje.PERSONA_TYNON, movimientos=movimientos_jugador1, golpes=golpes_jugador1,
                        combos=combinaciones_tonyn)
    player2 = Personaje(nombre=Personaje.PERSONA_ARNALDOR, movimientos=movimientos_jugador2, golpes=golpes_jugador2,
                        combos=combinaciones_arnaldor)

    juego = Juego(player1=player1, player2=player2)
    juego.combate()


if __name__ == "__main__":
    json_files_folder = os.path.join(os.path.dirname(__file__), "json_files")

    nombres_archivos = ["combate.json", "combate2.json", "combate3.json"]

    for nombre_archivo in nombres_archivos:
        ruta_archivo = os.path.join(json_files_folder, nombre_archivo)
        print(f"ARCHIVO: {ruta_archivo}")
        procesar_archivo(ruta_archivo)
