class Aluno:
  #função especial __init__
  def __init__(self, nome, nascimento, genero, matricula, nota = 0):
    self.__nome = nome
    self.__nascimento = nascimento
    self.__genero = genero
    self.__matricula = matricula
    self.__nota = nota

  def mostrar_nota(self):
    print("A nota de {} é {} pontos".format(self.__nome, self.__nota))

  def atribuir_nota(self, valor):
    self.__nota += valor
    
  def remover_nota(self, valor):
    self.__nota -= valor

  def get_nota(self):
    return self.__nota

  def get_matricula(self):
    return self.__matricula

  def get_genero(self):
    return self.__genero

  def set_genero(self, mudanca):
    self.__genero = mudanca

  @property
  def nome(self):
    print("Chamando @property nome()")
    return self.__nome

  @nome.setter
  def nome(self, nome):
    print("Chamando setter")
    self.__nome = nome

  def __pode_reduzir(self, valor_de_reducao):    
    return valor_de_reducao <= self.__nota

  def reducao_de_nota(self, valor_de_reducao):
    if(self.__pode_reduzir(valor_de_reducao)):
      self.__nota -= valor_de_reducao
    else:
      print("Redução maior do que a nota atual")

  @staticmethod
  def nome_senac_minas():
    return {"Senac Minas": "Itajubá"}
    
aluno = Aluno("Bruno", "01/01/2001", "M", 1100)

aluno.atribuir_nota(25)
aluno.remover_nota(10)

aluno.mostrar_nota()

print(aluno.get_nota())

aluno.set_genero("F")

print(aluno.get_genero())

print(aluno.nome)

aluno.nome = "Alkmin"

print(aluno.nome)

aluno.reducao_de_nota(16)
print(aluno.get_nota)

print(Aluno.nome_senac_minas())
