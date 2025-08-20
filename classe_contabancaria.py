class Contabancaria():

    ativo = False

    def __init__(self, titular, saldo:int):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'O titular {self.titular} tem R${self.saldo} na conta.'
    
    @classmethod
    def ativar_conta(cls):
        cls.ativo = True

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


cliente1 = Contabancaria("Joao", 130)
cliente2 = Contabancaria("Maria", 983)
print(cliente1)
cliente1.ativar_conta()
print(cliente1.ativo)

cliente01 = ClienteBanco("Cleidosvaldo", 94, "cleido@gmail.com", "nivel1")

print(cliente01)
cliente01.ativar_vip()
print(cliente01.vip)
