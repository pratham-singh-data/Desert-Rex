# maximum fps of the game
fps = 60

# hardcoded screen dimentions
screen_width = 800
screen_height = 400

# position of the ground
ground_width = 70
ground_height = 50
ground_offset = 70
ground_x_offset = 0

# name of the game
game_name = 'Endless Runner'

# Font for score
font_url = None
font_size = 50
font_color = "#FF00FF"

# scoreboard
score = 0
scoreboard = f"Score: {score}"

# background image
background_url = "Assets/Images/Background/Background.png"
background_namehint = "Desert Background Image"

# image for ground
ground_url = "Assets/Images/Background/Ground.png"
ground_namehint = "Ground Tile"

# enemies
# cactus 1
enemy_cactus1_url = "Assets/Images/Enemies/Cactus (1).png"
enemy_cactus1_namehint = "Cactus 1"
enemy_cactus1_width = 20
enemy_cactus1_height = 40

# cactus 2
enemy_cactus2_url = "Assets/Images/Enemies/Cactus (2).png"
enemy_cactus2_namehint = "Cactus 2"
enemy_cactus2_width = 40
enemy_cactus2_height = 30

# cactus 3
enemy_cactus3_url = "Assets/Images/Enemies/Cactus (3).png"
enemy_cactus3_namehint = "Cactus 3"
enemy_cactus3_width = 35
enemy_cactus3_height = 45

# player dimensions
player_run_namehint = "Player run animation"
player_jump_namehint = "Player jump animation"
player_death_namehint = "Player death animation"
player_width = 60
player_height = 70
player_speed = 5
player_image_adjustment = 10
player_x_image_adjustment = 20
player_y_pos = screen_height - ground_offset - player_height + player_image_adjustment
default_player_y_pos = player_y_pos

# delay
delay = 0

# running state
running = True

# jump check
up = False
down = False
jumps = 0
jump_ceiling = player_y_pos

# player walk
player_run_1_url = "Assets/Images/Player/Run (1).png"
player_run_2_url = "Assets/Images/Player/Run (2).png"
player_run_3_url = "Assets/Images/Player/Run (3).png"
player_run_4_url = "Assets/Images/Player/Run (4).png"
player_run_5_url = "Assets/Images/Player/Run (5).png"
player_run_6_url = "Assets/Images/Player/Run (6).png"
player_run_7_url = "Assets/Images/Player/Run (7).png"
player_run_8_url = "Assets/Images/Player/Run (8).png"

# player jump
player_jump_1_url = "Assets/Images/Player/Jump (1).png"
player_jump_2_url = "Assets/Images/Player/Jump (2).png"
player_jump_3_url = "Assets/Images/Player/Jump (3).png"
player_jump_4_url = "Assets/Images/Player/Jump (4).png"
player_jump_5_url = "Assets/Images/Player/Jump (5).png"
player_jump_6_url = "Assets/Images/Player/Jump (6).png"
player_jump_7_url = "Assets/Images/Player/Jump (7).png"
player_jump_8_url = "Assets/Images/Player/Jump (8).png"
player_jump_9_url = "Assets/Images/Player/Jump (9).png"
player_jump_10_url = "Assets/Images/Player/Jump (10).png"
player_jump_11_url = "Assets/Images/Player/Jump (11).png"
player_jump_12_url = "Assets/Images/Player/Jump (12).png"

# player death
player_death_1_url = "Assets/Images/Player/Dead (1).png"
player_death_2_url = "Assets/Images/Player/Dead (2).png"
player_death_3_url = "Assets/Images/Player/Dead (3).png"
player_death_4_url = "Assets/Images/Player/Dead (4).png"
player_death_5_url = "Assets/Images/Player/Dead (5).png"
player_death_6_url = "Assets/Images/Player/Dead (6).png"
player_death_7_url = "Assets/Images/Player/Dead (7).png"
player_death_8_url = "Assets/Images/Player/Dead (8).png"

# enemy speed
speed_enemy = 5

# enemy generator seed
# higher => less enemies
gen_seed = 40

# jump ceilings
jump_ceiling_global = player_y_pos - 200