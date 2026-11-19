from playwright.sync_api import sync_playwright
from informacoes import Onibus, Sentido, Horarios
import json

listaInformacoes = []

with sync_playwright() as pw:
    navegador = pw.chromium.launch(channel="msedge", headless=True)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://onibus.info/linhas")

    terminais = pagina.locator(".onibus-content").get_by_text("expand_more").all()
    # pagina.locator("[id=\"Terminal Central\"]").get_by_text("0040").click()

    for terminal in terminais:
        if terminal.is_visible():
            terminal.click()

            links = pagina.locator(".mdl-card__actions").get_by_role("link")
            urls = links.evaluate_all("elements => elements.map(element => element.href)")

            for url in urls:
                pagina.goto(url)
                pagina.wait_for_load_state("domcontentloaded")
            
                pagina.get_by_role("link", name="Horários").click()
                pagina.get_by_text("Ver tabela horário").click()
                pagina.wait_for_load_state("domcontentloaded")

                novoObjeto = Onibus(pagina.locator(".mdl-typography--headline").nth(0).inner_text(), pagina.locator(".onibus-routes__id-big").nth(0).inner_text())
                sentidosPagina = pagina.locator(".onibus-route__direction-mid").locator(".onibus-text-strong").all()  

                for i in range(len(sentidosPagina)):
                    sentido = Sentido(sentidosPagina[i].inner_text())

                    if len(sentidosPagina) == 1:
                        divHorario = pagina.locator("#general-timetable")
                    else:
                        divHorario = pagina.locator("#general-timetable").locator(f"#tt-{i}")

                    tabelasHorarios = divHorario.locator(".timetable-print").all()
                    for cell in tabelasHorarios:
                        listaHorarioslocator = cell.locator(".onibus-route__time-cell").all()
                        listaHorarios = [horario.inner_text() for horario in listaHorarioslocator]
                        horario = Horarios(cell.locator(".onibus-text-regular").inner_text())
                        horario.adicionar_horario(listaHorarios)
                        sentido.adicionar_listahorario(horario)    

                    paradas = divHorario.locator("#timetable-itinerary").locator(".ng-binding").all()
                    for parada in paradas:
                        sentido.adicionar_parada(parada.inner_text())

                    novoObjeto.adicionarSentido(sentido)

                listaInformacoes.append(novoObjeto)
                pagina.go_back()
                pagina.wait_for_load_state("networkidle")


    dados = [onibus.to_dict() for onibus in listaInformacoes]
    with open("onibus.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print("Arquivo JSON gerado com sucesso!")

    navegador.close()