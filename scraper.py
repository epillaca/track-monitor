from playwright.sync_api import sync_playwright


URL = "https://cddistribution.com/pe/backorder-coleccionables/"


def obtener_productos():

    productos = []

    with sync_playwright() as p:

        navegador = p.chromium.launch(
            headless=True
        )

        pagina = navegador.new_page()

        pagina.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=90000
        )

        pagina.wait_for_timeout(8000)

        tarjetas = pagina.locator(
            "li.product"
        )

        cantidad = tarjetas.count()

        print("Productos encontrados:", cantidad)

        for i in range(cantidad):

            producto = tarjetas.nth(i)

            try:
                nombre = producto.locator(
                    ".woocommerce-loop-product__title"
                ).inner_text()

            except:
                continue

            try:
                enlace = producto.locator(
                    "a"
                ).first.get_attribute("href")

            except:
                enlace = ""

            try:
                precio = producto.locator(
                    ".price"
                ).inner_text()

            except:
                precio = ""

            productos.append(
                {
                    "nombre": nombre.strip(),
                    "url": enlace,
                    "precio": precio.strip()
                }
            )

        navegador.close()

    return productos
