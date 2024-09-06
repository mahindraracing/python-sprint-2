import random

def simulate_race(laps):
    teams = {
        "Mahindra Racing": {"skill": 85, "reliability": 90},
        "Team A": {"skill": 82, "reliability": 88},
        "Team B": {"skill": 88, "reliability": 85},
        "Team C": {"skill": 80, "reliability": 92}
    }

    results = {team: 0 for team in teams}
    
    for lap in range(laps):
        print(f"\nLap {lap + 1}:")
        for team in teams:
            skill = teams[team]["skill"]
            reliability = teams[team]["reliability"]
            
            lap_time = random.randint(80, 100) - (skill * 0.1)
            
            if random.randint(1, 100) > reliability:
                print(f"{team} had a technical issue!")
                lap_time += 10
            
            results[team] += lap_time
            print(f"{team}: {lap_time:.2f}s")
    
    return results

def get_feedback():
    feedback = input("Escreva seu feedback: ")
    return feedback

def avaliate_feedback():
    

def main():
    while True:
        print("""
        Menu:
              1 - Simulate Race
              2 - Send Feedback
    """)    
        
        escolha = input("Selecione uma opção 1-*")
        match escolha:
            case 1:
                laps = input("How many laps you would like the race to have?")
                simulate_race(laps)
            
    

if __name__ == "__main__":
    main()