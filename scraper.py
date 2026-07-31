from playwright.sync_api import sync_playwright


URL = "https://cddistribution.com/pe/backorder-coleccionables/"


def obtener_productos():
    productos = []

    with sync_playwright() as p:

        navegador = p.chromium.launch(
            headless=True
        )

        pagina = navegador.new_page(
            viewport={
                "width": 1280,
                "height": 1200
            }
        )

        pagina.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=90000
        )

        pagina.wait_for_timeout(8000)

        pagina.screenshot(
            path="pagina.png",
            full_page=True
        )

        html = pagina.content()

        with open(
            "pagina.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)

        tarjetas = pagina.locator("li.product")

        cantidad = tarjetas.count()

        print("Productos encontrados:", cantidad)

        for i in range(cantidad):

            producto = tarjetas.nth(i)

            try:
                nombre = producto.locator(
                    ".woocommerce-loop-product__title"
                ).inner_text()
            except:
                nombre = ""

            try:
                enlace = producto.locator(
                    "a"
                ).first.get_attribute(
                    "href"
                )
            except:
                enlace = ""

            try:
                precio = producto.locator(
                    ".price"
                ).inner_text()
            except:
                precio = ""

            if nombre:
                productos.append(
                    {
                        "nombre": nombre.strip(),
                        "url": enlace,
                        "precio": precio.strip()
                    }
                )

        navegador.close()

    return productos


# Verificación para evitar errores de importación
if __name__ == "__main__":
    print(obtener_productos())
