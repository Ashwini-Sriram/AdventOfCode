import os.path

from api import *
from solution import get_puzzle_answer


def call_solution(day):
    input = fetch_input(day)
    get_puzzle_answer(input)



def fetch_input(day):
    if os.path.exists(f'input{day}.txt'):
        with open(f"input{day}.txt") as file:
            input = file.read()
            return input

    else:
        get_input(day)

