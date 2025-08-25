from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #primeira letra maiuscula
        self._categoria = categoria.upper() #todas maiusculas
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(15)} | {"Avaliação".ljust(15)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(15)} | {str(restaurante.media_avaliacao).ljust(15)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if nota <= 5:
            self._avaliacao.append(avaliacao)
        else:
            print(f"{cliente}, a nota maxima permitida é 5")

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "Sem avaliações"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media