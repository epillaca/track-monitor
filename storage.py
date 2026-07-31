
import json
import os

FILE = "productos.json"


def cargar_productos():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_productos(productos):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            productos,
            f,
            ensure_ascii=False,
            indent=2
        )
