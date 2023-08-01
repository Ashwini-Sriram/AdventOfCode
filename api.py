import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sessionToken = os.getenv('AOC_TOKEN')

print(sessionToken)

def get_input(day):
    url = "https://adventofcode.com/2022/day/"+str(day)+"/input"
    headers = {'Cookie': f"session={sessionToken}"}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return r.text
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")




get_input(1)
