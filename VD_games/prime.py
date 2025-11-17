import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)

    progression = [start + i * step for i in range(length)]
    return progression


def get_question_answer():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)

    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


instruction = "What number is missing in the progression?"
