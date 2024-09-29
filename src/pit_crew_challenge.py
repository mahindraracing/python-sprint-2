import random
from src.helpers import force_list

# Dicionário para diferentes cenários de corrida
race_scenarios = {
    "tire_wear": {
        "description": "The tires are wearing faster than expected.",
        "options": {
            "best": "Request driver to manage tire wear",
            "OK": "Pit for new tires immediately",
            "worse": "Push with current tires"
        },
        "answers": {
            "1": "You request the driver to manage tire wear, he managed to do it and got an advantage!",
            "2": "You pit for new tires immediately, you lost time but it's okay, you manage to keep the same position.",
            "3": "You push with current tires. It got worse and the driver needed to change tires. You lost time and position." 
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
            "1": "You use attack mode. You lost some energy, but the driver kept up and gained some positions!",
            "2": "You instruct the driver to save energy. He did it, but he stayed in the same position.",
            "3": "You maintain current energy usage. The energy started to end and the driver couldn't keep up. You lost position." 
        }
    },
    "weather_change": {
        "description": "A sudden rain shower is approaching the track.",
        "options": {
            "best": "Pit for wet tires preemptively",
            "OK": "Wait and see how the weather develops",
            "worse": "Stick with dry tires"
        },
        "answers": {
            "1": "You pit for wet tires just before the rain hits. The driver gains multiple positions as others struggle!",
            "2": "You wait to see how the weather develops. The rain is light, and you maintain your position.",
            "3": "You stick with dry tires. The rain intensifies, and the driver struggles to keep the car on track, losing positions."
        }
    },
    "rival_strategy": {
        "description": "Your main rival is attempting an aggressive overtake.",
        "options": {
            "best": "Instruct driver to defend strategically",
            "OK": "Let the rival pass to save energy",
            "worse": "Engage in a risky battle for position"
        },
        "answers": {
            "1": "Your driver defends strategically, maintaining position while preserving energy and tires.",
            "2": "You let the rival pass, saving energy. You plan to counter-attack later in the race.",
            "3": "You engage in a risky battle. Both cars lose time, and you end up losing more positions in the process."
        }
    }
}

# Sistema de pontuação
points_system = {
    "race_finish": {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1},
    "fastest_lap": 1,
    "energy_efficiency": 2,
    "clean_racing": 1,
    "qualifying_position": {1: 3, 2: 2, 3: 1}  
}

# Estágios da corrida
race_stages = ["Race Start", "Mid-Race", "Late Race", "Final Laps"]

# Função para apresentar o cenário
def present_scenario(scenario):
    print(f"\nScenario: {scenario['description']}")
    for i, option in enumerate(scenario['options'].values(), 1):
        print(f"{i}. {option}")
    
    choice = force_list("Choose an option between 1-3: ", ["1", "2", "3"], "That's not a valid option! Please select a number between 1 and 3: ")
    
    return choice

# Função para atualizar a posição da corrida
def update_race_position(choice, current_position, scenario):
    position_change = 0
    if choice == "1":
        position_change = -random.randint(1, 2)  # Ganhar 1-2 posições 
    elif choice == "2":
        position_change = random.randint(1, 2)  # Perder 1-2 posições
    
    new_position =  current_position + position_change  # Garantir que posição esteja entre 1 e 20
    
    print(scenario["answers"][choice])
    if new_position != current_position:
        print(f"{'Gained' if position_change < 0 else 'Lost'} {abs(position_change)} position(s).")
    
    return new_position

# Função para calcular pontos
def calculate_points(position, fastest_lap, energy_efficiency, positions_gained, clean_racing, qualifying_position):
    total_points = 0

    if position in points_system["race_finish"]:
        total_points += points_system["race_finish"][position]

    if fastest_lap:
        total_points += points_system["fastest_lap"]
    
    if energy_efficiency == 1:  # 1 sendo o mais eficiente
        total_points += points_system["energy_efficiency"]

    if clean_racing:
        total_points += points_system["clean_racing"]

    if qualifying_position in points_system["qualifying_position"]:
        total_points += points_system["qualifying_position"][qualifying_position]

    total_points += positions_gained

    return total_points

# Função que remove o cenário para não repetí-lo no jogo
def select_and_remove_scenario(scenarios):
    scenario_key = random.choice(list(scenarios.keys()))
    scenario = scenarios.pop(scenario_key)
    return scenario

# Função que simula as qualificatórias
def simulate_qualifying():
    print("\n--- Qualifying Session ---")
    print("Your driver is heading out for the qualifying session.")
    qualifying_position = random.randint(1, 20)
    print(f"Qualifying result: P{qualifying_position}")
    return qualifying_position

# Função principal
def main_game_loop():
    print("Welcome to the Mahindra Racing Virtual Pit Crew Challenge!")
    total_points = 0
    qualifying_position = simulate_qualifying()
    race_position = qualifying_position
    energy_level = 100
    tire_wear = 0
    clean_racing = True

    available_scenarios = race_scenarios.copy()

    for stage in race_stages:
        print(f"\n--- {stage} ---")
        
        if available_scenarios:
            scenario = select_and_remove_scenario(available_scenarios)
        else:
            print("All scenarios have been used. Reusing all scenarios.")
            available_scenarios = race_scenarios.copy()
            scenario = select_and_remove_scenario(available_scenarios) 

        choice = present_scenario(scenario)

        race_position = update_race_position(choice, race_position, scenario)
        
        # Atualizar parâmetros de corrida
        energy_level -= random.randint(5, 15)
        tire_wear += random.randint(5, 15)
        
        if random.random() < 0.1:  # 10% de chance de perder o status de corrida limpa
            clean_racing = False
            print("Warning: Minor contact with another car. Clean racing bonus at risk!")
        
        print(f"Current race position: P{race_position}")
        print(f"Energy level: {energy_level}%")
        print(f"Tire wear: {tire_wear}%")

        if energy_level <= 20:
            print("Low energy warning! Consider energy-saving tactics.")
        if tire_wear >= 80:
            print("High tire wear warning! Consider a pit stop soon.")

    # End of race calculations
    fastest_lap = random.random() < 0.2  # 20% de chance de pegar a rodada mais rápida
    energy_efficiency = random.randint(1, 10)
    positions_gained = qualifying_position - race_position

    total_points = calculate_points(race_position, fastest_lap, energy_efficiency, positions_gained, clean_racing, qualifying_position)
    
    print("\n--- Race Summary ---")
    print(f"Starting position: P{qualifying_position}")
    print(f"Final position: P{race_position}")
    print(f"Positions gained: {positions_gained}")
    print(f"Fastest lap: {'Yes' if fastest_lap else 'No'}")
    print(f"Energy efficiency ranking: {energy_efficiency}/10")
    print(f"Clean racing: {'Yes' if clean_racing else 'No'}")
    print(f"Total points earned: {total_points}")