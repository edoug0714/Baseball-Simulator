import pybaseball
import pandas as pd
import numpy as np
import math
import random as rand

teams_list = {'ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CWS', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KAN', 'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TB', 'TEX', 'TOR', 'WAS', 'WSH'}

#def get_data(team1, team2):
    
def get_user_input():
    #Get Info for First Team
    stored = False
    user_input = input('Please enter your first team (ex: 2020 LAD):')
    while stored == False:
        if user_input == 'q' or user_input == 'Q':
            print('Exiting program.')
            exit(0)
        year1 = user_input.split()[0]
        team1 = user_input.split()[-1]
        if year1.isnumeric():
            if int(year1) > 2014 and int(year1) < 2024:
                if team1 in teams_list:
                    stored = True
        if stored == False:
            user_input = input('Please enter your team with the correct format (ex: 2020 LAD):')

    #Get Info for Second Team
    stored = False
    user_input = input('Please enter your second team (ex: 2020 TB):')
    while stored == False:
        if user_input == 'q' or user_input == 'Q':
            print('Exiting program.')
            exit(0)
        year2 = user_input.split()[0]
        team2 = user_input.split()[-1]
        if year2.isnumeric():
            if int(year2) > 2014 and int(year2) < 2024:
                if team2 in teams_list:
                    stored = True
        if stored == False:
            user_input = input('Please enter your team with the correct format (ex: 2020 TB):')

    result = [team1, year1, team2, year2]
    return result

def get_hitting(team, year):
    logs = pybaseball.team_batting_bref(team, int(year))
    logs = logs.iloc[:9]
    logs = logs[['Pos', 'Name', 'PA', 'H', '2B', '3B', 'HR', 'BB', 'SO', 'HBP', 'SB', 'CS', 'IBB']]
    percent_stats = logs.drop(columns=['Pos', 'Name']).astype(int)
    percent_stats['hit%'] = percent_stats['H'] / percent_stats['PA']
    percent_stats['walk/hbp%'] = (percent_stats['BB'] + percent_stats['HBP']) / percent_stats['PA']
    percent_stats['attempt_steal%'] = (percent_stats['CS'] + percent_stats['SB']) / (percent_stats['H'] + percent_stats['BB'] + percent_stats['IBB'] + percent_stats['HBP'])
    percent_stats['cs%'] = percent_stats['CS'] / (percent_stats['CS'] + percent_stats['SB'])
    percent_stats['HR%'] = percent_stats['HR'] / percent_stats['H']
    percent_stats['3B%'] = percent_stats['3B'] / percent_stats['H']
    percent_stats['2B%'] = percent_stats['2B'] / percent_stats['H']
    percent_stats['k%'] = percent_stats['SO'] / percent_stats['H']
    percent_stats = percent_stats.fillna(0)
    percent_stats['Name'] = logs['Name']
    percent_stats['Pos'] = logs['Pos']

    stats = percent_stats.drop(columns=['PA', 'H', '2B', '3B', 'HR', 'BB', 'SO', 'HBP', 'SB', 'CS', 'IBB'])
    stats = stats[['Pos', 'Name', 'hit%', '2B%', '3B%', 'HR%', 'walk/hbp%', 'k%', 'attempt_steal%', 'cs%']]
    #print(stats)
    return stats


def get_pitching(team, year):
    logs = pybaseball.team_pitching_bref(team, int(year))
    logs = logs[logs['Pos'] != '']

    percent_stats = logs[['H', 'BB', 'IBB', 'HBP', 'SO', 'WP', 'IP']].astype(float)
    percent_stats['total_faced'] = percent_stats['H'] + percent_stats['BB'] + percent_stats['HBP'] + percent_stats['IBB'] + (percent_stats['IP'] * 10) % 10 + round(percent_stats['IP']) * 3
    percent_stats['hit%'] = percent_stats['H'] / percent_stats['total_faced']
    percent_stats['walk/hbp%'] = (percent_stats['BB'] + percent_stats['IBB'] + percent_stats['HBP']) / percent_stats['total_faced']
    percent_stats['wp%'] = percent_stats['WP'] / percent_stats['total_faced']
    percent_stats['k%'] = percent_stats['SO'] / percent_stats['total_faced']
    percent_stats = percent_stats.fillna(0)
    percent_stats['Name'] = logs['Name']
    percent_stats['Pos'] = logs['Pos']

    stats = percent_stats.drop(columns=['H', 'BB', 'IBB', 'SO', 'HBP', 'WP', 'IP', 'total_faced'])
    stats = stats[['Pos', 'Name', 'hit%', 'walk/hbp%', 'k%', 'wp%']]
    #print(stats)
    return stats


#Batter_Stats: [hit%, 2B%, 3B%, HR%, walk/hbp%, k%, attempt_steal%, cs%]
#Pitcher_Stats: [hit%, walk/hbp%, k%, wp%]
def at_bat(home_batting, away_batting, home_pitching, away_pitching, pitcher, batter, top_bot):
    if top_bot == 'Top':
        batter_stats = away_batting[away_batting['Name'] == batter]
        pitcher_stats = home_pitching[home_pitching['Name'] == pitcher]
    else:
        batter_stats = home_batting[home_batting['Name'] == batter]
        pitcher_stats = away_pitching[away_pitching['Name'] == pitcher]

    batter_stats = batter_stats.drop(columns=['Name', 'Pos']).astype(float)
    pitcher_stats = pitcher_stats.drop(columns=['Name', 'Pos']).astype(float)

    print(batter_stats)
    print(pitcher_stats)

    hit = round((batter_stats.iloc[0, 0] + pitcher_stats.iloc[0, 0]) / 2 * 1000)
    walk = round((batter_stats.iloc[0, 4] + pitcher_stats.iloc[0, 1]) / 2 * 1000)
    strikeout = round((batter_stats.iloc[0, 5] + pitcher_stats.iloc[0, 2]) / 2 * 1000)
    homer = round(batter_stats.iloc[0, 3] * 1000)
    triple = round(batter_stats.iloc[0, 2] * 1000)
    double = round(batter_stats.iloc[0, 1] * 1000)
    single =  1000 - double - triple - homer

    print('Hit: ', hit, ' Walk: ', walk, ' Strikeout: ', strikeout)

    #[single, double, triple, homer, walk, strikeout, out]
    event_counter = [0, 0, 0, 0, 0, 0, 0]

    for i in range(1000):
        event = ''
        rand.seed()
        num = rand.randint(1, 1000)
        if(num <= walk):
            event = 'Walk'
            event_counter[4] += 1
        elif (num <= walk + hit):
            num = rand.randint(1, 1000)
            if(num <= homer):
                event = 'Home Run'
                event_counter[3] += 1
            elif (num <= homer + triple):
                event = 'Triple'
                event_counter[2] += 1
            elif(num <= homer + triple + double):
                event = 'Double'
                event_counter[1] += 1
            else:
                event = 'Single'
                event_counter[0] += 1
        elif(num <= walk + hit + strikeout):
            event = 'Strikeout'
            event_counter[5] += 1
        else:
            event = 'Fielded Out'
            event_counter[6] += 1

    print(event_counter)

     

def main():
    teams = get_user_input()

    home_batting = get_hitting(teams[0], teams[1])
    away_batting = get_hitting(teams[2], teams[3])

    home_pitching = get_pitching(teams[0], teams[1])
    away_pitching = get_pitching(teams[2], teams[3])

    at_bat(home_batting, away_batting, home_pitching, away_pitching, 'Blake Snell', 'Will Smith', 'Bot')



    


main()

