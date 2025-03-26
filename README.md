## **Planejador de Viagens Interativo**

Este projeto, desenvolvido para a disciplina de Projeto de Software, visa criar um planejador de itinerário de viagem interativo e personalizado, permitindo que os usuários criem e gerenciem seus planos de viagem de forma eficiente. Além disso, o projeto implementa conceitos fundamentais de Programação Orientada a Objetos (POO), como **herança, polimorfismo, classes abstratas e encapsulamento**, garantindo um design modular e escalável.

---

### **Conceitos de POO Aplicados**

- **Herança:** A classe `Itinerary` herda da classe `TravelPlan`, permitindo que ela reutilize e expanda funcionalidades relacionadas aos detalhes da viagem.
- **Polimorfismo:** O método `exibir_info()` é definido na classe `TravelPlan` e sobrescrito na classe `Itinerary`, permitindo que cada classe exiba informações conforme sua necessidade.
- **Classe Abstrata:** `TravelPlan` é uma classe abstrata, impedindo que seja instanciada diretamente e garantindo que suas subclasses implementem métodos essenciais.
- **Encapsulamento:** Os atributos `_trip_data` e `_activities` são protegidos, garantindo que apenas métodos controlados possam acessar ou modificar esses dados.

---

### **Classes e Funcionalidades**

#### **Classe TravelPlan (Classe Abstrata)**
- **Propósito:** Define a estrutura base de um plano de viagem.
- **Atributos:**
  - `_trip_data`: Armazena os detalhes da viagem, como horário, data, transporte e categoria.
- **Métodos:**
  - `set_trip_details()`: Define os detalhes da viagem.
  - `get_trip_details()`: Retorna uma cópia dos detalhes da viagem.
  - `exibir_info()`: Método abstrato que deve ser implementado pelas subclasses.

#### **Classe Itinerary (Herança de TravelPlan)**
- **Propósito:** Gerencia as atividades do itinerário de viagem.
- **Atributos:**
  - `_activities`: Lista de atividades do itinerário.
- **Métodos:**
  - `add_activity(name)`: Adiciona uma atividade ao itinerário.
  - `remove_activity(index)`: Remove uma atividade com base no índice.
  - `exibir_info()`: Exibe o itinerário completo e os detalhes da viagem.

#### **Classe DestinationInfo**
- **Propósito:** Fornece informações sobre destinos de viagem.
- **Atributos:**
  - `_destinations`: Dicionário contendo informações detalhadas sobre diversos destinos.
- **Métodos:**
  - `get_info(price_preference, preferred_continent)`: Exibe uma lista de destinos filtrados por preferências de preço e continente.

#### **Classe ExpenseManager**
- **Propósito:** Gerencia as despesas da viagem.
- **Atributos:**
  - `_expenses`: Lista de despesas registradas.
- **Métodos:**
  - `add_expense()`: Permite ao usuário adicionar uma despesa com categoria e valor.
  - `show_expenses()`: Exibe todas as despesas registradas e o total gasto na viagem.

---

### **Funcionalidades Principais**
1. **Criação e Personalização de Itinerários:** Os usuários podem criar itinerários de viagem, adicionando atividades e removendo-as quando necessário.
2. **Informações Detalhadas sobre Destinos:** Os usuários podem explorar destinos de viagem filtrados por preço e continente.
3. **Gerenciamento de Despesas:** O sistema permite registrar e visualizar despesas de viagem.
4. **POO Aplicada:** O código foi estruturado para ser modular e escalável, utilizando herança, polimorfismo, encapsulamento e classes abstratas.

---

### **Estrutura do Projeto**
O projeto é organizado em três classes principais, juntamente com a classe abstrata `TravelPlan`, que define a estrutura base para itinerários:
1. **Classe `TravelPlan` (Abstrata):** Fornece a base para qualquer plano de viagem.
2. **Classe `Itinerary`:** Gerencia atividades e detalhes do itinerário.
3. **Classe `DestinationInfo`:** Exibe informações detalhadas sobre destinos.
4. **Classe `ExpenseManager`:** Registra e gerencia despesas de viagem.

---
