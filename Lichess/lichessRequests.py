# Almost the same as Chess.com
# Lichess has API for everything, but i just want my public data
# so i don't need personal API token

import requests, json
from datetime import datetime

# Get stats data of my lichess.com account
x = requests.get('https://lichess.org/api/user/Domachi123')

# Output formated content of stats data to a file
if(False):
    with open('./Lichess/lichess.txt','w') as f:
        f.write(json.dumps(x.json(), indent=4))

# Output selected content of stats data to a file (Current blitz stats)
# You get numbers of games / your current rating / Relability Deviation data / Progresion over last 12 games
with open('./Lichess/lichess.txt','w') as f:
    f.write(json.dumps(x.json()["perfs"]["blitz"]))