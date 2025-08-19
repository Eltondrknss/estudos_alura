class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #primeira letra maiuscula
        self._categoria = categoria.upper() #todas maiusculas
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.listar_restaurantes()