from solution import *
from api import get_input
import os
def test_output_for_solution1():
     day = 1
     if not os.path.exists(f'input{day}.txt'):
          get_input(day)
     with open(f"input{day}.txt") as file:
        input = file.read()
     assert get_puzzle_answer1(input) == ''

def test_output_for_solutiion2():
     day = 1
     if not os.path.exists(f'input{day}.txt'):
         get_input(day)
     with open(f"input{day}.txt") as file:
        input = file.read()
     assert get_puzzle_answer2(input) == ''
