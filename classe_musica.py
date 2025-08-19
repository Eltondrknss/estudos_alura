class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'In the End'
musica1.artista = 'Linkin Park'
musica1.duracao = 339

musica2 = Musica()
musica2.nome = 'Clube dos Canalhas'
musica2.artista = 'Matanza'
musica2.duracao = 308

musica3 = Musica()
musica3.nome = 'Teto de Vidro'
musica3.artista = 'Pitty'
musica3.duracao = 347

musicas = [musica1, musica2, musica3]

print(vars(musica1))