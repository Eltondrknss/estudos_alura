from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Fast Food")
restaurante_sujeira = Restaurante("Podrão", "Comida caseira")
restaurante_frufru = Restaurante("Bife de unicórnio", "Gourmet")

restaurante_frufru.receber_avaliacao("Chico", 5)
restaurante_frufru.receber_avaliacao("Joana", 10)
restaurante_frufru.receber_avaliacao("Felca", 8)


restaurante_sujeira.alternar_estado()

def main():
    Restaurante.listar_restaurantes()





if __name__ == "__main__":
    main()

