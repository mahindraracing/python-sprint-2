import random
from feedbacks import get_feedback, avaliate_feedback, display_feedbacks
from races import simulate_race

def main():
    feedbacks = {
    "good-feedbacks": {},
    "bad-feedbacks": {},
    "neutral-feedbacks": {}
    }

    while True:
        print("""
        Menu:
              1 - Simulate Race
              2 - Send Feedback
              3 - View Fedbacks
    """)
        
        escolha = input("Selecione uma opção 1-3: ")
        match escolha:
            case "1":
                laps = input("How many laps you would like the race to have?")
                simulate_race(laps)
            case "2":
                feedback = get_feedback()
                feedbacks = avaliate_feedback(feedback, feedbacks)
            case "3":
                display_feedbacks(feedbacks)


if __name__ == "__main__":
    main()