import random
from src.feedbacks import get_feedback, evaluate_feedback, display_feedbacks
from src.races import simulate_race
from src.pit_crew_challenge import main_game_loop
from src.helpers import force_list, force_number
from src.quiz import run_quiz

def main():
    feedbacks = {
        "good-feedbacks": {},
        "neutral-feedbacks": {},
        "bad-feedbacks": {}
    }

    # Loop principal
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
            

if __name__ == "__main__":
    main()