class Onibus:
    def __init__(self, nome, linha):
        self.nome = nome
        self.linha = linha
        self.sentidos: list[Sentido] = []

    def adicionarSentido(self, sentido: Sentido):
        self.sentidos.append(sentido)

    def to_dict(self):
        return {
            "nomeLinha": self.nome,
            "linha": self.linha,
            "sentidos": [sentido.to_dict() for sentido in self.sentidos]
        }

class Sentido:
    def __init__(self, nome):
        self.nome = nome
        self.paradas = []
        self.horarios: list[Horarios] = []

    def adicionar_listahorario(self, horarios: Horarios):
            self.horarios.append(horarios)

    def adicionar_parada(self, parada):
        self.paradas.append(parada)

    def to_dict(self):
        return {
            "nomeSentido": self.nome,
            "paradas": self.paradas,
            "horarios": [horario.to_dict() for horario in self.horarios]
        }

class Horarios:
    def __init__(self, diaSemana):
        self.diaSemana = diaSemana
        self.horario = []

    def adicionar_horario(self, horario):
        self.horario.append(horario)

    def to_dict(self):
        return {
            "diaSemana": self.diaSemana,
            "horarios": self.horario
        }

