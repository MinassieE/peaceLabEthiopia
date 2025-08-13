# Advanced Multiple-Choice Quiz App with Levels and Retry Option

# Quiz questions grouped by level
quiz_levels = {
    "Easy": [
        {
            "text": "What is the capital of France?",
            "choices": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "correct_answer": "A"
        },
        {
            "text": "Which number is even?",
            "choices": ["A. 3", "B. 7", "C. 10", "D. 9"],
            "correct_answer": "C"
        }
    ],
    "Medium": [
        {
            "text": "Which language is used to create web pages?",
            "choices": ["A. Python", "B. HTML", "C. C++", "D. Java"],
            "correct_answer": "B"
        },
        {
            "text": "Which planet is known as the Red Planet?",
            "choices": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
            "correct_answer": "B"
        }
    ],
    "Hard": [
        {
            "text": "Which of these is a Python data type?",
            "choices": ["A. int", "B. float", "C. str", "D. All of the above"],
            "correct_answer": "D"
        },
        {
            "text": "Which Python keyword is used to create a function?",
            "choices": ["A. function", "B. def", "C. fun", "D. define"],
            "correct_answer": "B"
        }
    ]
}

def run_quiz_level(level_name, questions):
    """Run a single level of the quiz and return the score and percentage."""
    print("\n=== " + level_name + " Level ===")
    level_score = 0
    
    for question_number, question in enumerate(questions, 1):
        print(str(question_number) + ". " + question["text"])
        for choice in question["choices"]:
            print(choice)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == question["correct_answer"]:
            print("Correct!\n")
            level_score += 1
        else:
            print("Wrong! The correct answer is " + question["correct_answer"] + ".\n")
    
    total_questions = len(questions)
    percentage = (level_score / total_questions) * 100
    print(level_name + " Level Completed! Score: " + str(level_score) + "/" + str(total_questions) + " (" + str(round(percentage, 1)) + "%)")
    
    return level_score, percentage

def start_quiz():
    print("Welcome to the Advanced Quiz!\n")
    total_score = 0
    total_questions = 0
    
    levels = ["Easy", "Medium", "Hard"]
    current_level_index = 0
    
    while current_level_index < len(levels):
        level_name = levels[current_level_index]
        questions = quiz_levels[level_name]
        
        level_score, percentage = run_quiz_level(level_name, questions)
        total_score += level_score
        total_questions += len(questions)
        
        # Check if user passed the level
        if percentage < 60:
            print("\nYou did not score at least 60% in this level.")
            retry = input("Do you want to retry this level? (yes/no): ").strip().lower()
            if retry == "yes":
                # Reset level score but do not move to next level
                total_score -= level_score
                total_questions -= len(questions)
                continue
            else:
                print("\nQuiz Ended. You did not pass the level.")
                break
        else:
            # Passed: ask if user wants to continue to next level (if not last level)
            if current_level_index < len(levels) - 1:
                cont = input("Do you want to continue to the next level? (yes/no): ").strip().lower()
                if cont != "yes":
                    break
            current_level_index += 1
    
    print("\nQuiz Finished!")
    print("Your total score: " + str(total_score) + "/" + str(total_questions))

if __name__ == "__main__":
    start_quiz()
