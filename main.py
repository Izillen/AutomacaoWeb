from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    navegador = pw.chromium.launch(channel="msedge", headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://onibus.info/linhas")

    terminais = pagina.locator("[class=\"onibus-content\"]").get_by_text("expand_more").all()
    # pagina.locator("[id=\"Terminal Central\"]").get_by_text("0040").click()

    for terminal in terminais:
        linhas = terminal.locator()

    navegador.close()