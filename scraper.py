import requests
from bs4 import BeautifulSoup


def obtener_productos():
    """
    Función principal del scraper.
    Retorna una lista de productos.
    """

    productos = []

    try:
        # URL de prueba (puedes cambiarla por tu fuente real)
        url = "https://example.com"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            productos.append({
                "nombre": "Scraper funcionando",
                "precio": 0,
                "estado": "OK"
            })

        else:
            productos.append({
                "nombre": "Error HTTP",
                "precio": 0,
                "estado": response.status_code
            })

    except Exception as e:
        productos.append({
            "nombre": "Error scraper",
            "precio": 0,
            "estado": str(e)
        })

    return productos
