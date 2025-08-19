class Carro():

    def __init__(self, modelo, cor, ano: str):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
    def __str__(self):
        return f"O carro é um {self.modelo}, da cor {self.cor}, fabricado no ano de {self.ano}."

class Restaurante():

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.entrega = False
        self.rodizio = False

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    def resumo_restaurante(self):
        tem_entrega = ""
        tem_rodizio = ""
        
        if self.entrega:
            tem_entrega = "faz entregas"
        else:
            tem_entrega = "não faz entregas"
        
        if self.rodizio:
            tem_rodizio = "tem rodízio"
        else:
            tem_rodizio = "não tem rodízio"

        if self.ativo:
            esta_ativo = "está ativo"
        else:
            esta_ativo = "não está ativo"

        print(f"O restaurante {self.nome} é da categoria {self.categoria}. Ele {tem_entrega}, {tem_rodizio}, e no momento {esta_ativo}.")

class Cliente():
    def __init__(self, cadastro: str, nome, sexo, prato_favorito):
        self.cadastro = cadastro
        self.nome = nome
        self.sexo = sexo
        self.prato_favorito = prato_favorito
    
    def __str__(self):
        return f"{self.cadastro} | {self.nome} | {self.sexo} | {self.prato_favorito}"

restaurante1 = Restaurante("Copo Sujo", "Boteco")
restaurante1.ativo = True
restaurante1.entrega = True
restaurante1.rodizio = False

restaurante1.resumo_restaurante()
print(restaurante1)

cliente1 = Cliente(1, "Joao", "Masculino", "Chuleta")
cliente2 = Cliente(2, "Roberta", "Feminino", "File de frango")
cliente3 = Cliente(3, "Aline", "Feminino", "Batata Frita")
cliente4 = Cliente(4, "Jubileu", "Masculino", "Pinga")

clientes = [cliente1, cliente2, cliente3, cliente4]

for Cliente in clientes:
    print(Cliente)

carro1 = Carro("Fusca", "Azul", 1931)

print (carro1)