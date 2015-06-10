import requests

url = 'http://stats.nba.com/stats/playerdashptshotlog'
headers = { ... }
params = {'PlayerID': 202710, 'Season': '2014-15', ... }
r = requests.get(url, headers=headers, params=params)

if r.ok:
    do_something(r.json())
