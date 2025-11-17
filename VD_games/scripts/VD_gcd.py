from VD_games.engine import run_game
from VD_games.gcd import get_question_answer, instruction


def main():
    run_game(get_question_answer, instruction)


if __name__ == "__main__":
    main()
