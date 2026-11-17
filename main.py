from playwright.sync_api import sync_playwright
from informacoes import Onibus, Sentido

listaInformacoes = []

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
                linha.click()

                pagina.wait_for_load_state("domcontentloaded")
            
                novoObjeto = Onibus(pagina.locator(".mdl-typography--title").inner_text(), pagina.locator(".onibus-routes__id-big").inner_text())

                pagina.get_by_role("link", name="Horários").click()
                pagina.get_by_text("Ver tabela horário").click()
                sentidosPagina = pagina.locator(".onibus-route__direction-mid").locator(".onibus-text-strong").all()

                for i in range(len(sentidosPagina)):
                    sentido = Sentido(sentidosPagina[i].inner_text())

                    horarios = pagina.locator(".onibus-route__time-cell").all()
                    for horario in horarios:
                        sentido.adicionar_horario(horario.inner_text())

                    paradas = sentidosPagina[i].locator("#timetable-itinerary").locator(".ng-scope").all()
                    for parada in paradas:
                        sentido.adicionar_parada(parada.inner_text())

                    novoObjeto.adicionarSentido(sentido)

                listaInformacoes.append(novoObjeto)
                pagina.go_back()
                pagina.wait_for_load_state("networkidle")

    print(listaInformacoes)

    navegador.close()