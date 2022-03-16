# import libraries
import pygame
from sys import exit
from numpy import random
from variables import *

pygame.init() # inirialise game engine
screen = pygame.display.set_mode((screen_width, screen_height)) # set screen
pygame.display.set_caption(game_name)
clock = pygame.time.Clock() # set max fps timer

# add music
pygame.mixer.music.load(default_track_url)
pygame.mixer.music.play(loops, default_track_offset)

# background surface
desert_background = pygame.image.load(background_url, background_namehint).convert_alpha()
desert_background = pygame.transform.scale(desert_background, (screen_width, screen_height))

# ground surface
ground_surface = pygame.image.load(ground_url, ground_namehint).convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (ground_width, ground_height))

# enemies
# cactus1
enemy_cactus1_surface = pygame.image.load(enemy_cactus1_url, enemy_cactus1_namehint).convert_alpha()
enemy_cactus1_surface = pygame.transform.scale(enemy_cactus1_surface, (enemy_cactus1_width, enemy_cactus1_height))

# cactus2
enemy_cactus2_surface = pygame.image.load(enemy_cactus2_url, enemy_cactus2_namehint).convert_alpha()
enemy_cactus2_surface = pygame.transform.scale(enemy_cactus2_surface, (enemy_cactus2_width, enemy_cactus2_height))

# cactus3
enemy_cactus3_surface = pygame.image.load(enemy_cactus3_url, enemy_cactus3_namehint).convert_alpha()
enemy_cactus3_surface = pygame.transform.scale(enemy_cactus3_surface, (enemy_cactus3_width, enemy_cactus3_height))

# player
# running
player_surface_run_1 = pygame.image.load(player_run_1_url, player_run_namehint).convert_alpha()
player_surface_run_1 = pygame.transform.scale(player_surface_run_1, (player_width, player_height))

player_surface_run_2 = pygame.image.load(player_run_2_url, player_run_namehint).convert_alpha()
player_surface_run_2 = pygame.transform.scale(player_surface_run_2, (player_width, player_height))

player_surface_run_3 = pygame.image.load(player_run_3_url, player_run_namehint).convert_alpha()
player_surface_run_3 = pygame.transform.scale(player_surface_run_3, (player_width, player_height))

player_surface_run_4 = pygame.image.load(player_run_4_url, player_run_namehint).convert_alpha()
player_surface_run_4 = pygame.transform.scale(player_surface_run_4, (player_width, player_height))

player_surface_run_5 = pygame.image.load(player_run_5_url, player_run_namehint).convert_alpha()
player_surface_run_5 = pygame.transform.scale(player_surface_run_5, (player_width, player_height))

player_surface_run_6 = pygame.image.load(player_run_6_url, player_run_namehint).convert_alpha()
player_surface_run_6 = pygame.transform.scale(player_surface_run_6, (player_width, player_height))

player_surface_run_7 = pygame.image.load(player_run_7_url, player_run_namehint).convert_alpha()
player_surface_run_7 = pygame.transform.scale(player_surface_run_7, (player_width, player_height))

player_surface_run_8 = pygame.image.load(player_run_8_url, player_run_namehint).convert_alpha()
player_surface_run_8 = pygame.transform.scale(player_surface_run_8, (player_width, player_height))

# jumping
player_surface_jump_1 = pygame.image.load(player_jump_1_url, player_jump_namehint).convert_alpha()
player_surface_jump_1 = pygame.transform.scale(player_surface_jump_1, (player_width, player_height))

player_surface_jump_2 = pygame.image.load(player_jump_2_url, player_jump_namehint).convert_alpha()
player_surface_jump_2 = pygame.transform.scale(player_surface_jump_2, (player_width, player_height))

player_surface_jump_3 = pygame.image.load(player_jump_3_url, player_jump_namehint).convert_alpha()
player_surface_jump_3 = pygame.transform.scale(player_surface_jump_3, (player_width, player_height))

player_surface_jump_4 = pygame.image.load(player_jump_4_url, player_jump_namehint).convert_alpha()
player_surface_jump_4 = pygame.transform.scale(player_surface_jump_4, (player_width, player_height))

player_surface_jump_5 = pygame.image.load(player_jump_5_url, player_jump_namehint).convert_alpha()
player_surface_jump_5 = pygame.transform.scale(player_surface_jump_5, (player_width, player_height))

player_surface_jump_6 = pygame.image.load(player_jump_6_url, player_jump_namehint).convert_alpha()
player_surface_jump_6 = pygame.transform.scale(player_surface_jump_6, (player_width, player_height))

player_surface_jump_7 = pygame.image.load(player_jump_7_url, player_jump_namehint).convert_alpha()
player_surface_jump_7 = pygame.transform.scale(player_surface_jump_7, (player_width, player_height))

