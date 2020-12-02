import requests
from bs4 import BeautifulSoup
import pandas as pd

firstName, secondName = [], []
fullName = []
playersName = []
playersStats = []
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
playersYear = []

for i in range(2010, 2020):
    url1 = 'https://www.mlb.com/stats/games/'
    page = requests.get(url1 + '{}'.format(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    for players_name in  soup.find_all('span', {'class': 'full-3fV3c9pF'}):
        playersName.append(players_name.text)
    for players_position in soup.find_all('div', {'class': 'position-28TbwVOg'}):
        playersPosition.append(players_position.text)
        playersYear.append(i)
    for players_stats in soup.find_all('td'):
        playersStats.append(players_stats.text)

numberOfPlayers = (int)(len(playersName) / 2)


for elements in playersName[::2]:
    firstName.append(elements)

for elements in playersName[1::2]:
    secondName.append(elements)

for i in range(numberOfPlayers):
    fullName.append(firstName[i] + " " + secondName[i])

for elements in playersStats[::17]:
    playersTeam.append(elements)

for elements in playersStats[1::17]:
    playersGames.append(elements)

for elements in playersStats[2::17]:
    playersAB.append(elements)
    
for elements in playersStats[3::17]:
    playersRuns.append(elements)

for elements in playersStats[4::17]:
    playersHits.append(elements)

for elements in playersStats[5::17]:
    playersDoubles.append(elements)

for elements in playersStats[6::17]:
    playersTriples.append(elements)
    
for elements in playersStats[7::17]:
    playersHR.append(elements)

for elements in playersStats[8::17]:
    playersRBI.append(elements)

for elements in playersStats[9::17]:
    playersBB.append(elements)

for elements in playersStats[10::17]:
    playersSO.append(elements)
    
for elements in playersStats[11::17]:
    playersSB.append(elements)       

for elements in playersStats[12::17]:
    playersCS.append(elements) 

for elements in playersStats[13::17]:
    playersAVG.append(elements)

for elements in playersStats[14::17]:
    playersOBP.append(elements)

for elements in playersStats[15::17]:
    playersSLG.append(elements)

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
        'SLG' : playersSLG,
        'Year' : playersYear
    } 

df = pd.DataFrame(playersDic)
print(df)
df.to_csv('./Hitting_stats/Hitting_stats_firstpage_2010_2019.csv', index=False)
