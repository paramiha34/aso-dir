import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_question_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f"{a} {b}"
    result = gcd(a, b)

    return question, result


instruction = "Find the greatest common divisor of given numbers."
