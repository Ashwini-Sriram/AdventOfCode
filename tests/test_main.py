import os
from unittest.mock import patch
from tests import BaseTestCase
from api import *
from main import *
from solution import *

cwd = os.getcwd()
# cwd = os.path.normpath(os.getcwd() + os.sep + os.pardir)

class TestService(BaseTestCase):


    def test_get_input(self):
        day = 1
        get_input(day)
        FILE_PATH =  cwd+f"/input{day}.txt"
        assert os.path.exists(FILE_PATH)


    def test_call_solution(self):
        day = 1
        with patch("main.fetch_input") as mock_fetch_input:
            call_solution(day)
        mock_fetch_input.assert_called_once_with(day)


    def test_call_solution_for_answer(self):
        day = 1

        with patch("solution.get_puzzle_answer") as mock_get_puzzle_answer:
            call_solution(day)
        mock_get_puzzle_answer.assert_called_once

    




    def test_get_input_writes_only_once(self):
        day =1;
        fetch_input(day)
        if os.path.exists(f"input{day}.txt"):
            with patch("api.get_input") as mock_get_input:
                fetch_input(day)
            mock_get_input.assert_not_called()







