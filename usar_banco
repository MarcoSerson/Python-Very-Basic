class Banco:
  def __init__(self, nome, saldo):
    self.nome = nome
    self.saldo = saldo
    

  def saque(self, valor):
    self.saldo -= valor
    print(f"Voce sacou R$ {valor}, e seu saldo atual é {self.saldo}")

  def deposito(self, valor2):
    self.saldo += valor2
    print(f"Voce depositou R$ {valor2}, e seu saldo atual é {self.saldo}")

  def transferir(self, valor3, usu):
     self.saldo -= valor3
     usu.saldo += valor3
     print(f"Voce transferiu R$ {valor3} para {usu.nome}. Voce agora tem R$ {self.saldo} e a outra pessoa tem R$ {usu.saldo}")
          

usuario = Banco("Marco", 500) 
usuario2 = Banco("Sabrina", 100)
print(usuario.nome, usuario.saldo)
print(usuario2.nome, usuario2.saldo)


usuario.saque(50) 

usuario.deposito(100)

usuario.transferir(200, usuario2)
