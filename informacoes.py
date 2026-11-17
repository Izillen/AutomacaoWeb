class Onibus:
    def __init__(self, nome, linha, nomeSentido):
        self.nome = nome
        self.linha = linha
        self.sentidos = Sentido(nomeSentido)


class Sentido:
    def __init__(self, nome):
        self.nome = nome
        self.paradas = []
        self.horarios = []

    def adicionar_horario(self, horario):
            self.horarios.append(horario)

    def adicionar_parada(self, parada):
        self.paradas.append(parada)