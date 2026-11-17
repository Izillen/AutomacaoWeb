from playwright.sync_api import sync_playwright
from informacoes import Onibus, Sentido

with sync_playwright() as pw:
    navegador = pw.chromium.launch(channel="msedge", headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://onibus.info/linhas")

    terminais = pagina.locator(".onibus-content").get_by_text("expand_more").all()
    # pagina.locator("[id=\"Terminal Central\"]").get_by_text("0040").click()

    for terminal in terminais:
        if terminal.is_visible():
            terminal.click()

            for linha in pagina.locator(".mdl-card__actions").get_by_role("link").all():
                with contexto.expect_page() as nova_pagina:
                    linha.click()

                paginaLinha = nova_pagina.value
                paginaLinha.wait_for_load_state("networkidle")

                novoObjeto = Onibus(paginaLinha.locator(".mdl-typography--title").inner_text(), paginaLinha.locator(".onibus-routes__id-big").inner_text())

                paginaLinha.get_by_role("link", name="Horários").click()

                sentidosPagina = paginaLinha.locator(".onibus-route__direction-mid").get_by_role("link").all()

                for sentidoPagina in sentidosPagina:
                    novoObjeto.sentidos = Sentido(sentidoPagina.inner_text())

                enderecos = paginaLinha.locator(".timeline").get_by_role("link").all()
                for endereco in enderecos:
                    if endereco.is_visible():
                        novoObjeto.adicionar_parada(endereco.inner_text())

                itemHorario = paginaLinha.get_by_role("link", name="Horários").click()



                paginaLinha.go_back()
                paginaLinha.wait_for_load_state("networkidle")

    navegador.close()