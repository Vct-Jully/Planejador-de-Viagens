from .travelPlan import TravelPlan
from utils import get_user_input

class Itinerary(TravelPlan):
    def __init__(self):
        super().__init__()
        self._activities = []


    def add_activity(self, name):

        if not self._trip_data:
            print("\nPreencha os detalhes da viagem primeiro:")
            horario = get_user_input("Horário de partida: ")
            data = get_user_input("Data da viagem (DD-MM-AAAA): ")
            transporte = get_user_input("Tipo de transporte: ")
            pessoas = int(get_user_input("Quantidade de pessoas: "))

            print("Categorias de viagem:")
            print("1. Trabalho")
            print("2. Amigos")
            print("3. Família")
            print("4. Faculdade")
            category_choice = get_user_input("Escolha a categoria da viagem (1-4): ")
            categories = {"1": "Trabalho", "2": "Amigos", "3": "Família", "4": "Faculdade"}
            categoria = categories.get(category_choice, "Categoria inválida")

            self.set_trip_details(horario, data, transporte, pessoas, categoria)

        self._activities.append({"nome": name})
        print("\nAtividade adicionada com sucesso!\n")


    def remove_activity(self, index):
        if 0 <= index < len(self._activities):
            "atividade removida!"
            return self._activities.pop(index)
        return None

    def exibir_info(self):
        super().exibir_info()

        print("\nAtividades planejadas:")
        for i, atividade in enumerate(self._activities, 1):
            print(f"{i}. {atividade['nome']}")
            if self._trip_data:
                print(f"\n Viagem: {self._trip_data['categoria_da_viagem']}")
                print(f" Horário de partida: {self._trip_data['horario']}")
                print(f" Data: {self._trip_data['data_da_viagem']}")
                print(f" Transporte: {self._trip_data['tipo_de_transporte']}")
                print(f" Pessoas: {self._trip_data['quantidade_de_pessoas']}")
            else:
                print("\n Detalhes da viagem não preenchidos.")
