class Livro():

    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        icone_disponivel = "✅" if self.disponivel else "❌"
        return f'{icone_disponivel.ljust(5)} | {self.titulo.ljust(15)} | {self.autor.ljust(15)} | {str(self.ano_publicacao)}' 

    def emprestar(self):
        self.disponivel = False

    def listar(self):
        print("=" * 45)
        print(f'{"Status".ljust(5)} | {"Nome".ljust(15)} | {"Autor".ljust(15)} | {"Ano"}')
        print(self)

    @staticmethod
    def verificar_disponibilidade(ano):
        resultado = []
        for x in Livro.livros:
            if x.disponivel and x.ano_publicacao == ano:
                resultado.append(x)
        return resultado
    


livro1 = Livro ("Harry Potter", "Dumbledore", 2001)
livro2 = Livro ("Blade", "Dracula", 1934)
livro3 = Livro ("Rapunzel", "Valdisney", 1934)
livro4 = Livro ("Pinoquio", "Ze'da manga", 1921)

livro1.emprestar()

# livro1.listar()

# Livro.verificar_disponibilidade(1934)

livros_1934 = Livro.verificar_disponibilidade(1934)
for x in livros_1934:
    print(x.autor)
print(len(livros_1934))