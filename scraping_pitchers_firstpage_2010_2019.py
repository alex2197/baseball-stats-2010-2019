import requests
from bs4 import BeautifulSoup
import pandas as pd

firstName, secondName = [], []
playersYear = []
playersName = []
playersStats = []
playersPosition = []
fullName = []
playersTeam = []
playersWin = []
playersLoses = []
playersERA = []
playersGames = []
playersGS = []
playersCG = []
playersSHO = []
playersSaves = []
playersSVO = []
playersIP = []
playersHits = []
playersRuns = []
playersER = []
playersHR = []
playersHB = []
playersBB = []
playersSO = []
playersWHIP = []
playersAVG = []


for i in range(2010, 2020):
    url1 = 'https://www.mlb.com/stats/'
    page = requests.get(url1 + 'pitching/games/{}'.format(i))
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

for elements in playersStats[::20]:
    playersTeam.append(elements)

for elements in playersStats[1::20]:
    playersWin.append(elements)

for elements in playersStats[2::20]:
    playersLoses.append(elements)

for elements in playersStats[3::20]:
    playersERA.append(elements)

for elements in playersStats[4::20]:
    playersGames.append(elements)

for elements in playersStats[5::20]:
    playersGS.append(elements)

for elements in playersStats[6::20]:
    playersCG.append(elements)

for elements in playersStats[7::20]:
    playersSHO.append(elements)

for elements in playersStats[8::20]:
    playersSaves.append(elements)

for elements in playersStats[9::20]:
    playersSVO.append(elements)

for elements in playersStats[10::20]:
    playersIP.append(elements)

for elements in playersStats[11::20]:
    playersHits.append(elements)

for elements in playersStats[12::20]:
    playersRuns.append(elements)

for elements in playersStats[13::20]:
    playersER.append(elements)

for elements in playersStats[14::20]:
    playersHR.append(elements)

for elements in playersStats[15::20]:
    playersHB.append(elements)

for elements in playersStats[16::20]:
    playersBB.append(elements)

for elements in playersStats[17::20]:
    playersSO.append(elements)

for elements in playersStats[18::20]:
    playersWHIP.append(elements)

for elements in playersStats[19::20]:
    playersAVG.append(elements)

playersDic = {
    
    'Players' : fullName,
    'Team' : playersTeam,
    'Win' : playersWin,
    'Lost' : playersLoses,
    'ERA' : playersERA,
    'Games' : playersGames,
    'GS' : playersGS,
    'CG' : playersCG,
    'SHO' : playersSHO,
    'Saves' : playersSaves,
    'SVO' : playersSVO,
    'IP' : playersIP,
    'Hits' : playersHits,
    'Runs' : playersRuns,
    'ER' : playersER,
    'HR' : playersHR,
    'HB' : playersHB,
    'BB' : playersBB,
    'SO' : playersSO,
    'WHIP' : playersWHIP,
    'AVG' : playersAVG, 
    'Year': playersYear
}

df = pd.DataFrame(playersDic)
print(df)
df.to_csv('./Pitching_stats/pitching_stats_firstpage_2010_2019.csv', index=False)
