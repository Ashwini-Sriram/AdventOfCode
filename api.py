import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()
 
#AOC_TOKEN = '53616c7465645f5f400b0e919ccbfd43c47eb526dc1561615804bdf6248d6c21cc3b1566b0f4a4b1409a2308e036a43c1e4a8b8270df40b09a9201ba4805fd8c'
sessionToken = os.getenv('AOC_TOKEN')

print(sessionToken)
 
def get_input(day):
    url = "https://adventofcode.com/2022/day/"+str(day)+"/input"
    headers = {'Cookie': f"session={sessionToken}"}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(type(r.content))
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")
    


    
get_input(1)

