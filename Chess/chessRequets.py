# requests - fetch API data
# json - for working with JSON data
# datetime - converting time

import requests, json
from datetime import datetime

# Get HTML page of my chess.com account
if(False):
    x = requests.get('https://www.chess.com/member/domachi123')

# Get stats data of my chess.com account
x = requests.get('https://api.chess.com/pub/player/domachi123/stats')

# Print the response text (the content of stats data):
if(False): 
    print(x.text)

# Output the response text (the content of stats data):
if(False):
    with open('chess.com.txt','w') as f:
        f.write(x.text)

# Print formated content of stats data
if(False):
    print(json.dumps(x.json(), indent=4))

# Output formated content of stats data to a file
if(False):
    with open('chess.com.txt','w') as f:
        f.write(json.dumps(x.json(), indent=4))

# Output selected content of stats data to a file (Current blitz stats)
# You get rating data / Int32 data of date / Relability Deviation data
if (False):
    with open('./Chess/chess.txt','w') as f:
        f.write(json.dumps(x.json()["chess_blitz"]["last"]))

# Print Blitz date rating in readable format
# With json, you get the date, which you convert it to int, so it can be converted to time stamp
print(datetime.fromtimestamp(int(json.dumps(x.json()["chess_blitz"]["last"]["date"]))))