player_surface_jump_8 = pygame.image.load(player_jump_8_url, player_jump_namehint).convert_alpha()
player_surface_jump_8 = pygame.transform.scale(player_surface_jump_8, (player_width, player_height))

player_surface_jump_9 = pygame.image.load(player_jump_9_url, player_jump_namehint).convert_alpha()
player_surface_jump_9 = pygame.transform.scale(player_surface_jump_9, (player_width, player_height))

player_surface_jump_10 = pygame.image.load(player_jump_10_url, player_jump_namehint).convert_alpha()
player_surface_jump_10 = pygame.transform.scale(player_surface_jump_10, (player_width, player_height))

player_surface_jump_11 = pygame.image.load(player_jump_11_url, player_jump_namehint).convert_alpha()
player_surface_jump_11 = pygame.transform.scale(player_surface_jump_11, (player_width, player_height))

player_surface_jump_12 = pygame.image.load(player_jump_12_url, player_jump_namehint).convert_alpha()
player_surface_jump_12 = pygame.transform.scale(player_surface_jump_12, (player_width, player_height))

# player death
player_surface_death_1 = pygame.image.load(player_death_1_url, player_death_namehint).convert_alpha()
player_surface_death_1 = pygame.transform.scale(player_surface_death_1, (player_width, player_height))

player_surface_death_2 = pygame.image.load(player_death_2_url, player_death_namehint).convert_alpha()
player_surface_death_2 = pygame.transform.scale(player_surface_death_2, (player_width, player_height))

player_surface_death_3 = pygame.image.load(player_death_3_url, player_death_namehint).convert_alpha()
player_surface_death_3 = pygame.transform.scale(player_surface_death_3, (player_width, player_height))

player_surface_death_4 = pygame.image.load(player_death_4_url, player_death_namehint).convert_alpha()
player_surface_death_4 = pygame.transform.scale(player_surface_death_4, (player_width, player_height))

player_surface_death_5 = pygame.image.load(player_death_5_url, player_death_namehint).convert_alpha()
player_surface_death_5 = pygame.transform.scale(player_surface_death_5, (player_width, player_height))

player_surface_death_6 = pygame.image.load(player_death_6_url, player_death_namehint).convert_alpha()
player_surface_death_6 = pygame.transform.scale(player_surface_death_6, (player_width, player_height))

player_surface_death_7 = pygame.image.load(player_death_7_url, player_death_namehint).convert_alpha()
player_surface_death_7 = pygame.transform.scale(player_surface_death_7, (player_width, player_height))

player_surface_death_8 = pygame.image.load(player_death_8_url, player_death_namehint).convert_alpha()
player_surface_death_8 = pygame.transform.scale(player_surface_death_8, (player_width, player_height))

# current enemies
# [enemy, enemy_width, x_pos, y_pos, dodged]
enemies = []

# current player
player_current = player_surface_run_1

# Font
text_font = pygame.font.Font(font_url, font_size)
restart_font = pygame.font.Font(restart_font_url, restart_font_size)

# start death music
def death_music():
    global death_music_startable

    if death_music_startable:
        death_music_startable = False

        # play death music
        death_music_track = pygame.mixer.music.load(death_track_url)
        pygame.mixer.music.play(loops, death_track_offset)
    
        # play crash tone
        crash_tone = pygame.mixer.Sound(crash_tone_url)
        crash_tone.play(crash_loop, crash_tone_offset)

# draw ground
def draw_ground(x_offset):
    for i in range(0 - x_offset, screen_width, ground_width):
        screen.blit(ground_surface, (i, screen_height - ground_offset))

# animate player charachter
def update_player():
    global player_current
    global running

    if player_current == player_surface_run_1:
        player_current = player_surface_run_2
    elif player_current == player_surface_run_2:
        player_current = player_surface_run_3
    elif player_current == player_surface_run_3:
        player_current = player_surface_run_4
    elif player_current == player_surface_run_4:
        player_current = player_surface_run_5
    elif player_current == player_surface_run_5:
        player_current = player_surface_run_6
    elif player_current == player_surface_run_6:
        player_current = player_surface_run_7
    elif player_current == player_surface_run_7:
        player_current = player_surface_run_8
    elif player_current == player_surface_run_8:
        player_current = player_surface_run_1
    elif player_current == player_surface_jump_1:
        player_current = player_surface_jump_2
    elif player_current == player_surface_jump_2:
        player_current = player_surface_jump_3
    elif player_current == player_surface_jump_3:
        player_current = player_surface_jump_4
    elif player_current == player_surface_jump_4:
        player_current = player_surface_jump_5
    elif player_current == player_surface_jump_5:
        player_current = player_surface_jump_6
    elif player_current == player_surface_jump_6:
        player_current = player_surface_jump_7
    elif player_current == player_surface_jump_7:
        player_current = player_surface_jump_8
    elif player_current == player_surface_jump_8:
        player_current = player_surface_jump_9
    elif player_current == player_surface_jump_9:
        player_current = player_surface_jump_10
    elif player_current == player_surface_jump_10:
        player_current = player_surface_jump_11
    elif player_current == player_surface_jump_11:
        player_current = player_surface_jump_12
    elif player_current == player_surface_jump_12:
        player_current = player_surface_run_1
    elif player_current == player_surface_death_1:
        player_current = player_surface_death_2
    elif player_current == player_surface_death_2:
        player_current = player_surface_death_3
    elif player_current == player_surface_death_3:
        player_current = player_surface_death_4
    elif player_current == player_surface_death_4:
        player_current = player_surface_death_5
    elif player_current == player_surface_death_5:
        player_current = player_surface_death_6
    elif player_current == player_surface_death_6:
        player_current = player_surface_death_7
    elif player_current == player_surface_death_7:
        player_current = player_surface_death_8
    elif player_current == player_surface_death_8:
        running = False

