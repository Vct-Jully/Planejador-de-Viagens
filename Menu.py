class Itinerary:
    def __init__(self):
        self._activities = []
        self.trip_data = {}

    def add_trip_details(self):
        print("\nPreencha os detalhes da viagem:")
        self.trip_data['horario'] = input("Horário de partida: ")
        self.trip_data['data_da_viagem'] = input("Data da viagem (AAAA-MM-DD): ")
        self.trip_data['tipo_de_transporte'] = input("Tipo de transporte: ")
        self.trip_data['quantidade_de_pessoas'] = int(input("Quantidade de pessoas: "))
        print("Categorias de viagem:")
        print("1. Trabalho")
        print("2. Amigos")
        print("3. Família")
        print("4. Faculdade")
        category_choice = input("Escolha a categoria da viagem (1-4): ")
        categories = {
            "1": "Trabalho", "2": "Amigos", "3": "Família", "4": "Faculdade"
        }
        self.trip_data['categoria_da_viagem'] = categories.get(category_choice, "Categoria inválida")
        print("Detalhes da viagem adicionados!")

    def add_activity(self, name):
        self._activities.append({"nome": name})
        print("Atividade adicionada!\n")

    def remove_activity(self):
        if not self._activities:
            print("\nNenhuma atividade no itinerário para remover.\n")
            return

        choice = int(input("Digite o número da atividade a ser removida: ")) - 1
        if 0 <= choice < len(self._activities):
            removed_activity = self._activities.pop(choice)
            print(f'\n-----------------------------------------------------\nAtividade \'{removed_activity["nome"]}\' removida!')
        else:
            print("\nOpção inválida. Atividade não removida.")

    def show_itinerary(self):
        if not self._activities:
            print("\nAinda não há atividades no itinerário.")
            return  # Return early if no activities

        print("\nItinerário de Viagem:")
        if self.trip_data:
          for index, activity in enumerate(self._activities, start=1):
            print(f'{index}. {activity["nome"]}')
            for key, value in self.trip_data.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("-" * 20) #separator line

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

    def get_info(self, price_preference=None, preferred_continent=None):
        print("\nDestinos disponíveis: ---------------------------------\n")
        if price_preference and preferred_continent:
            filtered_destinations = self._filter_destinations(price_preference, preferred_continent)
            for dest in filtered_destinations:
                print(f'- {dest}')
        else:
            for dest in self._destinations.keys():
                print(f'- {dest}')

        choice = input("\nEscolha um destino para mais informações (digite 'sair' para voltar): ")
        if choice.lower() == 'sair':
            return

        closest_match = self._find_closest_match(choice)
        print(f'\n{self._destinations.get(closest_match, "Destino não encontrado")}')

    def _filter_destinations(self, price_preference, preferred_continent):
        filtered_destinations = []
        for dest, info in self._destinations.items():
            if info["preço"] == price_preference and info["continente"] == preferred_continent:
                filtered_destinations.append(dest)
        return filtered_destinations

    def _find_closest_match(self, user_input):
        user_input_lower = user_input.lower()
        closest_match = None
        min_distance = float('inf')
        for dest in self._destinations.keys():
            dest_lower = dest.lower()
            distance = sum(1 for a, b in zip(user_input_lower, dest_lower) if a != b)
            if distance < min_distance:
                min_distance = distance
                closest_match = dest
        return closest_match

class ExpenseManager:
    def __init__(self):
        self._expenses = []

    def add_expense(self):
        category = input("\nCategoria da despesa: ")
        amount_str = input("Valor gasto (R$): ")
        try:
            amount = float(amount_str)
            self._expenses.append({"categoria": category, "valor": amount})
            print("\nDespesa adicionada!")
        except ValueError:
            print("\nValor inválido. Por favor, insira um número válido.")

    def show_expenses(self):
        if not self._expenses:
            print("\nNenhuma despesa registrada.\n")
        else:
            print("\nDespesas registradas: ---------------------------------\n")
            for exp in self._expenses:
                print(f'\n - {exp["categoria"]}: R$ {exp["valor"]:.2f}')

def get_user_input(prompt):
    return input(prompt)

def show_menu():
    print("\nMenu:")
    print("1 - Adicionar atividade ao itinerário")
    print("2 - Remover atividade")
    print("3 - Visualizar itinerário")
    print("4 - Informações sobre destinos (com preferências)")
    print("5 - Adicionar despesa")
    print("6 - Visualizar despesas")
    print("7 - Sair")

def main():
    itinerary = Itinerary()
    destination_info = DestinationInfo()
    expense_manager = ExpenseManager()

    show_menu() 

    while True:
        choice = get_user_input("Escolha uma opção: --------------------------------\n")

        if choice == "1":
            name = get_user_input("\nNome da atividade: ")
            itinerary.add_activity(name)
            itinerary.add_trip_details()

        elif choice == "2":
            itinerary.remove_activity()
        elif choice == "3":
            itinerary.show_itinerary()
        elif choice == "4":
            price_pref = get_user_input("\nPreferência de preço (Baixo, Médio, Alto): ")
            continent_pref = get_user_input("Continente preferido (Europa, Ásia, América do Sul, América do Norte, África, Oceania, ): ")
            destination_info.get_info(price_pref, continent_pref)
        elif choice == "5":
            expense_manager.add_expense()
        elif choice == "6":
            expense_manager.show_expenses()
        elif choice == "7":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida, tente novamente.")

        see_menu = input("\n-----------\nDeseja ver o menu novamente? (s/n):\n-----------\n ")
        if see_menu.lower() == "s":
            show_menu()

if __name__ == "__main__":
    main()
