class Carro:
  def __init__(self, marca, valor, portas, tanque):
    self.marca = marca
    self.valor = valor
    self.portas = portas
    self.tanque = tanque

  def abastece(self, encher):
    if self.tanque >= 50:
      print("Tanque cheio.")
    else:  
      self.tanque += encher
      if self.tanque > 50:
        self.tanque = 50
        print("Tanque com capacidade máxina de 50 litros.")

  def dirigir(self, anda):
      km = 10
      self.tanque = self.tanque - (anda / km)
      


x1= Carro("BMW", 200000.00, 4, 0)


x1.abastece(50)
print(x1.tanque)
x1.dirigir(200)
print(x1.tanque)
x1.abastece(100)
print(x1.tanque)
