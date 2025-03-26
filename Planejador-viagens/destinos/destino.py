class DestinationInfo:
  def __init__(self):
      self._destinations = {
          "Paris": {"descrição": "Cidade Luz, famosa pela Torre Eiffel e pela gastronomia requintada.", "preço": "Alto", "continente": "Europa"},
          "Nova York": {"descrição": "Metrópole vibrante, lar da Estátua da Liberdade e da Times Square.", "preço": "Alto", "continente": "América do Norte"},
          "Tóquio": {"descrição": "Capital do Japão, mescla tecnologia de ponta e tradição, com templos históricos.", "preço": "Alto", "continente": "Ásia"},
          "Roma": {"descrição": "Cidade antiga com o icônico Coliseu e rica história do Império Romano.", "preço": "Médio", "continente": "Europa"},
          "Rio de Janeiro": {"descrição": "Cidade brasileira famosa pela praia de Copacabana e o Cristo Redentor.", "preço": "Médio", "continente": "América do Sul"},
          "Londres": {"descrição": "Cidade multicultural com o Big Ben e a Torre de Londres.", "preço": "Alto", "continente": "Europa"},
          "Cairo": {"descrição": "Cidade egípcia com as Grandes Pirâmides e o Museu Egípcio.", "preço": "Baixo", "continente": "África"},
          "Sydney": {"descrição": "Cidade portuária com a icônica Ópera de Sydney e belas praias.", "preço": "Alto", "continente": "Oceania"},
          "Barcelona": {"descrição": "Cidade espanhola com arquitetura de Gaudí e vida noturna vibrante.", "preço": "Médio", "continente": "Europa"},
          "Pequim": {"descrição": "Capital chinesa com a Cidade Proibida e a Grande Muralha.", "preço": "Médio", "continente": "Ásia"},
          "Cape Town": {"descrição": "Cidade sul-africana com Table Mountain e paisagens deslumbrantes.", "preço": "Baixo", "continente": "África"},
          "Amsterdã": {"descrição": "Cidade dos canais, famosa por seus museus e vida noturna.", "preço": "Médio", "continente": "Europa"},
          "Dubai": {"descrição": "Cidade dos Emirados, conhecida por sua arquitetura moderna e luxo.", "preço": "Alto", "continente": "Ásia"},
          "Lisboa": {"descrição": "Cidade costeira com bondes históricos e o Castelo de São Jorge.", "preço": "Baixo", "continente": "Europa"},
          "Bangkok": {"descrição": "Cidade tailandesa com templos budistas e vida noturna animada.", "preço": "Baixo", "continente": "Ásia"},
          "Machu Picchu": {"descrição": "Cidade Inca antiga nas montanhas peruanas.", "preço": "Baixo", "continente": "América do Sul"},
          "Los Angeles": {"descrição": "Cidade do entretenimento, lar de Hollywood e praias famosas.", "preço": "Alto", "continente": "América do Norte"},
          "Istambul": {"descrição": "Cidade turca que une Europa e Ásia, com a Mesquita Azul.", "preço": "Médio", "continente": "Europa/Ásia"},
          "Reykjavik": {"descrição": "Capital da Islândia, com fontes termais e a Aurora Boreal.", "preço": "Médio", "continente": "Europa"},
          "Mumbai": {"descrição": "Cidade indiana vibrante com Bollywood e Gateway of India.", "preço": "Baixo", "continente": "Ásia"},
          "Buenos Aires": {"descrição": "Cidade argentina com rica cultura do tango e arquitetura colonial.", "preço": "Baixo", "continente": "América do Sul"}
      }

  def list_destinations(self):
      print("\nDestinos disponíveis:")
      for dest in self._destinations.keys():
          print(f"- {dest}")

  def get_info(self, destination_name):
      if destination_name in self._destinations:
          info = self._destinations[destination_name]
          print(f"\n{destination_name}: {info['descrição']} (Preço: {info['preço']}, Continente: {info['continente']})")
      else:
          print("Destino não encontrado.")
