class Onibus:
    def __init__(self, nome, linha):
        self.nome = nome
        self.linha = linha
        self.sentidos: list[Sentido] = []

        def adicionarSentido(self, sentido: Sentido):
            self.sentidos.append(sentido)

class Sentido:
    def __init__(self, nome):
        self.nome = nome
        self.paradas = []
        self.horarios = []

    def adicionar_horario(self, horario):
            self.horarios.append(horario)

    def adicionar_parada(self, parada):
        self.paradas.append(parada)