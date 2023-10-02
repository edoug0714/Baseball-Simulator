import pygame
import math
import pandas as pd
import numpy as np
from pybaseball import standings

###
#statcast(start_dt="2019-06-24", end_dt="2019-06-25").columns
#Index(['pitch_type', 'game_date', 'release_speed', 'release_pos_x',
              #'release_pos_z', 'player_name', 'batter', 'pitcher', 'events',
             # 'description', 'spin_dir', 'spin_rate_deprecated',
             # 'break_angle_deprecated', 'break_length_deprecated', 'zone', 'des',
             # 'game_type', 'stand', 'p_throws', 'home_team', 'away_team', 'type',
            #  'hit_location', 'bb_type', 'balls', 'strikes', 'game_year', 'pfx_x',
             # 'pfx_z', 'plate_x', 'plate_z', 'on_3b', 'on_2b', 'on_1b',
             # 'outs_when_up', 'inning', 'inning_topbot', 'hc_x', 'hc_y',
             # 'tfs_deprecated', 'tfs_zulu_deprecated', 'fielder_2', 'umpire', 'sv_id',
             # 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az', 'sz_top', 'sz_bot',
             # 'hit_distance_sc', 'launch_speed', 'launch_angle', 'effective_speed',
             # 'release_spin_rate', 'release_extension', 'game_pk', 'pitcher.1',
             # 'fielder_2.1', 'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6',
             # 'fielder_7', 'fielder_8', 'fielder_9', 'release_pos_y',
             # 'estimated_ba_using_speedangle', 'estimated_woba_using_speedangle',
             # 'woba_value', 'woba_denom', 'babip_value', 'iso_value',
             # 'launch_speed_angle', 'at_bat_number', 'pitch_number', 'pitch_name',
             # 'home_score', 'away_score', 'bat_score', 'fld_score', 'post_away_score',
              #'post_home_score', 'post_bat_score', 'post_fld_score',
             # 'if_fielding_alignment', 'of_fielding_alignment', 'spin_axis',
             # 'delta_home_win_exp', 'delta_run_exp'],
            #dtype='object')
###

def get_data():
    data = standings(2023)
    print(data)




def runner_on_second() -> bool:
    return True

#Creating Window
pygame.init()
background = (50, 50, 50)
(width, height) = (1920, 1080)
base_size = width / 16
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial')
screen.fill(background)

#Draw Field
dirt = pygame.draw.polygon(screen, (193, 153, 107), [(width / 2, height / 80), (width / 2 - width / 8, height / 80 + width / 8), (width / 2, height / 80 + width / 4), (width / 2 + width / 8, height /80 + width / 8)], 0)
grass = pygame.draw.polygon(screen, (0, 128, 0), [(width / 2, height / 80 + width / 24 + width / 48), (width / 2 - width / 8 + width / 24 + width / 48, height / 80 + width / 8), (width / 2, height / 80 + width / 4 - width / 24 - width / 48), (width / 2 + width / 8 - width / 24 - width / 48, height / 80 + width / 8)], 0)
home_plate = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2, height / 80 + width / 4 - width / 96), (width / 2 - width / 72, height / 80 + width / 4 - width / 48), (width / 2 - width / 72, height / 80 + width / 4 - width / 24), (width / 2 + width / 72, height / 80 + width / 4 - width / 24), (width / 2 + width / 72, height / 80 + width / 4 - width / 48)], 0)                                                                                                                       
third_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2 - width / 8 + width / 48 + width / 96, height / 80 + width / 8 - width / 48), (width / 2 - width / 8 + width / 96, height / 80 + width / 8), (width / 2 - width / 8 + width / 48 + width / 96, height / 80 + width / 8 + width / 48), (width / 2 - width / 8 + width / 24 + width / 96, height / 80 + width / 8) ], 0)
second_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2, height / 80 + width / 96), (width / 2 - width / 48, height / 80 + width / 48 + width / 96), (width / 2, height / 80 + width / 24 + width / 96), (width / 2 + width / 48, height / 80 + width / 48 + width / 96)], 0)
first_base = pygame.draw.polygon(screen, (255, 255, 255), [(width / 2 + width / 8 - width / 48 - width / 96, height / 80 + width / 8 - width / 48), (width / 2 + width / 8 - width / 24 - width / 96, height / 80 + width / 8), (width / 2 + width / 8 - width / 48 - width / 96, height / 80 + width / 8 + width / 48), (width / 2 + width / 8 - width / 96, height / 80 + width / 8)], 0)
pygame.draw.polygon(screen, (255, 255, 255), [(second_base.center), (first_base.center), (home_plate.center), (third_base.center)], 12) 
pygame.display.flip()

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    get_data()
    
    if runner_on_second():
        second_base = pygame.draw.polygon(screen, (255, 234, 0), [(width / 2, height / 80 + width / 96), (width / 2 - width / 48, height / 80 + width / 48 + width / 96), (width / 2, height / 80 + width / 24 + width / 96), (width / 2 + width / 48, height / 80 + width / 48 + width / 96)], 0)



   


    pygame.display.flip()

