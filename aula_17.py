#1 - Crie uma classe chamada Cachorro com um atributo nome e um método latir que imprima "Woof!" quando chamado. Em seguida, crie um objeto da classe Cachorro e chame o método latir.

class Cachorro:
  def __init__(self, name):
    self.name = name
    
  def latir(self):
    print("Woof!")
    
cachorro = Cachorro("Totó")
cachorro.latir()


#2 - Crie uma classe chamada Retangulo com atributos largura e altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura
    
  def calcular_area(self):
    return self.largura * self.altura
    
retangulo = Retangulo(40,10)
print(retangulo.calcular_area())

#3: Crie uma classe chamada Carro com um atributo chamado velocidade (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta avelocidade em 5 unidades a cada vez que é chamado.

class Carro:
  def __init__(self, velocidade):
    self.velocidade = velocidade
    
  def acelerar(self):
    self.acelerar = self.velocidade + 5
    
carro = Carro(0)
carro.acelerar()
print(carro.acelerar)