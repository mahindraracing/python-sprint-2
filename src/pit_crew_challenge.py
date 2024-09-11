import random
from src.helpers import force_list

# Dicionário para armazenar cenários da corrida
race_scenarios = {
    "tire_wear": {
        "description": "The tires are wearing faster than expected.",
        "options": {
            "best": "Request driver to manage tire wear",
            "OK": "Pit for new tires immediately",
            "worse": "Push with current tires"
        },
        "answers": {
            1: "You request the driver to manage tire wear, he managed to do it and got an advantage!",
            2: "You pit for new tires immediately, you lost time but it's okay, you manage to keep the same position.",
            3: "You push with current tires. It got worse and the driver needed to change tires. You lost time and position." 
        }
    },
    "energy_management": {
        "description": "Energy levels are lower than anticipated.",
        "options": {
            "best": "Use attack mode to gain positions",
            "OK": "Instruct driver to save energy",
            "worse": "Maintain current energy usage"
        },
        "answers": {
            1: "You use attack mode. You lost some energy, but the driver kept up and gained some positions!",
            2: "You instruct the driver to save energy. He did it, but he stayed in the same position.",
            3: "You maintain current energy usage. The energy started to end and the driver couldn't keep up. You lost position." 
        }
    }
    # TODO: Add mais cenários
}

# Dicionário para armazenar sistemas de pontos
points_system = {
    "race_finish": {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1},
    "fastest_lap": 1,
    "energy_efficiency": 2,
}

# Lista para armazenar os estágios da corrida
race_stages = ["Race Start", "Mid-Race", "Final Laps"]

def present_scenario(scenario):
    print(f"\nScenario: {scenario['description']}")
    for i, option in enumerate(scenario['options'].values(), 1):
        print(f"{i}. {option}")
    
    choice = force_list([1, 2, 3], "That's not a valid option! Please select a number between 1 and 3: ")
    
    return choice


def update_race_position(choice, current_position):
    # Se a escolha for a melhor, diminui a posição, se for a pior, aumenta a posição e caso for a neutra, não faz nada
    if choice == 1:
        current_position -= 1
    elif choice == 3:
        current_position += 1

    # Mostrar o texto dependendo do cenário
    if race_scenarios["energy_management"]:
        print(race_scenarios["energy_management"]["answers"][choice])    
    elif race_scenarios["tire_wear"]:
        print(race_scenarios["tire_wear"]["answers"][choice])
    
    return current_position


# Função para calcular pontos
def calculate_points(position, fastest_lap, energy_efficiency, positions_gained):
    total_points = 0

    if position in points_system["race_finish"]:
        total_points += points_system["race_finish"][position]

    if fastest_lap:
        total_points += points_system["fastest_lap"]
    
    if energy_efficiency == 1: # 1 sendo o mais eficiente
        total_points += points_system["energy_efficiency"]

    total_points += positions_gained

    return total_points

def main_game_loop():
    print("Welcome to the Mahindra Racing Virtual Pit Crew Challenge!")
    total_points = 0
    race_position = 10  # Posição inicial

    for stage in race_stages:
        print(f"\n--- {stage} ---")
        # Randomiza um cenário para apresentar
        scenario = random.choice(list(race_scenarios.values()))

        # Apresenta o cenário
        choice = present_scenario(scenario)
        
        # Dependendo da resposta do usuário, sobe ou abaixa na posição da corrida
        race_position = update_race_position(choice, race_position)
        
        # TODO: Update other race parameters (tire wear, energy levels, etc.)
        
        print(f"Current race position: {race_position}")

    # Cálculos do final da corrida

    # Randomizar se em uma das laps, o jogador foi o mais rápido 
    fastest_lap = random.choice([True, False])

    # Randomizar a eficiência de energia
    energy_efficiency = random.randint(1, 10)

    # Calcular as posições ganhas
    positions_gained = 10 - race_position  # Posição inicial 10

    total_points = calculate_points(race_position, fastest_lap, energy_efficiency, positions_gained)
    print(f"\nRace finished! Final position: {race_position}")
    print(f"Total points earned: {total_points}")