from solution import YourSolutionForPuzzle1
from solution import YourSolutionForPuzzle2
from api import get_input
import os

def test_output_for_solution1():
     day = 1
     if not os.path.exists(f'input{day}.txt'):
          get_input(day)
     with open(f"input{day}.txt") as file:
        input = file.read()
     assert YourSolutionForPuzzle1.get_puzzle_answer (input) == ''

def test_output_for_solutiion2():
     day = 1
     if not os.path.exists(f'input{day}.txt'):
         get_input(day)
     with open(f"input{day}.txt") as file:
        input = file.read()
     assert YourSolutionForPuzzle2.get_puzzle_answer(input) == ''
