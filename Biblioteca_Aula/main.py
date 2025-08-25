from  classe_biblioteca import Livro

livro001 = Livro ("dicionario", "Aurelio", 1921)
livro002 = Livro ("Bula Dorflex", "Sidnei Moreira", 1932)
livro003 = Livro ("A cabana", "Alguem", 1999)

livro002.emprestar()
livro001.listar()
print(livro002)
print(livro003)

temalgum = Livro.verificar_disponibilidade(1921)
print(temalgum)