import os.path

from api import *
from solution import YourSolutionForPuzzle1

def call_solution(day):
    input = fetch_input(day)
    YourSolutionForPuzzle1.get_puzzle_answer(input)



def fetch_input(day):
    if not os.path.exists(f'input{day}.txt'):
        get_input(day)
    with open(f"input{day}.txt") as file:
        input = file.read()
        return input



