from playwright.sync_api import sync_playwright

URL = "https://cddistribution.com/pe/?s=ichibansho"

def obtener_html():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-first-run",
                "--disable-infobars",
            ]
        )

        context = browser.new_context(

            locale="es-PE",

            timezone_id="America/Lima",

            viewport={
                "width": 1366,
                "height": 768
            },

            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
        )

        page = context.new_page()

        # Oculta navigator.webdriver
        page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """)

        page.goto(URL, wait_until="networkidle", timeout=120000)

        page.wait_for_timeout(5000)

        print(page.title())

        html = page.content()

        browser.close()

        return html
