# 🏎️ Mahindra Racing Python Sprint 2 🏁

## 🌟 Project Overview

This project is a Python-based application developed for Mahindra Racing to enhance visibility and engagement. It simulates various aspects of Formula E racing, including race simulations, a virtual pit crew challenge, and an interactive quiz about Mahindra Racing.

## 🚀 Features

1. **🏁 Race Simulation**: Simulates a Formula E race with customizable lap counts.
2. **🔧 Virtual Pit Crew Challenge**: An interactive game where players make strategic decisions during a race.
3. **💬 Feedback System**: Allows users to provide feedback, which is then categorized and displayed.
4. **🧠 Mahindra Racing Quiz**: Tests users' knowledge about Mahindra Racing and Formula E.
5. **📋 Interactive Menu**: Provides easy navigation through different features of the application.

## 📂 Project Structure

- `main.py`: The entry point of the application, containing the main menu and game loop.
- `src/`:
  - `feedbacks.py`: Handles the feedback system.
  - `races.py`: Contains the race simulation logic.
  - `pit_crew_challenge.py`: Implements the Virtual Pit Crew Challenge game.
  - `helpers.py`: Utility functions used across the project.
  - `quiz.py`: Implements the Mahindra Racing quiz.

## 🚗 How to Run

1. Ensure you have Python installed on your system.
2. Clone the repository: `git clone https://github.com/mahindraracing/python-sprint-2.git`
3. Navigate to the project directory: `cd python-sprint-2`
4. Run the main script: `python main.py`

## 👥 Team Members

This project was developed by students from FIAP University:

- 👨‍💻 Caio Suzano Ferreira da Silva (RM 554763)
- 👨‍💻 Matheus Rivera Montovaneli (RM 555499)
- 👨‍💻 Lucas Vasquez Silva (RM 555159)
- 👨‍💻 Guilherme Linard F. R. Gozzi (RM 555768)
- 👨‍💻 André Nakamatsu Rocha (RM 555004)

## 🤝 Contributing

This is a university project and is not open for external contributions at this time.

## 🧑‍💻 Code Explanation

### main.py

```python
def main():
    feedbacks = {
        "good-feedbacks": {},
        "neutral-feedbacks": {},
        "bad-feedbacks": {}
    }
    while True:
        print("""
    Menu:
        1 - Simulate Race
        2 - Virtual Pit Crew Challenge
        3 - Send Feedback
        4 - View Fedbacks
        5 - Play Quiz
        """)
        
        choice = input("Select an option 1-5: ")
        match choice:
            case "1":
                laps = force_number("How many laps you would like the race to have? ", "Please enter a number: ")
                simulate_race(laps)
            case "2":
                main_game_loop()
            case "3":
                feedback = get_feedback()
                feedbacks = evaluate_feedback(feedback, feedbacks)
            case "4":
                display_feedbacks(feedbacks)
            case "5":
                run_quiz()
            case _:
                print("That's not valid! Please select an option between 1-5")
```

This is the main entry point of the application. It creates a dictionary to store feedbacks and enters an infinite loop that displays a menu and handles user input using a match-case statement. Each case corresponds to a different feature of the application.

### feedbacks.py

```python
def evaluate_feedback(feedback, feedbacks_dict):
    key_words = {
        "good": {"great", "good", "amazing", "funny", "entertaining", "cool"},
        "bad": {"awful", "bad", "horrible"}
    }
    
    feedback_lower = feedback.lower()
    
    if any(word in feedback_lower for word in key_words["good"]):
        category = "good-feedbacks"
    elif any(word in feedback_lower for word in key_words["bad"]):
        category = "bad-feedbacks"
    else:
        category = "neutral-feedbacks"
    
    feedback_count = len(feedbacks_dict[category])
    feedbacks_dict[category][feedback_count] = feedback
    return feedbacks_dict
```

This function categorizes user feedback as good, neutral, or bad based on keywords, and adds it to the appropriate category in the feedbacks dictionary.

### pit_crew_challenge.py

```python
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
        
        # Update other race parameters
        energy_level -= random.randint(5, 15)
        tire_wear += random.randint(5, 15)
        
        if random.random() < 0.1:  # 10% chance of a clean racing incident
            clean_racing = False
            print("Warning: Minor contact with another car. Clean racing bonus at risk!")
        
        print(f"Current race position: P{race_position}")
        print(f"Energy level: {energy_level}%")
        print(f"Tire wear: {tire_wear}%")

    # ... end of race calculations ...
```

This function implements the main loop of the Virtual Pit Crew Challenge. It simulates a race, presenting scenarios at each stage and updating race parameters based on the player's choices.

### quiz.py

```python
def run_quiz():
    display_welcome()
    score = 0
    question_number = 0
    score_matrix = [[0 for _ in range(6)] for _ in range(5)]  #6x5 matrix to store scores
    for question, data in random.sample(list(questions.items()), 5):
        question_number += 1
        user_answer = ask_question(question, data["options"])
        correct = user_answer == data["correct"]
        
        if correct:
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {data['correct']}")
        
        score_matrix[question_number - 1][min(score, 5)] = 1  # Mark score in matrix
        print(f"Your current score: {score}/{question_number}\n")
    display_final_score(score)
    display_score_matrix(score_matrix)
```

This function runs the Mahindra Racing quiz. It selects random questions, asks them, keeps track of the score, and displays the final results including a score matrix.

### races.py

```python
def simulate_race(laps):
    teams = {
        "Mahindra Racing": {"skill": 85, "reliability": 90},
        "Team A": {"skill": 82, "reliability": 88},
        "Team B": {"skill": 88, "reliability": 85},
        "Team C": {"skill": 80, "reliability": 92}
    }
    laps = int(laps)
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
```

This function simulates a Formula E race. It takes a number of laps as input, defines teams with different skill and reliability ratings, and then simulates each lap of the race. It calculates lap times based on team skill and randomly occurring technical issues based on team reliability.

## 🏎️ Happy racing with Mahindra! 🏁
