import os

from tests import BaseTestCase
from api import get_input

cwd = os.getcwd()
# cwd = os.path.normpath(os.getcwd() + os.sep + os.pardir)

class TestService(BaseTestCase):


    def test_get_input(self):
        day = 1
        get_input(day)
        FILE_PATH =  cwd+f"/input{day}.txt"
        assert os.path.exists(FILE_PATH)




