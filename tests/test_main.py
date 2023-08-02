import os

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

    def test_call_solution():
        with patch("main.fetch_input") as mock_fetch_input:
            call_solution(day=1)
        with patch("solution.get_puzzle_answer") as mock_get_puzzle_answer:
            call_solution(day=1)
        with patch("api.check") as mock_check_solution:
            call_solution(day=1)
        mock_fetch_input.assert_called_once_with(day=1)
        mock_get_puzzle_answer.assert_called_once_with(day=1)
        mock_check_solution.assert_called_once_with(day=1)

