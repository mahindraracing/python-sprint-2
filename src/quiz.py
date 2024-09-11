import random
from src.helpers import force_list

# Dictionary to store questions, options, and correct answers
questions = {
    "What year did Mahindra Racing join Formula E?": {
        "options": ["2014", "2015", "2016", "2017"],
        "correct": "2014"
    },
    "Who was Mahindra Racing's first Formula E driver?": {
        "options": ["Karun Chandhok", "Bruno Senna", "Nick Heidfeld", "Felix Rosenqvist"],
        "correct": "Karun Chandhok"
    },
    "What color is prominently featured in Mahindra Racing's livery?": {
        "options": ["Red", "Blue", "Green", "Yellow"],
        "correct": "Red"
    },
    "In which season did Mahindra Racing achieve their first Formula E podium?": {
        "options": ["Season 1", "Season 2", "Season 3", "Season 4"],
        "correct": "Season 2"
    },
    "What is Mahindra Racing's best finish in the Formula E Team Championship?": {
        "options": ["1st", "2nd", "3rd", "4th"],
        "correct": "4th"
    }
}

def display_welcome():
    print("Welcome to the Mahindra Racing Formula E Quiz!")
    print("Test your knowledge about one of Formula E's exciting teams.")
    print("You'll be asked 5 questions. Good luck!\n")

def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = force_list("Enter the number of your asnwer", options, f"Invalid input. Please enter a number between 1 and {len(options)}") 

    return answer    
    
def display_final_score(score):
    print(f"Quiz completed! Your final score is: {score}/5")
    if score == 5:
        print("Perfect score! You're a true Mahindra Racing expert!")
    elif score >= 3:
        print("Great job! You know your Mahindra Racing facts.")
    else:
        print("Good effort! There's always more to learn about Mahindra Racing.")

def display_score_matrix(matrix):
    print("\nScore Matrix (Questions x Scores):")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
    print("Rows represent questions, columns represent cumulative correct answers.")

def run_quiz():
    display_welcome()
    score = 0
    question_number = 0
    score_matrix = [[0 for _ in range(5)] for _ in range(5)]  # 5x5 matrix to store scores

    for question, data in random.sample(list(questions.items()), 5):
        question_number += 1
        user_answer = ask_question(question, data["options"])
        correct = user_answer == data["correct"]
        
        if correct:
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {data['correct']}")
        
        score_matrix[question_number - 1][score - 1] = 1  # Mark score in matrix
        print(f"Your current score: {score}/{question_number}\n")

    display_final_score(score)
    display_score_matrix(score_matrix)
