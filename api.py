import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sessionToken = os.getenv('AOC_TOKEN')

def get_input(day):
    url = "https://adventofcode.com/2022/day/"+str(day)+"/input"
    headers = {'Cookie': f"session={sessionToken}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f'input{day}.txt','w') as fd:
            fd.write(response.text)

    else:
        sys.exit(f"/api/alerts response: {response.status_code}: {response.reason} \n{response.content}")




get_input(1)
