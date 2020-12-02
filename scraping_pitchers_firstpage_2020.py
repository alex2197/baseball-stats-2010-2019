import requests
from bs4 import BeautifulSoup
import pandas as pd

firstName, secondName = [], []
fullName = []
playersPosition = []
playersTeam = []
playersGames = []
playersAB = []
playersRuns = []
playersHits = []
playersDoubles = []
playersTriples = []
playersHR = []
playersRBI = []
playersBB = []
playersSO = []
playersSB = []
playersCS = []
playersAVG = []
playersOBP = []
playersSLG = []


url = 'https://www.mlb.com/stats/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

players_name = soup.find_all('span', {'class': 'full-3fV3c9pF'})
players_position = soup.find_all('div', {'class': 'position-28TbwVOg'})
players_stats = soup.find_all('td')


for elements in players_name[::2]:
    firstName.append(elements.text)

for elements in players_name[1::2]:
    secondName.append(elements.text)

for i in range(25):
    fullName.append(firstName[i] + " " + secondName[i])
    playersPosition.append(players_position[i].text)

for elements in players_stats[::17]:
    playersTeam.append(elements.text)

for elements in players_stats[1::17]:
    playersGames.append(elements.text)

for elements in players_stats[2::17]:
    playersAB.append(elements.text)
    
for elements in players_stats[3::17]:
    playersRuns.append(elements.text)

for elements in players_stats[4::17]:
    playersHits.append(elements.text)

for elements in players_stats[5::17]:
    playersDoubles.append(elements.text)

for elements in players_stats[6::17]:
    playersTriples.append(elements.text)
    
for elements in players_stats[7::17]:
    playersHR.append(elements.text)

for elements in players_stats[8::17]:
    playersRBI.append(elements.text)

for elements in players_stats[9::17]:
    playersBB.append(elements.text)

for elements in players_stats[10::17]:
    playersSO.append(elements.text)
    
for elements in players_stats[11::17]:
    playersSB.append(elements.text)       

for elements in players_stats[12::17]:
    playersCS.append(elements.text) 

for elements in players_stats[13::17]:
    playersAVG.append(elements.text)

for elements in players_stats[14::17]:
    playersOBP.append(elements.text)

for elements in players_stats[15::17]:
    playersSLG.append(elements.text)

playersDic = {
        'Players': fullName, 
        'Position': playersPosition,
        'Team' : playersTeam,
        'Games' : playersGames,
        'At Bats' : playersAB,
        'Runs' : playersRuns,
        'Hits' : playersHits,
        'Doubles' : playersDoubles,
        'Triples' : playersTriples,
        'Home Runs' : playersHR,
        'RBI' : playersRBI,
        'BB' : playersBB,
        'SO' : playersSO,
        'SB' : playersSB,
        'CS': playersCS,
        'Average' : playersAVG,
        'OBP' : playersOBP,
        'SLG' : playersSLG
    } 

df = pd.DataFrame(playersDic)
print(df)
df.to_csv('./Hitting_stats/Hitting_stats_firstpage.csv', index=False)
