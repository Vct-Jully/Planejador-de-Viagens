from itinerario import Itinerary
from destinos import DestinationInfo
from despesas import ExpenseManager
from utils import get_user_input, show_menu

def menu():
    itinerary = Itinerary()
    destination_info = DestinationInfo()
    expense_manager = ExpenseManager()

    while True:
        show_menu()
        choice = get_user_input("Escolha uma opção: ")

        if choice == "1":
            name = get_user_input("Nome da atividade: ")
            itinerary.add_activity(name)
        elif choice == "2":
            itinerary.exibir_info()  
            index = int(get_user_input("Digite o número da atividade a ser removida: ")) - 1
            itinerary.remove_activity(index)
        elif choice == "3":
            itinerary.exibir_info()
        elif choice == "4":
            price_pref = get_user_input("\nPreferência de preço (Baixo, Médio, Alto): ")
            continent_pref = get_user_input("Continente preferido (Europa, Ásia, América do Sul, América do Norte, África, Oceania, ): ")
            destination_info.get_info(price_pref, continent_pref)
        elif choice == "5":
            categoria = get_user_input("Categoria da despesa: ")
            valor = float(get_user_input("Valor gasto (R$): "))
            expense_manager.add_expense(categoria, valor)
        elif choice == "6":
            expense_manager.show_expenses()
        elif choice == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        ver_menu = get_user_input("\n Deseja ver o menu novamente? (s/n): ").strip().lower()
        if ver_menu != "s":
            print("\n Obrigado por usar o planejador de viagens!")
            break
