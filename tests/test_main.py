import os
import shutil

from main import fetch_input

cwd = os.getcwd()



def test_fetch_input():
    day = 1
    fetch_input(day)
    FILE_PATH =  cwd+f"input{day}.txt"
    assert os.path.exists(FILE_PATH)
    shutil.rmtree(FILE_PATH)



