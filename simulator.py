
from pybaseball import standings
import pygame
import test
import adjust_score

(width, height) = (1920, 1080)

def runner_on_second() -> bool:
    return True



def create_window():
    pygame.init()
    background = (50, 50, 50)
    base_size = width / 16
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial')
    screen.fill(background)

    return screen

def draw_field():
    screen = create_window()
    dirt = pygame.draw.polygon(screen, (193, 153, 107), [(width / 2, height / 80), (width / 2 - width / 8, height / 80 + width / 8), (width / 2, height / 80 + width / 4), (width / 2 + width / 8, height /80 + width / 8)], 0)
    grass = pygame.draw.polygon(screen, (0, 128, 0), [(width / 2, height / 80 + width / 24 + width / 48), (width / 2 - width / 8 + width / 24 + width / 48, height / 80 + width / 8), (width / 2, height / 80 + width / 4 - width / 24 - width / 48), (width / 2 + width / 8 - width / 24 - width / 48, height / 80 + width / 8)], 0)
    home_plate = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2, height / 80 + width / 4 - width / 96), (width / 2 - width / 72, height / 80 + width / 4 - width / 48), (width / 2 - width / 72, height / 80 + width / 4 - width / 24), (width / 2 + width / 72, height / 80 +width / 4 - width / 24), (width / 2 + width / 72, height / 80 + width / 4 - width / 48)], 0)                                                                                                                       
    third_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2 - width / 8 + width / 48 + width / 96, height / 80 + width / 8 - width / 48), (width / 2 - width / 8 + width / 96, height / 80 + width / 8), (width / 2 - width / 8 + width / 48 + width / 96, height / 80 + width / 8 + width / 48), (width / 2 - width / 8 + width / 24 + width / 96, height / 80 + width / 8) ], 0)
    second_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2, height / 80 + width / 96), (width / 2 - width / 48, height / 80 + width / 48 + width / 96), (width / 2, height / 80 + width / 24 + width / 96), (width / 2 + width / 48, height / 80 + width / 48 + width / 96)], 0)
    first_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2 + width / 8 - width / 48 - width / 96, height / 80 + width / 8 - width / 48), (width / 2 + width / 8 - width / 24 - width / 96, height / 80 + width / 8), (width / 2 + width / 8 - width / 48 - width / 96, height / 80 + width / 8 + width / 48), (width / 2 + width / 8 - width / 96, height / 80 + width / 8)], 0)
    pygame.draw.polygon(screen, (255, 255, 255), [(second_base.center), (first_base.center), (home_plate.center), (third_base.center)], 12) 
    pygame.display.flip()


#Game Loop
def simulate():
    screen = create_window()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        if runner_on_second():
            second_base = pygame.draw.polygon(screen, (255, 234, 0), [(width / 2, height / 80 + width / 96), (width / 2 - width / 48, height / 80 + width / 48 + width / 96), (width / 2, height / 80 + width / 24 + width / 96), (width / 2 + width / 48, height / 80 + width / 48 + width / 96)], 0)

    pygame.display.flip()


def main():
    teams = test.get_user_input()

    #print(teams)

    home_batting = test.get_hitting(teams[0], teams[1])
    away_batting = test.get_hitting(teams[2], teams[3])
    home_pitching = test.get_pitching(teams[0], teams[1])
    away_pitching = test.get_pitching(teams[2], teams[3])

    away_batter_list = away_batting['Name'].tolist()
    home_batter_list = home_batting['Name'].tolist()

    home_starters = home_pitching[home_pitching['Pos'] == 'SP'].iloc[:5]
    home_bullpen = home_pitching[home_pitching['Pos'] != 'SP']
    away_starters = away_pitching[away_pitching['Pos'] == 'SP'].iloc[:5]
    away_bullpen = away_pitching[away_pitching['Pos'] != 'SP']

    print(home_starters[['Name', 'ERA', 'WHIP']])
    home_pitcher = input('\nChoose the starting pitcher for the home team:')
    print(away_starters[['Name', 'ERA', 'WHIP']])
    away_pitcher = input('\n\nChoose the starting pitcher for the away team:')

    #This for loop is the main driver for the sim
    dummy = 0
    #i = 0
    j = 0
    k = 0
    game_over = False
    home_runs = 0
    away_runs = 0
    pitcher_stamina = 100
    home_strikeout_counter = 0
    away_strikeout_counter = 0
    #while game_over == False:
    for i in range(18):
        if i % 2 == 0:
            if i == 0:
                print('\n\nTOP OF THE 1ST INNING')
            elif i == 2:
                print('\n\nTOP OF THE 2ND INNING')
            elif i == 4:
                print('\n\nTOP OF THE 3RD INNING')
            else:
                print('\n\nTOP OF THE', str(round((i+2) / 2)) + 'TH INNING')
            
            #Start of each half inning
            #[1ST, 2ND, 3RD, RUNS_ON_PLAY]
            runners = [0, 0, 0, 0, 0]
            print('Pitching for ' + teams[0] + ': ', home_pitcher)
            while runners[4] < 3:
                starting_outs = runners[4]
                batter = away_batter_list[j]
                print('Batting for ' + teams[2] + ': ', batter)
                result = test.at_bat(home_batting, away_batting, home_pitching, away_pitching, home_pitcher, batter, 'Top')

                #If at bat results in a strikeout, display pitcher's strikeout total
                if result == 'Strikeout':
                    home_strikeout_counter += 1
                    print(result + '(' + str(home_strikeout_counter) + ')')
                else:
                    print(result)

                runners = adjust_score.adjust_score(runners, result)
                if runners[3] != 0:
                    away_runs += int(runners[3])
                    print(teams[0] + ':', home_runs, '|', teams[2] + ':', away_runs)
                    runners[3] = 0

                #Increase number of outs when an out occurs
                if starting_outs != runners[4]:
                    if runners[4] == 1:
                        print('1 OUT!')
                    elif runners[4] == 2:
                        print('2 OUTS!')
                    else:
                        print('3 OUTS!')

                print(runners)
                print('\n')

                if j == 8:
                    j = 0
                else:
                    j += 1

        else:
            if i == 1:
                print('\n\nBOTTOM OF THE 1ST INNING')
            elif i == 3:
                print('\n\nBOTTOM OF THE 2ND INNING')
            elif i == 5:
                print('\n\nBOTTOM OF THE 3RD INNING')
            else:
                print('\n\nBOTTOM OF THE', str(round((i+1) / 2)) + 'TH INNING')
            runners = [0, 0, 0, 0, 0]
            print('Pitching for ', teams[2] + ': ', away_pitcher)
            while runners[4] < 3:
                starting_outs = runners[4]
                batter = home_batter_list[k]
                print('Batting for ', teams[0] + ': ', batter)
                result = test.at_bat(home_batting, away_batting, home_pitching, away_pitching, away_pitcher, batter, 'Bot')
                print(result)

                runners = adjust_score.adjust_score(runners, result)
                if runners[3] != 0:
                    home_runs += int(runners[3])
                    print(teams[0] + ':', home_runs, '|', teams[2] + ':', away_runs)
                    runners[3] = 0

                if starting_outs != runners[4]:
                    if runners[4] == 1:
                        print('1 OUT!')
                    elif runners[4] == 2:
                        print('2 OUTS!')
                    else:
                        print('3 OUTS!')

                print(runners)
                print('\n')

                if k == 8:
                    k = 0
                else:
                    k += 1



main()
