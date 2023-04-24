"""
* Assignment 4
* Xueyao Wang
* Create 2 random teams from a list of players
* Sample output:
*   Players:  ['Harry', 'Hermione', 'Neville', 'Ginny', 'Luna']
*   Team names:  ['Alligators', 'Gorillas', 'Eagles', 'Pythons', 'Wasps', 'Panthers']
*   Here are your teams:
*   Panthers ['Luna', 'Hermione', 'Ginny']
*   Alligators ['Neville', 'Harry']

"""
from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players: ', players)

teamA = []
teamB = []

while len(players)>0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

teams = ['Alligators', 'Gorillas', 'Eagles', 'Pythons', 'Wasps', 'Panthers']
print('Team names: ',teams)

team_a_name = choice(teams)
teams.remove(team_a_name)
team_b_name = choice(teams)

print('\nHere are your teams:\n')
print(team_a_name, teamA)
print(team_b_name, teamB)

