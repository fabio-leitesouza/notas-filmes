class Jogo:
  #função especial __init__
  def __init__(self, titulo, ano, genero, plataforma):
    self.titulo = titulo
    self.ano = ano
    self.genero = genero
    self.plataforma = plataforma
#zelda é a refencia para usar meu objeto
zelda = Jogo("Zelda", 1986, "Aventura", "Nintendinho")

print(zelda.titulo)