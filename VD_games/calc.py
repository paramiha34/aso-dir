import random

operations = ["+", "-", "*"]


def get_question_answer():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(operations)

    question = f"{a} {op} {b}"

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    else:
        result = a * b

    return question, result


instruction = "What is the result of the expression?"
