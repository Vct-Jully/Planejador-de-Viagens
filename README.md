## Planejador de Viagens Interativo

Este projeto, desenvolvido para a disciplina de Projeto de Software, visa criar um planejador de itinerário de viagem interativo e personalizado, permitindo que os usuários criem e gerenciem seus planos de viagem de forma eficiente.

### Classes e Funcionalidades:

#### Classe Itinerary:
- **Propósito:** Gerencia as atividades do itinerário de viagem.
- **Atributos:**
  - `_activities`: Lista de atividades do itinerário.
- **Métodos:**
  - `add_activity(name, horario)`: Adiciona uma atividade ao itinerário com nome e horário.
  - `remove_activity()`: Remove uma atividade selecionada pelo usuário.
  - `show_itinerary()`: Exibe o itinerário completo com todas as atividades e detalhes da viagem.

#### Classe DestinationInfo:
- **Propósito:** Fornece informações sobre destinos de viagem.
- **Atributos:**
  - `_destinations`: Dicionário contendo informações detalhadas sobre diversos destinos.
- **Métodos:**
  - `get_info(price_preference, preferred_continent)`: Exibe uma lista de destinos filtrados por preferências de preço e continente, e fornece informações detalhadas sobre o destino escolhido.

#### Classe ExpenseManager:
- **Propósito:** Gerencia as despesas da viagem.
- **Atributos:**
  - `_expenses`: Lista de despesas registradas.
- **Métodos:**
  - `add_expense()`: Permite ao usuário adicionar uma despesa com categoria e valor.
  - `show_expenses()`: Exibe todas as despesas registradas e o total gasto na viagem.

### Funcionalidades Principais:
1. **Criação e Personalização de Itinerários:** Os usuários podem criar itinerários de viagem, adicionando atividades com nomes e horários. Eles também podem remover atividades e visualizar o itinerário completo.
2. **Informações Detalhadas sobre Destinos:** Fornece uma lista de destinos e permite aos usuários explorar informações detalhadas, incluindo descrições, preços e continentes. Os usuários podem filtrar destinos com base em suas preferências de preço e continente.
3. **Gerenciamento de Despesas:** Os usuários podem registrar despesas com categorias e valores. O aplicativo exibe as despesas registradas e o total gasto na viagem.
4. **Visualização Completa:** O aplicativo oferece uma visão abrangente do itinerário de viagem, incluindo atividades, detalhes da viagem (horário de partida, data, tipo de transporte, quantidade de pessoas, e categoria da viagem) e despesas.

### Estrutura do Projeto:
O projeto é organizado em três classes principais que trabalham em conjunto para criar uma experiência de planejamento de viagens completa:
1. **Classe Itinerary:** Gerencia as atividades do itinerário, permitindo aos usuários adicionar, remover e visualizar suas atividades planejadas.
2. **Classe DestinationInfo:** Fornece informações ricas sobre destinos, ajudando os usuários a explorar e escolher seus locais de viagem.
3. **Classe ExpenseManager:** Lida com o gerenciamento de despesas, permitindo que os usuários registrem e visualizem seus gastos durante a viagem.

### Instalação:
Para executar este projeto, siga estes passos:
1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório para o seu ambiente local.
3. Execute o arquivo principal do projeto.

Este projeto oferece uma experiência de planejamento de viagens interativa e personalizada, permitindo que os usuários criem itinerários, explorem destinos e gerenciem suas despesas de forma eficiente.
