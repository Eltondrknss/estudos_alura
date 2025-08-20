class Contabancaria():

    ativo = False

    def __init__(self, titular, saldo:int):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f'O titular {self._titular} tem R${self._saldo} na conta.'
    
    @classmethod
    def ativar_conta(cls):
        cls.ativo = True


cliente1 = Contabancaria("Joao", 130)
cliente2 = Contabancaria("Maria", 983)
print(cliente1)
print(cliente2)
cliente1.ativar_conta()
print(cliente1.ativo)
print(f'Titular da conta: {cliente2._titular}')

##############################################################################

class ClienteBanco():

    vip = False

    def __init__(self, nome, idade:str, email, tipoconta):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.tipoconta = tipoconta

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos, usa o email {self.email} e tem a conta {self.tipoconta}.'
    
    @classmethod
    def ativar_vip(cls):
        cls.vip = True

    @classmethod
    def criar_conta(cls, nome, idade, email, tipoconta):
        conta = ClienteBanco(nome, idade, email, tipoconta)
        return conta
    
new_cliente01 = ClienteBanco.criar_conta("Malevola", 149, "male.vola@gmail.com", "Nivel Evil")


cliente01 = ClienteBanco("Cleidosvaldo", 94, "cleido@gmail.com", "nivel1")

print(cliente01)
cliente01.ativar_vip()
print(cliente01.vip)

print(new_cliente01)