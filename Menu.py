class Itinerary:
  def __init__(self):
    self._activities = []

  def add_activity(self, name, hours):
    self._activities.append({"nome": name, "horario": hours})
    print("Atividade adicionada!")

  def remove_activity(self, name):
    self._activities = [activity for activity in self._activities if activity["nome"] != name]
    print("Atividade removida!")

  def show_itinerary(self):
    if not self._activities:
      print("\n Ainda não há nenhuma atividade no itnerario.")
    else:
      print("\nItnerário de Viagem\n")
      for activity in self._activities:
        print(f'-{activity["nome"]} às {activity["horario"]}')

class DestinationInfo:
  def __init__(self):
    self._destinations = {
    "Paris": "Cidade Luz, famosa pela Torre Eiffel e gastronomia.",
    "Nova York": "Grande metrópole, com a Estátua da Liberdade e Times Square.",
    "Tóquio": "Capital do Japão, com tecnologia avançada e templos históricos.",
    "Roma": "Cidade do Coliseu e da história do Império Romano.",
    "Rio de Janeiro": "Praia de Copacabana."
    }

  def get_info(self):
    print("\nDestinos disponíveis:")
    for dest in self._destinations.keys():
      print(f'- {dest}')
    choice = input("\nEscolha um destino para mais informações:")
    print(f'\n{self._destinations.get(choice, "Destino não encontrado")}')

class ExpenseManager:
  def __init__(self):
      self._expenses = []
  def add_expense(self):
    category = input("\nCategoria da despesa (Transporte, Alimentação, etc):")
    amount_str = input("Valor gasto R$: ")
    try:
        amount = float(amount_str)
        self._expenses.append({"categoria": category, "valor": amount})
        print("Despesa adcionada!")
    except ValueError:
      print("Valor inválido. Por favor, insira um número válido")
  def show_expenses(self):
    if not self._expenses:
      print("\nNenhuma despesa registrada.\n")
    for exp in self._expenses:
      print(f'\nDespesas registradas:')
      print(f'-{exp["categoria"]}: R$ {exp["valor"]:.2f}')

def get_user_input(prompt):
  return input(prompt)

def show_menu():
    print("\nMenu:")
    print("1 - Adicionar atividade ao itinerário")
    print("2 - Remover atividade")
    print("3 - Visualizar itinerário")
    print("4 - Informações sobre destinos")
    print("5 - Adicionar despesa")
    print("6 - Visualizar despesas")
    print("7 - Sair")

def main():
    itinerary = Itinerary()
    destination_info = DestinationInfo()
    expense_manager = ExpenseManager()

    show_menu() 

    while True:
        choice = get_user_input("Escolha uma opção: ")

        if choice == "1":
            name = get_user_input("\nNome da atividade: ")
            hours = get_user_input("Horário: ")
            itinerary.add_activity(name, hours)
        elif choice == "2":
            name = get_user_input("\nNome da atividade para remover: ")
            itinerary.remove_activity(name)
        elif choice == "3":
            itinerary.show_itinerary()
        elif choice == "4":
            destination_info.get_info()
        elif choice == "5":
            expense_manager.add_expense()
        elif choice == "6":
            expense_manager.show_expenses()
        elif choice == "7":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida, tente novamente.")

        see_menu = input("Deseja ver o menu novamente? (s/n): ")
        if see_menu.lower() == "s":
            show_menu()

if __name__ == "__main__":
    main()
    
