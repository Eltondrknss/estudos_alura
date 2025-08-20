class Pessoa():
    
    pessoas = []

    def __init__ (self, nome, idade: int, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__ (self):
        print(f'{"Nome".ljust(15)} | {"Idade".ljust(15)} | {"Profissão"}')
        return f'{self.nome.ljust(15)} | {str(self.idade).ljust(15)} | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    # @classmethod
    # def saudacao(cls):
    #     for pessoa in cls.pessoas:
    #         print(f'Meu nome é {pessoa.nome}. Eu tenho {pessoa.idade} anos e minha profissão é {pessoa.profissao}')

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
        
pessoa1 = Pessoa("Joao", 23, "CEO da NASA")
pessoa2 = Pessoa("beatriz", 19, "Dona da Zara")
pessoa3 = Pessoa("Marquito", 98, "Palhaço do programa do ratinho")

Pessoa.saudacao()
pessoa2.aniversario()
Pessoa.saudacao()
print(Pessoa.pessoas)