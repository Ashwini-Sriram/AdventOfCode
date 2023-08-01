import api
from solution import get_puzzle_answer
def call_solution():
    input = fetch_input()
    get_puzzle_answer(input)



def fetch_input():
    with open("input.txt") as file:
        input = file.read()
        return input

