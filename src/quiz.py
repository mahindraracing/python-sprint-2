import random
from src.helpers import force_list

# Dicinário para as perguntas e respostas
questions = {
    "What year did Mahindra Racing join Formula E?": {
        "options": ["2014", "2015", "2016", "2017"],
        "correct": "1"
    },
    "Who was Mahindra Racing's first Formula E driver?": {
        "options": ["Karun Chandhok", "Bruno Senna", "Nick Heidfeld", "Felix Rosenqvist"],
        "correct": "1"
    },
    "What color is prominently featured in Mahindra Racing's livery?": {
        "options": ["Red", "Blue", "Green", "Yellow"],
        "correct": "1"
    },
    "In which season did Mahindra Racing achieve their first Formula E podium?": {
        "options": ["Season 1", "Season 2", "Season 3", "Season 4"],
        "correct": "2"
    },
    "What is Mahindra Racing's best finish in the Formula E Team Championship?": {
        "options": ["1st", "2nd", "3rd", "4th"],
        "correct": "4"
    }
}

# Função que printa o bem-vindo do jogo
def display_welcome():
    print("Welcome to the Mahindra Racing Formula E Quiz!")
    print("Test your knowledge about one of Formula E's exciting teams.")
    print("You'll be asked 5 questions. Good luck!\n")

# Função que faz a pergunta ao usuário
def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = force_list("Enter the number of your answer: ", ["1", "2", "3", "4"], f"Invalid input. Please enter a number between 1 and {len(options)}: ") 

    return answer    

# Função que printa a pontuação final 
def display_final_score(score):
    print(f"Quiz completed! Your final score is: {score}/5")
    if score == 5:
        print("Perfect score! You're a true Mahindra Racing expert!")
    elif score >= 3:
        print("Great job! You know your Mahindra Racing facts.")
    else:
        print("Good effort! There's always more to learn about Mahindra Racing.")

# Função que mostra a matriz de pontuação
def display_score_matrix(matrix):
    print("\nScore Matrix (Questions x Scores):")
    print("  0 1 2 3 4 5")
    for i, row in enumerate(matrix, 1):
        print(f"{i} " + " ".join(str(cell) for cell in row))
    print("Rows represent questions, columns represent cumulative correct answers.")

# Função principal
def run_quiz():
    display_welcome()
    score = 0
    question_number = 0
    score_matrix = [[0 for _ in range(6)] for _ in range(5)]  #6x5 matriz para guardar pontuação

    for question, data in random.sample(list(questions.items()), 5):
        question_number += 1
        user_answer = ask_question(question, data["options"])
        correct = user_answer == data["correct"]
        
        if correct:
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {data['correct']}")
        
        score_matrix[question_number - 1][min(score, 5)] = 1  # Marcar pontuação na matriz
        print(f"Your current score: {score}/{question_number}\n")

    display_final_score(score)
    display_score_matrix(score_matrix)
