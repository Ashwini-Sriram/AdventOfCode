import os
import shutil
from main import fetch_input
from tests import BaseTestCase
from api import get_input
cwd = os.path.normpath(os.getcwd() + os.sep + os.pardir)

class TestService(BaseTestCase):


    def test_get_input(self):
        day = 1
        get_input(day)
        FILE_PATH =  cwd+f"/input{day}.txt"
        assert os.path.exists(FILE_PATH)
        shutil.rmtree(FILE_PATH)



