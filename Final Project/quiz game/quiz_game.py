# Simple Multiple-Choice Quiz App (Descriptive Names)

# List of quiz questions
# Each question has 'text', 'choices', and 'correct_answer'
quiz_questions = [
    {
        "text": "What is the capital of France?",
        "choices": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "correct_answer": "A"
    },
    {
        "text": "Which language is used to create web pages?",
        "choices": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "correct_answer": "B"
    },
    {
        "text": "Which number is even?",
        "choices": ["A. 3", "B. 7", "C. 10", "D. 9"],
        "correct_answer": "C"
    },
    {
        "text": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "correct_answer": "B"
    },
    {
        "text": "Which of these is a Python data type?",
        "choices": ["A. int", "B. float", "C. str", "D. All of the above"],
        "correct_answer": "D"
    }
]

def start_quiz():
    total_score = 0
    print("Welcome to the Quiz!\n")
    
    for question_number, question in enumerate(quiz_questions, 1):
        print(str(question_number) + ". " + question["text"])
        for choice in question["choices"]:
            print(choice)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == question["correct_answer"]:
            print("Correct!\n")
            total_score += 1
        else:
            print("Wrong! The correct answer is " + question["correct_answer"] + ".\n")
    
    print("Quiz Completed!")
    print("Your score: " + str(total_score) + "/" + str(len(quiz_questions)))

# Run the quiz
if __name__ == "__main__":
    start_quiz()