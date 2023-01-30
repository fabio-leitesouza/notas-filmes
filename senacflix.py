class Catalogo:
  def __init__(self, nome, ano):
    self.__nome = nome.title()
    self.ano = ano
    self.__like = 0
  
  @property
  def like(self):
    return self.__like
  
  def dar_like(self):
    self.__like += 1

  @property
  def nome(self):
    return self.__nome  

  def __str__(self):
    return f'Nome: {self.nome} Likes: {self.like}'


class Filme(Catalogo):
  def __init__(self, nome, ano, genero, duracao):
    super().__init__(nome, ano)
    self.genero = genero
    self.duracao = duracao
  def __str__(self):
    return f'Nome: {self.nome} - Genero: {self.genero} {self.duracao} min - Likes: {self.like}'

class Serie(Catalogo):
  def __init__(self, nome, ano, genero, temporadas):
    super().__init__(nome, ano)
    self.genero = genero
    self.temporadas = temporadas
  def __str__(self):
    return f'Nome: {self.nome} - Genero: {self.genero} - Temporadas {self.temporadas} - Likes: {self.like}'

class Doc(Catalogo):
  def __init__(self, nome, ano, duracao, indicacao):
    super().__init__(nome, ano)
    self.duracao = duracao
    self.indicacao = indicacao
  def __str__(self):
    return f'Nome: {self.nome} - Likes: {self.like} - Indicativo {self.indicacao}'

class Animacao(Catalogo):
  def __init__(self, nome, ano, genero, temporada, indicacao):
    super().__init__(nome, ano)
    self.genero = genero
    self.temporada = temporada
    self.indicacao = indicacao  
  def __str__(self):
    return f'Nome: {self.nome} - Genero: {self.genero} - Temporadas: {self.temporada} - Likes: {self.like} - Indicativo {self.indicacao}'

class Play_list():
  def __init__(self, nome, catalogo):
    self.nome = nome
    self._catalogo = catalogo

  def __getitem__(self, item):
    return self._catalogo[item]

  def __len__(self):
    return len(self._catalogo)


evil_dead = Filme("Elvil Dead", 1982, "Terrir", 110)
stranger_things = Serie("Stranger Things", 2016, "Terror", 4)
cabra_marcado_para_morrer = Doc("Cabra marcado para morre", 1982, 120, 18)
invencivel = Animacao("Invencivel", 2020, "Humor", 2, 18)

evil_dead.dar_like()
evil_dead.dar_like()
evil_dead.dar_like()
  
cabra_marcado_para_morrer.dar_like()

# print(evil_dead.like)

listinha = [evil_dead, stranger_things, cabra_marcado_para_morrer, invencivel]

# for nomes in listinha:
#   print(nomes)

lista_fim_de_semana = Play_list("Maratona_FDS", listinha)

for programas in lista_fim_de_semana:
  print(programas)