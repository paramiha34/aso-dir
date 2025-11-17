def welcome_user():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(get_question_answer, instruction):
    name = welcome_user()
    print(instruction)

    ROUNDS = 3

    for _ in range(ROUNDS):
        question, correct_answer = get_question_answer()

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