# restart functionality
def restore_defaults():
    global running
    global score
    global enemies
    global player_current
    global player_speed
    global enemy_speed
    global player_y_pos
    global up
    global down
    global jump_ceiling
    global jumps
    global death_music_startable


    running = True
    score = 0
    enemies.clear()
    player_current = player_surface_run_1
    enemy_speed = player_speed = 5
    player_y_pos = default_player_y_pos
    up = down = False
    jump_ceiling = default_player_y_pos
    jumps = 0
    pygame.mixer.music.load(default_track_url)
    pygame.mixer.music.play(loops, default_track_offset)
    death_music_startable = True

# main loop
while True:
    # generate scorboard
    scoreboard = f"Score: {score}"

    # events
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # spacebar click
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_speed != 0:
                if(jumps != 2):
                    up = True
                    down = False
                    jumps += 1
                    player_current = player_surface_jump_1

                    if(jump_ceiling > jump_ceiling_global):
                        jump_ceiling -= 100
            
            if event.key == pygame.K_r:
                restore_defaults()


    # jumping up
    if(up):
        player_y_pos -= player_speed
    
    # ceiling reached
    if(player_y_pos < jump_ceiling):
        down = True
        up = False
    
    # going down
    if(down):
        player_y_pos += player_speed
        jump_ceiling += player_speed

        if(player_y_pos >= default_player_y_pos):
            player_y_pos = default_player_y_pos
            jump_ceiling = player_y_pos
            player_current = player_surface_run_1
            jumps = 0
            down = False

    screen.blit(desert_background, (0, 0)) # add background
    draw_ground(ground_x_offset) # add ground

    # add scoreboard
    text_surface = text_font.render(scoreboard, True, font_color)
    screen.blit(text_surface, (0, 0)) # add text

    # restart message
    restart_surface = restart_font.render(restart_message, True , restart_font_color)
    screen.blit(restart_surface, (restart_x_pos, restart_y_pos))

    # add player
    screen.blit(player_current, (0, player_y_pos))

    # delay animation so user can perceive it
    if delay == 5:
        update_player()

        ground_x_offset += enemy_speed

        if(ground_x_offset > ground_width):
            ground_x_offset = 0

        delay = 1
    delay += 1

    # generate enemies
    generator = random.randint(0, 100)
    if(generator%gen_seed == 0):
        generator1 = random.randint(0, 3)

        if(generator1 == 0):
            enemies.append([enemy_cactus1_surface, screen_width - enemy_cactus1_width, screen_height - ground_offset - enemy_cactus1_height, False])
        elif(generator1 == 1):
            enemies.append([enemy_cactus2_surface, screen_width - enemy_cactus2_width, screen_height - ground_offset - enemy_cactus2_height, False])
        elif(generator1 == 2):
            enemies.append([enemy_cactus3_surface, screen_width - enemy_cactus3_width, screen_height - ground_offset - enemy_cactus3_height, False])

    # remove enemies once they are gone from the screen and calculate score
    for enemy in enemies:
        screen.blit(enemy[0], (enemy[1], enemy[2]))
        enemy[1] -= enemy_speed

    # make a duplicate array and copy all but undesired elements back to the original array
    enemies_copy = enemies.copy();
    enemies.clear()

    for enemy in enemies_copy:
        if(enemy[1] + player_x_image_adjustment < player_width and not enemy[3]):
            if(enemy[2] >= player_y_pos + player_height):
                score += 1

                # play success sound
                success_tone = pygame.mixer.Sound(success_tone_url)
                success_tone.play(success_loop, success_tone_offset)
            else:
                death_music()
                player_current = player_surface_death_1
                enemy_speed = 0
                player_speed = 0
            enemy[3] = True

        if(enemy[1] < 0): 
            continue
        enemies.append(enemy)
    
    enemies_copy.clear()

    # update display
    if running:
        pygame.display.update()

    # set maximum fps limit
    clock.tick(fps)