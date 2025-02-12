# Planejador-de-Viagens
Este projeto está sendo desenvolvido para a disciplina de **Projeto de Software** e visa criar um **planejador de itinerário de viagem interativo e personalizado**.

### Classes e Funcionalidades:
---
#### Classe `Itinerary`:
- **Propósito**: Gerencia as atividades do itinerário de viagem.
- **Atributos**:
  - `_activities`: Lista de atividades do itinerário.
- **Métodos**:
  - `add_activity(name, hours)`: Adiciona uma atividade ao itinerário.
  - `remove_activity(name)`: Remove uma atividade do itinerário.
  - `show_itinerary()`: Exibe o itinerário completo com todas as atividades.
---
#### Classe `DestinationInfo`:
- **Propósito**: Fornece informações sobre destinos de viagem.
- **Atributos**:
  - `_destinations`: Dicionário contendo informações sobre diversos destinos.
- **Métodos**:
  - `get_info()`: Exibe uma lista de destinos e permite ao usuário obter informações detalhadas sobre um destino específico.
---
#### Classe `ExpenseManager`:
- **Propósito**: Gerencia as despesas da viagem.
- **Atributos**:
  - `_expenses`: Lista de despesas registradas.
- **Métodos**:
  - `add_expense()`: Permite ao usuário adicionar uma despesa com categoria e valor.
  - `show_expenses()`: Exibe todas as despesas registradas e o total gasto na viagem.
---
### Funcionalidades Principais:
- Criação e personalização de itinerários de viagem.
- Fornece informações detalhadas sobre diversos destinos.
- Gerenciamento de despesas com categoria e valor.
- Visualização do itinerário completo e das despesas registradas.
---
### Instalação:
*Certifique-se de ter o Python instalado. Clone este repositório e execute o arquivo principal.*

---

### Estrutura do Projeto:
- O projeto é organizado em classes que representam diferentes aspectos do planejamento de viagens.
- A classe `Itinerary` gerencia as atividades, a classe `DestinationInfo` fornece informações sobre destinos, e a classe `ExpenseManager` lida com as despesas.

