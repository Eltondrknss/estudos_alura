class Restaurante:
    nome = ''
    categoria = 'pastelaria'
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#restaurante_pizza = Restaurante()
#restaurantes = [restaurante_praca, restaurante_pizza]

print (vars(restaurante_praca))
print ("------------------------------------------")

restaurante_praca.categoria = "Italiana"

print (restaurante_praca.nome)

if restaurante_praca.ativo:
    print (f"O restaurante {restaurante_praca.nome} está ativo")
else:
    print (f"O restaurante {restaurante_praca.nome} está inativo")

categoria = Restaurante.categoria
print (categoria)

restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

if restaurante_pizza.categoria == "Fast Food":
    print("A categoria é Fast Food")
else:
    print("A categoria não é Fast food")

restaurante_pizza.ativo = True

print (f"O nome do restaurante é {restaurante_pizza.nome} e a categoria dele é {restaurante_pizza.categoria}.")
