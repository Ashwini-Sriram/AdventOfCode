import requests 

def get_input():
    response = requests.get("https://adventofcode.com/2022/day/1/input")
    print(response)
    
get_input()

