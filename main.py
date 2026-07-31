
from scraper import obtener_productos
from storage import cargar_productos, guardar_productos
from telegram_bot import enviar_mensaje


def comparar(anteriores, actuales):

    antes = {
        p["url"]: p
        for p in anteriores
    }

    ahora = {
        p["url"]: p
        for p in actuales
    }

    nuevos = [
        ahora[x]
        for x in ahora
        if x not in antes
    ]

    eliminados = [
        antes[x]
        for x in antes
        if x not in ahora
    ]

    mensaje = ""

    if nuevos:
        mensaje += "🆕 Productos nuevos:\n\n"

        for p in nuevos:
            mensaje += f"- {p['nombre']}\n"

    if eliminados:
        mensaje += "\n❌ Productos retirados:\n\n"

        for p in eliminados:
            mensaje += f"- {p['nombre']}\n"


    if mensaje:
        enviar_mensaje(mensaje)


def ejecutar():

    anteriores = cargar_productos()

    actuales = obtener_productos()

    comparar(
        anteriores,
        actuales
    )

    guardar_productos(
        actuales
    )


if __name__ == "__main__":
    ejecutar()
